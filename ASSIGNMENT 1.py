#!/usr/bin/env python
# coding: utf-8
1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.ANS:

*  is an expression
'hello' is a string(value)
-87.8 is a float(value)
- is an expression

/ is an expression

+	Is an expression
6 is an integer(value)

2. What is the difference between string and variable?
ANS: A variable is like an empty bucket in which we can store anything from strings to numbers.
we can think of it as an identifier in which we can store a value in the memory location and to manipulate it if needed.

A string is a data type of sequenec of character. For example "sudhanshu".3. Describe three different data types.
Ans:
integer like 1,2,3
boolean (True and False)
string("sudh")
4. What is an expression made up of? What do all expressions do?
Ans:An expression is a combination of values, variables, operators, and calls to functions. Expressions need to be evaluated. If you ask Python to print an expression, the interpreter evaluates the expression and displays the result.5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
Ans:
Expression:
Expression is made up of values, containers, and mathematical operators (operands) and the statement is just like a command that a python interpreter executes like print.

Example: x = 5, y = 3, z = x + y

In the above example x, y and z are variables, 5 and 3 are values, = and + are operators.

So, the first combination x = 5 is an expression, the second combination y = 3 is an another expression and at last, z = x + y is also an expression.
An Expression always evaluates (calculate) to itself.


Statement:

statement may or may not produces or displays a result value, it only does whatever the statement says.

A Statement is the smallest executable unit of code that has an effect, like creating a variable or displaying a value.

Each and every line of code that we write in any programming language is called a statement.

Because, all the lines are executable by the interpreter or the compiler of that programming language.
Example:
 x = 3
print(x)

Output:
3

The first line is an assignment statement that gives a value to x. The second line is a print statement that displays the value of x.

When you type a statement then the interpreter executes it, which means that it does whatever the statement says.

Some other kinds of statements in Python are – if statement, else statement, while statement, for statement, import statement, etc. which will be discussed on later article.

6. After running the following code, what does the variable bacon contain?
Ans: 23
# In[2]:


bacon = 22
bacon +1

7. What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3

Ans:
'spam' + 'spamspam'
output:
'spamspamspam'

'spam' * 3
output:
'spamspamspam'

# In[4]:


'spam' + 'spamspam'


# In[6]:


'spam' * 3

8. Why is eggs a valid variable name while 100 is invalid?
Ans: This is because a variable names cannot begin with a number.9. What three functions can be used to get the integer, floating-point number, or string version of a value?
Ans:The int(), float(), and str() functions will evaluate to the integer, floating-point number, and string versions of the value passed to them.10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'
Ans: the above expression causes an error as we can not combine an integer with a string.
In the above question 99 is an integer while expression 'I have eaten ' & ' burritos' are strings.

To solve this we should use "99" intead of 99.
# In[8]:


'I have eaten ' + 99 + ' burritos.'

correct code
# In[9]:


'I have eaten ' + "99" + ' burritos.'

