# 뉴스 트렌드 분석을 위한 AI모델 개발

### Task 

##### 뉴스 트렌드 분석을 위한 AI 모델 개발 (개인 추가 프로젝트)
- 뉴스 트렌드 분석과 뉴스 문서 내 stock ticker 추출과 ticker 별 관계 추출 후 sentiment analysis.
- 위의 과정을 통해 특정 기간 내에 ticker 빈도 수 와 sentiment score 측정

### 해외 뉴스 / 한국어 뉴스
1. Topic modeling 
-> BERTopic / KoBERTopic

2. NER
-> Tner / KcElectra

3. Sentiment Analysis
-> finBERT / klue-bert-base (beta모델 고도화 예정)

4. Realtion Extraction
-> zero-shot model Ask2Transformers / 한국의 경우 관계추출이 어렵다...


### to be improved : Fine-tuning (Sentiment Analysis model, ner model)

- 지금까지는 시간관계상 직접 데이터셋을 구축하지는 않고 존재하고 있는 여러 데이터셋과 augmentation기법을 통해 fine-tuning을 진행함.

- 뉴스기사와 서비스에 맞는 데이터 셋을 직접 구축하여 활용한다면 성능 향상이 기대가됨.

