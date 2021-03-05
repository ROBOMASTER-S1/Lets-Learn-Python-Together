# Let's have some FUNctions and see just how they work with
# variables and values alike. Each function example below clearly
# shows how variables and values behave, depending on how
# you arrange the variables and the values in your Python program.

# For example, if you use variables with values inside the function's
# actual parameters, the arguments in the 'print' statement are
# either present or not present at all. Here are a few examples of
# why this happens. The first function program example below
# doesn't have any values inside the function's parameters; only
# the variables (a,b) are present. The 'print' statement stores
# 'a' and 'b', and also calculates them. The 'function_variable(2,3)'
# calls the function 'function_variables(a,b), without the use of the
# colon. The values inside the function's caller 2,3 are added
# together, via the 'print' statement inside the function block.

def function_variables(a,b):
    print(a+b)

function_variables(2,3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# In this Python program example, one of the values are present.
# The variable 'b' and its value '3' are inside the function's actual
# parameters. This means you leave out the value of 'b', when
# calling the function, 'function_variable(2)'. The 'print' statement
# had already been performed, while remaining inside the function
# block, until called by the function's caller 'function_variables(2).

def function_variables(a,b=3):
    print(a+b)

function_variables(2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# In this Python program example, two values are present. The
# variables 'a' and 'b' and their values '2'  and '3' are inside the
# function's actual parameters. Once again, this means you now
# leave out all the variables values inside the function's caller:
# 'function_variables(), without the use of the colon.

def function_variables(a=2,b=3):
    print(a+b)

function_variables()

# Note: any variables with values inside function parameters must
# always start from the last variable in sequence to the right first,
# before you can use anymore variables with values inside any function
# parameters.

# Tips to visually remember this 'rule of thumb!'
'''
def example_function(a,b,c,d):
    pass
def example_function(a,b,c,d=2):
    pass
def example_function(a,b,c=4,d=2):
    pass
def example_function(a,b=5,c=4,d=2):
    pass
def example_function(a=8,b=5,c=4,d=2):
    pass
'''
# Note: you cannot add variables with values inside function parameters
# starting from left to right. You will get a 'non-default argument follows
# default argument' error. Some examples are:
'''
def example_function(a=8,b,c,d):
    pass
def example_function(a=8,b,c=7,d):
    pass
def example_function(a=8,b,c=7,d=3):
    pass
def example_function(a=8,b=4,c=7,d):
    pass
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_variables(a,b):

# return the result directly inside the 'print' statement througth the
# function's coller. You can store the returned function's caller inside
# a variable, such as this program example below illustrates.

    return a+b

print(return_function_variables(2,3)) # why not

c=return_function_variables(2,3) # do this instead?

print(c) # use a variable to shorten long lines of code.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_variables(a,b=3):

# return the result directly inside the 'print' statement througth the
# function's coller.

    return a+b

# 'c' stores the function caller 'return_function_variables(2)

c=return_function_variables(2)

# The 'print' statement holds the variable 'c', which holds the function
# caller 'return_function_variables(2).

print(c)

# Try the rest of these return function Python program examples
# out on your own. Just remember the 'rule of thumb' when it comes
# to variables and values inside function parameters. Remember to
# always start from the last variable in sequence to the right if you want
# to add values inside the function parameters.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_variables(a=2,b=3):
    return a+b

c=return_function_variables()

print(c)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_variables(answer,a,b):
    return answer+str(a+b)

c=return_function_variables('Your answer = ',2,3)

print(c)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_variables(answer,a,b=3):
    return answer+str(a+b)

c=return_function_variables('Your answer = ',2)

print(c)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_variables(answer,a=2,b=3):
    return answer+str(a+b)

c=return_function_variables('Your answer = ')

print(c)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_variables(
    answer='Your answer = ',a=2,b=3):
    return answer+str(a+b)

c=return_function_variables()

print(c)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def create_return_values(
    value1,value2,value3,value4,
    value5,value6,value7,value8):
    
    return\
            value1+value2+\
            value3+value4+\
            value5+value6+\
            value7+value8+\
            "And that's how it's done!" # non formatted string

get_returned_values=create_return_values(
    'Argument Value 1\n','Argument Value 2\n',
    'Argument Value 3\n','Argument Value 4\n',
    'Argument Value 5\n','Argument Value 6\n',
    'Argument Value 7\n','Argument Value 8\n')

print(get_returned_values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def create_return_values(
    value1='Value 1\n',value2='Value 2\n',
    value3='Value 3\n',value4='Value 4\n',
    value5='Value 5\n',value6='Value 6\n',
    value7='Value 7\n',value8='Value 8\n'):
    
    return\
            value1+value2+\
            value3+value4+\
            value5+value6+\
            value7+value8+\
            "And that's how it's done!" # non formatted string

get_returned_values=create_return_values()

print(get_returned_values)

get_returned_values=create_return_values(
    'Argument Value 1\n','Argumet Value 2\n')

print(get_returned_values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def create_return_values(
    value1='Value 1\n',value2='Value 2\n',
    value3='Value 3\n',value4='Value 4\n',
    value5='Value 5\n',value6='Value 6\n',
    value7='Value 7\n',value8='Value 8\n'):
    
    return '{}{}{}{}{}{}{}{}And that\'s how it\'s done!'\
           .format(
               value1,value2,value3,value4,
               value5,value6,value7,value8) # old formatted string

get_returned_values=create_return_values()

print(get_returned_values)

get_returned_values=create_return_values(
    'Argument Value 1\n','Argumet Value 2\n')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def create_return_values(
    value1='Value 1\n',value2='Value 2\n',
    value3='Value 3\n',value4='Value 4\n',
    value5='Value 5\n',value6='Value 6\n',
    value7='Value 7\n',value8='Value 8\n'):
    
    return\
            f'{value1}{value2}{value3}\
{value4}{value5}{value6}{value7}\
{value8}And that\'s how it\'s done!' # new formatted f' string

get_returned_values=create_return_values()

print(get_returned_values)

get_returned_values=create_return_values(
    'Argument Value 1\n','Argumet Value 2\n')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_math_result(first_name,last_name,mc2,expon):
    return first_name+last_name+str(mc2**expon)

get_math_result=return_math_result('Albert ','Einstein ',186000,2)

albert_einstein=get_math_result

print(albert_einstein)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_math_result(first_name,last_name,mc2,expon=2):
    return first_name+last_name+str(mc2**expon)

get_math_result=return_math_result('Albert ','Einstein ',186000)

albert_einstein=get_math_result

print(albert_einstein)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_math_result(
    first_name,last_name,mc2=186000,expon=2):
    return first_name+last_name+str(mc2**expon)

get_math_result=return_math_result('Albert ','Einstein ')

albert_einstein=get_math_result

print(albert_einstein)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_math_result(
    first_name,last_name='Einstein ',mc2=186000,expon=2):
    return first_name+last_name+str(mc2**expon)

get_math_result=return_math_result('Albert ')

albert_einstein=get_math_result

print(albert_einstein)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_math_result(
    first_name='Albert ',last_name='Einstein ',
    mc2=186000,expon=2):
    return first_name+last_name+str(mc2**expon)

get_math_result=return_math_result()

albert_einstein=get_math_result

print(albert_einstein)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def  return_math_result(num1,num2):
    return num1**num2

mc2=return_math_result(186000,2)

print(mc2) # non formatted string

print('{:,}'.format(mc2)) # old formatted string

print(f'{mc2:,}') # new formatted f' string
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def  return_math_result(num1,num2=2):
    return num1**num2

mc2=return_math_result(186000)

print(mc2) # non formatted string

print('{:,}'.format(mc2)) # old formatted string

print(f'{mc2:,}') # new formatted f' string
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def  return_math_result(num1=186000,num2=2):
    return num1**num2

mc2=return_math_result()

print(mc2) # non formatted string

print('{:,}'.format(mc2)) # old formatted string

print(f'{mc2:,}') # new formatted f' string
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# For when you get bored, try these two Python programming experiments out.

def get_value(name,program,book,author='by Joseph C. Richardson'):
    return name,program,book,author,'is GREAT!'

get_name=get_value('Python','Programmer\'s','Glossary Bible')

for i in get_name:
    print(i,end=' ')

# Try this global variables function experiment out and see what happens
# when you delete or comment out the 'science()' function call statement,
# using the '#' in front of it like this: # science(), or simply delete it.

a,e='atom','electron'

def science():
    global a,e
    a,e='Albert','Einstein'

science() # comment out, or delete this function call statement.
    
print(a,e)
