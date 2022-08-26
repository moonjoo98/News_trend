# BERTopic을 활용해 국내 해외 뉴스 토픽 모델링

### 해외 뉴스 데이터 : Yahoo finance, CNBC

#### Foreign_news_bertopic.ipynb
- 주차 단위로 해외뉴스 토픽 모델링 진행, 뉴스 데이터셋마다 파라미터를 조정할 필요가 있으므로 ipynb파일로 생성

#### sentiment_count.py -> 테마별 Ticker 감성 분류
###### 필요한 데이터셋
- Ticker별 감성 스코어 Data -> 감성어사전 기반, DL 기반 감성분석으로 주차별 Ticker 감성 스코어를 계산한 파일
- 뉴스 테마와 연관 Ticker Data-> 토픽 모델링 결과와 NER모델을 활용해 뉴스 테마와 테마 관련 Ticker를 뽑아낸 파일

#### argument로 뉴스테마와 연관 Ticker 파일 이름과 Ticker별 감성 스코어 파일의 계산하고자 하는 주차 컬럼명 입력
(Linux ubuntu)

`python sentiment_count.py --data trend_220711.xlsx --date 2022_27`

#### cal_tfidf.py -> 주차별 tfidf값을 활용해 테마별 키워드 값을 계산해 테마 빈도 계산
##### 필요한 데이터셋
- sentiment_count.py에서 생성된 SA_count csv파일
- 주차단위로 수집한 뉴스 tfidf값

(Linux ubuntu)

`python cal_tfidf.py --data SA_count220708.csv --date tfidf_2022_27`

### UPDATE
#### (22/08/26) BERTopic 버전 업데이트로 새로운 기능 추가. 사전 텍스트 전처리에서 사후 전처리로 변경
- hhierarchical_topics, get_topic_tree 기능을 활용해 계층적 주제 모델링 진행
- BERTopic의 경우 사전 텍스트 전처리보다 사후 전처리를 진행할 시 토픽을 더 잘 나눌 수 있어 수정

### 국내 뉴스 데이터 : 구상중
