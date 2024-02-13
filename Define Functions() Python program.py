# Define Functions() Python program example.

# Created by Joseph C. Richardson, GitHub.com

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

# I use def functions() most of the time. These are used for either
# calling code through them, or they can be used as simple subroutines.
# You can also use them within lists, which is what these Python
# program examples shows. You can create a list[] of function
# calls, a tuple() a dictionary{} and a set{}. Note: sets{} do not use
# indexing like tuples and lists do. Sets{} only get rid of duplicate
# values, whereas lists[], tuples and dictionaries don't. We learn
# all of the above with these Python program def functions() examples.

# Let's create three def functions() called 'function_one', 'function_two'
# and 'function_three'.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

# Let's call each def function, one by one so we can see what's going on.
# To call a function, you have to call it like this:

function_one()     # do not use the colon : to call functions

function_two()     # do not use the colon : to call functions

function_three()  # do not use the colon : to call functions
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's try placing these same functions inside a tuple().
# Remember that tuples and lists always start at index[0].

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_tuple = (function_one,function_two,function_three)

my_functions_tuple[0]()  # index[0] is function_one

my_functions_tuple[1]()  # index[1] is function_two

my_functions_tuple[2]()  # index[2] is function_three

# When calling up a function through a tuple(), do not include the () parentheses
# right after the function call. The () parentheses go at the very end of the index[]()
# box: my_functions_tuple[0](). Now, let's move onto using def functions() within
# a list[], which is similar to a tuple(). But tuples() are not mutable, whereas lists[]
# are mutable, meaning they can be changed or modified; tuples cannot be
# changed or modified at all, meaning they are not mutable.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's try placing these same functions inside a list[].
# Remember that tuples and lists always start at index[0].

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_list = [function_one,function_two,function_three]

my_functions_list[0]()  # index[0] is function_one

my_functions_list[1]()  # index[1] is function_two

my_functions_list[2]()  # index[2] is function_three

# When calling up a function through a list[], do not include the () parentheses
# right after the function call. The () parentheses go at the very end of the index[]()
# box: my_functions_list[0](). Now, let's move onto using def functions() within
# a dictionary{} of values.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's try placing these same functions inside a dictionary{}.
# The dictionary 'keys' will be numbers or text if you like. But we are going to
# use numbers for the 'key's and make the values be the names of the functions
# we are using so the 'keys' will '.get' each of the values we call up, within our
# dictionary{}.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_dictionary = {1:function_one,2:function_two,3:function_three}

my_functions_dictionary.get(1)()  # "I'm Function One."

my_functions_dictionary.get(2)()  # "I'm Function Two."

my_functions_dictionary.get(3)()  # "I'm Function Three"

# When calling up a function through a dictionary{}, do not include the () parentheses
# right after the function call. The () parentheses go at the very end of the .get(n)(),
# my_functions_dictionary.get(1)(). Now, let's move onto using def functions() within
# a set of values. Note: sets{} get rid of duplicate values. They will also be in random
# order when using text values, instead of number values. Set{} do not produce
# output directly onto the screen at execute/run time. Instead you have to cast the
# values to a built-in tuple(), a built-in list() or a built-in dict() function.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's try placing these same functions inside a set{} in which we have to
# cast into a tuple() function, a list() function or a dict() function. We are only
# going to cast the set into a tuple() and a list() function for now.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_set = {function_one,function_two,function_three}

my_cast = tuple(my_functions_set)

my_cast[0]()

my_cast[1]()

my_cast[2]()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
my_functions_set = {function_one,function_two,function_three}

my_cast = list(my_functions_set)

my_cast[0]()

my_cast[1]()

my_cast[2]()

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
