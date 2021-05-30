# Play around with these George Boole Logic
# Python program examples to gain a much
# broader perspective of what logic truly means
# in computer programming. With Boolean Logic
# a computer can make decisions according to
# data input, via user input data. However, logical
# operators such as '==', '!=', '>', '<', '>=', '<=' work
# in conjunction with for-loops and while-loops.
# With the help of the 'if', 'elif' and 'else' statements
# this can be achieved with ease.

print(True and False)
print(False and True)
print(True and True)
print(False and False)

print(True and not False)
print(False and not True)
print(True and not True)
print(False and not False)

print(True or False)
print(False or True)
print(True or True)
print(False or False)

print(True or not False)
print(False or not True)
print(True or not True)
print(False or not False)

print(True is False)
print(False is True)
print(True is True)
print(False is False)

print(True is not False)
print(False is not True)
print(True is not True)
print(False is not False)

print(bool(1 and 0))
print(bool(0 and 1))
print(bool(1 and 1))
print(bool(0 and 0))

print(bool(1 and not 0))
print(bool(0 and not 1))
print(bool(1 and not 1))
print(bool(0 and not 0))

print(bool(1 or 0))
print(bool(0 or 1))
print(bool(1 or 1))
print(bool(0 or 0))

print(bool(1 or not 0))
print(bool(0 or not 1))
print(bool(1 or not 1))
print(bool(0 or not 0))

print(bool(1==1))
print(bool(1!=1))

print(bool(1>1))
print(bool(1<1))
print(bool(1>=1))
print(bool(1<=1))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the logical 'is', 'and', 'or' and 'not'
# operators. Let's also create two, packed
# variables 'a' and 'b' then set them to 'True'
# and 'False' values. The logical operators
# 'is' and 'not' simply mean equals '==' and
# not equals '!='.

a,b=True,False

print(a is b) # False
print(b is a) # False

print(a and b) # False
print(b and a) # False

print(a or b) # True
print(b or a) # True
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print(a is not b) # True
print(b is not a) # True

print(a and not b) # True
print(b and not a) # False

print(a or not b) # True
print(b or not a) # False
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the 'in' operator to check if a value is in
# variable 'a'. Use the 'in' operator in conjunction
# with the 'not' operator to tell if a value is not in
# the variable 'a'.

a=1,2,3,4,5,6,7,8,9,10

print(1 in a) # True
print(10 in a) # True
print(11 in a) # False

print(1 not in a) # False
print(10 not in a) # False
print(11 not in a) # True
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The 'all()' and 'any()' functions examples:

# Displays Boolean logic 'True' and 'False'
# values only.

num=0,1

x=all(num)
print(x) # False

x=any(num)
print(x) # True
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type and execute/run each of these program
# examples below to see how the logical operators
# work in conjunction with for-loops.

for i in range(1,11):
    if i==5:
        print(i,'is equal == to 5')
    elif i==8:
        print(i,'is equal == to 8')
    else:
        print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(1,11):
    if i!=5:
        print(i,'is not equal != to 5')
    elif i!=8:
        print(i,'is not equal != to 8')
    else:
        print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(1,11):
    if i<5:
        print(i,'is less < than 5')
    elif i>8:
        print(i,'is greater > than 8')
    else:
        print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(1,11):
    if i<=5:
        print(i,'is less < than or equal = to 5')
    elif i>=8:
        print(i,'is greater > than or equal = to 8')
    else:
        print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(1,5):
    if i==2 and 3:
        print(i)
    else:
        print(i,'skip!')

for i in range(1,5):
    if i==2 and 3:
        print(bool(i))
    else:
        print(i,'skip!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(1,5):
    if i==2 or 3:
        print(i)
    else:
        print(i,'skip!')

for i in range(1,5):
    if i==2 or 3:
        print(bool(i))
    else:
        print(i,'skip!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type and execute/run each of these program
# examples below to see how the logical operators
# work in conjunction with while-loops.

i=1
while i<11:
    if i==5:
        print(i,'is equal == to 5')
    elif i==8:
        print(i,'is equal == to 8')
    else:
        print(i)
    i+=1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
i=1
while i<11:
    if i!=5:
        print(i,'is not equal != to 5')
    elif i!=8:
        print(i,'is not equal != to 8')
    else:
        print(i)
    i+=1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
i=1
while i<11:
    if i<5:
        print(i,'is less < than 5')
    elif i>8:
        print(i,'is greater > than 8')
    else:
        print(i)
    i+=1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
i=1
while i<11:
    if i<=5:
        print(i,'is less < than or equal = to 5')
    elif i>=8:
        print(i,'is greater > than or equal = to 8')
    else:
        print(i)
    i+=1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now combine all the logical operators
# within a for-loop, along with more 'elif' statements.

for i in range(1,21):
    if i==5:
        print(i,'is equal == to 5')
    elif i!=8:
        print(i,'is not equal != to 8')
    elif i>11:
        print(i,'is greater > than 11')
    elif i<14:
        print(i,'is less < than 14')
    elif i>=17:
        print(i,'is greater > than or equal = to 17')        
    elif i<=20:
        print(i,'is less < than or equal = to 20')        
    else:
        pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now combine all the logical operators
# within a while-loop, along with more 'elif'
# statements.

i=1
while i<21:
    if i==5:
        print(i,'is equal == to 5')
    elif i!=8:
        print(i,'is not equal != to 8')
    elif i>11:
        print(i,'is greater > than 11')
    elif i<14:
        print(i,'is less < than 14')
    elif i>=17:
        print(i,'is greater > than or equal = to 17')        
    elif i<=20:
        print(i,'is less < than or equal = to 20')        
    else:
        pass
    i+=1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type and execute/run this program example
# and see how the while-loop only breaks when
# one of the two 'break' statements is executed.
# If none of them gets executed, the while-loop
# keeps on iterating. This program example is
# another great example of how the conditional
# 'if:' and 'elif:' statements work in conjunction
# with the logical operators.

while True:
    try:
        asterisks=int(input(f'How many asterisks would you like? ').strip())
        if asterisks>1:
            print(f'\n{asterisks} asterisks: [',' * '*asterisks,f']\n\nI gave you \
{asterisks} asterisks!\n\nI hope you enjoy your {asterisks} asterisks...')
            break
        
        elif asterisks==1:
            print(f'\n{asterisks} asterisk: [','*'*asterisks,f']\n\nI gave you \
{asterisks} asterisk!\n\nI hope you enjoy your \'One\' \
and \'Only\', single asterisk...')
            break
        
        elif asterisks==0:
            print('\nSorry Hero! Zero doesn\'t count.\n')        
    except ValueError:
        print('\nNumbers only please!\n')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This conditional while-loop example compares
# a random number against user input data. If
# the user picks the right number by luck alone,
# the while-loop will break out and the program
# ends. If the user picks the wrong number, the
# less (<) than or greater (>) than 'random_num'
# variable gets conditioned and the while-loop
# keeps on iterating until the right number is
# picked, via user input data.

# Note: Python executes/runs programs starting
# from the top, downward. Be very careful on how
# you place statements. Some statements cannot
# execute right, even if they work. This is simply
# because of the order that Python executes/runs
# its program statements.

# Note: The 'import random' module must be imported
# first.

import random

random_num=random.randint(1,10)

while True:
    try:
        pick_num=int(input('\nWhat number am I thinking \
of? Hint! It\'s between 1 and 10: ').strip())
        
        if pick_num<random_num:
            print('\nThe number I\'m thinking of is too low!')
            
        elif pick_num>random_num:
            print('\nThe number I\'m thinking of is too high!')
            
        elif pick_num==random_num:
            print(f'\nCongratulations! You won. "{random_num}" \
was the number I was thinking of.')
            break
        
    except ValueError:
        print('\nYou must type integers only please!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This very same program example as above
# works exactly the same way, but with one
# major difference; the while loop will only iterate
# three times. If the user picks the right number,
# the while loop breaks. If the user doesn't pick
# the right number after three times, the 'else'
# statement executes and says 'Sorry! You lost.',
# which ends the program.

# Note: the 'import random' module must be imported
# first.

import random

random_num=random.randint(1,10)

i=0

while i<3:
    try:
        pick_num=int(input('\nWhat number am I thinking of? \
Hint! It\'s between 1 and 10: ').strip())
        
        i+=1
        
        if pick_num<random_num:
            print('\nThe number I\'m thinking of is too low!')
            
        elif pick_num>random_num:
            print('\nThe number I\'m thinking of is too high!')
            
        elif pick_num==random_num:
            print(f'\nCongratulations. You won! "{random_num}" \
was the number I was thinking of.')            
            break
        
    except ValueError:
        print('\nYou must type integers only please!')
        
else:
    print('\nSorry. You lost!')    
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Once again, this is the very same program
# example as above before. However, this time
# the loop iterates in reverse instead of forward
# and the user is shown how many guesses they
# have left before they win or lose.

# Note: the 'import random' module must be
# imported first.

import random

random_num=random.randint(1,10)

i=3

while i>0:
    try:
        pick_num=int(input(f'\nWhat number am I thinking of? \
Hint! It\'s between 1 and 10:\n\nYou have {i} gesses left. ').strip())
        
        i-=1
        
        if pick_num<random_num:
            print('\nThe number I\'m thinking of is too low!')
            
        elif pick_num>random_num:
            print('\nThe number I\'m thinking of is too high!')
            
        elif pick_num==random_num:
            print(f'\nCongratulations. You won! "{random_num}" \
was the number I was thinking of.')
            break
        
    except ValueError:
        print('\nYou must type integers only please!')
        
else:
    print('\nSorry. You lost!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type and execute/run The George Boole Game
# program example to get a better understanding
# of how Boolean Logic works and why it works.
# Type different "True" and "False" combinations
# and see what Gearoge Boole does. Press 'Q' to
# quit playing.

print('\nThe George Boole Game\n')

print('George loves to play "True" or "False",\nbut \
he needs your help to play it.')

print('\nPress "Q" to quit!')

while True:
    Boole1=input('\nType "true" or "false" for the first value. ').strip()
    if Boole1=='q':
        print('Thanks for playing!')
        break
    
    print(f'\nYou chose "{Boole1.title()}" for your first value.\n')
    Boole2=input('\nType "True" or "False" for the second value. ').strip()
    
    if Boole2=='q':
        print('Thanks for playing!')
        break
    
    print(f'You chose "{Boole2.title()}" for your second value.\n')
    
    if Boole1=='true' and  Boole2=='true':
        print(f' "AND" is true because Boole1 is "{Boole1.title()}" \
and Bool2 is "{Boole2.title()}".\n')
        
    elif Boole1=='false' and Boole2=='false':
        print(f' "AND" is true because Boole1 is "{Boole1.title()}" and \
Boole2 is "{Boole2.title()}".\n')
        
    elif Boole1=='true' or Boole2=='true':
        print(f' "OR" is true because Boole1 is "{Boole1.title()}" and \
Boole2 is "{Boole2.title()}".\n')
        
    elif Boole1=='false' or Boole2=='false':
        print(f' "OR" is true because Boole1 is "{Boole1.title()}" and \
Boole2 is "{Boole2.title()}".\n')
        
    else:
        print('Type the right vales please!')
