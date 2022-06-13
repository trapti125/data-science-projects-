#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[11]:


data = pd. read_csv(r"student_data.csv")


# In[15]:


data.head()


# In[18]:


data.columns


# In[19]:


data.describe()


# In[20]:


data.isnull().sum()


# # relating the variables with scatter plots

# In[27]:


sns.relplot(x="failures",y="studytime",hue='freetime',data=data)


# In[28]:


sns.pairplot(data)


# In[31]:


sns.relplot(x="studytime",y="failures", kind='line' ,data =data)


# In[35]:


sns.catplot(x="studytime", y="failures", data=data)


# In[ ]:




