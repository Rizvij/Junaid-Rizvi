#!/usr/bin/env python
# coding: utf-8

# Assignment_6
Q1.What are escape characters, and how do you use them?
Ans: In python an escape character is a backslash \ followed by the character you want to insert.

It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return, "\b" is for backspace,"\f" is for form feed, "\ooo" is for octal value and "\xhh" is for  Hex value.


we can use escape character to insert characters that are illegal in a string,.
# In[5]:


# for example
print(" Delhi is \"capital\" of India")
# word "capital" is an illegal character as it is in double quote inside a string that is surrounded by double quotes.
# this problem can be fixed using \.

 "\" can be used to escape itself: "\\" is the literal backslash character.
# In[7]:


test1 = "This will insert \\ one backlash"
print(test1)


# In[ ]:





# In[ ]:





# Q2. What do the escape characters n and t stand for?
# Ans: "\t" is a tab, "\n" is a newline.

# In[9]:



test2 = "Hello\nWorld!"
print(test2) 


# In[10]:


test3 = "Hello\tWorld!"
print(test3) 


# In[ ]:





# In[ ]:




Q3. What is the way to include backslash characters in a string?
Ans: using \\
# In[11]:


test1 = "This will insert \\ one backlash"
print(test1)


# In[ ]:





# In[ ]:




Q4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?
Ans:Single quote character in the word Howl's not escaped a problem because the given string is in double quotes.
# In[ ]:





# In[ ]:




Q5. How do you write a string of newlines if you don't want to use the n character?
Ans:By using the parameter end ='\n' in print function.
# In[ ]:





# In[ ]:




Q6.6. What are the values of the given expressions?
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]
Ans:
# In[13]:


#'Hello, world!'[1]
print('Hello, world!'[1])


# In[15]:


#'Hello, world!'[0:5]
print('Hello, world!'[0:5])


# In[17]:


#'Hello, world!'[:5]
print('Hello, world!'[:5])


# In[20]:


#'Hello, world!'[3:]
print('Hello, world!'[3:])


# In[ ]:





# In[ ]:




Q7. What are the values of the following expressions?
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
Ans:
# In[21]:


#'Hello'.upper()
print('Hello'.upper())


# In[22]:


#'Hello'.upper().isupper()
#The isupper() method returns True if all the characters are in upper case, otherwise False.
print('Hello'.upper().isupper())


# In[23]:


#'Hello'.upper().lower()
print('Hello'.upper().lower())


# In[ ]:





# In[ ]:




Q8. What are the values of the following expressions?
Ans:'Remember, remember, the fifth of July.'.split()
'-'.join('There can only one.'.split())

# In[27]:


#You can use split() function to split a string based on a delimiter to a list of strings.
print('Remember, remember, the fifth of July.'.split())


# In[31]:


#You can use join() function to join a list of strings based on a delimiter to give a single string.
print('-'.join('There can only one.'.split()))


# In[ ]:





# In[ ]:




Q9. What are the methods for right-justifying, left-justifying, and centering a string?
Ans:The following methods are used for justifying stringscenter()

This function center aligns the string according to the width specified and fills remaining space of line with blank space if ‘ fillchr ‘ argument is not passed.

Syntax :
center( len, fillchr )

Parameters :
len : The width of string to expand it.
fillchr (optional): The character to fill in remaining space.

Return Value :
The resultant center aligned string expanding the given width.
# In[46]:


c = 'python for beginners'
c.center(30,'-')

ljust()

This function left aligns the string according to the width specified and fills remaining space of line with blank space if ‘ fillchr ‘ argument is not passed.

Syntax :
ljust( len, fillchr )

Parameters :
len : The width of string to expand it.
fillchr (optional): The character to fill in remaining space.

Return Value :
The resultant left aligned string expanding the given width.
# In[50]:


m = "python for beginners"
m.ljust(30,'-')

rjust()

This function right aligns the string according to the width specified and fills remaining space of line with blank space if ‘ fillchr ‘ argument is not passed.

Syntax :
rjust( len, fillchr )

Parameters :
len : The width of string to expand it.
fillchr (optional) : The character to fill in remaining space.

Return Value :
The resultant right aligned string expanding the given width.
# In[51]:


p = 'Python for beginners'
p.rjust(30,'-')


# In[ ]:





# In[ ]:




Q10. What is the best way to remove whitespace characters from the start or end?
Ans:lstrip() removes white spaces from left of the string and rstrip()  removes whitespaces from right of the string.

# In[53]:


p = '   python for beginners   '
p.lstrip()


# In[54]:


p = '   python for beginners   '
p.rstrip()

