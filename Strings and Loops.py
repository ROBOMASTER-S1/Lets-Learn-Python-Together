# Let's have some deep, deep Python programming
# fun and learn how to concatenate strings, create
# sets, complex for-loops and while-loops. See what
# happens when you type and execute/run each
# Python program example below.

string_concatenation,prt=(
    'my','pyt'+'hon','prog'+"ammer's",
    'glos'+'sary','bib'+'le'+' is','gre'+'ate!'),print

for i in string_concatenation:
    prt(i.capitalize())

for i in string_concatenation:
    prt(i.capitalize(),end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
string_concatenation,prt=(
    'my','pyt'+'hon','prog'+"ammer's",
    'glos'+'sary','bib'+'le'+' is','gre'+'ate!')[::-1],print

for i in string_concatenation:
    prt(i.capitalize())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
string_concatenation,prt=(
    'my','pyt'+'hon','prog'+"ammer's",
    'glos'+'sary','bib'+'le'+' is','gre'+'ate!'),print

for i in string_concatenation:
    prt(i[::-1].capitalize(),end=' ')

for i in string_concatenation:
    prt(f'{i[::-1].capitalize()}',end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
string_concatenation,prt,length=(
    'my','pyt'+'hon','prog'+"ammer's",
    'glos'+'sary','bib'+'le'+' is','gre'+'ate!'),print,len

prt(f'The string_concatenation tuple is \
{length(string_concatenation)} values long, \
including the "+" signs.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
set1,set2=({'Tom','John','Rob','Bob'},
           {'Dog','Cat','Bird','Fish'})

# this:
set1_set2=set1.union(set2) # 'union'

# or this:
set1_set2=set1 | (set2) # '|' short for 'union'

convert=list(set1_set2)
convert.sort()

print(f"{convert[1]}, {convert[5]} and {convert[7]} \
love {convert[6]}'s {convert[4]} tank.")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
set1,set2=({'Tom','John','Rob','Bob','intersect like values only'},
           {'Dog','Cat','Bird','Fish','intersect like values only'})

# this:       
print(set1.intersection(set2)) # 'intersection'

# or this:
print(set1 & set2) # '&' short for 'intersection'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
set1,set2=({'Tom','John','Rob','Bob'},
           {'Tom','John','Rob','Cat','Fish'})

# this:
print(set1.difference(set2)) # 'difference'

# or this:
print(set1 - set2) # '-' short for 'difference'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
set1,set2=({'Tom','John','Rob','Bob'},
           {'Tom','John','Rob','Cat','Fish'})

# this:
print(set1.symmetric_difference(set2)) # 'symmetric_difference'

# or this:
print(set1 ^ (set2)) # '^' short for 'symmetric_difference'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try these fun for-loop Python program examples:

for i in range(1,21,1):
    print('* '*i,i)

for i in range(20,0,-1):
    print('* '*i,i)

for i in range(1,21,1):
    if i==1:
        print('* '*i,i,'asterisk')
    elif i>1:
        print('* '*i,i,'asterisks')

for i in range(20,0,-1):
    if i==1:
        print('* '*i,i,'asterisk')
    elif i<21:
        print('* '*i,i,'asterisks')
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
        pick_num=int(input('\nWhat number am I thinking of? Hint! It\'s \
between 1 and 10: ').strip())
        
        if pick_num<random_num:
            print('\nThe number I\'m thinking of is too low!')
            
        elif pick_num>random_num:
            print('\nThe number I\'m thinking of is too high!')
            
        elif pick_num==random_num:
            print(f'\nCongratulations! You won. "{random_num}" was the \
number I was thinking of.')
            break
        
    except ValueError:
        print('\nYou must type integers only please!')

# This very same program example as above works
# exactly the same way, but with one major difference;
# the while loop will only iterate three times. If the user
# picks the right number, the while loop breaks. If the
# user doesn't pick the right number after three times,
# the 'else' statement executes and says 'Sorry! You
# lost.', which ends the program.

# Note: the 'import random' module must be imported
# first.

import random

random_num=random.randint(1,10)

i=0

while i<3:
    try:
        pick_num=int(input('\nWhat number am I thinking of? Hint! It\'s \
between 1 and 10: ').strip())
        
        i+=1
        
        if pick_num<random_num:
            print('\nThe number I\'m thinking of is too low!')
            
        elif pick_num>random_num:
            print('\nThe number I\'m thinking of is too high!')
            
        elif pick_num==random_num:
            print(f'\nCongratulations. You won! "{random_num}" was the number \
I was thinking of.')            
            break
        
    except ValueError:
        print('\nYou must type integers only please!')
        
else:
    print('\nSorry. You lost!')

# Once again, this is the very same program example
# as above before. However, this time the loop iterates
# in reverse instead of forward and the user is shown
# how many guesses they have left before they win or
# lose.

# Note: the 'import random' module must be imported
# first.

import random

random_num=random.randint(1,10)

i=3

while i>0:
    try:
        pick_num=int(input(f'\nWhat number am I thinking of? Hint! It\'s \
between 1 and 10:\n\nYou have {i} gesses left. ').strip())
        
        i-=1
        
        if pick_num<random_num:
            print('\nThe number I\'m thinking of is too low!')
            
        elif pick_num>random_num:
            print('\nThe number I\'m thinking of is too high!')
            
        elif pick_num==random_num:
            print(f'\nCongratulations. You won! "{random_num}" was the number \
I was thinking of.')
            break
        
    except ValueError:
        print('\nYou must type integers only please!')
        
else:
    print('\nSorry. You lost!')
