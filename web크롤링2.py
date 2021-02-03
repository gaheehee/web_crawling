#!/usr/bin/env python
# coding: utf-8

# In[20]:


import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.consumerreports.org/cro/a-to-z-index/products/index.htm")

data = BeautifulSoup(response.text,"html.parser")

subdata = data.find_all("a",class_ ="products-a-z__results__item")

for i in subdata:
    if i.string is not None:
        print(i.string.strip())
    # stirng 붙이면 태그 빼고 안의 내용만 나옴
    # strip: 공백 없애기


# In[34]:


import pandas as pd

menupan = {'Delivery': [19000,20000,1000,5000],
          'Normal': [17000,18000,1000,5000],
          'Togo': [16000,17000,1000,5000]}

df = pd.DataFrame(menupan)
df.index = ['치킨','피자','사이다','맥주']

newC = ['Normal','Delivery','Togo','Crazy']
df2 = pd.DataFrame(menupan, columns = newC)
df2.index = ['치킨','피자','사이다','맥주']

df2.Crazy = 1000

print(df2)
print(df2.index)
print(df2.values)
print(df2.columns)


# In[47]:


#%matplotlib inline
from matplotlib import pyplot as plt

plt.plot([1,2,3],[1,4,9])
plt.plot([2,3,4],[5,6,7])
                            
plt.xlabel('City')
plt.ylabel('Response')
plt.title('Exper iment Result')

plt.legend(['Mouse','Cat'])

plt.show()


# In[46]:


from matplotlib import pyplot as plt

y = [5,3,6,5,1,4,6,6]
x = range(len(y))
plt.bar(x,y,width = 0.5, color = 'blue')
plt.show()


# In[50]:


from matplotlib import pyplot as plt

'''figure = plt.figure()
axes1 = figure.add_subplot(121)
axes2 = figure.add_subplot(122)'''

figure, axes = plt.subplots(2,2)

axes[0][0].plot([1,2])
axes[0][1].plot([2,1])
axes[1][0].plot([1,2])
axes[1][1].plot([2,1])

plt.show()


# In[76]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import wordcloud

keywords={"Hello":2, "Python":2,"World":1, "hihi":1, "UiJin" : 4, "GaHee" : 4,"JiYeong":4}

wc = wordcloud.WordCloud("C:\\Windows\\Fonts\\H2GTRE.TTF")
cloud = wc.generate_from_frequencies(keywords)

figure = plt.figure()
plt.imshow(cloud)
plt.show()

figure.savefig('wordCloud.png')


# In[89]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

response = requests.get("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")

data= BeautifulSoup(response.text,"lxml")
         
seoul = data.find("location")

seoulDict = {}
for seouldata in seoul.find_all("data"):
    #print(seouldata)
    seoulDict[seouldata.tmef.string] = [int(seouldata.tmn.string), int(seouldata.tmx.string)]

df = pd.DataFrame(seoulDict)
df2 = df.transpose()
#print(df)

plt.plot(df2)
plt.show()


# In[ ]:




