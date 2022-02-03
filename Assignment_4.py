#!/usr/bin/env python
# coding: utf-8

# Python Basic Assignment
# Assignment_4
Q1. What exactly is []?
Ans: It is used to create list in python.The data is written inside square brackets ([]), and the values are separated by comma(,).
# In[ ]:





# In[ ]:





# Q2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
# 

# In[3]:


spam = [2,4,6,8,10]


# In[5]:


spam[3]="hello"


# In[7]:


spam


# In[ ]:





# In[ ]:





# Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
# 

# In[ ]:





# In[ ]:





# Q3. What is the value of spam[int(int('3' * 2) / 11)]?

# In[9]:


spam = ['a','b', 'c' , 'd' ]


# In[14]:


'3'*2


# In[17]:


int('3'*2)/11


# In[18]:


int(int('3'*2)/11)


# In[11]:


spam[int(int('3'*2)/11)]


# In[ ]:





# In[ ]:




Q4. What is the value of spam[-1]?
# In[20]:


spam[-1]


# In[ ]:




Q5. What is the value of spam[:2]?
# In[22]:


spam[:2]


# In[ ]:





# In[ ]:




Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
# In[1]:


bacon = [3.14 , 'cat',11,'cat',True]

Q6. What is the value of bacon.index('cat')?
Ans: 1.
'cat' is present at index 1 and 3, python is giving the index number of 'cat' mentioned first in the list.
# In[26]:


bacon.index('cat')


# In[ ]:




Q7. How does bacon.append(99) change the look of the list value in bacon?
Ans: It will add 99 in the list named bacon. 
# In[2]:


bacon.append(99)


# In[3]:


bacon


# In[ ]:





# In[ ]:





# Q8. How does bacon.remove('cat') change the look of the list in bacon?
# Ans: It will remove str 'cat' from the list.

# In[5]:


bacon.remove('cat')


# In[6]:


bacon


# In[ ]:





# In[ ]:





# Q9. What are the list concatenation and list replication operators?
# Ans:The operator for list concatenation is +, while the operator for replication is *

# In[8]:


l1 = [1,2,3,4]
l2=[5,6,7,8]


# In[12]:


l1+l2  # concatenation


# In[14]:


l1*2  # replication


# In[ ]:





# In[ ]:




Q10. What is difference between the list methods append() and insert()?
Ans:The difference between the two methods is that.append () adds an item to the end of a list, whereas.insert () inserts and item in a specified position in the list.
# In[ ]:


#append()


# In[29]:


l1 = [1,2,3,4]
l2=[5,6,7,8]
l1.append(l2)    #list_name.append(element)
l1


# In[ ]:


#inser()


# In[30]:


l2


# In[31]:


l2.insert(1,'cat')  #list_name(index,element)


# In[32]:


l2


# In[ ]:





# In[ ]:





# Q11. What are the two methods for removing items from a list?
# Ans: The methods are remove(), pop() and clear() .Besides the list methods,we can also use a del keyword to remove items from a list.

# In[ ]:


#list.remove(element)


# In[1]:


l = [11,12,13,14,15]


# In[2]:


l.remove(13)


# In[3]:


l


# In[ ]:


#list.pop(index)


# In[9]:


l1 = [13,45,66,77,"sudh"]
l1.pop(0)


# In[10]:


l1


# In[11]:


#list.clear()


# In[13]:


l1


# In[15]:


l1.clear()


# In[16]:


l1


# In[17]:


#del list[index]


# In[26]:


l2 =[23,35,69,85,56,"ineuron"]


# In[27]:


del l2[0]


# In[28]:


l2


# In[ ]:





# In[ ]:




Q12. Describe how list values and string values are identical.
Ans:
(i) We can use len() function to both list and string.
(ii)Both can be concatenated and replicated.
(iii)We can use loop to both list and string.
(iv)We can use slicing on both of them.
(v)We can use indexing on both of them.
(vi) We can use in and not operator on both of them.

# In[ ]:





# In[ ]:




Q13. What's the difference between tuples and lists?
Ans:(i)tuples are immutable objects while the lists are mutable.
(ii)tuples are more memory efficient than the lists.
# In[31]:


t = (1,23,55,6,78)  # example of tuple
t[0]=100          # tuple are immutable


# In[34]:


l = [1,23,55,6,78] # example of list
l[0]=100   #list are immutable
l


# In[ ]:





# In[ ]:





# Q14. How do you type a tuple value that only contains the integer 42?
# Ans: t =(42,)

# In[36]:


t = (42,)


# In[37]:


type(t)


# In[ ]:





# In[ ]:




Q15. How do you get a list value's tuple form? How do you get a tuple value's list form?
Ans: we can do this by using list[] and tuple() functions.
# In[38]:


#for example


# In[41]:


#list from tuple
t =(1,2,3)
l =list(t)
l


# In[42]:


#tuple from list
l=[1,2,3]
t = tuple(l)
t


# In[ ]:





# In[ ]:




Q16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
Ans:A list variable holds a list of values (for example, logins or passwords) to be used in scenarios. We can say that they a kind of references to list value.
# In[ ]:





# In[ ]:




Q17. How do you distinguish between copy.copy() and copy.deepcopy()?
Ans:

The copy.copy() function will do a shallow copy.Shallow Copy stores the references of objects to the original memory address.   Q17. How do you distinguish between copy.copy() and copy.deepcopy()?

The copy.deepcopy() function will do a deep copy.Deep copy stores copies of the object’s value.
only copy.deepcopy() will duplicate any lists inside the  list