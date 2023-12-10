#!/usr/bin/env python
# coding: utf-8

# In[70]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split


stroke = pd.read_csv('full_data.csv')
stroke.info()


# In[71]:


stroke.head()


# In[72]:


stroke['smoking_status'].unique()


# In[73]:


stroke['smoking_status'].value_counts()


# In[74]:


#stroke[stroke['smoking_status']=='never smoked']
stroke[['stroke','ever_married']][stroke['smoking_status']=='never smoked']


# In[94]:


train_set,test_set = train_test_split(stroke,test_size=0.1,random_state=42)
gender=train_set['gender']
stroke.head()


# In[95]:


ax = sns.countplot(x="gender", data=stroke,)
plt.title("Female = 1 & Male = 0")


# In[96]:


plt.hist(stroke['age'],bins=10,edgecolor='black')
plt.title("age")plt.hist(stroke['age'],bins=10,edgecolor='black')
plt.title("age")


# In[78]:


ax = sns.countplot(x="hypertension", data=stroke,)
plt.title("0 = Doesn't have hypertension & 1 = Have hypertension")


# In[79]:


ax = sns.countplot(x="heart_disease", data=stroke,)
plt.title("0 = Doesn't have heart_disease & 1 = Have heart_disease")


# In[80]:


ax = sns.countplot(x="ever_married", data=stroke,)
plt.title(" not married or married")


# In[81]:


stroke['work_type'].unique()


# In[82]:


ax = sns.countplot(x="work_type", data=stroke,)
plt.title("Private or Self-employed or  Govt_job or children")


# In[83]:


ax = sns.countplot(x="Residence_type", data=stroke,)
plt.title("urban or rural")


# In[84]:


plt.hist(stroke['avg_glucose_level'],bins=10,edgecolor='black')
plt.title("avg_glucose_level")


# In[85]:


plt.hist(stroke['bmi'],bins=10,edgecolor='black')
plt.title("bmi")


# In[86]:


stroke['smoking_status'].unique()


# In[89]:


ax = sns.countplot(x="smoking_status", data=stroke,)
plt.title("formerly smoked or never smoked or  smokes or Unknown")


# In[107]:


ax = sns.countplot(x="stroke", data=stroke,)
plt.title("  dont have stroke = 0 & have stroke = 1")


# In[ ]:




