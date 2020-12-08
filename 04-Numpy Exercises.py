#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[7]:


import numpy as np


# #### Create an array of 10 zeros 

# In[8]:


np.zeros(10)


# In[2]:





# #### Create an array of 10 ones

# In[9]:


np.ones(10)


# In[3]:





# #### Create an array of 10 fives

# In[10]:


np.ones(10)*5


# In[4]:





# #### Create an array of the integers from 10 to 50

# In[11]:


np.arange(10,51)


# In[5]:





# #### Create an array of all the even integers from 10 to 50

# In[ ]:


np.arange


# In[20]:


np.arange(10,51,2)


# In[6]:





# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[64]:


np.arange(9).reshape(3,3)


# In[7]:





# #### Create a 3x3 identity matrix

# In[22]:


np.eye(3,3)


# In[8]:





# #### Use NumPy to generate a random number between 0 and 1

# In[65]:


np.random.rand(1)


# In[15]:





# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[32]:


np.random.randn(25)


# In[33]:





# #### Create the following matrix:

# In[38]:


np.arange(0.01,1.01,0.01).reshape(10,10)


# In[66]:


np.linspace(0.01,1,100).reshape(10,10)


# In[35]:





# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[43]:


np.linspace(0,1,20)


# In[36]:





# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[50]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[51]:


mat[2:,1:]


# In[40]:





# In[53]:


mat[3,-1]


# In[41]:





# In[55]:


mat[:3,1].reshape(3,1)


# In[67]:


mat[:3,1:2]


# In[42]:





# In[56]:


mat[-1,:]


# In[46]:





# In[57]:


mat[3:,:]


# In[49]:





# ### Now do the following

# #### Get the sum of all the values in mat

# In[58]:


mat.sum()


# In[50]:





# #### Get the standard deviation of the values in mat

# In[59]:


mat.std()


# In[51]:





# #### Get the sum of all the columns in mat

# In[63]:


mat.sum(0)


# In[53]:





# # Great Job!
