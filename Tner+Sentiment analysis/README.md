# Tner과 Finbert를 활용한 NER + Sentiment analysis

### Tner_change_ticker_papago.ipynb

Tner https://github.com/asahi417/tner <- NER 모델 출처

`!pip install tner`

NER Flow

#### Target : 뉴스 테마별 Ticker 감성분석 

#### Problem 
- 종목 감성분석을 위해 뉴스 문서 내에서 종목과 관련된 문장과 Ticker를 뽑아낼 필요가 있음.

#### Solution
- 뉴스 문서를 문장 단위로 토큰화 (sent_tokenize)

  -> tner의 tokenize 역시 문장 단위로 전처리를 진행하기 때문에 그대로 사용

- pretrained tner model 모델에 Finance Dataset으로 fine-tuning을 진행해 entity가 organzation인 것만 추출 (tner 모델 output 수정)

  -> Finance data, OntoNotes, CoNLL 2003등 하나씩 Fine-tuning을 진행해봤지만 모든 영어 데이터셋에서 fine-tuning된 XLM-R 대형모델이 가장 좋은 결과를 보여줌.
    
    ++ 추후 데이터셋을 직접 구축하여 fine-tuning 진행 예정

- 뉴스에 따라 회사명을 다르게 추출하기 때문에 추출한 entity를 Ticker로 변환하기 위해 직접 사전 정의

#### Result
- 뉴스 문서에서 종목 관련된 문장을 추출하고 문장 내에서 ticker리스트를 함께 결과 생성

![image](https://user-images.githubusercontent.com/103553532/178190584-f889df13-f3fa-4daa-b5b3-80686f2a69f9.png)


### Finbert_training.ipynb

https://huggingface.co/ProsusAI/finbert <- pretrained-model 출처

###### ProsusAI/finbert
- 대규모 금융 코퍼스를 사용한 언어모델을 사용하고 Finance dataset으로 fine-tuning된 모델

  -> 다양한 Finbert모델이 존재하지만 결과를 test해본 결과 ProsusAI의 finbert가 가장 좋은 결과를 뽑아내서 사용
  
#### later..
- 직접 수집하는 Finance news데이터에 대한 라벨링을 직접 함으로써 task에 맞는 데이터셋을 구축하고 fine-tuning 진행시 성능 향상을 기대할 수 있음.(추후 시도)

- 문장 내에서 2개 이상의 ticker가 발생하면 어느 종목이 긍정이고 부정인지 알수가 없음 -> Realtion Extraction으로 ticker간의 관계 추출을 진행할 예정


![image](https://user-images.githubusercontent.com/103553532/178198490-29f5eed6-eb32-4639-8fea-e8b888009c42.png)

  





