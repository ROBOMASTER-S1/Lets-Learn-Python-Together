'''
Written and created by Joseph C. Richardson, GithHub.com

I know, I've covered this topic before, but I really want to hit it home, so you can
fully understand how to use '*args' and '**kwargs' like a true Python Pro and why
they can become quite the handy tools to know about and how to use the tools.

Let's learn what '*args' are all about. The word '*args' simply means the word
'arguments' for short. One asterisk * is used for '*args'. Use '*args' when you
don't know how many argument variables you want within your define function
parameters. Note: you do not need to call the word '*args' as args. However,
you will need to invoke the asterisk * to make '*args' work. Programmers
know the word as '*args' by standard definition, but you can use your own words.
'''
# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

def book(*args): # one argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book('unknown number of argument values.','add another unknown argument value.') # two argument values

# Create your own '*args' function parameter variable as shown below.

def book(*my_unknown_num_arguments): # one argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book('unknown number of argument values.','add another unknown argument value.') # two argument values
'''
As shown in the other define function() examples above, how we needed the exact
number of argument values to the exact number of argument variables. However,
with '*args' you no longer have to worry about how many argument values you will
need to satisfy the number of argument variables within the define function parameters.
'''
# Let's do some more '*args' with return functions

def book(*args): # one argumant variable
    return 'Python Programmer\'s Glossary Bible'

print(book('by Joseph C. Richardson','add another unknown argument value.')) # two argument values

def nums(*args): # one argument variable
    return args

print(nums(2,3)) # two argument values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Let's learn what '**kwargs' are all about. The word '**kwargs' simply means the words
'keyword arguments' for short. Two asterisks ** are used for '**kwargs'. Use '**kwargs'
when you don't know how many keyword argument variables you want within your
define function parameters. Note: you do not need to call the word '**kwargs' as '**kwargs'.
However, you will need to invoke two asterisks ** to make '**kwargs' work. Programmers
know the word as '**kwargs' by standard definition, but you can use your own words.
'''
def book(**kwargs): # one keyword argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book(keyword='keyword',argument='argument') # two keyword argument values

# This example is without any '**kwargs' at all; we have to name our keyword arguments.

def book(keyword_arg1,keyword_arg2): # two keyword argument variables
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book(keyword_arg1='keyword',keyword_arg2='argument') # two keyword argument values
'''
As shown in the define function() example above, how we needed the exact number of keyword
argument values to the exact number of keyword argument variables. However, with '**kwargs'
you no longer have to worry about how many keyword argument values you will need to satisfy
the number of keyword argument variables within the define function parameters.
'''
# Can you see the difference between '*args' and '**kwargs'? Yes, because the 'args' Python
# program example has the print() function right inside the def function(), whereas the
# '**kwargs' has the very same print() function inside the def function(). However, if you
# notice how the book(keyword value has equal = signs in the keyword variables, whereas
# the '*args' def function() doesn't use any equal = signs at all. This way, you can clearly see
# the difference between the two def functions(), '*args' and '**kwargs'

# book(keyword='keyword',argument='argument') # two keyword argument values

def book(*args): # one argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book('unknown number of argument values.','add another unknown argument value.') # two argument values

def book(**kwargs): # one keyword argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book(keyword='keyword',argument='argument') # two keyword argument values
'''
Let's make this even simpler, so we can truly understand and grasp this '*args' and
'**kwargs' concepts.

No matter how many arguments you use, the count just doesn't matter when using
'*args' and '**kwargs'. And that's when these are great tools to have, once you learn them.
Mind you, it even took me some time to learn all about how to fully understand and use
these tools myself. Here is a simple form of these two types of tools. Take a really close
look at these '*args' and '**kwargs' examples, they are broken up with ',' between all the worded
text. They don't mind having missing arguments. The best part is, let's say you have a 
def function() with far too many parameters variables to keep track of. That's where '*args'
and '**kwargs' really shines bright. Because without these wonderful Python tools, we would
have to make sure we have all the counted arguments to satisfy all the variables in the
def function's parameter range. Believe me, that can be a real headache to keep track of.
'''
def book(*args): # one argument variable
    print('Python','Programmer\'s','Glossary Bible\n','by Joseph C. Richardson')
    
book('unknown number of argument values.','add another unknown argument value.')

def book(**kwargs): # one keyword argument variable
    print('Python','Programmer\'s','Glossary Bible\n','by Joseph C. Richardson')

book(keyword='keyword') # one keyword argument value

# Let's do a def function() far too many parameter values and you will see just what I mean.
# We won't use any '*args' at all. Not at all.

def book(arg_1,arg_2): # two parameter argument variables
    print('See how we have to make sure we have the exact number of parameter variables?')

book('argument_1','argument_2')

# Try to execute/run this Python program example below and see what doesn't happen.

def book(arg_1): # one parameter argument variable
    print('See how we have to make sure we have the exact number of parameter variables?')

book('argument_1','argument_2')

# This is what happens instead. You will get a parameter and argument error message.

# Traceback (most recent call last):
#  File "C:\Users\mogie54321\Desktop\EXP Python.py", line 11, in <module>
#    book('argument_1','argument_2')
# TypeError: book() takes 1 positional argument but 2 were given

# Now, let's do the headache set of argument parameters and see just how dreadful that is.
# to keep track of without the use of '*args'

def book(arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,
         arg_9,arg_10,arg_11,arg_12,arg_13,arg_14,arg_15,arg_16,
         arg_17,arg_18,arg_19,arg_20):

    print("Wow! That's a lot of parameter argument variables. Now, I have a HEADACHE!")

book('argument_1','argument_2','argument_3','argument_4','argument_5',
     'argument_6','argument_7','argument_8','argument_9','argument_10',
     'argument_11','argument_12','argument_13','argument_14','argument_15',
     'argument_16','argument_17','argument_18','argument_19','argument_20')
'''
Now! Aren't you glad that '*args' exist? I sure am!! Here is our very same example below,
using the '*args' for our savior to avoid headaches.
'''
def book(*args):

    print("Wow! '*args' are so GREAT!")

book('argument_1','argument_2')

# The '*args' does not have to have a satisfied number of parameter arguments. Whereas
# without the '*args', we would be in deep doo doo if we had to keep track of a large parameters
# full of argument variables. OUCH! That hurts my head just to think about it. Now, just
# imagine what the world would be like without '**kwargs'? Imagine having to do countless
# keyword arguments and having to keep track of them all to make sure they're satisfied
# with the def functions() argument parameters. That would be a HUGE Headache.

# So now you know how to use these two, very important Python tools '*args' and '**kwargs'
# and what they are all about. I hope this helped.
