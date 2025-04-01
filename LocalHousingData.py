#!/usr/bin/env python
# coding: utf-8

# Local County Housing Survey Data

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
#import scipy 
import pandas as pd

#filename not included for public
housing_data = pd.read_csv(filename, sep='\t')


# In[4]:


housing_data['Question1'].value_counts().plot(kind='bar')
plt.title("Are you currently unhoused or worried that you might lose your housing?")
plt.xlabel("")


# In[5]:


housing_data['Question3'].value_counts().plot(kind='bar')
plt.title("Do you rent or own your home?")
plt.xlabel("")


# In[6]:


housing_data['Question4'].value_counts().plot(kind='bar')
plt.title("Have you ever given or received financial assistance for housing related expenses?")
plt.xlabel("")


# In[7]:


housing_data['Question5'].value_counts().plot(kind='bar')
plt.title("Have you or a loved one had trouble paying your mortgage or rent in the last year?")
plt.xlabel("")


# In[8]:


housing_data['Question6'].value_counts().plot(kind='bar')
plt.title("If you own your home, have you had trouble paying your property taxes?")
plt.xlabel("")


# In[54]:


housing_data['Question7'].value_counts().plot(kind='bar')
plt.title("Have you ever had to forgo another bill or expense to pay your rent or mortgage?")
plt.xlabel("")


# In[9]:


housing_data['Question8'].value_counts().plot(kind='bar')
plt.title("Have you or a loved one seen a large increase in your utility bill in the last two years?")
plt.xlabel("")


# In[56]:


housing_data['Question9'].value_counts().plot(kind='bar')
plt.title("Within 10 blocks of your home, have you seen a major development project be built in the last 5 years?")
plt.xlabel("")


# In[10]:


housing_data['Question10'].value_counts().plot(kind='bar')
plt.title("Are you concerned about the future of housing for yourself or your loved ones in this area? (ex. Will it be affordable to live here, retire here?)")
plt.xlabel("")


# In[11]:


housing_data['Question11'].value_counts().plot(kind='bar')
plt.title("If you've seen recent development in your community, are you concerned these developments will lead to less affordable rental or housing costs?")
plt.xlabel("")


# In[59]:


housing_data['Question12'].value_counts().plot(kind='bar')
plt.title("Have you seen an increase in the number of unhoused people in your congregation, family, community, or neighborhood?")
plt.xlabel("")


# In[12]:


housing_data['Question13'].value_counts().plot(kind='bar')
plt.title("Does you home need major repairs that you cannot afford?")
plt.xlabel("")


# In[13]:


housing_data['Question14'].value_counts().plot(kind='bar')
plt.title("Do you believe the city/county is doing enough to proactively invest in safe, affordable housing for all of us?")
plt.xlabel("")


# In[14]:


housing_data['Question15'].value_counts().plot(kind='bar')
plt.title("Have you felt unsafe in your neighborhood in the last year?")
plt.xlabel("")


# In[15]:


housing_data['Question16a'].value_counts().plot(kind='bar')
plt.title("Have you moved in the past 12 months?")
plt.xlabel("")


# In[16]:


housing_data['Question17'].value_counts().plot(kind='bar')
plt.title("How often have you moved in the last 10 years?")
plt.xlabel("")


# In[17]:


housing_data['Question20'].value_counts().plot(kind='bar')
plt.title("Would you be willing to share your story in a public meeting?")
plt.xlabel("")


# In[18]:


housing_data['Question21'].value_counts().plot(kind='bar')
plt.title("Can we contact you about future actions we are taking to address this issue?")
plt.xlabel("")


# In[ ]:




