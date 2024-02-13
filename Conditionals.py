'''Conditionals and Logical Operators: (<) (>) (<=) (>=) (==) (!=)'''
'''
Conditionals change the outcome of a program's execution run, depending
on what the program is doing at the time. The conditionals in Python are the
'if:' statement, 'elif:' statement and the 'else:' statement, along with the 'True:'
and 'False:' statements. Conditionals are mainly used in conjunction with 'input'
statements and conditional while-loops. However, Logical operators are also used
to test whether a condition is less than (<), greater than (>), less than (<=) or equal
to, greater than (>=) or equal to, equals (==) equals and not (!=) equal to. For example, 5
is greater (>) than 4 and 4 is less (<) than 5. Here are a few examples of logical operators,
which test integer values against other integer values within 'print' statements.
These 'print' statement illustration examples below will either display on the screen
output as "True" or "False", depending on the outcome of the results.

print(4<5) True: 4 is less than 5
print(4>5) False: 4 is not greater than 5
print(4<=5) True: 4 is less than or equal to 5
print(4>=5) False: 4 is not greater than or equal to 5
print(4==5) False: 4 does not equal 5
print(4!=5) True: 4 does not equal 5
'''
# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

print(4<5)

# Screen output: True
'''-----------------------------------------------------------------------------'''
# Type and execute/run these 'print' statement program examples, using the (f')
# format implementer.

# The 'int' statement is for integer values only.

num=int(input('Type in a number and I will condition the result against 5 as either \
"true" or false" ').strip())

print(f'{num<5}')
print(f'{num>5}')
print(f'{num<=5}')
print(f'{num>=5}')
print(f'{num==5}')
print(f'{num!=5}')

'''Boolean Logic:'''
"IF" "ELIF" "ELSE" "TRUE" "FALSE" "AND" "OR" "NOT"
'''
There once was a man, named 'George Boole' who was a famous mathematician. He invented
these conditionals called Boolean Logic, which indirectly brought about the computer age we
now live. The conditionals of George Boole are as follows.

These conditionals are: 'IF', 'ELSE', 'TRUE', 'FALSE', 'AND', 'OR' 'NOT'

In computer terminology, these conditionals are called "Boolean Logic". Boolean Logic is simply
all about the concept of decision making laws, meaning if something is true, then it is not false.
Likewise, if something is false, then it is not true.

When it comes to program development, sometimes logical operators aren't enough alone to do
the job. In most cases, other conditionals are needed to help the logical operators do the job. With
the 'if:', 'elif:', 'else', 'true', 'false', 'and', 'or' and 'not' conditionals, the logical operators can do the
job as they were designed for doing, which are to test values against other values and comparing
data against user input data.
'''
'''-----------------------------------------------------------------------------'''
# Using simple 'print' statements, you can do simple True and False tests to help you
# determine the outcome of a conditional against another conditional, such as True
# and False conditionals. For example:

print(True and True)
print(False and False)
print(True and False)
print(False and True)

print(True or True)
print(False or False)
print(True or False)
print(False or True)

print(True and not True)
print(False and not False)
print(True and not False)
print(False and not True)

print(True or not True)
print(False or not False)
print(True or not False)
print(False or not True)

print(True is not True)
print(False is not False) 
print(True is not False)
print(False is not True)
'''-----------------------------------------------------------------------------'''
# Use operators to check to see if a value is True or False.

print(True == True)
print(False == False)
print(True != False) 
print(False != True)
print(True >= False)
print(True <= False)

# Here is a prime example of how these conditionals work in conjunction with the
# logical operators. In this program example, the conditionals 'if:' and 'elif:' are
# implement along with the logical operators. The user is asked to type in a number, if
# the number is equal equals: == 5, the first conditional 'if:' statement is executed
# "print(f'True! {num} equals equals 5.')". If the number is less than 5, the first 'elif:'
# statement is executed "print(f'True! {num} is less than 5.')". If the number is greater
# than 5, the second 'elif:' statement is executed "print(f'False! {num} is not greater
# than 5.')". If the number is less than or equal to 5, the third 'elif:' statement is
# executed "print(f'True! {num} is less than or equal to 5.')". If the number is greater
# than or equal to 5, the last 'elif:' statement is executed "print(f'False! {num} is is not
# greater than or equal to 5.')".

# Note: Python executes/runs programs starting from the top, downward. Be very
# careful on how you place statements. Some statements cannot execute right, even if
# they work. This is simply because of the order that Python executes/runs its
# program statements in the background.

# Type and execute/run this program example below and see what happens.

# The 'int' statement is for integer values only.

num=int(input('Type in a number and I will condition the result against 5 as either \
"true" or false" ').strip())

if num==5:
    print(f'True! {num} equals equals 5.')
    
elif num<5:
    print(f'True! {num} is less than 5.')
    
elif num>5:
    print(f'False! {num} is not greater than 5.')
    
elif num<=5:
    print(f'True! {num} is less than or equal to 5.')
    
elif num>=5:
    print(f'False! {num} is is not greater than or equal to 5.')
'''-----------------------------------------------------------------------------'''
# In this program example, the conditional 'else:' statement is executed only when the
# value 5 equals itself. Type and execute/run the program below and see what
# happens.

# The 'int' statement is for integer values only.

integer=int(input("Please enter an integer less than 5 or greater than 5: ").strip())

if integer<5:
    print(f'{integer} is less then 5')
    
elif integer>5:
    print(f'{integer} is greater than 5')
    
else:
    if integer==5:
        print(f'True! {integer} equals equals 5.')
'''-----------------------------------------------------------------------------'''
# Type and execute/run this program example and change the value 'num=5' to
# different values, such as 'num=9', 'num=-7'.....

num=6

if num<5:
    print(f'{num} is less than 5')
    
elif num>5:
    print(f'{num} is greater than 5')
    
else:
    if num==5:
        print(f'{num} equals equals 5.')

# In this program example, the conditional 'else:' statement is executed only when the
# value 5 equals itself. Type and execute/run the program below and see what
# happens.

# The 'int' statement is for integer values only.

integer=int(input("Please enter an integer less than 5 or greater than 5: ").strip())

if integer<5:
    print(f'{integer} is less then 5')
    
elif integer>5:
    print(f'{integer} is greater than 5')
    
else:
    if integer==5:
        print(f'True! {integer} equals equals 5.')
