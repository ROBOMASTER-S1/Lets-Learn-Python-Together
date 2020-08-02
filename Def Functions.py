'''The Definition Function:'''
'''
Most Python programs consist of functions. Functions in Python allow programmers to \
add functionality in their programs that might be needed again and again throughout \
the program's execution run. With functions, programmers can call/execute functions \
from another file as part of the main program’s execution run from the main file. Note: \
calling files from other files must be stored within the same directory path or folder; via \
Windows for example. Functions can also return values, which can be changed or modified \
throughout the program’s execution run. Just remember that functions simply add \
functionality. Also remember the acronym or abbreviation (DRY): Don’t Repeat Yourself!           
'''
# Definition functions are called def functions for short. Def function statements
# always start with the word ‘def’ followed by parameters or without parameters.
# However, all def statements must proceed with a semicolon (:) at the end of all def
# statements. For example, def example(): is a function without parameters, whereas
# def example(self,name,age): has three parameters. The semicolon assures that any
# program statements underneath the def statements are always indented, which is
# Python’s way of keeping the program statements as part of the complete def
# function. Note: any program statements, which are not indented will simply be
# bypassed altogether, meaning they won’t be executed as part of the def function at
# all; thus creating potential errors to occur. Now it's time to get your feet a little bit
# more wet. Are you ready?

# Like strings, def functions must not have any empty spaces between words. Use an
# underscore ie: (_) in place of empty spaces instead.

# This small program shows no output whatsoever on the screen.

def my_first_function():
    print('My first function')

# Now, let's call the function with the following statement so we can see the output on
# the screen.

my_first_function()

'''----------------------------------------------------------------'''

# Type and execute/run the program with the def function's call statement
# my_first_function() to see the actual output on the screen.

def my_first_function():
    print('My first function')

my_first_function()

'''----------------------------------------------------------------'''

# Now, let's expand our understanding of functions by adding more program
# statements to truly create some functionality in our def function program.
# Remember to 'call the function' to see the output on the screen with the statement
# 'my_second_function()'

def my_second_function():
    print('My second function.')
    print('add some more functionality.')
    print('Wow! This was so easy to create!')

my_second_function()

'''----------------------------------------------------------------'''

# Now, let's dive a little deeper into program functionality with a simple for-loop in our
# def statement block. Type and execute/run the program and see what happens.

def my_third_function():
    for i in range(3):
        print('My third function example.')

my_third_function()

'''----------------------------------------------------------------'''

# Now, let’s combine some strings with a for-loop inside our forth def function block
# program example. Type and execute/run the program and see what happens.

tuple_string=('Python','Programmer\'s','Glossary','Bible')

def my_forth_function():
    for i in tuple_string:
        print(i,end=' ')

my_forth_function()

'''----------------------------------------------------------------'''

# The (end=' ') emitter forces the print statement to keep printing on the same line.
# Below is the very same program example as above, but without the (end=' ') emitter.
# Type and execute/run the program and see what happens.

tuple_string=('Python','Programmer\'s','Glossary','Bible')

def my_forth_function():
    for i in tuple_string:
        print(i)

my_forth_function()

'''----------------------------------------------------------------'''

# Now, let's use some parameters in our def function statement program example.
# Type and execute/run the program below and see what happens.

def my_function(first_parameter,second_parameter,third_parameter):
    print(first_parameter,second_parameter,third_parameter)
  
my_function('first parameter','second parameter','third parameter')

# When using parameters inside def function statements, you must also take note that
# you must use the exact number of variables to how many values you use within the
# function's call statement. For example, if you use three parameter variables, you
# must also use exactly three values to satisfy all three parameter variables. If you
# exceed the number of variables, or exceed the number of parameter values within
# the function's call statement, you will get an index out of range error; thus crashing
# the prgram. It's imperative that, including simple strings or anything that takes
# variables and values must always be equal to be satisfied. As for the print statement,
# you can leave out arguments, and use them later on. Here is an example of what the
# very same program below does when you leave out some arguments within the print 
# statement; the program continues to run fine. However, if you try to add an
# argument that does not exist inside the def function's parameter variables, a crash
# will occur.

def my_function(first_parameter,second_parameter,third_parameter):
    print(first_parameter,second_parameter,third_parameter)
  
my_function('first parameter','second parameter','third parameter')

'''----------------------------------------------------------------'''

# Here is the very same program example, but with arguments that don't belong to the
# function's parameter variables at all. When you 'try' to run the program, a crash will
# occur. Type and execute/run the program below and see what happens, when you
# try to use non-existent arguments within the print statement.

def my_function(first_parameter,second_parameter,third_parameter):
    print(first_parametr,second_parameter,third_paramete)
  
my_function('first parameter','second parameter','third parameter')

'''----------------------------------------------------------------'''

# The program above has two arguments, which don't belong called 'first_parametr'
# and 'third_paramete'. The programmer didn't catch the error, because the 'e' and
# the 'r' were left out of the argument's variables, which was the root cause of the
# error. Variables and values must be literal, meaning they must be the same, unless
# they are modified, which the program example below shows. Type and execute/run
# the program below and see what happens.

def my_function(first_parameter,second_parameter,third_parameter):
    print('mod first_parametr',second_parameter,'mod third_paramete')
  
my_function('first parameter','second parameter','third parameter')

# Single (') or double (") quote marks can be used to modify the print statement's
# argument variables. However, if you use single quote marks, you have to use only
# single quote marks. If you use double quote marks, you must use only double quote
# marks. The quote marks always have to be the same regardless. Here is a simple
# print statement that uses the wrong quote marks. Type and execute/run the one line
# program example below and see how the program causes an error.

print("the program will crash, because the quotes are wrong')

# Here are the two correct ways to use single or double quote marks.

print('The program runs, because the quote marks are the same')

print("The program runs, because the quote marks are the same")
      
'''----------------------------------------------------------------'''

# Now, let's use the very same def function program example below and change some
# values in the function's call statement, so we can understand functions a little bit
# better. However, this topic on functions is quite lengthy; we have much to cover
# before we get into class functions, which is also quite the lengthy topic in itself.

# We already know that using one variable means using just one value. We also know
# that if we use two variables, we must also use two values to satisfy the two variables,
# i.e. For example:

#	variable_1='value 1'

#	variable_1,variable_2='value 1','value 2'

#	variable_1,variable_2,variable_3='value 1','value 2','value 3'

variable_1,variable_2,variable_3='value 1','value 2','value 3'

print(variable_1)

# The print statement contains the argument variable, variable_1, which its value is
# called 'value 1'. The argument variable passes the value, 'value 1' right into the print
# statement, 'variable_1'. You can use as many of the same argument variables you so
# desire. You can save argument variables for later use as well. You can also use and
# reuse argument variables over and over again, such in this program example below.
# Type and execute/run the program example below and see what happens.

variable_1,variable_2,variable_3='value 1','value 2','value 3'

print(variable_1,variable_1,variable_3,variable_2,variable_3)

# Take a look at the call statement 'my_function' and change the word 'value 1' to say
# the word "Python". Make sure you use single or double quote marks in each value.
# Double quote marks are used as an example for one value to show how quote marks
# behave. Type and execute/run the program below and see what happens.

def my_function(first_parameter,second_parameter,third_parameter):
    print(first_parameter,second_parameter,third_parameter)
  
my_function("Value 1",'Value 2','Value 3')

# Take a close look at the quote marks at "value2" in the function's call statement. You
# can use single or double quotes, but you cannot mix double quotes with single
# quotes on the same value. For example:

#	my_function("Python',"Value 2",'Value 3')

#	my_function('Python","Value 2",'Value 3") 

def my_function(first_parameter,second_parameter,third_parameter):
    print(first_parameter,second_parameter,third_parameter)
  
my_function("Python","Value 2",'Value 3')

# Note: always use commas to separate multiple variables, multiple values and
# multiple arguments, including strings, tuples, lists and dictionaries alike. Use the (\)
# inline emitter to wrap long statements of any sort.
      
'''----------------------------------------------------------------'''

# Now, let's add some more argument variables in our def function program example.
# Note: if you have three variables, and three values, you can only use three, named
# arguments. However, you can use and reuse arguments over and over again, and as
# many times as you like.

def my_function(first_parameter,second_parameter,third_parameter):
    print(first_parameter,second_parameter,third_parameter,first_parameter,
          third_parameter,first_parameter)
  
my_function("Python",'Value 2','Value 3')

# You can also save arguments for later use, such as the case with this very same
# program example below. Type and execute/run the program and see what happens.

def my_function(first_parameter,second_parameter,third_parameter):
    print('I don\'t want to use any arguments for now.')
  
my_function("Python",'Value 2','Value 3')
      
'''----------------------------------------------------------------'''

# Now it's time to ratchet things up a bit with more def functions. Are you ready?

# Take a close look at this def function's parameter variables. Just like before, but this
# time the values are inside the def function statement along with the def function's
# variables. Also take a close look at the def function's call statement; nothing needs
# to be inside the call statement 'my_function'. That's because the variables and the
# values are inside the def function statement's parameters themselves. Type and
# execute/run the program below and see what happens.

def my_function(var1='value1',var2='value2',var3='value3'):
    print(var1)
    print(var2)
    print(var3,var1,var3,var2)

my_function()

# Remeber you can use and reuse arguments over and over again.

# Def functions can return values via the 'return' statement. Type and execute/run the
# programs below and see what happens.

def get_value(name):
    return name

print(get_value('Python Programmer\'s Glossary Bible'))
      
'''----------------------------------------------------------------'''

# This program example below does the very same thing as the program example
# above illustrates. If name values are too long, they can be stored inside a variable
# instead. For example, the variable 'get_name' takes the place of this really long
# string value:

#	get_value('Python Programmer\'s Glossary Bible')

def get_value(name):
    return name

get_name=get_value('Python Programmer\'s Glossary Bible')

print(get_name)

def get_value(name,program):
    return name

get_name=get_value('Python','Programmer\'s Glossary Bible')

print(get_name)

def get_value(name,program):
    return program

get_name=get_value('Python','Programmer\'s Glossary Bible')

print(get_name)

# Use the index [ ] emitter to create nicer looking screen output.

def get_value(name,program,book):
    return name,program,book

get_name=get_value('Python','Programmer\'s','Glossary Bible')

print(get_name[0],get_name[1],get_name[2])

# Without the index [ ] emitter, the screen output looks sort of unfinished such as in
# this program example below illustrates.

def get_value(name,program,book):
    return name,program,book

get_name=get_value('Python','Programmer\'s','Glossary Bible')

print(get_name)

# Use the (f') format function to concatenate/add words with strings. Use curly braces
# { } in conjunction with the (f') format function. Type and execute/run the program
# example below and see what happens.

def  software(name,program,book):
    return f'I love my {name} {program} {book} very much!'

Python=software('Python','Programmer\'s','Glossary Bible')

print(Python)
      
'''----------------------------------------------------------------'''

# Def functions can return the result of a given number value. For example 'num's
# value is equal to '4', which is in the print statement. When multiplying 'num*num, the
# value '4' also gets multiplied ie: '4*4', which now equals '16'. So the result of the
# returning value is '16'. Type and execute/run each progarm example below and see
# what happens.

def multiply(num):
    return num*num

print(multiply(4))

# You can add versatility to functions with the 'return' statement. You can return 'num
# as much as you like. For example:

def multiply(num):
    return num*num+num

print(multiply(4))

# You can also combine ordinary integer numbers with values, such as this program
# example below illustrates. Just remember the golden rules of "BEDMAS" -2+5 = 3+2
# = 5-2 = '3'.

def multiply(num):
    return num*num+num+num-2+5

print(multiply(4))

# The 'return' statement returns the results of the value 'num'.

# The result of the returned value 'num' is: 4*4+4+4-2+5 = '27'

def multiply(num):
    return num*num+num+num-2+5

print(multiply(4+3))

# The result of the returned value 'num' is: 7*7+7+7-2+5 = '66'

# Let's create a return function that returns two values called 'num1 and 'num2'. The
# value of 'num1=4' and the value of 'num2=3'.

def multiply(num1,num2):
    return num1*num2

print(multiply(4,3))

# The result of the returned values of 'num1' and 'num2' is: 4*3 = '12'

# You can keep these two values as separate values, which return their separate
# results. for example:

#	4*3,3+4 = 12,7

# Use a comma (,) to separate values inside the 'return' statement.

#	return num1*num2,num1+num2

def multiply(num1,num2):
    return num1*num2,num1+num2

print(multiply(4,3))
      
'''----------------------------------------------------------------'''

# Type and execute/run the program example above and see what happens.

# Let's cube a number with a return function and see what happens when you type and
# execute/run the program example below.

def cube(num):
    return num**num

print(cube(3))

# Use a double asterisk (**) to cube numbers. The value 3 works like this:

#	3*3*3 = '27'

#	print(3*3*3)

# Return an integer number with the 'int' function.

def multiply(num1,num2):
    return int(num1*num2)

print(multiply(4,3.0))

# Return a floating-point number with the 'float' function.

def multiply(num1,num2):
    return float(num1*num2)

print(multiply(4,3))
      
'''----------------------------------------------------------------'''

# Let's create an outer function and an inner function, then call the outer function by
# assigning the variable 'get_function' to it. Type and execute/run the program
# example below and see what happens.

def outer_function():
    message='Python'
    def inner_function():
        print(f'{message} Programmer\'s Glossary Bible')
        
    return inner_function

get_function=outer_function()

get_function()
      
'''----------------------------------------------------------------'''

# Let's pass the variable 'message' into the outer function and return the value
# through the inner function. Next, let's call the outer and inner functions by assigning
# the variables 'get_function1' and 'get_function2' to them. Type and execute/run this
# program example below and see what happens.

def outer_function(message):
    message=message
    def inner_function():
        print(message)
        
    return inner_function

get_function1=outer_function('Get Function One.')
get_function2=outer_function('Get Function Two.')

get_function1()
get_function2()
      
'''----------------------------------------------------------------'''

# Let's pass the variable 'message' right into the inner function and then call the outer
# and inner functions by assigning the variables 'get_function1' and 'get_function2 to
# them. Type and execute/run the program example below and see what happens.

def outer_function(message):
    def inner_function():
        print(message)
        
    return inner_function

get_function1=outer_function('Get Function One.')
get_function2=outer_function('Get Function Two.')

get_function1()
get_function2()
      
'''----------------------------------------------------------------'''

# Python or any other object oriented programming languages, such as 'C' has no
# 'goto', 'gosub' or any 'jump to subroutine' commands at all. To get around this
# problem, Python uses 'def functions' to create subroutines. Type and execute/run
# the program example below and see what happens.

def subroutine_1():
    print('This is subroutine 1')
    
def subroutine_2():
    print('This is subroutine 2')
    
def subroutine_3():
    print('This is subroutine 3')
    
while True:
    
    get_subroutine=input("Press '1', '2' or '3' to get the subroutine \
you want to display: ").lower().strip()

    while True:
        
        if get_subroutine=='1':
            subroutine_1()
            break
        
        elif get_subroutine=='2':
            subroutine_2()
            break
        
        elif get_subroutine=='3':
            subroutine_3()
            break
        
        else:
             print('Sorry! No subroutine exist for',
                   get_subroutine)
             break
            
    display_again=input("Would you like to display anymore subroutines? \
Type 'Yes' or 'No' to confirm. ").lower().strip()
    
    if display_again=='yes':
        continue
    
    elif display_again=='no':
        break
    
    else:
        print('Sorry! I don\'t understand that.')
