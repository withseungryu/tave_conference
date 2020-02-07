#!/usr/bin/env python
# coding: utf-8

# In[2]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import os

currdir = os.path.dirname("C:/Users/alstm/dev/tave/petition/static/img/" )
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc1.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc1.png")
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc2.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc2.png")
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc3.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc3.png")
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc4.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc4.png")
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc5.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc5.png")
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc6.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc6.png")
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc7.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc7.png")
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc8.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc8.png")
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc9.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc9.png")
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc10.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc10.png")
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc11.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc11.png")
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc12.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc12.png")
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc13.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc13.png")
if os.path.isfile("C:/Users/alstm/dev/tave/petition/static/img/wc14.png"):
  os.remove("C:/Users/alstm/dev/tave/petition/static/img/wc14.png")  




# In[3]:


def remove_tag(content):
   cleanr =re.compile('<.*?>')
   cleantext = re.sub(cleanr, '', content)
   return cleantext


# In[4]:


remove_tag('<h3 class="petitionsView_title">세종대왕 탄신일(5월15일)을 국가기념일로 지정해 주셨으면 합니다.</h3>')


# In[5]:


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
for i in range(579501, 580000): 
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


 


# In[6]:


from pandas import Series, DataFrame


# In[7]:


# df 으로 만들기
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


# In[8]:


category = pd.DataFrame(df['category'].value_counts()).reset_index()
category.columns = ['category', 'counts']



# In[20]:


before1= df[df['category'].str.match('정치개혁')]
before2 = df[df['category'].str.match('외교/통일/국방')]
before3 = df[df['category'].str.match('일자리')]
before4 = df[df['category'].str.match('보건복지')]
before5 = df[df['category'].str.match('육아/교육')]
before6 = df[df['category'].str.match('일자리')]
before7 = df[df['category'].str.match('저출산/고령화대책')]
before8 = df[df['category'].str.match('행정')]
before9 = df[df['category'].str.match('반려동물')]
before10 = df[df['category'].str.match('교통/건축/국토')]
before11 = df[df['category'].str.match('경제민주화')]
before12 = df[df['category'].str.match('인권/성평등')]
before13 = df[df['category'].str.match('문화/예술/체육/언론')]
before14 = df[df['category'].str.match('기타')]


# In[21]:


# df 저장
df.to_csv("petition_word.csv", header=True, index=False)


# In[22]:


# df 가져오기
df = pd.read_csv('petition_word.csv' )


# In[23]:


import pandas as pd
import numpy as np
import re


# In[24]:


df=df.dropna()


# In[25]:


df.isnull().values.any()


# In[26]:


from soynlp.tokenizer import RegexTokenizer

tokenizer = RegexTokenizer()


# In[34]:


def preprocessing(text):
    # 개행문자 제거
    text = re.sub('\\\\n', ' ', text)
    return text


# In[35]:


# %time을 찍어주면 해당 코드를 실행할 때 걸리는 시간을 출력해 줍니다
sentences1 = before1['content'].apply(preprocessing)
sentences2 = before2['content'].apply(preprocessing)
sentences3 = before3['content'].apply(preprocessing)
sentences4 = before4['content'].apply(preprocessing)
sentences5 = before5['content'].apply(preprocessing)
sentences6 = before6['content'].apply(preprocessing)
sentences7 = before7['content'].apply(preprocessing)
sentences8 = before8['content'].apply(preprocessing)
sentences9 = before9['content'].apply(preprocessing)
sentences10 = before10['content'].apply(preprocessing)
sentences11 = before11['content'].apply(preprocessing)
sentences12 = before12['content'].apply(preprocessing)
sentences13 = before13['content'].apply(preprocessing)
sentences14 = before14['content'].apply(preprocessing)


# In[36]:


tokens1 = sentences1.apply(tokenizer.tokenize)
tokens2 = sentences2.apply(tokenizer.tokenize)
tokens3 = sentences3.apply(tokenizer.tokenize)
tokens4 = sentences4.apply(tokenizer.tokenize)
tokens5 = sentences5.apply(tokenizer.tokenize)
tokens6 = sentences6.apply(tokenizer.tokenize)
tokens7 = sentences7.apply(tokenizer.tokenize)
tokens8 = sentences8.apply(tokenizer.tokenize)
tokens9 = sentences9.apply(tokenizer.tokenize)
tokens10 = sentences10.apply(tokenizer.tokenize)
tokens11 = sentences11.apply(tokenizer.tokenize)
tokens12 = sentences12.apply(tokenizer.tokenize)
tokens13 = sentences13.apply(tokenizer.tokenize)
tokens14 = sentences14.apply(tokenizer.tokenize)


# In[37]:




# 나눔고딕 설치

import matplotlib.font_manager as fm
import PIL.Image as pilimg
fontpath = '/NanumBarunGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=9)


# In[38]:


stopwords_kr = ['하지만', '그리고', '그런데', '저는','제가',
                '그럼', '이런', '저런', '합니다',
                '많은', '많이', '정말', '너무','자신','상태','분들','가까'] 


# In[50]:


from wordcloud import WordCloud

mask_img = np.array(pilimg.open("wp2.jpg")) 
def displayWordCloud(data = None, num='', backgroundcolor = 'white', width=800, height=600):
    wordcloud = WordCloud(
                        font_path = fontpath, 
                        stopwords = stopwords_kr, 
                        background_color = backgroundcolor,
                        mask = mask_img,
                        width = width, height = height).generate(data)
    wordcloud.to_file(os.path.join(currdir,"wc"+num+".png"))
    #plt.figure(figsize = (15 , 10))
    #plt.imshow(wordcloud)
    #plt.axis("off")
    #plt.show() 


# In[51]:


from soynlp.noun import LRNounExtractor


# In[52]:



noun_extractor = LRNounExtractor(verbose=True)
noun_extractor.train(sentences1)
nouns1 = noun_extractor.extract()
noun_extractor.train(sentences2)
nouns2 = noun_extractor.extract()
noun_extractor.train(sentences3)
nouns3 = noun_extractor.extract()
noun_extractor.train(sentences4)
nouns4 = noun_extractor.extract()
noun_extractor.train(sentences5)
nouns5 = noun_extractor.extract()
noun_extractor.train(sentences6)
nouns6 = noun_extractor.extract()
noun_extractor.train(sentences7)
nouns7 = noun_extractor.extract()
noun_extractor.train(sentences8)
nouns8 = noun_extractor.extract()
noun_extractor.train(sentences9)
nouns9 = noun_extractor.extract()
noun_extractor.train(sentences10)
nouns10 = noun_extractor.extract()
noun_extractor.train(sentences11)
nouns11 = noun_extractor.extract()
noun_extractor.train(sentences12)
nouns12 = noun_extractor.extract()
noun_extractor.train(sentences13)
nouns13 = noun_extractor.extract()
noun_extractor.train(sentences14)
nouns14 = noun_extractor.extract()


# In[53]:


# 추출된 명사를 찍어봅니다.
if(len(nouns1)>0):
    displayWordCloud(' '.join(nouns1),'1')
if(len(nouns2)>0):
    displayWordCloud(' '.join(nouns2),'2')
if(len(nouns3)>0):
    displayWordCloud(' '.join(nouns3),'3')
if(len(nouns4)>0):
    displayWordCloud(' '.join(nouns4),'4')
if(len(nouns5)>0):
    displayWordCloud(' '.join(nouns5),'5')
if(len(nouns6)>0):
    displayWordCloud(' '.join(nouns6),'6')
if(len(nouns7)>0):
    displayWordCloud(' '.join(nouns7),'7')
if(len(nouns8)>0):
    displayWordCloud(' '.join(nouns8),'8')
if(len(nouns9)>0):
    displayWordCloud(' '.join(nouns9),'9')
if(len(nouns10)>0):
    displayWordCloud(' '.join(nouns10),'10')
if(len(nouns11)>0):
    displayWordCloud(' '.join(nouns11),'11')
if(len(nouns12)>0):
    displayWordCloud(' '.join(nouns12),'12')
if(len(nouns13)>0):
    displayWordCloud(' '.join(nouns13),'13')
if(len(nouns14)>0):
    displayWordCloud(' '.join(nouns14),'14')

