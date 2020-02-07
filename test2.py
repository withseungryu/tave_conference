
import pandas as pd
import numpy as np
import re
from petition.models import *


petitions = pd.read_csv('petition_new.csv',
                        parse_dates=['start', 'end'])


df=petitions

df.isnull().sum()

df.isnull().values.any()

df=df.dropna()


# 전체 데이터 중 투표가 500건 이상인 데이터를 기준으로 가져옵니다. 
# 아웃라이어 데이터 제거를 위해 20만건 이상 데이터도 제거합니다.
petition_remove_outlier = df.loc[(df['category']=='정치개혁')]
petition_remove_outlier.shape


df = petition_remove_outlier.copy()

df.describe()



from konlpy.tag import Twitter
import re
twitter = Twitter()

text=Article.objects.latest('id').contents
#print(text)

if len(df.loc[df["content"]==text])>0:
    print("중복된 청원이 존재합니다.")
    print(df.loc[df["content"]==text]["content"])


malist = twitter.pos(text, norm=True, stem=True)
#print(malist)
results=[]
for word in malist:
            # 어미/조사/구두점 등은 대상에서 제외 
            if not word[1] in ["Josa", "Eomi", "Punctuation"]:
                results.append(word[0])


type(results)
import re
p = re.compile('.*(개새끼|새끼|미친|병신|미치다).*')
bad1=[]
for mal in results:
    #print(mal)
    for r in p.findall(mal):
        bad1.append(r)
if len(bad1)>0:
    comment1 = "비속어가 검출되었습니다."
else:
    comment1 = "검출X"





p = re.compile('.*(정신병|빌어먹을|죽여주다|바보).*')
bad2=[]

for mal in results:

    for r in p.findall(mal):
 
        bad2.append(r)
        
if len(bad2)>0:
    comment2 = "폭력적인 어휘가 검출되었습니다."

else:
    comment2 = "검출X"

# 2-2. 집단혐오 어휘
import re
p = re.compile('.*(꼴페미|한남|흑형|짱깨).*')
bad3=[]

for mal in results:
    #print(mal)
    for r in p.findall(mal):
        #print(r)
        bad3.append(r)
        
if len(bad3)>0:
    comment3 ="집단혐오 어휘가 검출되었습니다."

else:
    comment3 = "검출X"

# 2-3. 청와대 권한을 넘어서는 어휘
import re
p = re.compile('.*(처벌|사형|수사).*')
bad4=[]

for mal in results:
    #print(mal)
    for r in p.findall(mal):
        #print(r)
        bad4.append(r)
        
if len(bad4)>0:
    comment4 = "청와대 권한을 넘어서는 어휘가 검출되었습니다."

else:
    comment4 = "검출X"


# In[ ]:


# 나머지는 그래도 복붙해서 보여주면 되요.

    