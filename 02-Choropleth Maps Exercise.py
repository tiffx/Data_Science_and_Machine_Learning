#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # Choropleth Maps Exercise 
# 
# Welcome to the Choropleth Maps Exercise! In this exercise we will give you some simple datasets and ask you to create Choropleth Maps from them. Due to the Nature of Plotly we can't show you examples
# 
# [Full Documentation Reference](https://plot.ly/python/reference/#choropleth)
# 
# ## Plotly Imports

# In[48]:


import plotly.graph_objs as go
import chart_studio.plotly as py
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True) 


# ** Import pandas and read the csv file: 2014_World_Power_Consumption**

# In[22]:


import pandas as pd


# In[23]:


df = pd.read_csv('2014_World_Power_Consumption')


# ** Check the head of the DataFrame. **

# In[24]:


df.head()


# In[156]:





# ** Referencing the lecture notes, create a Choropleth Plot of the Power Consumption for Countries using the data and layout dictionary. **

# In[34]:


data = dict(type='choropleth',
           locations = df['Country'],
           locationmode = 'country names', 
           z = df['Power Consumption KWH'],
           text = df['Country'],
           marker = dict(line = dict(color = 'rgb(12,12,12)', width = 1)), 
           colorbar = {'title':'Power Consumption in KWH'})

layout = dict(title='2014 World Power Consumption KWH',
             geo = dict(showframe=False,
                       projection={'type':'natural earth'}))


# In[37]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# ## USA Choropleth
# 
# ** Import the 2012_Election_Data csv file using pandas. **

# In[39]:


df2 = pd.read_csv('2012_Election_Data')


# ** Check the head of the DataFrame. **

# In[40]:


df2.head()


# In[110]:





# ** Now create a plot that displays the Voting-Age Population (VAP) per state. If you later want to play around with other columns, make sure you consider their data type. VAP has already been transformed to a float for you. **

# In[51]:


data = dict(type = 'choropleth',
           colorscale = 'ylorrd', 
           locations = df2['State Abv'],
           locationmode = 'USA-states',
           z = df2['Voting-Age Population (VAP)'],
           text = df2['State'],
           marker = dict(line = dict(color = 'rgb(12,12,12)', width = 1)), 
           colorbar = {'title':'VAP per State'})

layout = dict(title='2012 Election Data',
             geo = dict(scope = 'usa', showlakes = True, lakecolor = 'rgb(85,173,240)'))


# In[ ]:





# In[52]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# # Great Job!
