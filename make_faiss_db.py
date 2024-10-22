# 스크랩한 문서를 전처리하고 split하여 각각의 임베딩을 구하고 FAISS로 index 만들어 로컬에 저장
import os
import re
import json
import datetime
import argparse
from langchain.text_splitter import RecursiveCharacterTextSplitter, TextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_text_splitters import MarkdownHeaderTextSplitter

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--urls_path', type=str, default='data/crawl4ai/main_homepage_urls', help="스크랩한 파일들이 저장된 폴더의 root 위치")
    parser.add_argument('--posts_path', type=str, default='data/posts', help="스크랩한 파일들이 저장된 폴더의 root 위치")
    parser.add_argument('--emb_model', type=str, default='emb_models/20241017_crawl4ai_gpt-4o-mini/model_epoch_23', help="임베딩 모델 경로")
    args = parser.parse_args()

    
    urls_root_path = args.urls_path
    posts_root_path = args.posts_path

    urls_paths = []
    for root, dirs, files in os.walk(urls_root_path):
        for dir_name in dirs:
            urls_paths.append(os.path.join(root, dir_name))
            
    posts_paths = []
    for root, dirs, files in os.walk(posts_root_path):
        for dir_name in dirs:
            posts_paths.append(os.path.join(root, dir_name))
            

    
    print(f"URL 수: {len(urls_paths)}")

    url_docs = []
    url_metadatas = []
    
    # url 데이터
    for data_path in urls_paths:
        file_path = os.path.join(data_path, 'contents_class_html.json')

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        text = data['content']
        # text = re.sub(r'(\t)\1+', r'\1', text)
        # text = re.sub(r'(\n)\1+', r'\1', text)
        # text = re.sub(r'(\n\s*){2,}', r'\n', text)
        # text = re.sub(r' {5,}', '', text)
        
        
        text = re.sub(r"\\\\", "", text)
        text = re.sub(r"fnctId=sitemenu,menuViewType=tab", "", text)
        text = re.sub(r"/WEB-INF/jsp/k2web/com/cop/site/layout.jsp inu_sub", "", text)
        text = re.sub(r"/WEB-INF/jsp/k2web/com/cop/site/layout.jsp\r\n\tinu_sub\r", "", text)

        url_docs.append(text)

        metadata = {'category': f"인천대학교 홈페이지의 {data['metadata']['category']} 에 있는 정보입니다.", "url": data['metadata']['url']}
        url_metadatas.append(metadata)
    
    
    print(f"게시판에서 크롤링된 게시물 수: {len(posts_paths)}")
    
    post_docs = []
    post_metadatas = []
        
    # 게시판 형태 수집 데이터
    for data_path in posts_paths:
        file_path = os.path.join(data_path, 'data.json')

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        text = data['contents']
        post_docs.append(text)

        metadata = {'title': data['title'], 'url':data['url'], 'date': data['date'], 'files': []}
        if "attachment" in data and data["attachment"]:
            for key, file_info in data["attachment"].items():
                metadata['files'].append(file_info['url'])
        
        post_metadatas.append(metadata)
    
        
        

    # 문서를 분할할 헤더 레벨과 해당 레벨의 이름을 정의합니다.
    headers_to_split_on = [  
        (
            "#",
            "Header 1",
        ),  
        (
            "##",
            "Header 2",
        ),  
        (
            "###",
            "Header 3",
        ), 
    ]
    
    text_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False)
    
    

    url_chunks = []
    url_chunks_metadatas = []

    for text, meta_d in zip(url_docs,url_metadatas):
        chunks = text_splitter.split_text(text)
        chunks = [ meta_d['category'] + '\n' + chunk.page_content + '\n출처: ' + meta_d['url'] + '\n\n'  for chunk in chunks ]
        url_chunks.extend(chunks)
        url_chunks_metadatas.extend([meta_d] * len(chunks))

    print('url chunk sample:')
    
    for ck in  url_chunks[50:]:
        print(ck)

    print()
    print('-------------')
    
    

    post_chunks = []
    posts_chunks_metadatas = []

    for text, meta_d in zip(post_docs,post_metadatas):
        chunks = text_splitter.split_text(text)
        chunks = [ f"제목: {meta_d['title']}\n작성일: {meta_d['date']}\n" + chunk.page_content + '\n출처: ' + meta_d['url'] + '\n\n첨부파일: ' + ', '.join(meta_d['files']) + '\n\n' for chunk in chunks ] # 
        post_chunks.extend(chunks)
        posts_chunks_metadatas.extend([meta_d] * len(chunks))

    print('crawled_data chunk sample:')
    print(post_chunks[0])
    print(posts_chunks_metadatas[0])



    total_chunck = url_chunks + post_chunks #+ menu_chunks
    total_metadata = url_chunks_metadatas + posts_chunks_metadatas #+ menu_chunks_metadatas

    print(f"전체 Chunk 수: {len(total_chunck)}")
    #print(chunks_metadatas)

   
    
    model_name = args.emb_model
    model_kwargs = {'device': 'cuda',
                    'trust_remote_code': True}
    encode_kwargs = {'normalize_embeddings': True}

    ko_embed = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs,
        query_instruction= f'Instruct: Given a web search query, retrieve relevant passages that answer the query. \nQuery: '
    )

    print('임베딩을 구합니다..')
    db = FAISS.from_texts(
        texts = total_chunck,
        embedding=ko_embed,
        metadatas=total_metadata
    )

   
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    faiss_path = 'faiss'

    if not os.path.exists(faiss_path):
        os.makedirs(faiss_path)
        print(f"Directory created: {faiss_path}")

    index_path = os.path.join(faiss_path, timestamp)
    print(f'{index_path}에 faiss_index를 저장합니다..')
    db.save_local(index_path)
    
    
    chunk_path = os.path.join('chunks', timestamp)
    if not os.path.exists(chunk_path):
        os.makedirs(chunk_path)
        print(f"Directory created: {chunk_path}")
       
       

    print(f'{chunk_path}에 분할된 chunk들과 메타데이터를 저장합니다..')

    with open(os.path.join(chunk_path, 'chunk_list.json'), 'w', encoding='utf-8') as file:
        json.dump(total_chunck, file, ensure_ascii=False, indent=4)
    
    with open(os.path.join(chunk_path, 'metadata_list.json'), 'w', encoding='utf-8') as file:
        json.dump(total_metadata, file, ensure_ascii=False, indent=4)
        
