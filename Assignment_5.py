#!/usr/bin/env python
# coding: utf-8

# Python Basic Assignment
# Assignment_4

# Q1. What does an empty dictionary's code look like?

# In[3]:


d ={}


# In[5]:


type(d)


# In[ ]:





# In[ ]:





# Q2. What is the value of a dictionary value with the key 'foo' and the value 42?

# In[11]:


d = {"foo": 42}


# In[29]:


d["foo"]


# In[ ]:





# In[ ]:




Q3. What is the most significant distinction between a dictionary and a list?
Ans:A list is an ordered sequence of objects, whereas dictionaries are unordered sets. However, the main difference is that items in dictionaries are accessed via keys and not via their position.
# In[30]:


l =[22,33,5,6,7,] # example of list


# In[32]:


l[3]   # an item in a list can be accesed by its index number


# In[37]:


d = {"key1":"junaid" , "key2":"rizvi"}  # example of a dictionary


# In[39]:


d["key1"]          # we can access a dictioanry by key value.


# In[ ]:





# In[ ]:




Q4.What happens if you try to access spam['foo'] if spam is {'bar': 100}?
Ans: we get a KeyError as spam is a dictionary and can be accessed by keyword 'bar' only.
# In[41]:


spam = {'bar':100}


# In[43]:


spam['foo']


# In[ ]:





# In[ ]:





# Q5.If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# Ans: Basically there is no difference between the two. Both cheks whether 'cat' is a key in dictionary spam.
# 
# The in operator checks whether a value exists as a key in the dictionary, in case it is present, the in operator will return True otherwise False.
# 
# 

# In[46]:


spam = {'cat': 2}


# In[53]:


spam.keys()


# In[54]:


'cat' in spam.keys()


# In[50]:


'cat' in spam


# In[ ]:





# In[ ]:





# Q6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

# In[30]:


#this question is same as Q5.

Ans:Ans: Basically there is no difference between the two. Both cheks whether 'cat' is a key in dictionary spam.

The in operator checks whether a value exists as a key in the dictionary, in case it is present, the in operator will return True otherwise False.

# In[31]:


spam = {'cat': 2}


# In[32]:


'cat' in spam.keys()


# In[33]:


'cat' in spam


# In[ ]:





# In[ ]:




Q7. What is a shortcut for the following code?
if 'color' not in spam:
spam['color'] = 'black'

# In[ ]:





# In[13]:


spam ={}
if 'color' not in spam:
    spam['color'] = 'black'


# In[14]:


spam


# In[15]:


# short cut of above code


# In[17]:


spam.setdefault('color', 'black')
spam


# In[ ]:





# In[ ]:




Q.8. How do you "pretty print" dictionary values using which module and function?
Ans:First, declare an array of dictionaries. Afterward, pretty print it using the function pprint.pprint()
# In[22]:


import pprint 


# In[27]:


d1  = {'name' : "sudhanshu" , "mo_no" :3454354353 , "mail_id" :"sudhanshu@xyz.com",'key1':[4,5,6,7] , "key2" :(3,4,5,6),"key3" : {3,4,5,4,3,3,3,3,3,3,3},'key4':{1:5,4:6}}


# In[28]:


pprint.pprint(d1)


# In[29]:


print(d1)  #printing with pretty print


# In[ ]:




