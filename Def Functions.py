# Define Functions() Python program examples.

# Created by Joseph C. Richardson, GitHub.com

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE
'''
Most Python programs consist of functions. Functions in Python allow programmers to
add functionality in their programs that might be needed again and again throughout
the program's execution run. With functions, programmers can call/execute functions
from another file as part of the main program’s execution run from the main file. Note:
calling files from other files must be stored within the same directory path or folder; via
Windows for example. Functions can also return values, which can be changed or modified
throughout the program’s execution run. Just remember that functions simply add
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
# the program. It's imperative that, including simple strings or anything that takes
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
