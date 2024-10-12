import os
import json
from tqdm import tqdm
import data
from crawl4ai import WebCrawler

def scrap_from_dict(url_dict):
    
    crawler = WebCrawler() 
    crawler.warmup()

    for key, value in tqdm(url_dict.items()):
        try:
            result = crawler.run(url=value, css_selector='.wrap-contents')  

            text = result.markdown

            metadata = {
                'url': value,
                'category': key,
            }

            json_data = {
                'content': text,
                'metadata': metadata
            }

            key_sanitized = key.replace('/', '_')

            result_path = os.path.join('data', 'crawl4ai', 'main_homepage_urls', key_sanitized)
            if not os.path.exists(result_path):
                os.makedirs(result_path)
                print(f"디렉토리가 생성되었습니다: {result_path}")

            file_path = os.path.join(result_path, 'contents_class_html.json')
            with open(file_path, "w", encoding='utf-8') as f:
                json.dump(json_data, f, indent=4, ensure_ascii=False)

        except Exception as e:
            print(f"URL 처리 중 오류가 발생했습니다 ({value}): {e}")

if __name__ == '__main__':
    url_dict = data.main_homepage
    scrap_from_dict(url_dict)
