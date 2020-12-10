#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___
# # Ecommerce Purchases Exercise
# 
# In this Exercise you will be given some Fake Data about some purchases done through Amazon! Just go ahead and follow the directions and try your best to answer the questions and complete the tasks. Feel free to reference the solutions. Most of the tasks can be solved in different ways. For the most part, the questions get progressively harder.
# 
# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
# 
# Also note that all of these questions can be answered with one line of code.
# ____
# ** Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom. **

# In[1]:


import pandas as pd


# In[3]:


ecom = pd.read_csv('Ecommerce Purchases')


# **Check the head of the DataFrame.**

# In[4]:


ecom.head()


# ** How many rows and columns are there? **

# In[5]:


ecom.info()


# ** What is the average Purchase Price? **

# In[6]:


ecom['Purchase Price'].mean()


# ** What were the highest and lowest purchase prices? **

# In[7]:


ecom['Purchase Price'].max()


# In[8]:


ecom['Purchase Price'].min()


# ** How many people have English 'en' as their Language of choice on the website? **

# In[17]:


ecom[ecom['Language']=='en'].count()


# ** How many people have the job title of "Lawyer" ? **
# 

# In[21]:


ecom[ecom['Job']=='Lawyer'].count()


# ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
# 
# **(Hint: Check out [value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) ) **

# In[25]:


ecom['AM or PM'].value_counts()


# ** What are the 5 most common Job Titles? **

# In[28]:


ecom['Job'].value_counts().head(5)


# ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

# In[30]:


ecom[ecom['Lot']=='90 WT']['Purchase Price']


# ** What is the email of the person with the following Credit Card Number: 4926535242672853 **

# In[32]:


ecom[ecom['Credit Card']==4926535242672853]['Email']


# ** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# In[37]:


ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()


# ** Hard: How many people have a credit card that expires in 2025? **

# In[40]:


sum(ecom['CC Exp Date'].str.contains('/25'))


# ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

# In[65]:


def emailhost(email):
    return email.split('@')[1]


# In[79]:


ecom['Email'].apply(lambda x: emailhost(x)).value_counts().head(5)


# # Great Job!
