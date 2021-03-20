# Here are some simple return function examples to
# practice with.

def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def square(num1,num2):
    return num1**num2
def division(num1,num2):
    return num1/num2
def name(first_name,last_name,mc2=18600**2):
    return first_name+last_name+str(mc2)

a=addition(8,2)
s=subtraction(8,2)
m=multiplication(8,2)
d=division(8,2)
e=square(8,2)

nums=int(a+s+m+d+e)

name=name('Albert ','Einstein = ',nums)

# remove the 'nums' variable and see what happens when
# you re-execute/run the above Python program example.

print(name)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# How Parentheses, Square Brackets and Curly Braces
# work in Python.

# Parentheses: '()'
# Parentheses are used for 'Tuples', along with other uses,
# such as 'print' functions and functions alike.

# Square Brackets: '[]'
# Square Brackets are used for 'lists' and '2d lists', along
# with other uses, such as indexing character strings and
# values alike.

# Curly Braces: '{}'
# Curly Braces are used for 'sets' and 'dictionaries', along
# with other uses, such as formatted character strings.

# Here is a simple 'tuple' example:
# names=('John','Ron','Tom','Bob')

# Here is a simple 'list' example:
# names=['John','Ron','Tom','Bob']

# Here is a simple 'dictionary' example:
# names={1:'John',2:'Ron',3:'Tom',4:'Bob'}

# Here is a simple 'set' example:
# names={'John','Ron','Tom','Bob'}
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Variable Scope:

# L= Local
# E= Enclosing
# G= Global
# B=Built-in
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# predefined returned values to arguments example:

def values_example(value0,value1,value2,value3):
    return 0,1,2,3

print(values_example('Value0','Value1','Value2','Value3')[2])

# undefined returned values to arguments example:

# If you aren't sure how many returned values to variables
# are needed, use the '*args' function instead. You can name
# the word 'args' to any name you like, but the (*) is needed.
# For example: '*get_any_number_of_returned_values' works.
# However in python, programmers use the standard as '*args'
# short for (arguments). Use '*args' if you want to update the
# function's returned values, without the worry of how many
# actual argument variables are needed inside the 'print'
# statement, such as the example above illustrates.

# Example 1:

def args_example(*args):
    return args[0]

print(args_example(0,1,2,3,4,5,6,7,8,9))

# Example 2:

def args_example(*args):
    return 0,1,2,3,4,5,6,7,8,9

print(args_example()[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# undefined returned values to keyword arguments example:

# If you aren't sure how many returned values to variables are
# needed, use the '**kwargs' function instead. You can name the
# word 'kwargs' to any name you like, but the (**) is needed. For
# example: '**get_any_number_of_returned_values' works. However
# in python, programmers use the standard as '**kwargs' short for
# (keyword arguments). Use '**kwargs' if you want to update the
# function's returned values, without the worry of how many actual
# keyword argument variables are needed inside the 'return'
# statement.

def kwargs_example(**kwargs):
    return 0,1,2,3,4,5,6,7,8,9

print(kwargs_example()[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are the very same examples below, but with hard line
# breaks. In most cases, you must use parenthesis '()' to surround
# hard line breaks, such as these examples illustrate.

# Example 1:

def args_example(*args):
    return args[0]

print(args_example( # insert a hard line break if you like.
  'Text with numbers',0,1,2,3,4,5,6,7,8,9,'Example.'))

# Example 2:

def args_example(*args):
    return( # insert a hard line break if you like.
    'Text with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

print(args_example()[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def kwargs_example(**kwargs):
  return( # insert a hard line break if you like.
    'Text with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

print(kwargs_example()[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are the very same examples again, but with the use of
# variables to shorten our code a bit in the 'print' statements.

def args_example(*args):
  return args

args=args_example( # insert a hard line break if you like.
  'Text with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

print(args[0])

# Example 2:

def args_example(*args):
  return( # insert a hard line break if you like.
    'Text with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

args=args_example()

print(args[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def kwargs_example(**kwargs):
  return( # insert a hard line break if you like.
    'Text with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

kwargs=kwargs_example()

print(kwargs[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Using the knowledge we've learnt so far, let's create an
# arguments variable list loop using a for-loop.

def args_example(*args):
  return args

args=args_example( # insert a hard line break if you like.
  'Text with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

for i in args:
  print(i,end=' ') # add the 'end=' function to create single-line text output.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Using the knowledge we've learnt so far, let's create a
# keyword arguments variable list loop using a for-loop.

def kwargs_example(**kwargs):
  return( # insert a hard line break if you like.
    'Text with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

kwargs=kwargs_example()

for i in kwargs:
  print(i,end=' ') # add the 'end=' function to create single-line text output.
