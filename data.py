# 인천대학교 홈페이지 https://www.inu.ac.kr에 있는 웹 문서들을 수집하고 전처리하여 json 파일로 저장하는 코드

main_homepage = {

  # 대학생활 탭
  
  '대학생활 > 학생지원 > 장학금 > 교내장학금': 'https://www.inu.ac.kr/inu/840/subview.do',
  '대학생활 > 학생지원 > 장학금 > 교외장학금': 'https://www.inu.ac.kr/inu/841/subview.do',
  '대학생활 > 학생지원 > 장학금 > 국가장학금': 'https://www.inu.ac.kr/inu/842/subview.do',
  '대학생활 > 학생지원 > 장학금 > 국가근로장학금': 'https://www.inu.ac.kr/inu/843/subview.do',
  '대학생활 > 학생지원 > 등록금 > 등록금정책': 'https://www.inu.ac.kr/inu/844/subview.do',
  '대학생활 > 학생지원 > 등록금 > 등록안내': 'https://www.inu.ac.kr/inu/845/subview.do',
  '대학생활 > 학생지원 > 등록금 > 분할납부': 'https://www.inu.ac.kr/inu/846/subview.do',
  '대학생활 > 학생지원 > 등록금 > 자주묻는질문': 'https://www.inu.ac.kr/inu/846/subview.do',
  '대학생활 > 학생지원 > 증명발급': 'https://www.inu.ac.kr/inu/638/subview.do',
  '대학생활 > 학생지원 > 학생증발급': 'https://www.inu.ac.kr/inu/639/subview.do',
  '대학생활 > 학생지원 > 병무행정,예비군 > 병사행정': 'https://www.inu.ac.kr/inu/848/subview.do',
  '대학생활 > 학생지원 > 병무행정,예비군 > 예비군연대': 'https://www.inu.ac.kr/inu/849/subview.do',
  '대학생활 > 학생지원 > IT서비스': 'https://www.inu.ac.kr/inu/641/subview.do',
  '대학생활 > 학생지원 > 편의,복지': 'https://www.inu.ac.kr/inu/642/subview.do',
  '대학생활 > 학생지원 > 식당메뉴': 'https://www.inu.ac.kr/inu/643/subview.do', # 정보 불확실, 소비자 협동조합 홈페이지 데이터(https://inucoop.com/main.php?mkey=2&w=2&l=1)를 사용하는게 더 좋을 듯.
  '대학생활 > 학생지원 > 기숙사': 'https://www.inu.ac.kr/inu/644/subview.do',
  '대학생활 > 학생지원 > 보건진료소 > 송도캠퍼스': 'https://www.inu.ac.kr/inu/857/subview.do',
  '대학생활 > 학생지원 > 보건진료소 > 공지사항': 'https://www.inu.ac.kr/inu/858/subview.do', # 게시판 형태
  '대학생활 > 학생지원 > 보건진료소 > Q&A': 'https://www.inu.ac.kr/inu/859/subview.do', # 게시판 형태
  '대학생활 > 학생지원 > 보건진료소 > 보건교육': 'https://www.inu.ac.kr/inu/860/subview.do', # 게시판 형태
  '대학생활 > 학사안내 > 학사일정': 'https://www.inu.ac.kr/inu/651/subview.do', # 월별로 페이지 다름
  '대학생활 > 학사안내 > 수업 > 수강신청': 'https://www.inu.ac.kr/inu/653/subview.do',
  '대학생활 > 학사안내 > 수업 > 출결': 'https://www.inu.ac.kr/inu/11548/subview.do',
  '대학생활 > 학사안내 > 수업 > 계절학기': 'https://www.inu.ac.kr/inu/656/subview.do',
  '대학생활 > 학사안내 > 수업 > 학점교류안내': 'https://www.inu.ac.kr/inu/667/subview.do',
  '대학생활 > 학사안내 > 성적 > 시험,성적': 'https://www.inu.ac.kr/inu/655/subview.do',
  '대학생활 > 학사안내 > 성적 > 재수강,재이수': 'https://www.inu.ac.kr/inu/654/subview.do',
  '대학생활 > 학사안내 > 전공 > 부전공,복수전공': 'https://www.inu.ac.kr/inu/659/subview.do',
  '대학생활 > 학사안내 > 전공 > 연계전공': 'https://www.inu.ac.kr/inu/661/subview.do',
  '대학생활 > 학사안내 > 전공 > 전과,전공배정': 'https://www.inu.ac.kr/inu/662/subview.do',
  '대학생활 > 학사안내 > 전공 > 전공심화트랙': 'https://www.inu.ac.kr/inu/652/subview.do',
  '대학생활 > 학사안내 > 학적 > 휴복학': 'https://www.inu.ac.kr/inu/658/subview.do',
  '대학생활 > 학사안내 > 학적 > 제적': 'https://www.inu.ac.kr/inu/660/subview.do',
  '대학생활 > 학사안내 > 학적 > 학사징계': 'https://www.inu.ac.kr/inu/664/subview.do',
  '대학생활 > 학사안내 > 학적 > 재입학': 'https://www.inu.ac.kr/inu/663/subview.do',
  '대학생활 > 학사안내 > 학적 > 학적부기재사항정정': 'https://www.inu.ac.kr/inu/668/subview.do',
  '대학생활 > 학사안내 > 졸업 > 수료,졸업': 'https://www.inu.ac.kr/inu/666/subview.do',
  '대학생활 > 학사안내 > 졸업 > 영어졸업인증제': 'https://www.inu.ac.kr/inu/665/subview.do',
  '대학생활 > 학사안내 > 졸업 > 평생교육사': 'https://www.inu.ac.kr/inu/657/subview.do',
  '대학생활 > 학사안내 > 양식자료실': 'https://www.inu.ac.kr/inu/669/subview.do', # 게시판 형태 (카테고리별)
  
  '대학생활 > 열린강좌 > 한국어교육센터': 'https://www.inu.ac.kr/inu/670/subview.do',
  '대학생활 > 열린강좌 > 외국어교육센터': 'https://www.inu.ac.kr/inu/671/subview.do',
  '대학생활 > 열린강좌 > 공자학원': 'https://www.inu.ac.kr/inu/672/subview.do',
  '대학생활 > 열린강좌 > 평생교육트라이버시티': 'https://www.inu.ac.kr/inu/673/subview.do',
  '대학생활 > 열린강좌 > 정보전산원': 'https://www.inu.ac.kr/inu/674/subview.do',
  '대학생활 > 열린강좌 > 스포츠센터': 'https://www.inu.ac.kr/inu/675/subview.do',
  
  '대학생활 > 학생활동 > 동아리': 'https://www.inu.ac.kr/inu/11707/subview.do', # 각 동아리 링크 존재
  '대학생활 > 학생활동 > 동아리 > 효월검우회' : 'https://www.inu.ac.kr/inu/887/subview.do',
  '대학생활 > 학생활동 > 동아리 > 돌핀' : 'https://www.inu.ac.kr/inu/883/subview.do',
  '대학생활 > 학생활동 > 동아리 > UITC' : 'https://www.inu.ac.kr/inu/884/subview.do',
  '대학생활 > 학생활동 > 동아리 > 바이킹' : 'https://www.inu.ac.kr/inu/882/subview.do',
  '대학생활 > 학생활동 > 동아리 > PANG' : 'https://www.inu.ac.kr/inu/877/subview.do',
  '대학생활 > 학생활동 > 동아리 > 다크호스' : 'https://www.inu.ac.kr/inu/880/subview.do',
  '대학생활 > 학생활동 > 동아리 > INU W FC' : 'https://www.inu.ac.kr/inu/878/subview.do',
  '대학생활 > 학생활동 > 동아리 > 퍼펙트' : 'https://www.inu.ac.kr/inu/881/subview.do',
  '대학생활 > 학생활동 > 동아리 > 산악부 UIAC' : 'https://www.inu.ac.kr/inu/885/subview.do',
  '대학생활 > 학생활동 > 동아리 > 싸우라비' : 'https://www.inu.ac.kr/inu/879/subview.do',
  '대학생활 > 학생활동 > 동아리 > BOSS' : 'https://www.inu.ac.kr/inu/11443/subview.do',
  '대학생활 > 학생활동 > 동아리 > INU START W' : 'https://www.inu.ac.kr/inu/11444/subview.do',
  '대학생활 > 학생활동 > 동아리 > 별천지' : 'https://www.inu.ac.kr/inu/898/subview.do',
  '대학생활 > 학생활동 > 동아리 > 기우회' : 'https://www.inu.ac.kr/inu/899/subview.do',
  '대학생활 > 학생활동 > 동아리 > 셔플' : 'https://www.inu.ac.kr/inu/900/subview.do',
  '대학생활 > 학생활동 > 동아리 > 유스호스텔' : 'https://www.inu.ac.kr/inu/901/subview.do',
  '대학생활 > 학생활동 > 동아리 > 하양검정' : 'https://www.inu.ac.kr/inu/902/subview.do',
  '대학생활 > 학생활동 > 동아리 > 한아랑' : 'https://www.inu.ac.kr/inu/903/subview.do',
  '대학생활 > 학생활동 > 동아리 > 인유공방' : 'https://www.inu.ac.kr/inu/897/subview.do',
  '대학생활 > 학생활동 > 동아리 > 보.인.다' : 'https://www.inu.ac.kr/inu/896/subview.do', 
  '대학생활 > 학생활동 > 동아리 > Cookinu' : 'https://www.inu.ac.kr/inu/11447/subview.do',
  
  '대학생활 > 학생활동 > 동아리 > 멋쟁이사자처럼' : 'https://www.inu.ac.kr/inu/888/subview.do',
  '대학생활 > 학생활동 > 동아리 > I\'M아임' : 'https://www.inu.ac.kr/inu/889/subview.do',
  '대학생활 > 학생활동 > 동아리 > unexpecTED' : 'https://www.inu.ac.kr/inu/890/subview.do',
  '대학생활 > 학생활동 > 동아리 > 세치혀' : 'https://www.inu.ac.kr/inu/891/subview.do',
  '대학생활 > 학생활동 > 동아리 > 아르고나우츠' : 'https://www.inu.ac.kr/inu/892/subview.do',
  '대학생활 > 학생활동 > 동아리 > DT(독서토론마당)' : 'https://www.inu.ac.kr/inu/893/subview.do',
  '대학생활 > 학생활동 > 동아리 > 영어토론회 EDA' : 'https://www.inu.ac.kr/inu/894/subview.do',
  '대학생활 > 학생활동 > 동아리 > PINCOM' : 'https://www.inu.ac.kr/inu/895/subview.do',
  '대학생활 > 학생활동 > 동아리 > 하늬울림' : 'https://www.inu.ac.kr/inu/872/subview.do',
  '대학생활 > 학생활동 > 동아리 > INUO' : 'https://www.inu.ac.kr/inu/866/subview.do',
  '대학생활 > 학생활동 > 동아리 > 함성' : 'https://www.inu.ac.kr/inu/873/subview.do',
  '대학생활 > 학생활동 > 동아리 > 포크라인' : 'https://www.inu.ac.kr/inu/876/subview.do',
  '대학생활 > 학생활동 > 동아리 > 인스디스' : 'https://www.inu.ac.kr/inu/867/subview.do',
  '대학생활 > 학생활동 > 동아리 > 인인극회' : 'https://www.inu.ac.kr/inu/871/subview.do',
  '대학생활 > 학생활동 > 동아리 > 젊은영상' : 'https://www.inu.ac.kr/inu/875/subview.do',
  '대학생활 > 학생활동 > 동아리 > 크레퍼스' : 'https://www.inu.ac.kr/inu/868/subview.do',
  '대학생활 > 학생활동 > 동아리 > 파이오니아' : 'https://www.inu.ac.kr/inu/870/subview.do',
  '대학생활 > 학생활동 > 동아리 > 로타렉트' : 'https://www.inu.ac.kr/inu/915/subview.do',
  '대학생활 > 학생활동 > 동아리 > 초아다솜' : 'https://www.inu.ac.kr/inu/912/subview.do',
  '대학생활 > 학생활동 > 동아리 > 느을사랑' : 'https://www.inu.ac.kr/inu/914/subview.do',
  '대학생활 > 학생활동 > 동아리 > 뫼골둥지' : 'https://www.inu.ac.kr/inu/913/subview.do',
  '대학생활 > 학생활동 > 동아리 > JDM' : 'https://www.inu.ac.kr/inu/905/subview.do',
  '대학생활 > 학생활동 > 동아리 > JOY선교회' : 'https://www.inu.ac.kr/inu/911/subview.do',
  '대학생활 > 학생활동 > 동아리 > CMI' : 'https://www.inu.ac.kr/inu/907/subview.do',
  '대학생활 > 학생활동 > 동아리 > CFM' : 'https://www.inu.ac.kr/inu/904/subview.do',
  '대학생활 > 학생활동 > 동아리 > 예수전도단(YWAM)' : 'https://www.inu.ac.kr/inu/910/subview.do',
  '대학생활 > 학생활동 > 동아리 > CCC' : 'https://www.inu.ac.kr/inu/908/subview.do',
  '대학생활 > 학생활동 > 동아리 > IVF' : 'https://www.inu.ac.kr/inu/906/subview.do',
  '대학생활 > 학생활동 > 동아리 > 카톨릭학생회' : 'https://www.inu.ac.kr/inu/909/subview.do',
  
  '대학생활 > 학생활동 > 동아리 > 댄스동아리 I.U.D.C' : 'https://www.inu.ac.kr/inu/869/subview.do',
  '대학생활 > 학생활동 > 동아리 > 풍물패 울림' : 'https://www.inu.ac.kr/inu/874/subview.do',
  
  
  ###### ----------------------------------------------------------------------------------  ######
  
  
  # 대학/대학원 (대학 탭만)
  
  '대학/대학원 > 대학 > 대학전체' : 'https://www.inu.ac.kr/inu/602/subview.do',
  '대학/대학원 > 대학 > 인문대학 > 전체' : 'https://www.inu.ac.kr/inu/753/subview.do',
  '대학/대학원 > 대학 > 인문대학 > 국어국문학과' : 'https://www.inu.ac.kr/inu/754/subview.do',
  '대학/대학원 > 대학 > 인문대학 > 영어영문학과' : 'https://www.inu.ac.kr/inu/755/subview.do',
  '대학/대학원 > 대학 > 인문대학 > 독어독문학과' : 'https://www.inu.ac.kr/inu/756/subview.do',
  '대학/대학원 > 대학 > 인문대학 > 불어불문학과' : 'https://www.inu.ac.kr/inu/757/subview.do',
  '대학/대학원 > 대학 > 인문대학 > 일본지역문화학과' : 'https://www.inu.ac.kr/inu/758/subview.do',
  '대학/대학원 > 대학 > 인문대학 > 중어중국학과' : 'https://www.inu.ac.kr/inu/759/subview.do',
  '대학/대학원 > 대학 > 자연과학대학 > 전체' : 'https://www.inu.ac.kr/inu/760/subview.do',
  '대학/대학원 > 대학 > 자연과학대학 > 수학과' : 'https://www.inu.ac.kr/inu/761/subview.do',
  '대학/대학원 > 대학 > 자연과학대학 > 물리학과' : 'https://www.inu.ac.kr/inu/762/subview.do',
  '대학/대학원 > 대학 > 자연과학대학 > 화학과' : 'https://www.inu.ac.kr/inu/763/subview.do',
  '대학/대학원 > 대학 > 자연과학대학 > 패션산업학과' : 'https://www.inu.ac.kr/inu/764/subview.do',
  '대학/대학원 > 대학 > 자연과학대학 > 해양학과' : 'https://www.inu.ac.kr/inu/765/subview.do',
  '대학/대학원 > 대학 > 사회과학대과 > 전체' : 'https://www.inu.ac.kr/inu/766/subview.do',
  '대학/대학원 > 대학 > 사회과학대과 > 사회복지학과' : 'https://www.inu.ac.kr/inu/767/subview.do',
  '대학/대학원 > 대학 > 사회과학대과 > 미디어커뮤니케이션학과' : 'https://www.inu.ac.kr/inu/768/subview.do',
  '대학/대학원 > 대학 > 사회과학대과 > 문헌정보학과' : 'https://www.inu.ac.kr/inu/769/subview.do',
  '대학/대학원 > 대학 > 사회과학대과 > 창의인재개발학과' : 'https://www.inu.ac.kr/inu/770/subview.do',
  '대학/대학원 > 대학 > 글로벌정경대학 > 전체' : 'https://www.inu.ac.kr/inu/772/subview.do',
  '대학/대학원 > 대학 > 글로벌정경대학 > 행정학과' : 'https://www.inu.ac.kr/inu/773/subview.do',
  '대학/대학원 > 대학 > 글로벌정경대학 > 정치외교학과' : 'https://www.inu.ac.kr/inu/774/subview.do',
  '대학/대학원 > 대학 > 글로벌정경대학 > 경제학과' : 'https://www.inu.ac.kr/inu/775/subview.do',
  '대학/대학원 > 대학 > 글로벌정경대학 > 무역학부' : 'https://www.inu.ac.kr/inu/776/subview.do',
  '대학/대학원 > 대학 > 글로벌정경대학 > 소비자학과' : 'https://www.inu.ac.kr/inu/777/subview.do',
  '대학/대학원 > 대학 > 공과대학 > 전체' : 'https://www.inu.ac.kr/inu/778/subview.do',
  '대학/대학원 > 대학 > 공과대학 > 기계공학과' : 'https://www.inu.ac.kr/inu/779/subview.do',
  '대학/대학원 > 대학 > 공과대학 > 전기공학과' : 'https://www.inu.ac.kr/inu/781/subview.do',
  '대학/대학원 > 대학 > 공과대학 > 전자공학과' : 'https://www.inu.ac.kr/inu/782/subview.do',
  '대학/대학원 > 대학 > 공과대학 > 산업경영공학과' : 'https://www.inu.ac.kr/inu/783/subview.do',
  '대학/대학원 > 대학 > 공과대학 > 신소재공학과' : 'https://www.inu.ac.kr/inu/784/subview.do',
  '대학/대학원 > 대학 > 공과대학 > 안전공학과' : 'https://www.inu.ac.kr/inu/785/subview.do',
  '대학/대학원 > 대학 > 공과대학 > 에너지화학공학과' : 'https://www.inu.ac.kr/inu/786/subview.do',
  '대학/대학원 > 대학 > 공과대학 > 바이오-로봇시스템공학과' : 'https://www.inu.ac.kr/inu/780/subview.do',
  '대학/대학원 > 대학 > 정보기술대학 > 전체' : 'https://www.inu.ac.kr/inu/787/subview.do',
  '대학/대학원 > 대학 > 정보기술대학 > 컴퓨터공학부' : 'https://www.inu.ac.kr/inu/788/subview.do',
  '대학/대학원 > 대학 > 정보기술대학 > 정보통신공학과' : 'https://www.inu.ac.kr/inu/789/subview.do',
  '대학/대학원 > 대학 > 정보기술대학 > 임베디드시스템공학과' : 'https://www.inu.ac.kr/inu/790/subview.do',
  '대학/대학원 > 대학 > 경영대학 > 전체' : 'https://www.inu.ac.kr/inu/791/subview.do',
  '대학/대학원 > 대학 > 경영대학 > 경영학부' : 'https://www.inu.ac.kr/inu/792/subview.do',
  '대학/대학원 > 대학 > 경영대학 > 데이터과학과' : 'https://www.inu.ac.kr/inu/793/subview.do',
  '대학/대학원 > 대학 > 경영대학 > 세무회계학과' : 'https://www.inu.ac.kr/inu/794/subview.do',
  '대학/대학원 > 대학 > 예술체육대학 > 전체' : 'https://www.inu.ac.kr/inu/796/subview.do',
  '대학/대학원 > 대학 > 예술체육대학 > 조형예술학부' : 'https://www.inu.ac.kr/inu/797/subview.do',
  '대학/대학원 > 대학 > 예술체육대학 > 디자인학부' : 'https://www.inu.ac.kr/inu/799/subview.do',
  '대학/대학원 > 대학 > 예술체육대학 > 공연예술학과' : 'https://www.inu.ac.kr/inu/800/subview.do',
  '대학/대학원 > 대학 > 예술체육대학 > 소프츠과학부' : 'https://www.inu.ac.kr/inu/801/subview.do',
  '대학/대학원 > 대학 > 예술체육대학 > 운동건강학부' : 'https://www.inu.ac.kr/inu/802/subview.do',
  '대학/대학원 > 대학 > 사범대학 > 전체' : 'https://www.inu.ac.kr/inu/803/subview.do',
  '대학/대학원 > 대학 > 사범대학 > 국어교육과' : 'https://www.inu.ac.kr/inu/804/subview.do',
  '대학/대학원 > 대학 > 사범대학 > 영어교육과' : 'https://www.inu.ac.kr/inu/805/subview.do',
  '대학/대학원 > 대학 > 사범대학 > 일어교육과' : 'https://www.inu.ac.kr/inu/806/subview.do',
  '대학/대학원 > 대학 > 사범대학 > 수학교육과' : 'https://www.inu.ac.kr/inu/807/subview.do',
  '대학/대학원 > 대학 > 사범대학 > 체육교육과' : 'https://www.inu.ac.kr/inu/808/subview.do',
  '대학/대학원 > 대학 > 사범대학 > 유아교육과' : 'https://www.inu.ac.kr/inu/809/subview.do',
  '대학/대학원 > 대학 > 사범대학 > 역사교육과' : 'https://www.inu.ac.kr/inu/810/subview.do',
  '대학/대학원 > 대학 > 사범대학 > 윤리교육과' : 'https://www.inu.ac.kr/inu/811/subview.do',
  '대학/대학원 > 대학 > 도시과학대학 > 전체' : 'https://www.inu.ac.kr/inu/812/subview.do',
  '대학/대학원 > 대학 > 도시과학대학 > 도시행정학과' : 'https://www.inu.ac.kr/inu/813/subview.do',
  '대학/대학원 > 대학 > 도시과학대학 > 건설환경공학' : 'https://www.inu.ac.kr/inu/814/subview.do',
  '대학/대학원 > 대학 > 도시과학대학 > 환경공학' : 'https://www.inu.ac.kr/inu/815/subview.do',
  '대학/대학원 > 대학 > 도시과학대학 > 도시공학과' : 'https://www.inu.ac.kr/inu/816/subview.do',
  '대학/대학원 > 대학 > 도시과학대학 > 건축공학' : 'https://www.inu.ac.kr/inu/817/subview.do',
  '대학/대학원 > 대학 > 도시과학대학 > 도시건축학' : 'https://www.inu.ac.kr/inu/818/subview.do',
  '대학/대학원 > 대학 > 생명과학기술대학 > 전체' : 'https://www.inu.ac.kr/inu/819/subview.do',
  '대학/대학원 > 대학 > 생명과학기술대학 > 생명과학부(생명과학전공)' : 'https://www.inu.ac.kr/inu/820/subview.do',
  '대학/대학원 > 대학 > 생명과학기술대학 > 생명과학부(분자의생명전공)' : 'https://www.inu.ac.kr/inu/821/subview.do',
  '대학/대학원 > 대학 > 생명과학기술대학 > 생명공학부(생명공학전공)' : 'https://www.inu.ac.kr/inu/822/subview.do',
  '대학/대학원 > 대학 > 생명과학기술대학 > 생명공학부(나노바이오공학전공)' : 'https://www.inu.ac.kr/inu/823/subview.do',
  '대학/대학원 > 대학 > 동북아국제통상물류학부 > 전체' : 'https://www.inu.ac.kr/inu/824/subview.do',
  '대학/대학원 > 대학 > 동북아국제통상물류학부 > 동북아국제통상전공' : 'https://www.inu.ac.kr/inu/825/subview.do',
  '대학/대학원 > 대학 > 동북아국제통상물류학부 > 스마트물류공학전공' : 'https://www.inu.ac.kr/inu/826/subview.do',
  '대학/대학원 > 대학 > 동북아국제통상물류학부 > IBE전공' : 'https://www.inu.ac.kr/inu/827/subview.do',
  '대학/대학원 > 대학 > 법학부' : 'https://www.inu.ac.kr/inu/616/subview.do',
  
  
  ###### ----------------------------------------------------------------------------------  ######
  
  
  # 대학소개 탭
  
  '대학소개 > 총장실 > 인사말': 'https://www.inu.ac.kr/inu/708/subview.do',
  '대학소개 > 총장실 > 프로필': 'https://www.inu.ac.kr/inu/709/subview.do',
  '대학소개 > 총장실 > 총장에게 바란다': 'https://www.inu.ac.kr/inu/710/subview.do',# 게시판 형태
  '대학소개 > 총장실 > 역대총장': 'https://www.inu.ac.kr/inu/711/subview.do', # 동적 웹
  '대학소개 > 총장실 > 총장 연설모음': 'https://www.inu.ac.kr/inu/712/subview.do', # 게시판 형태
  '대학소개 > 총장실 > 최근 동정': 'https://www.inu.ac.kr/inu/713/subview.do', # 게시판 형태
  '대학소개 > 학교법인 > 학교법인': 'https://www.inu.ac.kr/inu/714/subview.do', 
  '대학소개 > 학교법인 > 이사회': 'https://www.inu.ac.kr/inu/743/subview.do', 
  '대학소개 > 학교법인 > 이사회의사록': 'https://www.inu.ac.kr/inu/715/subview.do',  # 게시판 형태, 이사회를 통해 접속이 가능하나 세부 경로 아님
  '대학소개 > 학교법인 > 안전보건경영 > 공지사항': 'https://www.inu.ac.kr/inu/936/subview.do', # 게시판 형태
  '대학소개 > 학교법인 > 안전보건경영 > 비전 및 추진체계': 'https://www.inu.ac.kr/inu/937/subview.do', 
  '대학소개 > 학교법인 > 안전보건경영 > 안전보건경영방침': 'https://www.inu.ac.kr/inu/938/subview.do', # 동적 웹, PDF 링크 존재
  '대학소개 > 학교법인 > 안전보건경영 > 안전보건현황판': 'https://www.inu.ac.kr/inu/939/subview.do', # 게시판 형태
  '대학소개 > 학교법인 > 안전보건경영 > 안전신문고': 'https://www.inu.ac.kr/inu/940/subview.do', # 게시판 형태
  '대학소개 > 학교법인 > UI소개 > UI규정 > 심벌': 'https://www.inu.ac.kr/inu/726/subview.do', # UI 다운로드 존재
  '대학소개 > 학교법인 > UI소개 > UI규정 > 로고 타입': 'https://www.inu.ac.kr/inu/727/subview.do', # UI 다운로드 존재
  '대학소개 > 학교법인 > UI소개 > UI규정 > 슬로건': 'https://www.inu.ac.kr/inu/732/subview.do', # UI 다운로드 존재
  '대학소개 > 학교법인 > UI소개 > UI규정 > 사용금지규정': 'https://www.inu.ac.kr/inu/729/subview.do', # UI 다운로드 존재
  '대학소개 > 학교법인 > UI소개 > UI규정 > 엠블럼': 'https://www.inu.ac.kr/inu/730/subview.do', # UI 다운로드 존재
  '대학소개 > 학교법인 > UI소개 > 색상': 'https://www.inu.ac.kr/inu/728/subview.do', # UI 다운로드 존재
  '대학소개 > 학교법인 > UI소개 > 40주년 엠블럼': 'https://www.inu.ac.kr/inu/733/subview.do', # UI 다운로드 존재
  '대학소개 > 횃불이캐릭터': 'https://www.inu.ac.kr/inu/731/subview.do', # 횃불이 캐릭터 다운로드 존재
  
  '대학소개 > 위원회안내 > 교육연구위원회' : 'https://www.inu.ac.kr/inu/745/subview.do', # 게시판 형태
  '대학소개 > 위원회안내 > 재무경영위원회' : 'https://www.inu.ac.kr/inu/746/subview.do', # 게시판 형태
  '대학소개 > 위원회안내 > 장학복지위원회' : 'https://www.inu.ac.kr/inu/747/subview.do', # 게시판 형태
  '대학소개 > 위원회안내 > 등록금심의위원회' : 'https://www.inu.ac.kr/inu/748/subview.do', # 게시판 형태
  '대학소개 > 조직 및 기관 > 조직도' : 'https://www.inu.ac.kr/inu/723/subview.do', # 동적 웹
  '대학소개 > 조직 및 기관 > 소속/교직원 검색' : 'https://www.inu.ac.kr/inu/742/subview.do', # 동적 웹
  '대학소개 > 조직 및 기관 > 부속기관' : 'https://www.inu.ac.kr/inu/724/subview.do',
  '대학소개 > 조직 및 기관 > 국책센터 및 부설기관 > 국책센터' : 'https://www.inu.ac.kr/inu/956/subview.do',
  '대학소개 > 조직 및 기관 > 국책센터 및 부설기관 > 부설기관' : 'https://www.inu.ac.kr/inu/957/subview.do',
  '대학소개 > 청렴센터 > 공지사항' : 'https://www.inu.ac.kr/inu/700/subview.do', # 게시판 형태
  '대학소개 > 청렴센터 > 공개자료실 > 업무추진비' : 'https://www.inu.ac.kr/inu/930/subview.do',  #업무추진비양식 다운로드 존재, 게시판 형태
  '대학소개 > 청렴센터 > 공개자료실 > 감사정보' : 'https://www.inu.ac.kr/inu/931/subview.do', # 게시판 형태
  '대학소개 > 청렴센터 > 공개자료실 > 부패공직자 현황공개' : 'https://www.inu.ac.kr/inu/932/subview.do', # 게시판 형태
  '대학소개 > 청렴센터 > 공개자료실 > 청렴소통 자료실' : 'https://www.inu.ac.kr/inu/933/subview.do', # 게시판 형태
  '대학소개 > 청렴센터 > 공개자료실 > 친인척 채용현황' : 'https://www.inu.ac.kr/inu/934/subview.do', # 게시판 형태
  '대학소개 > 청렴센터 > 청렴정책 및 규정안내' : 'https://www.inu.ac.kr/inu/702/subview.do', # 게시판 형태
  '대학소개 > 청렴센터 > 부패방지 제도개선 제안방' : 'https://www.inu.ac.kr/inu/703/subview.do', # 열람권한 필요
  '대학소개 > 청렴센터 > 청탁금지법 상담센터' : 'https://www.inu.ac.kr/inu/704/subview.do', # 게시판 형태
  '대학소개 > 청렴센터 > INU신문고 > 부패행위신고' : 'https://www.inu.ac.kr/inu/749/subview.do',  #신고서양식 다운로드 존재
  '대학소개 > 청렴센터 > INU신문고 > 클린신고센터' : 'https://www.inu.ac.kr/inu/750/subview.do',  #신고서양식 다운로드 존재
  '대학소개 > 청렴센터 > INU신문고 > 공익신고' : 'https://www.inu.ac.kr/inu/751/subview.do',
  '대학소개 > 청렴센터 > INU신문고 > 갑질행위신고' : 'https://www.inu.ac.kr/inu/752/subview.do',
  '대학소개 > 청렴센터 > INU신문고 > E-감사실' : 'https://www.inu.ac.kr/inu/707/subview.do', # 게시판 형태
  
  '대학소개 > 대학비전/역사 > 대학비전' : 'https://www.inu.ac.kr/inu/717/subview.do',
  '대학소개 > 대학비전/역사 > 발자취 > 2020년대' : 'https://www.inu.ac.kr/inu/8008/subview.do',
  '대학소개 > 대학비전/역사 > 발자취 > 2010년대' : 'https://www.inu.ac.kr/inu/8009/subview.do',
  '대학소개 > 대학비전/역사 > 발자취 > 2000년대' : 'https://www.inu.ac.kr/inu/8010/subview.do',
  '대학소개 > 대학비전/역사 > 발자취 > 1990년대' : 'https://www.inu.ac.kr/inu/8011/subview.do',
  '대학소개 > 대학비전/역사 > 발자취 > 1980년대' : 'https://www.inu.ac.kr/inu/8012/subview.do',
  '대학소개 > 대학비전/역사 > 발자취 > 1970년대' : 'https://www.inu.ac.kr/inu/8013/subview.do',
  '대학소개 > 대학비전/역사 > 발자취 > 주요연혁' : 'https://www.inu.ac.kr/inu/8014/subview.do',
  '대학소개 > 대학비전/역사 > 대학운영계획' : 'https://www.inu.ac.kr/inu/719/subview.do', #게시판 목록 안에 pdf 존재
  '대학소개 > 캠퍼스 안내 > 찾아오시는길 > 송도캠퍼스' : 'https://www.inu.ac.kr/inu/1473/subview.do', #안에 주소와 지도 있음
  '대학소개 > 캠퍼스 안내 > 찾아오시는길 > 제물포캠퍼스' : 'https://www.inu.ac.kr/inu/1474/subview.do', #안에 주소와 지도 있음
  '대학소개 > 캠퍼스 안내 > 찾아오시는길 > 미추홀캠퍼스' : 'https://www.inu.ac.kr/inu/1475/subview.do', #안에 주소와 지도 있음
  '대학소개 > 캠퍼스 안내 > 찾아오시는길 > 셔틀버스' : 'https://www.inu.ac.kr/inu/1476/subview.do',
  '대학소개 > 캠퍼스 안내 > 찾아오시는길 > 주차정보' : 'https://www.inu.ac.kr/inu/1477/subview.do',
  '대학소개 > 캠퍼스 안내 > 캠퍼스맵' : 'https://www.inu.ac.kr/inu/739/subview.do', # 동적 웹
  '대학소개 > 캠퍼스 안내 > 캠퍼스 투어 > 캠퍼스투어소개 > 단체투어' : 'https://www.inu.ac.kr/inu/975/subview.do',
  '대학소개 > 캠퍼스 안내 > 캠퍼스 투어 > 캠퍼스투어소개 > 정기투어' : 'https://www.inu.ac.kr/inu/976/subview.do',
  '대학소개 > 캠퍼스 안내 > 캠퍼스 투어 > 투어신청 및 일정' : 'https://www.inu.ac.kr/inu/963/subview.do', # 동적 웹
  '대학소개 > 캠퍼스 안내 > 캠퍼스 투어 > 홍보대사 > 소개' : 'https://www.inu.ac.kr/inu/979/subview.do',
  '대학소개 > 캠퍼스 안내 > 캠퍼스 투어 > 홍보대사 > 활동' : 'https://www.inu.ac.kr/inu/980/subview.do',
  '대학소개 > 캠퍼스 안내 > 캠퍼스 투어 > 홍보대사 > 후기' : 'https://www.inu.ac.kr/inu/981/subview.do',
  '대학소개 > 캠퍼스 안내 > 캠퍼스 투어 > 홍보대사 > FAQ' : 'https://www.inu.ac.kr/inu/982/subview.do',
  '대학소개 > 대학현황 > 대학 주요현황 > 대학 주요현황' : 'https://www.inu.ac.kr/inu/949/subview.do',
  '대학소개 > 대학현황 > 대학 주요현황 > 통계연보' : 'https://www.inu.ac.kr/inu/950/subview.do', # 게시판 형태
  '대학소개 > 대학현황 > 대학 주요현황 > 대학자체평가' : 'https://www.inu.ac.kr/inu/952/subview.do', # 게시판 형태
  '대학소개 > 대학현황 > 예결산 공고' : 'https://www.inu.ac.kr/inu/721/subview.do', # 게시판 형태

}
