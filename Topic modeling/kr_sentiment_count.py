#!/usr/bin/env python
# coding: utf-8

# In[51]:


# import pandas as pd
# import numpy as np
# import string
# import argparse
# import datetime
# import os


# In[52]:


# data='trend_220829_KR.xlsx'
# TEST=pd.read_excel('data/'+data,header=2) # 엑셀 파일 그대로 넣기
# TEST=TEST.iloc[1:]
# TEST.reset_index(drop=True,inplace=True)
# TEST.rename(columns={'종목(테마관련뉴스만 사용)':'종목'},inplace=True)
# TEST['종목']=TEST['종목'].fillna('없당')
# TEST.dropna(subset=['대표 키워드 (해시태그)'],how='any',axis=0,inplace=True)
# TEST['종목']=TEST.종목.str.replace(',',' ')


# In[53]:


# summary_sa=pd.read_csv('data/KR_equity_sent_summary.csv')#이부분도..
# summary_sa.fillna(999,inplace=True)


# In[54]:



# for i in range(TEST.shape[0]):
#     symbol_list=[]
#     count=len(TEST.종목[i].split())
#     for j in range(count):
#         symbol=TEST.종목[i].split()[j].lstrip('0')
#         symbol_list.append(symbol)
#     TEST.at[i,'종목']=symbol_list


# In[60]:



# TEST.종목=TEST.종목.astype(str)
# TEST.종목=TEST['종목'].str.replace('[',"",regex=True)
# TEST.종목=TEST['종목'].str.replace(']',"",regex=True)
# TEST.종목=TEST['종목'].str.replace('"',"",regex=True)


# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import string
import argparse
import datetime
import os


# # 데이터 불러오기 + 전처리

# In[27]:


def call_data(data):
    TEST=pd.read_excel('data/'+data,header=2) # 엑셀 파일 그대로 넣기
    TEST=TEST.iloc[1:]
    TEST.reset_index(drop=True,inplace=True)
    TEST.rename(columns={'종목(테마관련뉴스만 사용)':'종목'},inplace=True)
    TEST['종목']=TEST['종목'].fillna('없당')
    TEST.dropna(subset=['대표 키워드 (해시태그)'],how='any',axis=0,inplace=True)
    TEST['종목']=TEST.종목.str.replace(',',' ')
    

    for i in range(TEST.shape[0]):
        symbol_list=[]
        count=len(TEST.종목[i].split())
        for j in range(count):
            symbol=TEST.종목[i].split()[j].lstrip('A')
            symbol=symbol.lstrip('0')
            symbol_list.append(symbol)
        TEST.at[i,'종목']=symbol_list
        
    
    TEST.종목=TEST.종목.astype(str)
    TEST.종목=TEST['종목'].str.replace('[',"",regex=True)
    TEST.종목=TEST['종목'].str.replace(']',"",regex=True)
    TEST.종목=TEST['종목'].str.replace("'","",regex=True)
    TEST['종목']=TEST.종목.str.replace(',','')


    summary_sa=pd.read_csv('data/KR_equity_sent_summary.csv')#이부분도..
    #Cnbc=pd.read_csv('data/SA_US_cnbc.csv')#이부분도..
    #Ynbc=pd.concat([Yahoo,Cnbc])
    summary_sa.fillna(999,inplace=True)

    return TEST,summary_sa


# In[9]:


# TEST=pd.read_csv('sentiment_sa_0526.csv')#이부분만 수정하면 됨.
# TEST.rename(columns={'종목(테마관련뉴스만 사용)':'종목'},inplace=True)
# TEST['종목']=TEST['종목'].fillna('없당')
# TEST['종목']=TEST.종목.str.replace(',',' ')
# TEST.dropna(subset=['대표 키워드 (해시태그)'],how='any',axis=0,inplace=True)

# Yahoo=pd.read_csv('data/SA_US_yahoo.csv')#이부분도..
# Cnbc=pd.read_csv('data/SA_US_cnbc.csv')#이부분도..
# Ynbc=pd.concat([Yahoo,Cnbc])
# Ynbc.fillna(999,inplace=True)


# In[10]:


#TEST.종목.fillna('0',inplace=True)
#TEST['종목']=TEST['종목'].apply(lambda x : ''.join([k for k in x if k not in string.punctuation]))
#TEST['키워드']=TEST.키워드.str.replace('  ',' ')


# In[11]:


# Yahoo=pd.read_csv('data/SA_US_W_E.csv')
# Ynbc=Yahoo


# # 감성값 딕셔너리

# In[39]:


#중복제거 + 평균
def unique_mean(file,date):
    mean_=file.groupby('Code')[date].mean()
    mean_df=pd.DataFrame(mean_)
    mean_dict=mean_df.T.to_dict('list')
    return mean_dict

def make_dict(file,dic):
    for i in range(file.shape[0]):
        globals()[f'symbol{i}'] = list(set(file['종목'].str.split()[i]))

    #리스트 생성
    for i in range(file.shape[0]):
        globals()[f'sentiment_score{i}'] = []
        globals()[f'symbol_list{i}'] = []
    #리스트 추가    
    for i in range(file.shape[0]):
            for j in range(50):
                try:
                    symbol_name=int(globals()[f'symbol{i}'][j])
                    globals()[f'sentiment_score{i}'].append(dic[symbol_name][0])
                    globals()[f'symbol_list{i}'].append(symbol_name)
                except:
                    pass
                
    for i in range(file.shape[0]):
        dict_ = { x:y for x,y in zip(globals()[f'symbol_list{i}'],globals()[f'sentiment_score{i}']) }

        globals() [f'symbol_df{i}']=pd.DataFrame(dict_.values(),index=dict_.keys())
        if globals() [f'symbol_df{i}'].shape[0] ==0:
            globals() [f'symbol_df{i}']=pd.DataFrame({f'col_{i}':[999]})
        else:
            globals() [f'symbol_df{i}'].rename(columns={0:f'col_{i}'},inplace=True)
        

    list_of_df = []
    for i in range(file.shape[0]):
        symbol=globals()[f'symbol_df{i}'][f'col_{i}']
        list_of_df.append(symbol)
        
    symbol_sum_df=pd.DataFrame(list_of_df).T

    sa_score=symbol_sum_df.mean()#감성평균값

    return symbol_sum_df, sa_score


# In[53]:


# i=0
# symbol_sum_df=pd.concat([globals()[f'symbol_df{i}'],globals()[f'symbol_df{i+1}'],globals()[f'symbol_df{i+2}']
#                         ,globals()[f'symbol_df{i+3}'],globals()[f'symbol_df{i+4}'],globals()[f'symbol_df{i+5}']
#                         ,globals()[f'symbol_df{i+6}'],globals()[f'symbol_df{i+7}'],globals()[f'symbol_df{i+8}']
#                               ,globals()[f'symbol_df{i+9}']],axis=1)#,globals()[f'symbol_df{i+10}'],globals()[f'symbol_df{i+11}']],axis=1)
# #                              ,globals()[f'symbol_df{i+12}'],globals()[f'symbol_df{i+13}'],globals()[f'symbol_df{i+14}']
# #                              ,globals()[f'symbol_df{i+15}'],globals()[f'symbol_df{i+16}'],globals()[f'symbol_df{i+17}']
# #                              ,globals()[f'symbol_df{i+18}'],globals()[f'symbol_df{i+19}']],axis=1)


# In[58]:


def sentiment_summary(file,df,score):
    def count_sa(x):
        if x > 0:
            return 1
        if x == 0:
            return 0
        if x < 0 :
            return -1
    last=[]
    good=[]
    soso=[]
    bad=[]
    for i in range(file.shape[0]):
        col_= f'col_{i}'
        sa_count=df[col_].apply(count_sa).value_counts()
        df[col_]=df[col_].apply(count_sa)
        good_=list(df[df[col_]==1].index)
        soso_=list(df[df[col_]==0].index)
        bad_=list(df[df[col_]==-1].index)
        good.append(good_)
        soso.append(soso_)
        bad.append(bad_)
        last.append(sa_count)

    good_df=pd.DataFrame(pd.Series(good))
    good_df.columns=['긍정']
    good_df=good_df.T
    soso_df=pd.DataFrame(pd.Series(soso))
    soso_df.columns=['중립']
    soso_df=soso_df.T
    bad_df=pd.DataFrame(pd.Series(bad))
    bad_df.columns=['부정']
    bad_df=bad_df.T

    for i in range (file.shape[0]):
        good_df.rename(columns={i : f'col_{i}'},inplace=True)
        soso_df.rename(columns={i : f'col_{i}'},inplace=True)
        bad_df.rename(columns={i : f'col_{i}'},inplace=True)

    count_df=pd.concat([df,pd.DataFrame(last).T,good_df,soso_df,bad_df,pd.DataFrame(score).T],axis=0)
    count_df=count_df.fillna('제외')
    TT=count_df.iloc[-4:].T
    TT.reset_index(drop=True,inplace=True)
    TT.rename(columns={0:'감성평균'},inplace=True)
    test_df=pd.concat([file,TT],axis=1)

    date = datetime.datetime.now().strftime('%y%m%d')
    address='./SA_count/' 
    fileName = 'SA_count'+date+'.csv'
    try:
        if not os.path.exists('SA_count'):
            os.makedirs('SA_count')
    except:
        print('이미 폴더가 생성됐습니다.')
    test_df.to_csv(address+fileName,encoding='utf-8-sig')
    print('SA_count폴더에 csv파일이 생성됐습니다!')
#good_df.columns=['col_0','col_1','col_2','col_3','col_4','col_5','col_6','col_7','col_8','col_9']
#soso_df.columns=['col_0','col_1','col_2','col_3','col_4','col_5','col_6','col_7','col_8','col_9']
#bad_df.columns=['col_0','col_1','col_2','col_3','col_4','col_5','col_6','col_7','col_8','col_9']


# In[59]:


def main(data='trend_220607.xlsx',date='2022_22'):
    TEST,Ynbc=call_data(data)
    week_dict=unique_mean(Ynbc,date)
    symbol_sum_df,sa_score=make_dict(TEST,week_dict)
    sentiment_summary(TEST,symbol_sum_df,sa_score)
    
    


# In[33]:


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='--data input data file name ex)trend_220711.xlsx, --date input SA_score_columns ex)2022_27')
    parser.add_argument('--data',type=str,default='trend_220607.xlsx')
    parser.add_argument('--date',type=str,default='2022_05')
    args = parser.parse_args()
    
    main(args.data,args.date)


# In[ ]:




