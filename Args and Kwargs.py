'''
Let's learn what *args are all about. The word 'args' simply means the word
'arguments' for short. One asterisk * is used for *args. Use *args when you
don't know how many argument variables you want within your define function
parameters. Note: you do not need to call the word '*args' as args. However,
you will need to invoke the asterisk * to make *args work. Programmers
know the word as *args by standard definition, but you can use your own words.
'''
# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

def book(*args): # one argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book('unknown number of argument values.','add another unknown argument value.') # two argument values

# Create your own *args function parameter variable as shown below.

def book(*my_unknown_num_arguments): # one argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book('unknown number of argument values.','add another unknown argument value.') # two argument values
'''
As shown in the other define function() examples above, how we needed the exact
number of argument values to the exact number of argument variables. However,
with *args you no longer have to worry about how many argument values you will
need to satisfy the number of argument variables within the define function parameters.
'''
# Let's do some more *args with return functions

def book(*args): # one argumant variable
    return 'Python Programmer\'s Glossary Bible'

print(book('by Joseph C. Richardson','add another unknown argument value.')) # two argument values

def nums(*args): # one argument variable
    return args

print(nums(2,3)) # two argument values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Let's learn what **kwargs are all about. The word 'kwargs' simply means the words
'keyword arguments' for short. Two asterisks ** are used for **kwargs. Use **kwargs
when you don't know how many keyword argument variables you want within your
define function parameters. Note: you do not need to call the word '**kwargs' as kwargs.
However, you will need to invoke two asterisks ** to make **kwargs work. Programmers
know the word as **kwargs by standard definition, but you can use your own words.
'''
def book(**kwargs): # one keyword argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book(keyword='keyword',argument='argument') # two keyword argument values

# This example is without any **kwargs at all; we have to name our keyword arguments.

def book(keyword_arg1,keyword_arg2): # two keyword argument variables
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book(keyword_arg1='keyword',keyword_arg2='argument') # two keyword argument values
'''
As shown in the define function() example above, how we needed the exact number of keyword
argument values to the exact number of keyword argument variables. However, with **kwargs
you no longer have to worry about how many keyword argument values you will need to satisfy
the number of keyword argument variables within the define function parameters.
'''
# Let's create some define functions that act like subroutines.
'''
Since there are no line numbers in Python, also means that we cannot create any such 'go to',
or 'go sub' commands at all with Python. So how can we create subroutines with Python?. How
can we create subroutines without making them jump to line numbers, like we did in the old days?
Well the answer is quite simple. Let's use define functions() with a while loop to create our subroutine
examples.
'''
def subroutine1():
    print('You picked subroutine1')

def subroutine2():
    print('You picked subroutine2')

def subroutine3():
    print('You picked subroutine3')

while True:
    message=input('Please type 1, 2 or 3 to select the subroutine you wish to \
display or type (q) to quit: ').strip()
    
    if message=='q':
        break
    while True:        
        if message=='1':
            subroutine1()
            break
        elif message=='2':
            subroutine2()
            break
        elif message=='3':
            subroutine3()
            break
        else:
            print('Sorry! No subroutine for that.')
            break
