import os
os.environ["CUDA_VISIBLE_DEVICES"]= "1"
import re
import argparse
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import VLLM
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from datetime import datetime
from zoneinfo import ZoneInfo
import CoT_prompts
import time
import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


os.environ["OPENAI_API_KEY"] = ""



import os

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "qwen2.5_20240927"
os.environ["LANGCHAIN_API_KEY"] = ""





def get_today_menu():
    
    base_url = 'https://inucoop.com/main.php?mkey=2&w=4'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    session = requests.Session()
    session.headers.update(headers)
    
    response = session.get(base_url)
    if response.status_code != 200:
        print(f"페이지를 가져오지 못했습니다. 상태 코드: {response.status_code}")
        return ""
    
    response.encoding = 'utf-8'  # 필요에 따라 조정
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    form = soup.find('form', attrs={'name': 'menuForm'})
    if not form:
        print("menuForm을 찾을 수 없습니다.")
        return ""
    
    action_url = form['action']
    if not action_url.startswith('http'):
        action_url = requests.compat.urljoin(base_url, action_url)
    
    dates = []
    date_cells = soup.find_all('td', class_=['yo_mn', 'yo_mns2'])
    for cell in date_cells:
        onclick = cell.get('onclick', '')
        if 'sdt.value' in onclick:
            sdt_value = onclick.split("sdt.value='")[1].split("';")[0]
            date_text = cell.get_text(strip=True)
            dates.append({'sdt': sdt_value, 'date_text': date_text})
    
    today = datetime.now().strftime('%Y%m%d')

    today_info = None
    for date_info in dates:
        if date_info['sdt'] == today:
            today_info = date_info
            break
    
    if not today_info:
        print("오늘의 메뉴를 찾을 수 없습니다.")
        return ""
    
    sdt_value = today_info['sdt']
    date_text = today_info['date_text']
    print(f"{date_text}의 메뉴를 처리 중입니다...")
    
    post_data = {
        'jun': '0',  # 폼에서 'jun'은 '0'으로 유지
        'sdt': sdt_value
    }
    
    menu_response = session.post(action_url, data=post_data)
    if menu_response.status_code != 200:
        print(f"{date_text}의 메뉴를 가져오지 못했습니다. 상태 코드: {menu_response.status_code}")
        return ""
    
    menu_response.encoding = 'utf-8'  # 필요에 따라 조정
    
    menu_soup = BeautifulSoup(menu_response.text, 'html.parser')
    
    menu_text = f"=== {date_text}의 메뉴 ===\n\n"
    
    # style="width:960px;"인 모든 테이블 찾기
    tables = menu_soup.find_all('table', attrs={'style': 'width:960px;'})
    
    for table in tables:
        canteen_name_row = table.find('tr')
        canteen_name_cell = canteen_name_row.find('td', attrs={
            'colspan': True, 
            'style': 'font-size:14pt;font-weight:bold;'
        })
        if canteen_name_cell:
            canteen_name = canteen_name_cell.get_text(strip=True)
            menu_text += f"식당: {canteen_name}\n"
        else:
            continue  # 식당 이름이 없으면 스킵
    
        meal_type_row = canteen_name_row.find_next_sibling('tr')
        meal_type_cells = meal_type_row.find_all('td', class_='td_mn')
        meal_types = [cell.get_text(strip=True) for cell in meal_type_cells]

        menu_row = meal_type_row.find_next_sibling('tr')
        if not menu_row:
            continue
        menu_cells = menu_row.find_all('td', class_=['din_lists', 'td_list'])
        menus = [cell.get_text(separator='\n', strip=True) for cell in menu_cells]

        if len(menu_cells) == 1 and '오늘 등록된 메뉴가 없습니다' in menus[0]:
            menu_text += f"  {menus[0]}\n"
            continue
    
        for meal_type, menu in zip(meal_types, menus):
            menu_text += f"\n--- {meal_type} ---\n"
            menu_text += f"{menu}\n"
        menu_text += "\n" + "="*10 + "\n\n"
    
    print(f"{date_text}의 메뉴를 가져왔습니다.")
    return menu_text


def is_menu_query(user_msg):
    weather_patterns = [
        r".*메뉴.*",
        r".*학식.*",
        r".*점심.*",
        r".*저녁.*",
        r".*메누.*",
        r".*점메추.*",
        r".*저메추.*",
        r".*기식.*",
        r".*교직원식당.*",
        r".*생협식당.*",
    ]
    for pattern in weather_patterns:
        if re.search(pattern, user_msg):
            return True
    return False


def get_menu_instruct(query: str) -> str:
    
    kst = ZoneInfo('Asia/Seoul')
    
    now_in_kst = datetime.now(kst)

    today = now_in_kst.strftime('%Y-%m-%d')
    
    menu_text = get_today_menu()
    
    return f'오늘({today})의 메뉴:{menu_text}Question: {query}\n핵심 메뉴만 간략하게 소개하세요. (학식은 학생 식당의 줄임말입니다. 2호관식당은 교직원 식당으로 불립니다(혹은 교식). 기식은 기숙사 식당입니다. 전부 소개하지 말고 학생이 질문한 식당의 메뉴만 안내하세요.)\n\n'


def get_detailed_instruct(query: str) -> str:

    kst = ZoneInfo('Asia/Seoul')
    
    now_in_kst = datetime.now(kst)

    today = now_in_kst.strftime('%Y-%m-%d')
    
    return f'Today is {today}. 오늘 날짜는 {today}입니다. 현재 인천대학교는 2024년 2학기 입니다. \nQuestion: {query}' # Query와 관련된 최신 passages를 찾아줘.
    

        
def create_context_string(docs):
    result = ""
    for idx, doc in enumerate(docs, start=1):
        result += f"Context{idx}: {doc.page_content} "
    return result.strip()
        
def custom_chat_loop(llm_chain, retrieval):
    while True:
        print()
        user_msg = input('User: ')
        if user_msg in ('-1', 'exit', 'exit()'):
            print("대화를 종료합니다..")
            return
  
        start_time = time.time()
        
        if is_menu_query(user_msg):
            docs = retrieval.invoke(user_msg)
            context = create_context_string(docs)
            question = get_menu_instruct(user_msg)
            llm_answer = llm_chain.run(context=context, question=question)
            print(question)
        else:
            docs = retrieval.invoke(user_msg)
            context = create_context_string(docs)
            question = get_detailed_instruct(user_msg)
            llm_answer = llm_chain.run(context=context, question=question)
            print(question)

        end_time = time.time()
        answer_time = end_time - start_time
        print()
        print(f'ChatINU: {llm_answer}')
        print(f'답변 시간: {answer_time:.2f}초')
        print()

        print('검색된 문서는 다음과 같습니다:')
        print(docs)
        print(f'총 {len(docs)} 개의 문서가 검색됨.')



def escape_braces(text):
    return text.replace('{', '{{').replace('}', '}}')




custom_prompt_template = """<|im_start|>system
당신은 지금부터 대한민국의 인천대학교(Incheon National University) 재학생들의 질문에 답변하는 챗봇입니다.
당신의 task는 학생들이 입력한 질문 혹은 대화에 적절한 대답을 하는 것입니다.

Context는 학생들이 입력한 텍스트와 의미적으로 유사한 검색된 문서들입니다.
학생들의 질문에 답하기 위해 Context에 있는 정보를 활용하세요.

하지만 검색 성능의 한계로 질문과 관련된 정보가 없을 수 있습니다. 이러한 경우에는 답을 억지로 생성하지 말고 모른다고 솔직하게 답하세요.

Context에 있는 작성일과 기간 정보에 주의하여 현재 시점 기준 유효한 정보만 제공하세요.

Context의 내용을 그대로 답변하지 말고 150글자 이내로 요약해서 답변하세요.

친절한 말투로 답변하세요.

만약 Context의 정보를 활용하여 답변했다면, 답변 후에 참조한 context의 url 링크를 제공해주세요. 

절대로 Context에 존재하지 않는 가짜 링크를 생성하지 마세요.

확실하지 않거나 애매하거나 너무 어려거나 복잡한 질문인 경우에는 직접 링크에 접속하여 자세한 내용을 확인하도록 유도하세요.

만약 인천대학교와 관련 없는 일반적인 질문이나 평상 시의 대화라면 Context를 무시하고 원래대로 대답하고 context의 링크를 제공하지 마세요.<|im_end|>

<|im_start|>user


Context: {context}

{question}

Answer:  <|im_end|><|im_start|>assistant

"""


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--llm', type=str, default='Qwen/Qwen2.5-32B-Instruct-GPTQ-Int8', help="LLM 모델 경로(허깅페이스 주소)")
    parser.add_argument('--emb_model', type=str, default='/media/inuai_02/ChatINU/emb_models/20241006_crawl4ai_gpt-4o-mini/model_epoch_22', help="임베딩 모델 경로(허깅페이스 주소)")
    parser.add_argument('--timestamp', type=str, default='20241012_164820', help="faiss index 생성 시간")
    parser.add_argument('--cuda', type=int, default=3, help="GPU 번호")
    args = parser.parse_args()

    device = args.cuda
    llm_path = args.llm
    timestamp = args.timestamp

    print(f"LLM: {llm_path}")
    print(f"device: {device}")

    
    auth_token = "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"

    
    llm_q = VLLM(
        model=llm_path,
        trust_remote_code=True,
        max_new_tokens=512,
        temperature=0.0,
        vllm_kwargs={"quantization": "gptq_marlin"},
    )


    emb_model_path = args.emb_model
    model_kwargs = {'device': 'cuda'}
    encode_kwargs = {'normalize_embeddings': True}
    ko_embed = HuggingFaceBgeEmbeddings(
        model_name=emb_model_path,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs,
        query_instruction='Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: '
    )

    # 저장했던 FAISS 로드
    faiss_path = os.path.join("faiss", timestamp)
    db = FAISS.load_local(faiss_path, ko_embed, allow_dangerous_deserialization=True)
    faiss_retriever = db.as_retriever(search_kwargs={"k": 5})
  

    

    
    CUSTOM_PROMPT = PromptTemplate(
        template=custom_prompt_template, input_variables=["context", "question"]
    )
    


    llm_chain = LLMChain(llm=llm_q, prompt=CUSTOM_PROMPT)

    
    custom_chat_loop(llm_chain, faiss_retriever)
  
