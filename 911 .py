#!/usr/bin/env python
# coding: utf-8

# 911 PROJECT

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv('911.csv')


# In[5]:


df.info()


# In[6]:


df.head()


# In[7]:


df['zip'].value_counts().head(5)


# In[8]:


df['twp'].value_counts().head()


# In[10]:


df['title'].nunique()


# CREATING NEW FEATURE USING LAMBDA EXP

# In[16]:


x= df['title'].iloc[0]


# In[17]:


x.split(':')[0]


# In[18]:


df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])


# In[19]:


df['Reason'].value_counts()


# In[21]:


sns.countplot(x='Reason',data=df)


# In[23]:


type(df['timeStamp'].iloc[0])


# In[24]:


df['timeStamp']=pd.to_datetime(df['timeStamp'])


# In[25]:


type(df['timeStamp'].iloc[0])


# In[36]:


time=df['timeStamp'].iloc[0]
time.hour


# In[37]:


time.dayofweek


# In[38]:


df['Hour']= df['timeStamp'].apply(lambda time: time.hour)


# In[39]:


df['Month']= df['timeStamp'].apply(lambda time: time.month)
df['Day of week']= df['timeStamp'].apply(lambda time: time.dayofweek)


# In[40]:


df.head()


# In[41]:


dmap ={0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'fri',5:'Sat',6:'Sun'}


# In[43]:


df['Day of week']= df['Day of week'].map(dmap)


# In[44]:


df.head()


# count PLOT USING SEABORN

# In[48]:


sns.countplot(x='Day of week',data=df,hue='Reason',palette='viridis')
# to relocate the legend
plt.legend(bbox_to_anchor=(1.05,1),loc=2, borderaxespad=0.)


# In[49]:


sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')
# to relocate the legend
plt.legend(bbox_to_anchor=(1.05,1),loc=2, borderaxespad=0.)


# In[50]:


byMonth = df.groupby('Month').count()


# In[51]:


byMonth.head()


# In[53]:


byMonth['title'].plot()


# In[57]:


sns.countplot(x='Month',data=df,palette='viridis')
# to relocate the legend
plt.legend(bbox_to_anchor=(1.05,1),loc=2, borderaxespad=0.)


# In[58]:


byMonth.reset_index()


# In[59]:


sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())


# In[60]:


t = df['timeStamp'].iloc[0]


# In[66]:


df['Date']=df['timeStamp'].apply(lambda t:t.date())


# In[67]:


df.head()


# In[75]:


df.groupby('Date').count()['lat'].plot()
plt.tight_layout


# In[76]:


df[df['Reason']=='EMS'].groupby('Date').count()['lat'].plot()
plt.title('EMS')
plt.tight_layout


# # HEAT MAP

# In[83]:


dayHour = df.groupby(by=['Day of week','Hour']).count()['Reason'].unstack()


# In[88]:


plt.figure(figsize=[12,10])
sns.heatmap(dayHour,cmap='viridis')


# In[95]:


sns.clustermap(dayHour,cmap='coolwarm')


# In[91]:


dayMonth = df.groupby(by=['Day of week','Month']).count()['Reason'].unstack()
dayMonth.head()


# In[92]:


plt.figure(figsize=[12,10])
sns.heatmap(dayMonth,cmap='viridis')


# In[94]:


sns.clustermap(dayMonth,cmap='coolwarm')


# In[ ]:




