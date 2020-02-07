
# coding: utf-8

# In[1]:



from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from petition.models import * 

import numpy as np



# In[2]:


def remove_tag(content):
   cleanr =re.compile('<.*?>')
   cleantext = re.sub(cleanr, '', content)
   return cleantext


# In[3]:


#remove_tag('<h3 class="petitionsView_title">세종대왕 탄신일(5월15일)을 국가기념일로 지정해 주셨으면 합니다.</h3>')


# In[121]:

pe_article_id=[]
pe_start = []
pe_end = []
pe_votes = []
pe_categorys = []
pe_titles = []
pe_contents = []
#pe_article_id.append('article_id')
#pe_start.append('start')
#pe_end.append('end')
#pe_votes.append('vote')
#pe_titles.append('title')
#pe_contents.append('content')
'''for i in range(579410,580410): 
    URL = "https://www1.president.go.kr/petitions/"+str(i)
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.find_all("h3",{"class" :"petitionsView_title"})
    if(len(titles)==0):
        continue
    votes = soup.find_all("span", {"class" : "counter"})
    contents = soup.find_all("div", {"class" : "View_write"})
    list_tag=[]
    for ultag in soup.find_all('ul', {'class': 'petitionsView_info_list'}):
        for litag in ultag.find_all('li'):
            list_tag.append(litag.text)

    pe_article_id.append(i)
    pe_categorys.append(list_tag[0][4:])
    pe_start.append(list_tag[1][4:])
    pe_end.append(list_tag[2][4:])
    pe_titles.append(titles[0].string)
    pe_contents.append(contents[0].get_text(" ", strip=True))
    pe_votes.append(votes[0].string)

 




from pandas import Series, DataFrame


# In[127]:


df=0
df=DataFrame()
df["article_id"]=pe_article_id
df["start"]=pe_start
df["end"]=pe_end
df["answered"]=0
df["votes"]=pe_votes
df["category"]=pe_categorys
df["title"]=pe_titles
df["content"]=pe_contents


# In[128]:




# In[129]:


df.to_csv("petition_new.csv", header=True, index=False)'''







df = pd.read_csv('petition_new.csv' )






# In[133]:



# In[134]:


#df=petitions


# In[135]:


df=df.dropna()


# In[136]:


df.isnull().values.any()


# In[137]:


type(df.loc[df["article_id"]==510943]["content"])


# In[138]:


df.loc[df["article_id"]==510943]["content"].to_string()




# In[140]:


df["10word"]=0


# In[141]:


from collections import Counter



from konlpy.tag import Twitter

nlpy = Twitter()


# In[142]:


for index in df.index[0:65]:
    nouns=0
    count=0
    lines=df["content"][index]
    nouns = nlpy.nouns(lines)
    count = Counter(nouns)
    list_10=[]
    for n,c in count.most_common(10):
        if len(n) >= 2 :
            list_10.append(n)
        
    df["10word"][index]=list_10



original_text=Article.objects.latest('id').contents
#original_text=Article.objects.get(id = num1)
#original=Article.objects.latest('id').contents
#print(original)

nouns=0
count=0
lines=Article.objects.latest('id').contents
nouns = nlpy.nouns(lines)
count = Counter(nouns)
list_10=[]
for n,c in count.most_common(10):
    if len(n) >= 2 :
        list_10.append(n)        
original_10word=list_10  #10개의 키워드를 뽑아줌








'''for index in df.index[0:65]:
    print(index)
    for word1 in df["10word"][index]:
        for word2 in original_10word:
            print(word1)
            print(word2)
            print("----------------")'''




similar_dict={}
original_index=0
original_10word
#print(original_10word)
#print("완료")
for index in df.index[0:65]:
    sum=0
    for word1 in df["10word"][index]:
        for word2 in original_10word:
            if word1==word2:
                sum=sum+1
    sum=sum/(len(df["10word"][index])+len(original_10word)-sum)*100
    if (sum<100)&(sum>0)&(sum!=100) :
        similar_dict[index]=sum
       # print(sum)


# In[149]:


import operator
similar_dict=sorted(similar_dict.items(), key=operator.itemgetter(1),reverse=True)


# In[150]:


similar_list=similar_dict
#similar_list


# In[151]:




same_content={}
a={}


#print(similar_list[0:11])
'''for index,sum in similar_list[0:11]:
    if(same_content!=df["content"][index]):
       # print("유사도 ",round(sum,2),"%")
       # print("동의수 : ",df["votes"][index])
       # print("올라온 날짜 : ",df["start"][index])
       # print(df["content"][index])
       # print("--------------------------------------------------------------------------------------------------")'''
same_content=df["content"][index]





