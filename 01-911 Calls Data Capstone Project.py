#!/usr/bin/env python
# coding: utf-8

# # 911 Calls Capstone Project

# For this capstone project we will be analyzing some 911 call data from [Kaggle](https://www.kaggle.com/mchirico/montcoalert). The data contains the following fields:
# 
# * lat : String variable, Latitude
# * lng: String variable, Longitude
# * desc: String variable, Description of the Emergency Call
# * zip: String variable, Zipcode
# * title: String variable, Title
# * timeStamp: String variable, YYYY-MM-DD HH:MM:SS
# * twp: String variable, Township
# * addr: String variable, Address
# * e: String variable, Dummy variable (always 1)
# 
# Just go along with this notebook and try to complete the instructions or answer the questions in bold using your Python and Data Science skills!

# ## Data and Setup

# ____
# ** Import numpy and pandas **

# In[1]:


import numpy as np
import pandas as pd


# ** Import visualization libraries and set %matplotlib inline. **

# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ** Read in the csv file as a dataframe called df **

# In[3]:


df = pd.read_csv('911.csv')


# ** Check the info() of the df **

# In[4]:


df.info()


# In[132]:





# ** Check the head of df **

# In[5]:


df.head()


# In[155]:





# ## Basic Questions

# ** What are the top 5 zipcodes for 911 calls? **

# In[6]:


df['zip'].value_counts().head(5)


# In[134]:





# ** What are the top 5 townships (twp) for 911 calls? **

# In[7]:


df['twp'].value_counts().head(5)


# In[135]:





# ** Take a look at the 'title' column, how many unique title codes are there? **

# In[8]:


df['title'].nunique()


# In[136]:





# ## Creating new features

# ** In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.** 
# 
# **For example, if the title column value is EMS: BACK PAINS/INJURY , the Reason column value would be EMS. **

# In[134]:


def reasoning(title):
    if 'EMS:' in title:
        return 'EMS'
    elif 'Fire:' in title:
        return 'Fire'
    elif 'Traffic:' in title:
        return 'Traffic'

df['Reason'] = df['title'].apply(lambda x: reasoning(x))


# In[9]:


# Best thing to do is grab an example and see what you would need to do to that example to get the result you want
# then use the solution for the lamdba expression
x = df['title'].iloc[0]


# In[10]:


x.split(':')[0]


# In[11]:


df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])


# In[12]:


df['Reason']


# ** What is the most common Reason for a 911 call based off of this new column? **

# In[135]:


df['Reason'].value_counts()


# In[138]:





# ** Now use seaborn to create a countplot of 911 calls by Reason. **

# In[22]:


sns.countplot(data = df, x='Reason',palette='viridis')
plt.show()


# In[139]:





# ___
# ** Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column? **

# In[13]:


type(df['timeStamp'].iloc[0])


# In[140]:





# ** You should have seen that these timestamps are still strings. Use [pd.to_datetime](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html) to convert the column from strings to DateTime objects. **

# In[14]:


df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[15]:


type(df['timeStamp'].iloc[0])


# In[17]:


time = df['timeStamp'].iloc[0]
time.hour
# time.dayofweek


# ** You can now grab specific attributes from a Datetime object by calling them. For example:**
# 
#     time = df['timeStamp'].iloc[0]
#     time.hour
# 
# **You can use Jupyter's tab method to explore the various attributes you can call. Now that the timestamp column are actually DateTime objects, use .apply() to create 3 new columns called Hour, Month, and Day of Week. You will create these columns based off of the timeStamp column, reference the solutions if you get stuck on this step.**

# In[18]:


df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# ** Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week: **
# 
#     dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

# In[19]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)


# In[20]:


df.head()


# ** Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column. **

# In[21]:


sns.countplot(data=df,x='Day of Week',hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


# In[168]:





# **Now do the same for Month:**

# In[40]:


sns.countplot(data=df,x='Month',hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


# In[3]:





# **Did you notice something strange about the Plot?**
# 
# _____
# 
# ** You should have noticed it was missing some Months, let's see if we can maybe fill in this information by plotting the information in another way, possibly a simple line plot that fills in the missing months, in order to do this, we'll need to do some work with pandas... **

# ** Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame. **

# In[47]:


byMonth = df.groupby('Month').count()


# In[48]:


byMonth.head()


# In[169]:





# ** Now create a simple plot off of the dataframe indicating the count of calls per month. **

# In[49]:


byMonth['Reason'].plot.line()
plt.show()


# In[175]:





# ** Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month. Keep in mind you may need to reset the index to a column. **

# In[50]:


byMonth_index_reset = byMonth.reset_index()


# In[51]:


byMonth_index_reset.head()


# In[54]:





# In[52]:


sns.lmplot(data=byMonth_index_reset,x='Month',y='twp')
plt.show()


# In[187]:





# **Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to use apply along with the .date() method. ** 

# In[53]:


df['Date'] = df['timeStamp'].apply(lambda time: time.date())


# In[54]:


df.head()


# ** Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.**

# In[58]:


byDate = df.groupby(df['Date']).count()


# In[59]:


byDate.head()


# In[60]:


byDate['Reason'].plot.line()
plt.tight_layout()
plt.show()


# In[197]:





# ** Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call**

# In[61]:


traffic = df[df['Reason']=='Traffic']
traffic.groupby('Date').count()['Reason'].plot()
plt.tight_layout()
plt.title('Traffic')
plt.show()


# In[199]:





# In[62]:


fire = df[df['Reason']=='Fire']
fire.groupby('Date').count()['Reason'].plot()
plt.tight_layout()
plt.title('Fire')
plt.show()


# In[201]:





# In[63]:


ems = df[df['Reason']=='EMS']
ems.groupby('Date').count()['Reason'].plot()
plt.tight_layout()
plt.title('EMS')
plt.show()


# In[202]:





# ____
# ** Now let's move on to creating  heatmaps with seaborn and our data. We'll first need to restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week. There are lots of ways to do this, but I would recommend trying to combine groupby with an [unstack](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.unstack.html) method. Reference the solutions if you get stuck on this!**

# In[65]:


tab1 = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
tab1


# In[203]:





# ** Now create a HeatMap using this new DataFrame. **

# In[68]:


plt.figure(figsize=(12,6))
sns.heatmap(data=tab1,cmap='viridis')
plt.show()


# In[204]:





# ** Now create a clustermap using this DataFrame. **

# In[260]:


sns.clustermap(data=tab1,cmap='viridis')
plt.show()


# In[205]:





# ** Now repeat these same plots and operations, for a DataFrame that shows the Month as the column. **

# In[69]:


tab2 = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
tab2


# In[207]:





# In[70]:


plt.figure(figsize=(12,6))
sns.heatmap(data=tab2,cmap='viridis')
plt.show()


# In[208]:





# In[267]:


sns.clustermap(data=tab2,cmap='viridis')
plt.show()


# In[209]:





# **Continue exploring the Data however you see fit!**
# # Great Job!
