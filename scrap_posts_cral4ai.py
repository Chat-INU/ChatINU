import os
import json
from tqdm import tqdm
from crawl4ai import WebCrawler
import lxml.html

# 기본 URL 정의
base_url = 'https://www.inu.ac.kr'
list_url = f'{base_url}/inu/1516/subview.do'

def collect_data(page_content, data, crawler):
    # HTML 파싱
    tree = lxml.html.fromstring(page_content)
    rows = tree.xpath('//table/tbody/tr')

    if not rows:
        return False  # 이 페이지에 더 이상 게시물이 없음

    for tr in rows:
        a_tag = tr.xpath('.//a')[0]
        href = a_tag.get('href')
        full_url = f"{base_url}{href}"
        title_tag = a_tag.xpath('.//strong')[0]
        date_tag = tr.xpath('.//td[contains(@class, "td-date")]')[0]
        writer_tag = tr.xpath('.//td[contains(@class, "td-write")]')[0]

        title = title_tag.text_content().strip().replace('/', '-')
        date = date_tag.text_content().strip()
        writer = writer_tag.text_content().strip()

        # 수집 중단 조건
        if date == "2023.12.04":
            print("수집 중단 조건 충족.")
            return False

        try:
            result = crawler.run(url=full_url, css_selector='.view-con')
            contents = result.markdown
            detail_page_content = result.html
            detail_tree = lxml.html.fromstring(detail_page_content)

            # 파일 첨부 정보 수집
            attachment = {}
            view_file_div = detail_tree.xpath('//div[contains(@class, "view-file")]')
            if view_file_div:
                file_links = view_file_div[0].xpath('.//a')
                for idx, file_a_tag in enumerate(file_links, start=1):
                    file_url = file_a_tag.get('href')
                    file_name = file_a_tag.text_content().strip()
                    attachment[f"file_{idx}"] = {
                        "name": file_name,
                        "url": f"{base_url}{file_url}"
                    }
        except Exception as e:
            print(f"상세 페이지를 가져오는 중 오류 발생: {e}")
            contents = ''
            attachment = {}

        key = f"인천대소식 > 학사 > {title}"
        data[key] = {
            "title": title,
            "url": full_url,
            "date": date,
            "writer": writer,
            "contents": contents,
            "attachment": attachment
        }

        result_path = os.path.join('data', 'crawl4ai', 'inu_news_posts', key)
        if not os.path.exists(result_path):
            os.makedirs(result_path)
            print(f"디렉토리가 생성되었습니다: {result_path}")

        filename = f"data.json"
        filepath = os.path.join(result_path, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as json_file:
            json.dump(data[key], json_file, ensure_ascii=False, indent=4)
    return True

def main():
    data = {}
    page_number = 1
    stop_collecting = False

    crawler = WebCrawler()
    crawler.warmup()

    while not stop_collecting:
        next_page_url = f"{base_url}/inu/1516/subview.do?page={page_number}"
        try:
            result = crawler.run(url=next_page_url)
            page_content = result.html
        except Exception as e:
            print(f"페이지 {page_number}를 불러오는데 실패했습니다: {e}")
            break

        stop_collecting = not collect_data(page_content, data, crawler)
        if stop_collecting:
            break

        print(f"{page_number} 페이지 수집 완료.")
        page_number += 1

    print("데이터가 성공적으로 저장되었습니다.")

if __name__ == '__main__':
    main()
