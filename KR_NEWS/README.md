# 한국 경제 뉴스기사 감성분류 / NER 모델

### [개인_Project]뉴스_감정분류_모델_baseline.ipynb

- 직접 커스터마이징한 모델과 fine-tuning에 사용한 데이터셋과 인퍼런스에 사용한 데이터셋은 공개할 수가 없어 베이스라인용 코드 제공
- Finance Phrase Bank 영어 데이터셋을 한국어로 번역 및 검수한 데이터로 베이스라인 학습 진행
- 모델 인퍼런스의 속도도 중요하기 때문에 klue/roberta-base를 사용하고 앙상블 진행 X

#### 성능
![image](https://user-images.githubusercontent.com/103553532/218941730-ecc95c1e-9f8e-4979-a1fc-978b3e135549.png)

- 적은 데이터셋과 base모델을 사용했음에도 0.84정도의 성능이면 준수한 성능을 보이며 생각보다 예측을 잘하는 것을 볼 수 있음.
- 데이터셋을 추가로 학습시키거나 augmentation 기법을 활용해 추가 학습을 진행시키면 성능 향상을 기대할 수 있다.
- base모델을 다른 언어모델로 바꿔서 학습을 진행하거나 여러 언어모델의 logit을 앙상블 하면 성능 향상을 기대할 수 있다.

#### 한국 경제 뉴스 기사 감정분류 모델 개발 리뷰 - https://mz-moonzoo.tistory.com/17

### [개인_Project] 한국뉴스_기업_KCELECTRA_NER.ipynb

- 한국 뉴스 기사내에서 여러 entity 중 기업들(조직,ORG)만 뽑아내는 것 입니다.
- 실습에서는 한국해양대학교 데이터셋과 네이버 데이터셋 두 가지만 사용해 학습을 진행했습니다.
- 기존 토크나이저는 wordpiece tokenizer로 tokenizing 결과를 반환하기 때문에 음절 tokenizer로 바꿔 사용했습니다.
- 언어모델로 가장 안정적인 성능이 나오는 KcELECTRA를 사용했습니다.

#### 성능
![image](https://user-images.githubusercontent.com/103553532/218941607-2ab9ddfc-7e4b-4c1a-8b9b-f926021073ac.png)

- 생각보다 성능이 잘나오는 것을 보고 놀랐습니다. 대부분의 ORG는 잘 잡아내는 것으로 보입니다.
- 다른 언어모델을 사용해보거나 데이터셋의 구성을 좀 다르게하고 파라미터를 변경해주면 더 좋은 성능이 나올수도 있다는 생각이 듭니다. 

#### 한국 경제 뉴스 기사 NER 모델 개발 리뷰 -https://mz-moonzoo.tistory.com/25
