import os
os.environ["CUDA_VISIBLE_DEVICES"]= "1"
import json
import argparse
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import VLLM
from langchain.chains import RetrievalQA, LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_teddynote.retrievers import OktBM25Retriever
import time
import torch
from transformers import pipeline
import utils

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


os.environ["OPENAI_API_KEY"] = ""


        
def custom_chat_loop(llm_chain, keyword_llm, semantic_retriever, bm25_retriever):
    
    word_file_path = 'word.jsonl'
    word_definitions = utils.load_word_definitions(word_file_path)
    
    
    while True:
        print()
        user_msg = input('User: ')
        if user_msg in ('-1', 'exit', 'exit()'):
            print("대화를 종료합니다..")
            return
  
        start_time = time.time()
        
        
        user_msg = utils.add_definitions_to_message(user_msg, word_definitions)
        
        
        messages = [
            {"role": "user", "content": f"{user_msg}\n\n위 질문의 키워드는? 딱 키워드만 생성하세요\n\n키워드: "},
        ]

        outputs = keyword_llm(messages, max_new_tokens=256)
        keyword = outputs[0]["generated_text"][-1]["content"].strip()
        print("Keyword: ", keyword)
        
        semantic_docs = semantic_retriever.invoke(user_msg)
        keyword_docs = bm25_retriever.invoke(keyword)
        total_docs = semantic_docs + keyword_docs
        
        if utils.is_menu_query(user_msg):
            context = utils.create_context_string(total_docs)
            question = utils.get_menu_instruct(user_msg)
            llm_answer = llm_chain.run(context=context, question=question)
            print(question)
        else:
            context = utils.create_context_string(total_docs)
            question = utils.get_detailed_instruct(user_msg)
            llm_answer = llm_chain.run(context=context, question=question)
            print(question)

        end_time = time.time()
        answer_time = end_time - start_time
        print()
        print(f'ChatINU: {llm_answer}')
        print(f'답변 시간: {answer_time:.2f}초')
        print()

        print('검색된 문서는 다음과 같습니다:')
        print(total_docs)
        print(f'총 {len(total_docs)} 개의 문서가 검색됨.')





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

만약 인천대학교와 관련 없는 일반적인 질문이나 평상 시의 대화라면 Context를 무시하고 원래대로 대답하고 context의 링크를 제공하지 마세요. <|im_end|>

<|im_start|>user


Context: {context}

{question}

Answer: <|im_end|><|im_start|>assistant

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

    
    auth_token = ""

    
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
    faiss_retriever = db.as_retriever(search_kwargs={"k": 4})
    
    
    chunk_path =  os.path.join("chunks", timestamp, 'chunk_list.json')
    chunk_metadata_path = os.path.join("chunks", timestamp, 'metadata_list.json')
    
    with open(chunk_path, 'r', encoding='utf-8') as file:
        docs_chunks = json.load(file)
    
    with open(chunk_metadata_path, 'r', encoding='utf-8') as file:
        chunks_metadatas = json.load(file)
    
    okt_retrieval = OktBM25Retriever.from_texts(docs_chunks, metadatas=chunks_metadatas)
    okt_retrieval.k = 4
    
    
    CUSTOM_PROMPT = PromptTemplate(
        template=custom_prompt_template, input_variables=["context", "question"]
    )
    

    llm_chain = LLMChain(llm=llm_q, prompt=CUSTOM_PROMPT)
    
    
    keyword_pipe = pipeline(
        "text-generation",
        model="google/gemma-2-2b-it",
        model_kwargs={"torch_dtype": torch.bfloat16},
        device="cuda",  # replace with "mps" to run on a Mac device
    )

    
    custom_chat_loop(llm_chain, keyword_pipe, faiss_retriever, okt_retrieval)
