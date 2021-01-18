#!/usr/bin/env python
# coding: utf-8

# # Desktop Notifier for Covid-19

# In[6]:


from urllib.request import urlopen , Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier


# In[7]:


header = {"User-Agent":"Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/india/" , headers = header)
html = urlopen(req)


# In[8]:


html.status


# In[9]:


obj = bs(html)


# In[15]:


new_cases = obj.find("li",{"class":"news_li"}).strong.text.split()[0]


# In[20]:


death = list(obj.find("li",{"class":"news_li"}).strong.next_siblings)[1].text.split()[0]


# In[21]:


# Notifier
notifier = ToastNotifier()


# In[22]:


message = "New Cases - "+new_cases +"\nDeath - "+death


# In[24]:


message


# In[25]:


notifier.show_toast(title="COVID-19 Update" , msg=message , duration=5 , icon_path =r"virus.ico")


# In[ ]:




