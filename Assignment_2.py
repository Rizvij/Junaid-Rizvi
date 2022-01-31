#!/usr/bin/env python
# coding: utf-8
Python Basic Assignment
 Assignment_2Q1.What are the two values of the Boolean data type? How do you write them?
Ans:Python boolean type is one of the built-in data types provided by Python, which represents one of the two values i.e. True or False.Q2. What are the three different types of Boolean operators?
The three basic boolean operators are: AND, OR, and NOT
Ans:The three basic boolean operators are: AND, OR, and NOTQ3.Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

Ans:
1. AND BOOLEAN OPERATOR TRUTH TABLE
True and True = True.
True and False = False.
False and True = False.
False and False = False.

2. OR BOOLEAN OPERATOR TRUTH TABLE

True or True = True
True or False = True
False or True = True
False or False = False

3. NOT BOOLEAN TRUTH TABLE

not(True) = False
not(False) = True
Q4. What are the values of the following expressions?
(5 > 4) and (3 == 5)
Ans: False

not (5 > 4)
Ans: False

(5 > 4) or (3 == 5)
Ans:True

not ((5 > 4) or (3 == 5))
Ans: False

(True and True) and (True == False)
Ans: False

(not False) or (not True)
Ans:True
# In[2]:


(5>4) and (3==5)


# In[4]:


not (5 > 4)


# In[6]:


(5 > 4) or (3 == 5)


# In[8]:


not ((5 > 4) or (3 == 5))


# In[10]:


(True and True) and (True == False)


# In[12]:


(not False) or (not True)

Q5. What are the six comparison operators?
Ans:Less than(<),
Greater than(>), 
Less than or equal to(<=), 
Greater than or equal to(>=),
Equal to(==),
Not equal to (!=).Q6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

Ans: In python '=' is an assignment operator  which simply assigns a value. For example, if a = 5, then it simply means taht value 5 is assigned to variable a using assignment operator '='.

Equal to in python is is an opertor denotes ad '=='. It simply checks wheter two given operands are equa or not. For example, if a = 5 and b = 10 , then using equal to opertor we can check whether a is equal to b or not.
# In[14]:


a = 5


# In[20]:


b = 10 


# In[22]:


a == b

Q7. Identify the three blocks in this code:
Ans: In python , block begins every time we increase indentation of a line and ends  just before the corersponding unindentation.

# In[29]:


spam = 0
if spam == 10:
    print('eggs')  # indentation occured, This is Block 1.
    if spam > 5:   # Still Block 1
        print('bacon') #Still Block 1 but again indentation occured, Block 2 is created inside Block 1.
    else:              #still block 1 but indent decreased,therefore,block 2 ended in line above.
        print('ham') #still block 1 but indent increased, therefore,block 3 is created inside block 1
    print('spam')    #still block 1, indent decreased, therefore, block 3 ended in line above.
print('spam')      #indent decreased, block 1 ended in above line.




Q9.If your programme is stuck in an endless loop, what keys you’ll press?
Ans" Ctrl + CQ10. How can you tell the difference between break and continue?
Ans:Python break and continue are used inside the loop to change the flow of the loop from its standard procedure.

A break statement, when used inside the loop, will terminate the loop and exit. If used inside nested loops, it will break out from the current loop.

A continue statement will stop the current execution when used inside a loop, and the control will go back to the start of the loop.
# In[1]:


#Example of braek statement
a = 1
while a<5:
    print(a)
    if a == 4:
        break
    a = a+1
 


# In[3]:


#Example of continue statement
a = 1 
while a < 5 :
    print(a)
    a = a + 1
    if a == 3:
        continue
    

Q11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
Ans: All three will give same result.
# In[5]:


range(10)


# In[7]:


range(0,10)


# In[9]:


range(0,10,1)

Q12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
# In[16]:


# program that prints the numbers 1 to 10 using a for loop
for i in range(1,11):
    print(i)


# In[17]:


#program that prints the numbers 1 to 10 using a while loop
i = 1
while i<= 10:
    print(i)
    i+=1

Q13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
Ans: spam.bacon()