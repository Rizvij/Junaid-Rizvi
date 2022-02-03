#!/usr/bin/env python
# coding: utf-8
Python Basic AssignmentAssignment_3
# In[ ]:




Q1. Why are functions advantageous to have in your programs?
Ans: Beacause of Functions , we dont have to write same code again and again.i.e, a function reduce the need for duplocate code which makes programm short and easy to read and update.

# In[ ]:




Q2.When does the code in a function run: when it's specified or when it's called?
Ans: A code function runs when its called.
# In[ ]:




Q3. What statement creates a function?
Ans:The def statement creates a function.
# In[2]:


#for example
def test(a,b):
    return a+b


# In[4]:


test(4,2)


# In[ ]:




Q4. What is the difference between a function and a function call?
Ans:

A function is a block of code that does a particular operation and returns a result. It usually accepts inputs as parameters and returns a result. The parameters are not mandatory.

A function call means invoking or calling that function. Unless a function is called there is no use of that function.


# In[5]:


# example of function
def test(a,b):
    return a*b


# In[7]:


#example of calling a function

test(5,6)

Q5. How many global scopes are there in a Python program? How many local scopes?
Ans:The scope of global variables is the entire program whereas the scope of local variable is limited to the function where it is defined.

In python,There is one global scope, and a local scope is created whenever a function is called.
# In[ ]:




Q6. What happens to variables in a local scope when the function call returns?
Ans:When a function returns, the local scope is destroyed, and all the variables in it are forgotten.
# In[ ]:




Q.7. What is the concept of a return value? Is it possible to have a return value in an expression?
Ans:A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression.
# In[4]:


# for example
def test(a,b):
    #returning sum od a and b
    return a+b


# In[7]:


test(4,5) + 5 # using return as an expression


# In[ ]:




Q8. If a function does not have a return statement, what is the return value of a call to that function?
Ans:If no return statement appears in a function definition, control automatically returns to the calling function after the last statement of the called function is executed. In this case, the return value of the called function is undefined.
# In[10]:


def test1(a,b):
    c = a*b
    


# In[12]:


test1(4,5)


# In[ ]:




Q9. How do you make a function variable refer to the global variable?
Ans: By using keyword global.
# In[2]:


x = "awesome"

def myfunc():
    print("ineuron is " + x)
myfunc()    
# x is a global variable beacuse it is created outside of function.


# In[6]:


# In this code both global ans local variable are created with same name x.
x = "awesome"   # global variable

def myfunc():
    x = "fantastic"  # here x is a local variable as it is created inside function and can be used inside the function only.
    print("ineuron is " + x)
    print(id(x))
myfunc()
print("ineuron is " + x)
print(id(x))

# we can see both x are stored in different location id as one is a local and other is a global variable.


# In[8]:


#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
    print("ineuron is " + x)
    print(id(x))
myfunc()
print("ineuron is " + x)
print(id(x))

# in this code x inside the funtion is also a global variable due to use of word global.
#id location of x is same as x inside and outside the function are global.


# In[ ]:





# Q10. What is the data type of None?
# Ans: None type.
# 
# None is used to define a null value. It is not the same as an empty string, False, or a zero. It is a data type of the class NoneType object. 
# 
# Assigning a value of None to a variable is one way to reset it to its original, empty state.

# In[10]:


print(type(None))


# In[12]:


x = None
type(x)


# In[ ]:





# Q11. What does the sentence import areallyourpetsnamederic do?
# Ans: It will import  module named areallyourpetsnamederic.

# In[ ]:





# Q12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
# Ans: This function can be called with spam.bacon()

# In[ ]:





# Q13. What can you do to save a programme from crashing if it encounters an error?
# Ans:Error handling can be used to notify the user of why the error occurred and gracefully exit the process that caused the error.

# In[7]:


try:
    def test(a,b):
        return a/b
    test(2,0)
except Exception as e:
    print("error:", e)


# In[ ]:




Q14. What is the purpose of the try clause? What is the purpose of the except clause?
Ans:Except statement catches an exception. It is used to test code for an error which is written in the “try” statement. If an error is encountered, the contents of the “except” block are run.