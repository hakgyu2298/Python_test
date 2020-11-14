#!/usr/bin/env python
# coding: utf-8

# In[4]:


np=[1.0,10.4,3.2,5.1,7.5,2.7]


# In[6]:


flotV=[np,np,np]


# In[7]:


flotV


# In[8]:


flotV[0]='Python'


# In[9]:


flotV


# In[11]:


import numpy as np


# In[12]:


a=np.array([1,2.5,4.0,5.5,7.0])


# In[13]:


a[3:]


# In[15]:


a.std()


# In[18]:


a.cumsum()


# In[19]:


print(a)


# In[20]:


print(a*2)


# In[21]:


print(a**2)


# In[22]:


print(np.sqrt(a))


# In[25]:


b=np.array([a,a**2])


# In[26]:


b


# In[27]:


b.sum(axis=0) #열끼리 더함


# In[28]:


b.sum(axis=1) #행끼리 더함


# In[31]:


import pandas as pd


# In[33]:


pandas_series=pd.Series([3000,3200,2700],
                       index=['2016-11-10','2016-11-11','2016-11-12'])


# In[34]:


print(type(pandas_series))


# In[35]:


pandas_series


# In[36]:


pandas_series[1:]


# In[37]:


df=pd.DataFrame([100,150,200,250,300],columns=['numbers'],
               index=['a','b','c','d','e'])


# In[38]:


df


# In[39]:


df.index


# In[40]:


df.columns


# In[ ]:





# In[ ]:




