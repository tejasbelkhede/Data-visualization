#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df=pd.read_csv("titanic-training-data.csv")


# In[3]:


df.head()


# In[4]:


df=df.drop(["PassengerId","Name","Ticket","Cabin"],axis=1)
df.head()


# In[5]:


sns.countplot(x="Survived",data=df)
plt.show()


# In[6]:


sns.countplot(x="Pclass",data=df)
plt.show()


# In[7]:


df.describe()


# In[8]:


sns.boxplot(x="Age",data=df)
plt.show()


# In[9]:


sns.boxplot(x="SibSp",data=df)
plt.show()


# In[10]:


sns.boxplot(x="Parch",data=df)
plt.show()


# In[11]:


plt.hist(x="Age",data=df)
plt.show()


# In[12]:


sns.countplot(x="Survived",hue="Sex",data=df)
plt.show()


# In[13]:


sns.countplot(x="Survived",hue="Pclass",data=df)
plt.show()


# In[14]:


sns.countplot(x="Survived",hue="Embarked",data=df)
plt.show()


# In[15]:


sns.relplot(x="Age",y="Fare",data=df)


# In[16]:


sns.relplot(x="Parch",y="Fare",data=df)


# In[17]:


sns.relplot(x="SibSp",y="Parch",data=df)


# In[18]:


sns.relplot(x="Fare",y="Pclass",data=df)


# In[20]:


sns.catplot(x="Survived",y="Age",data=df)


# In[21]:


sns.catplot(x="Pclass",y="Age",data=df)


# In[22]:


sns.catplot(x="Pclass",y="Age",data=df,kind='box')


# In[24]:


import warnings
warnings.filterwarnings("ignore")


# In[25]:


sns.catplot(x="Pclass",y="Age",data=df,kind='swarm')


# In[26]:


sns.catplot(x="Pclass",y="Age",data=df,kind='violin')


# In[27]:


sns.pairplot(df)


#  #multivariate analysis

# In[28]:


sns.catplot(x="Survived",y="Age",hue="Sex",data=df)


# In[30]:


sns.catplot(x="Pclass",y="Age",hue="Survived", data=df,kind='violin')


# In[31]:


sns.catplot(x="Pclass",y="Age",hue="Survived", data=df,kind='box')


# In[32]:


sns.catplot(x="Pclass",y="Age",hue="Survived", data=df,kind='swarm')


# In[33]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[34]:


df=pd.read_csv("CardioGoodFitness-1.csv")


# In[35]:


df.head()


# In[36]:


sns.countplot(x="Product",data=df)
plt.show()


# In[37]:


df.describe()


# In[38]:


sns.countplot(x="Age",data=df)
plt.show()


# In[39]:


sns.boxplot(x="Age",data=df)
plt.show()


# In[40]:


sns.boxplot(x="Education",data=df)
plt.show()


# In[41]:


sns.boxplot(x="Fitness",data=df)
plt.show()


# In[42]:


sns.boxplot(x="Income",data=df)
plt.show()


# In[43]:


sns.countplot(x="Age",hue="Income",data=df)
plt.show()


# In[ ]:




