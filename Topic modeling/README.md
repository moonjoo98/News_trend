# BERTopic을 활용해 해외 뉴스 토픽 모델링

### 직접 수집한 해외 뉴스 데이터를 활용해 해당 시점에 핫한 트렌드 파악해보자!

#### 해외 뉴스 데이터 : CNBC (직접 수집)

#### [Project] BERTopic_CNBC.ipynb
- 주차 단위로 해외뉴스 토픽 모델링 진행, 뉴스 데이터셋마다 파라미터를 조정할 필요가 있으므로 ipynb파일로 생성

#### BERTopic 블로그 링크 https://mz-moonzoo.tistory.com/23

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


# BERTopic을 활용한 국내 뉴스 토픽 모델링

#### 국내 뉴스 데이터 : 빅카인즈 (사이트 이용)

### [Project] KOBERTopic_한국뉴스 + 팔로업 뉴스 추천 시스템.ipynb
- 주차 단위로 국내 뉴스 토픽 모델링 진행, 마찬가지로 수집된 데이터셋마다 파라미터를 조정할 필요가 있으므로 ipynb파일로 생성

#### KoBERTopic 블로그 링크 https://mz-moonzoo.tistory.com/24

# UPDATE
#### (22/08/26) 해외 토픽 모델 고도화. 
##### BERTopic 버전 업데이트로 새로운 기능 추가. 사전 텍스트 전처리에서 사후 전처리로 변경
- hierarchical_topics, get_topic_tree 기능을 활용해 계층적 주제 모델링 진행
- BERTopic의 경우 사전 텍스트 전처리보다 사후 전처리를 진행할 시 토픽을 더 잘 나눌 수 있어 수정

#### (22/08/29) 국내 토픽 모델 고도화.
##### BERTopic 버전 업데이트로 새로운 기능 추가. 사전 텍스트 전처리에서 사후 전처리로 변경
- hierarchical_topics, get_topic_tree 기능을 활용해 계층적 주제 모델링 진행
- BERTopic의 경우 사전 텍스트 전처리보다 사후 전처리를 진행할 시 토픽을 더 잘 나눌 수 있어 수정

#### (22/08/30) 국내 뉴스 감성값 + tfidf 빈도값 계산 py파일 생성
- 해외 뉴스에 적용했던 테마별 sentiment_score, 키워드를 통한 빈도값 계산 py파일을 국내 버전으로 생성

#### (22/09/06) 국내 뉴스 종목코드 'A' 텍스트 추가.
- 종목코드 텍스트 전처리를 위해 코드 수정

#### (22/01/26) 국내 뉴스 전처리 진행
- 텍스트 내 이모티콘과 공백 2칸이상이 존재해 정규표현식을 활용해 제거

#### (22/01/27) 국내 뉴스 CustomTokenizer 수정.
- Mecab -> Spacy
- Spacy의 lemma, tag를 통해 명사만 추출
- vectorizer ngram_range(1,1)로 수정

#### (2023/02/13) 당일에 직접 수집한 CNBC 뉴스기사로 BERTopic 실습 진행한 파일 업로드.
- 블로그에 코드 리뷰까지 함께 작성해둠.

#### (2023/02/14) 빅카인즈에서 수집한 국내 뉴스 기사로 KoBERTopic 실습 진행한 파일 업로드.
- 블로그에 코드 리뷰까지 함께 작성해둠.

#### (2023/02/14) KoBERTopic내의 DACON 삼성전자 추천 뉴스 앱 코드공유 아이디어 적용
- 토픽의 핵심기사 내용을 보면서 헷갈리는 토픽의 주제를 쉽게 파악할 수 있을 거 같아서 적용해봤음.
- DACON 원본 글 https://dacon.io/competitions/official/235914/codeshare/5728 
- 팔로업 뉴스 추천 시스템 등 아이디어를 참고해서 새로운 서비스를 개발하는데 도움이 될 것 같아서 KoBERTopic파일 내에 코드를 작성함.
