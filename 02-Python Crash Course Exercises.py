#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp/?couponCode=PY20)

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


7**4


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[2]:


s = "Hi there Sam!"


# In[3]:


s.split()


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[4]:


planet = "Earth"
diameter = 12742


# In[7]:


print('The diameter of {} is {} kilometers.'.format(planet,diameter))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[8]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[12]:


lst[3][1][2]


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[13]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[29]:


print(d.get('k1')[3].get('tricky')[3].get('target')[3])


# ** What is the main difference between a tuple and a list? **

# In[23]:


# Tuple is immutable and list is mutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[30]:


def domainGet(email):
   return email.split('@')[1]


# In[31]:


domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[32]:


def findDog(string):
    return 'dog' in string.lower() 


# In[54]:


findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[55]:


def countDog(string):
    return string.lower().count('dog')


# In[56]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[41]:


seq = ['soup','dog','salad','cat','great']


# In[45]:


list(filter(lambda word: word.startswith('s'),seq))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[50]:


def caught_speeding(speed, is_birthday):
    if is_birthday:
        birthday_speed = speed-5
        if 60 >= birthday_speed:
            return 'No Ticket'
        elif 61 < birthday_speed <= 80:
            return 'Small Ticket'
        else:
            return 'Big Ticket'
    else:
        if 60 >= speed:
            return 'No Ticket'
        elif 61 < speed <= 80:
            return 'Small Ticket'
        else:
            return 'Big Ticket'


# In[51]:


caught_speeding(81,True)


# In[52]:


caught_speeding(81,False)


# # Great job!
