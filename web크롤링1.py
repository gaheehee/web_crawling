#!/usr/bin/env python
# coding: utf-8

# In[1]:


temp = 'hellohi'
print(temp[1])


# In[2]:


print(temp[-1])


# In[3]:


print(len(temp))


# In[5]:


print(temp[len(temp)-1])


# In[6]:


print(temp[1:3])


# In[12]:


temp = "i:can do it"
print(temp.split(":"))


# In[43]:


import requests 
from bs4 import BeautifulSoup

response = requests.get('http://naver.com')

data = BeautifulSoup(response.text,"html.parser")

print(data.title)
print(data.title.string)


# In[28]:


#header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}


# In[ ]:





# In[ ]:




