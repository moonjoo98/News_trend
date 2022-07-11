#!/usr/bin/env python
# coding: utf-8

# In[91]:


import pandas as pd
import numpy as np
import string
import argparse
import datetime
import os

# # TFDIF

# In[96]:





# # 데이터 불러오기 + 전처리

# In[102]:


def call_data(data):
    TEST=pd.read_csv('./SA_count/'+data)
    TEST.drop('Unnamed: 0', axis=1,inplace=True)
    #TEST.rename(columns={'대표 키워드 (해시태그)' : '키워드'},inplace=True)
    TEST['대표 키워드 (해시태그)']=TEST['대표 키워드 (해시태그)'].fillna('No_Key')
    TEST['대표 키워드 (해시태그)']=TEST['대표 키워드 (해시태그)'].str.replace(',',' ')
    TEST['대표 키워드 (해시태그)']=TEST['대표 키워드 (해시태그)'].str.replace('  ',' ')
    TEST['대표 키워드 (해시태그)']=TEST['대표 키워드 (해시태그)'].apply(lambda x:x.lower())
    
    tfidf=pd.read_csv('data/20220707_tfidf_cnbc.csv')# 필요시 이부분 수정
    tfidf.fillna(0,inplace=True)
    yahoo=pd.read_csv('data/20220707_tfidf_yahoo.csv')# 필요시 이부분 수정
    yahoo.fillna(0,inplace=True)
    Ynbc=pd.concat([yahoo,tfidf])
    
    return TEST,Ynbc

#TEST['키워드']=TEST['키워드'].apply(lambda x : ''.join([k for k in x if k not in string.punctuation]))
#TEST['키워드']=TEST['키워드'].apply(lambda x : ''.join([k for k in x if k not in string.digits]))


# # 빈도계산

# In[103]:


def cal_freq(data,file,date):
    tfidf_yh = pd.DataFrame({
        '단어': file.keyword,
        '값': file[date]
    })

    tfidf_yh=pd.DataFrame(file.groupby('keyword')[date].mean())

    tfidf_yh_dict=tfidf_yh.T.to_dict('list')

    for i in range(data.shape[0]):
        globals()[f'ass_word_list_{i}'] = list(set(data['대표 키워드 (해시태그)'].str.split()[i]))

    for i in range(data.shape[0]):
        globals()[f'frequency_yh{i}'] = []
        globals()[f'word_list_yh{i}'] = []

    remove_set = {999}
    for i in range(data.shape[0]):
            for j in range(50):
                try:
                    word_freq=globals()[f'ass_word_list_{i}'][j]
                    globals()[f'frequency_yh{i}'].append(tfidf_yh_dict[word_freq][0])
                    globals()[f'word_list_yh{i}'].append(word_freq)
                except:
                    pass
            globals()[f'frequency_yh{i}'] = [i for i in globals()[f'frequency_yh{i}'] if i not in remove_set]
            
    def rm_minmax(mylist):
#     for i in range(TEST.shape[0]):
#         for j in range(globals()[f'frequency{i}'].count(999)):
#             mylist.remove(999)
        if len(mylist) == 0:
            mylist.append(999)
        small=min(mylist)
        big=max(mylist)
        if len(mylist) > 5 : #키워드가 5보다 클경우 가장큰 값과 작은값 제거후 평균
            mylist.remove(small)
            mylist.remove(big)
        else:
            pass

        return mylist

    for i in range(data.shape[0]):
        rm_minmax(globals() [f'frequency_yh{i}'])

    for i in range(data.shape[0]):
        globals() [f'frequency_yh{i}']=np.mean(globals() [f'frequency_yh{i}'])
    
    fr_list=[]
    for i in range(data.shape[0]):
        frq=globals()[f'frequency_yh{i}']
        fr_list.append(frq)
    print('frequency 계산이 끝났다!')
    return fr_list


# # 데이터프레임에 빈도 값 추가후 CSV 파일변환

# In[104]:


def main(data,date):
    TEST,Ynbc=call_data(data)
    fr_list=cal_freq(TEST,Ynbc,date)
    TEST['빈도값']=fr_list
    date_ = datetime.datetime.now().strftime('%y%m%d')
    address='./SA_Tfidf/'
    fileName ='SA_Tfidf'+date_+'.csv'
    try:
        if not os.path.exists('SA_Tfidf'):
            os.makedirs('SA_Tfidf')
    except:
        print('파일이이미 생성됐다.')
    
    
    
    TEST.to_csv(address+fileName,encoding='utf-8-sig')
    
    


# In[ ]:





# In[88]:


if __name__== "__main__":
    parser = argparse.ArgumentParser(description='--data input news keyword data ex)SA_count220708.csv \n--date input week tfidf_value data ex) tfidf_2022_27')
    parser.add_argument('--data',type=str,default='trend_220607.xlsx')
    parser.add_argument('--date',type=str,default='2022_05')
    args = parser.parse_args()
    
    main(args.data,args.date)

    


# In[ ]:




