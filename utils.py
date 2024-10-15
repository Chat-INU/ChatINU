import re
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo

def get_today_menu():
    # 웹사이트의 기본 URL
    base_url = 'https://inucoop.com/main.php?mkey=2&w=4'
    
    # 실제 브라우저처럼 보이도록 헤더 설정
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    # 세션 시작 (쿠키 및 설정 유지)
    session = requests.Session()
    session.headers.update(headers)
    
    # 1단계: 초기 페이지에서 날짜와 sdt 값 가져오기
    response = session.get(base_url)
    if response.status_code != 200:
        print(f"페이지를 가져오지 못했습니다. 상태 코드: {response.status_code}")
        return ""
    
    # 올바른 인코딩 설정
    response.encoding = 'utf-8'  # 필요에 따라 조정
    
    # 초기 페이지 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 폼의 액션 URL 찾기
    form = soup.find('form', attrs={'name': 'menuForm'})
    if not form:
        print("menuForm을 찾을 수 없습니다.")
        return ""
    
    action_url = form['action']
    if not action_url.startswith('http'):
        # 액션이 상대 URL인 경우 전체 URL 생성
        action_url = requests.compat.urljoin(base_url, action_url)
    
    # 2단계: 사용 가능한 날짜와 sdt 값 추출
    dates = []
    date_cells = soup.find_all('td', class_=['yo_mn', 'yo_mns2'])
    for cell in date_cells:
        onclick = cell.get('onclick', '')
        if 'sdt.value' in onclick:
            sdt_value = onclick.split("sdt.value='")[1].split("';")[0]
            date_text = cell.get_text(strip=True)
            dates.append({'sdt': sdt_value, 'date_text': date_text})
    
    # 오늘 날짜 가져오기
    today = datetime.now().strftime('%Y%m%d')
    
    # 오늘의 메뉴 정보 찾기
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
    
    # POST 데이터 준비
    post_data = {
        'jun': '0',  # 폼에서 'jun'은 '0'으로 유지
        'sdt': sdt_value
    }
    
    # POST 요청 제출
    menu_response = session.post(action_url, data=post_data)
    if menu_response.status_code != 200:
        print(f"{date_text}의 메뉴를 가져오지 못했습니다. 상태 코드: {menu_response.status_code}")
        return ""
    
    # 올바른 인코딩 설정
    menu_response.encoding = 'utf-8'  # 필요에 따라 조정
    
    # 메뉴 페이지 파싱
    menu_soup = BeautifulSoup(menu_response.text, 'html.parser')
    
    menu_text = f"=== {date_text}의 메뉴 ===\n\n"
    
    # style="width:960px;"인 모든 테이블 찾기
    tables = menu_soup.find_all('table', attrs={'style': 'width:960px;'})
    
    # 메뉴 파싱 및 텍스트에 저장
    for table in tables:
        # 식당 이름 가져오기
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
    
        # 식사 종류 가져오기
        meal_type_row = canteen_name_row.find_next_sibling('tr')
        meal_type_cells = meal_type_row.find_all('td', class_='td_mn')
        meal_types = [cell.get_text(strip=True) for cell in meal_type_cells]
    
        # 메뉴 가져오기
        menu_row = meal_type_row.find_next_sibling('tr')
        if not menu_row:
            continue
        menu_cells = menu_row.find_all('td', class_=['din_lists', 'td_list'])
        menus = [cell.get_text(separator='\n', strip=True) for cell in menu_cells]
    
        # 메뉴가 없다는 메시지 처리
        if len(menu_cells) == 1 and '오늘 등록된 메뉴가 없습니다' in menus[0]:
            menu_text += f"  {menus[0]}\n"
            continue
    
        # 메뉴를 텍스트에 추가
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
        result += f"### Context {idx}: {doc.page_content}\n\n\n"
    return result.strip()



def load_word_definitions(file_path):
    word_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            word_dict[data["Word"]] = data["WordDefine"]
    return word_dict

# 부분 일치로 메시지에서 단어 정의를 추가하는 함수
def add_definitions_to_message(user_msg, word_dict):
    words = user_msg.split()  # 공백으로 단어를 나눔
    modified_msg = []
    
    for word in words:
        found = False
        for key in word_dict:
            if key in word:  # 부분 일치 여부 확인
                modified_msg.append(f"{word} ({word_dict[key]})")
                found = True
                break
        if not found:
            modified_msg.append(word)
    
    return ' '.join(modified_msg)
