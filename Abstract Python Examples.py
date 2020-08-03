# Abstract Python Examples:

# Unpack multiple values, using just one, single "=" sign.
# Not: You must use equal variables to equal values.

a,b,c=1,2,3

print(a,b,c)

# Add the values together.

print(a+b+c)

# Example 2:

a,b,c,d,e,f=1,2,3,4,5,6

print(a,b,c,d,e,f)

# Add the values together.

print(a+b+c+d+e+f)

# Example 3

name1,name2,name3='Bob','Rob','John'

print(name1,'and',name2,'went to',name3+"'s",'house for dinner.')

# You can use the 'f' format to make the above print statement
# read like this.

print(f"{name1} and {name2} went to {name3}'s house for dinner.")

# Old format example of the print statement from earlier Python versions.

print("{} and {} went to {}'s house for dinner.".format(name1,name2,name3))

'''----------------------------------------------------------------'''

# Unpacking multi-list example:

list_1,list_2,list_3=[
    [0,1,2,3,4,5,6,7,8,9],
    ['a','b','c','d','e','f','g','h','i','j','k','l','m',
     'n','o','p','q','r','s','t','u','v','w','x','y','z'],
    ['"Python',"Programmer's",'Glossary','Bible"']
    ]

print(list_1[9])
print(list_2[0])
print(list_3[0],list_3[1],list_3[2],list_3[3])

'''----------------------------------------------------------------'''

# Unpacking multi-list for-loop example:

list_1,list_2,list_3=[
    [0,1,2,3,4,5,6,7,8,9],
    ['a','b','c','d','e','f','g','h','i','j','k','l','m',
     'n','o','p','q','r','s','t','u','v','w','x','y','z'],
    ['"Python',"Programmer's",'Glossary','Bible"']
    ]

for i in list_1,list_2,list_3:
    print(i[0],i[1],i[2],i[3])
    
'''----------------------------------------------------------------'''

print(type('string'))

# <class 'str'>

print(type(2))

# <class 'int'>

# View string fuctions and string methods.

print(dir('string'))

# View integer fuctions and integer methods.

print(dir(2))

# Get the id from a string.

print(id('string'))

# Get the id from an integer.

print(id(2))

'''----------------------------------------------------------------'''

# These two 'print' statements below use the dunder method 'add', which is the same
# as the 'print' statements 'print(2+3)' and 'print('a'+'b')'. The 'int' function adds only
# integer numbers together, whereas the 'str' function concatenates/joins character
# strings together.

print(int.__add__(2,3))

# Screen output:	5

print(str.__add__('a','b'))

# Screen output:	ab

# Dunder methods assure functionality inside class functions. For example, you
# wouldn't use a dunder '__str__' method with integer values; likewise, you wouldn't
# use a dunder '__add__' method with character string values.

# Take a close look at these two program examples below. You notice there are
# yellow highlighted variables. These variables indicate how these two, very same
# program examples can be written. Both program examples do exactly the same
# thing, even though they look a wee bit different. Type and execute/run these two
# program examples below and see what happens.

# Program example 1:

class Dunder_add:
    def __init__(self,num):
        self.num=num
        
    def __add__(self,plus):
        return self.num+plus

a=Dunder_add(6)
b=Dunder_add(8)
c=Dunder_add(12)

print(a.num+b.num+c.num)

# Program example 2:

class Dunder_add:
    def __init__(self,num):
        self.num=num
        
    def __add__(self,plus):
        return self.num+plus.num

a=Dunder_add(6)
b=Dunder_add(8)
c=Dunder_add(12)

print(a+b+c.num)

'''----------------------------------------------------------------'''

x={1,2,3,4,9,6,7,8,5,9}
y={10,11,15,13,14,12,16,17,18,19,19}
z={20,21,22,23,27,25,26,24,28,29,22}

unionize=x.union(y).union(z)

convert=list(unionize)

a=slice(20)

print(convert[a])        

'''----------------------------------------------------------------'''

x={1,2,3,4,9,6,7,8,5,9}
y={10,11,15,13,14,12,16,17,18,19,19}
z={20,21,22,23,27,25,26,24,28,29,22}

unionize=x.union(y,z)

convert=list(unionize)

a=slice(20)

print(convert[a])

'''----------------------------------------------------------------'''

a=list()
for i in range(10):
    a.append(i)

b=set()
for i in range(10):
    b.add(i)

print(a)
print(b)

'''----------------------------------------------------------------'''

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 | nums2) # Union

print(nums1.union(nums2)) # Union

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 & nums2) # Intersection

print(nums1.intersection(nums2)) # Intersection

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 - nums2) # Difference

print(nums1.difference(nums2)) # Difference

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 ^ nums2) # Symmetric Difference

'''----------------------------------------------------------------'''

nums1={0,1,2,3,1,3,4,10,5,6,6,7,8,9,10,23}
nums2={1,2,7,1,3,4,10,5,6,6,7,8,9,10,11,22}

print(nums1 | nums2)
print(nums1 & nums2)
print(nums1 - nums2)
print(nums1 ^ nums2)

nums1=[1,2,3,1,3,4,10,5,6,6,7,8,9,10]
nums2=[1,2,3,1,3,4,10,5,6,6,7,8,9,10]

uniques1=set(nums1)
uniques2=set(nums2)

print(uniques1 | uniques2)

'''----------------------------------------------------------------'''

nums={0,1,2,3,1,3,4,10,5,6,6,7,8,9,10}

try:
    num=int(input('Enter a number: '))
    if num in nums:
        print(f'{num} is in nums.')
    elif num not in nums:
        print(f'{num} is not in nums.')
except ValueError:
    print('Sorry! I cannot do that.')

'''----------------------------------------------------------------'''

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 | nums2) # Union

'''----------------------------------------------------------------'''

my_set=['Fast','Fast','Frog','Fish','Frog','Fog','Floor']

print('This unsorted list',my_set,'has duplicates in it.')

duplicate=set(my_set)

print('\nThis converted set from a list',duplicate,'has no \
duplicates in it, but is always in random order.')

duplicate=sorted(duplicate)
my_set=list(duplicate)

print('\nThis random set order converts back into a sorted, \
non-duplicated list.',duplicate,)

print(f'\nNow you can call up a sorted, non-duplicate list item \
like this "{duplicate[4]}"')

'''----------------------------------------------------------------'''

x=tuple('123456789')

print(x)

x=tuple(('123456789','abcdefghij'))

print(x)

'''----------------------------------------------------------------'''

num1,num2=0,1
fib={num1,num2}

y,a,b=100,'is in the Fibonacci Number \
Sequence.','is not in the Fibonacci Number Sequence.'

for i in range(y):
    fib_num=num1+num2
    fib.add(fib_num)
    num1=num2
    num2=fib_num
    
while True:    
    try:
        x=int(input('Please enter a correct Fibonacci Sequence Number: '))
        if x in fib:
            print(x,a)        
        elif x not in fib:
            print(x,b)
    except ValueError:
        print('Sorry! Numbers only please.')

'''----------------------------------------------------------------'''

# input Fibonacci Number Sequence example, using a set{}

num1,num2=0,1

fib={num1,num2}

words=(
    'is in the Fibonacci Sequence.',
    'is not in the Fibonacci Sequence.',
    'Please enter a correct Fibonacci Sequence Number: ',
    'Sorry! Numbers only.',
    'Memory Error!'
    )

try:
    x=int(input(words[2]).strip())

    for i in range(x):
        fib_num=num1+num2
        fib.add(fib_num)
        num1=num2
        num2=fib_num

    if x in fib:
        print(x,words[0])
        
    elif x not in fib:
        print(x,words[1])
        
except ValueError:
    print(words[3])
    
except MemoryError:
    print(words[4])

'''----------------------------------------------------------------'''

import os,time;os.system('')

text_colours=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

text_words=(
    f'\n"Python Programmer\'s Glossary Bible" by Joseph \
C. Richardson','cls'
    )

length=0
while length<=len(text_words[0]):
    for i in text_colours:
        print(i+text_words[0][:length])
        time.sleep(.05)
        os.system(text_words[1])
        length+=1

print(i+text_words[0])

input('\nPress Enter to exit.')

'''----------------------------------------------------------------'''

# Random Generator Examples:

import random

print(random.randint(1,9))

print(random.randrange(1,9))

print(random.randrange(3,9,2))

'''----------------------------------------------------------------'''

import random

print(random.random())

print(random.uniform(20,60))

print(random.triangular(20,60,30))

'''----------------------------------------------------------------'''

import random

random_list=['Random 1','Random 2','Random 3','Random 4']

print(random.choice(random_list))

'''----------------------------------------------------------------'''

import random

random_list=[
    'Random 1','Random 2',
    'Random 3','Random 4'
    ]

random.shuffle(random_list)

print(random_list[0])

'''----------------------------------------------------------------'''

import random

random_list=[
    'Random Least1','Random Least2',
    'Random Less','Random Most'
    ]

print(random.choices(random_list,weights=[5,10,25,50],k=8))

'''----------------------------------------------------------------'''

import random

random.seed(10)

print(random.random())

'''----------------------------------------------------------------'''

import random

random.seed(10)

print(random.getstate())

'''----------------------------------------------------------------'''

import random

print(random.getrandbits(4))

'''----------------------------------------------------------------'''

import random

print(random.random())

# capture the state:

state=random.getstate()

# print another random number:

print(random.random())

# restore the state:

random.setstate(state)

# and the next random number should be
# the same as when you captured the state:

print(random.random())

'''----------------------------------------------------------------'''

from numpy import random

x=random.randint(100)
print(x)

'''----------------------------------------------------------------'''

from numpy import random

x=random.rand()
print(x)

'''----------------------------------------------------------------'''

from numpy import random

x=random.randint(100,size=(5))
print(x)

'''----------------------------------------------------------------'''

from numpy import random

x=random.randint(100,size=(3,5))
print(x)

'''----------------------------------------------------------------'''

from numpy import random

x=random.rand(5)
print(x)

'''----------------------------------------------------------------'''

from numpy import random

x=random.rand(3,5)
print(x)

'''----------------------------------------------------------------'''

from numpy import random

x=random.choice([3,5,7,9])
print(x)

'''----------------------------------------------------------------'''

from numpy import random

x=random.choice([3,5,7,9], size=(3,5))
print(x)

'''----------------------------------------------------------------'''

from numpy import random

x=random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(100))
print(x)

'''----------------------------------------------------------------'''

from numpy import random

x=random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(3,5))
print(x)

'''----------------------------------------------------------------'''

from numpy import random
import numpy as np

arr=np.array([1,2,3,4,5])

random.shuffle(arr)
print(arr)

'''----------------------------------------------------------------'''

from numpy import random
import numpy as np

arr=np.array([1,2,3,4,5])
print(random.permutation(arr))

'''----------------------------------------------------------------'''

import os,math,random
from time import sleep

while True:
    random_num=random.randint(1,10)
    if  random_num is 10:
        print('is equal to 10. The loop breaks')
        break
    elif random_num is not 10:
        print('is not equal to 10. The loop repeats')        
        sleep(1)

'''----------------------------------------------------------------'''

# This conditional while-loop example compares a random number against user input
# data. If the user picks the right number by luck alone, the while-loop will break out
# and the program ends. If the user picks the wrong number, the less (<) than or
# greater (>) than 'random_num' variable gets conditioned and the while-loop keeps
# on iterating until the right number is picked, via user input data.

# Note: Python executes/runs programs starting from the top, downward. Be very
# careful on how you place statements. Some statements cannot execute right, even if
# they work. This is simply because of the order that Python executes/runs its
# program statements.

# Note: The 'import random' module must be imported first.

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

'''----------------------------------------------------------------'''

# This very same program example as above works exactly the same way, but with
# one major difference; the while loop will only iterate three times. If the user picks the
# right number, the while loop breaks. If the user doesn't pick the right number after
# three times, the 'else' statement executes and says 'Sorry! You lost.', which ends the
# program.

# Note: the 'import random' module must be imported first.

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

'''----------------------------------------------------------------'''

# Once again, this is the very same program example as above before. However, this
# time the loop iterates in reverse instead of forward and the user is shown how many
# guesses they have left before they win or lose.

# Note: the 'import random' module must be imported first.

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
    
'''----------------------------------------------------------------'''

x=10**1
print(f'{x:,}') # =10 (TEN)

x=10**2
print(f'{x:,}') # =100 (ONE HUNDRED)

x=10**3
print(f'{x:,}') # =1,000 (ONE THOUSAND)

x=10**4
print(f'{x:,}') # =10,000 (TEN THOUSAND)

x=10**5
print(f'{x:,}') # =100,000 (ONE HUNDRED THOUSAND)

x=10**6
print(f'{x:,}') # =1,000,000 (ONE MILLION)

x=10**9
print(f'{x:,}') # =1,000,000,000 (ONE BILLION)

x=10**12
print(f'{x:,}') # =1,000,000,000,000 (ONE TRILLION)

x=10**15
print(f'{x:,}') # =1,000,000,000,000,000 (ONE QUADRILLION)

x=10**18
print(f'{x:,}') # =1,000,000,000,000,000,000 (ONE QUINTILLION)

x=10**21
print(f'{x:,}') # =1,000,000,000,000,000,000,000 (ONE SEXTILLION)

x=10**24
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000 (ONE SEPTILLION)

x=10**27
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000,000 (ONE OCTILLION)

x=10**30
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000,000,000 (ONE NONILLION)

x=10**33
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000,000,000,000 (ONE DECILLION)

x=10**36
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000,000,000,000,000 (ONE UNDECILLION)

x=10**39
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE DUODECILLION)

x=10**42
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE TREDECILLION)

x=10**45
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE QUATTTUOR-DECILLION)

x=10**48
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE QUINDECILLION)

x=10**51
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE SEXDECILLION)

x=10**54
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE SEPTEN-DECILLION)

x=10**57
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE OCTODECILLION)

x=10**60
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE NOVEMDECILLION)

x=10**63
print(f'{x:,}') # =1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE VIGINTILLION)

x=10**303
print(f'{x:,}') # =303 0's (ONE CENTILLION)

'''----------------------------------------------------------------'''

import math

print(min(3,6,9))

print(max(3,6,9))

print(pow(2,3))

print(abs(-10))

print(math.sqrt(9))

print(math.floor(45.17))

print(math.ceil(45.17))

'''----------------------------------------------------------------'''

def myfunc():
  global x
  x='fantastic.'

myfunc()

print('Python is '+x)

'''----------------------------------------------------------------'''

class Super_class:
    def super1(self):
        print('Super1')

    def super2(self):
        print('Super2')

    def super3(self):
        print('Super3')

class Class_all(Super_class):
    def get_values(self):
        super().super1()
        super().super2()
        super().super3()

Class_all().get_values()

'''----------------------------------------------------------------'''

class A:
    def __init__(self):
        super().__init__()
        print('first')
        
class B:
    def __init__(self):
        super().__init__()
        print('second')
        
class C:
    def __init__(self):
        super().__init__()
        print('third')
        
class D:
    def __init__(self):
        super().__init__()
        print('forth')
        
class All(A,B,C,D):
    def __init__(self):
        super().__init__()
        
All()

'''----------------------------------------------------------------'''

# This conditional while-loop will loop as long as the value is less (<) than 3, then it will
# stop its iteration no matter what wrong keys the user tries to type.

chance=0

name=input('\nWhat is your name please? ').strip()

while chance<3:
    try:
        age=int(input(f'\nHow old are you {name}? ').strip())
        print(f'\n{name}. You are {age} years old.')
        break
    
    except ValueError:
        print(f'\nYou have 3 chances left before the while-loop breaks out anyway!')
        
        chance+=1
        
'''----------------------------------------------------------------'''

# This for-loop example does exactly the same thing, the above while-loop example
# shows. The only difference is, the while-loop is a conditional loop, whereas the for-
# loop is an iterate. While-loops can also be 'True:' or 'False:', depending on the
# outcome of a program's excution run. While-loops also compare data greater than or
# less than other data, as shown in the examples above.

name=input('\nWhat is your name please? ').strip()

for chance in range(3):
    try:
        age=int(input(f'\nHow old are you {name}? ').strip())
        print(f'\n{name}. You are {age} years old.')
        break
    
    except ValueError:
        print('\nYou have 3 chances left before the while-loop breaks out anyway!')
        
        chance+=1

'''----------------------------------------------------------------'''

# This program example has three, separate conditional while-loops, each of them
# compares data against user input data. The first while-loop asks for the user's first
# name. The second while-loop asks for the user's last name, and the third while-loop
# asks for the user's age. In the first and second while-loop, the user's first name and
# user's last name are compared by how many letters the user types. The 
# 'str([first_name])' statement makes the user type in text only, not integers.

# Note: Python executes/runs programs starting from the top, downward. Be very
# careful on how you place statements. Some statements cannot execute right, even if
# they work. This is simply because of the order that Python executes/runs its
# program statements.

while True:
    first_name=input('\nWhat is your name please? ').strip()
    
    if first_name<str([first_name]):
        print('\nError: text only please!')
        
    elif len(first_name)<3:
        print('\nYour first name must be over 2 characters long.')
        
    elif len(first_name)>10:
        print('Your first name must be under 10 characters long.')
        
    else:
        break

while True:
    last_name=input(f'\nNice to meet you {first_name.title()}. \
What is your last name please? ').strip()
    
    if last_name<str([last_name]):
        print('\nError: text only please!')
        
    elif len(last_name)<3:
        print('\nYour last name must be over 2 characters long.')
        
    elif len(last_name)>10:
        print('\nYour last name must be under 10 characters long.')
        
    else:
        break

while True:
    try:
        age=int(input(f'\nHow old are you {first_name.title()}? ').strip())
        break
    
    except ValueError:
        print('\nError: integers only please!')
        
print(f'\nYour first name = {first_name.title()}:\nYour last name = \
{last_name.title()}:\nYour age = {age}:\n')

'''----------------------------------------------------------------'''

# Here's a fun, simple program example, which tells you how many seconds you have
# been on Earth for. Type and execute/run the program example below and see what
# happens when you type your age, then press the 'Enter' key. Note: this program
# example also uses the 'finally' statement to illustrate the use of the how the 'finally'
# command works. The 'finally' command will always execute, no matter the outcome.
# Also note that the 'finally' command only works with the 'try' and 'except' command
# blocks.

months=12
weeks=52
days=365

hours_per_day=24
minuts_per_hour=60
seconds_per_minute=60

string_tuple=(
    months,weeks,days,
    hours_per_day,
    minuts_per_hour,
    seconds_per_minute
    )

while True:
    
    try:        
        age=int(input('How old are you? ').strip())

        print(f'\nYou have been on Earth for {age} years.')
        
        print(f'\nYou have been on Earth for {age*string_tuple[0]:,} months.')
        
        print(f'\nYou have been on Earth for {age*string_tuple[1]:,} weeks.')
        
        print(f'\nYou have been on Earth for {age*string_tuple[2]:,} days.')

        print(f'\nYou have been on Earth for {age*string_tuple[2]*string_tuple[3]:,} hours.')

        print(f'\nYou have been on Earth for \
{age*string_tuple[2]*string_tuple[3]*string_tuple[4]:,} minutes.')

        print(f'\nYou have been on Earth for \
{age*days*string_tuple[3]*string_tuple[4]*string_tuple[5]:,} seconds.')
        
        break
    
    except ValueError:
        print('\nSorry! Numbers only please.\n')
        
    finally:
        print('Finally will always execute no matter the outcome.')

'''----------------------------------------------------------------'''

# This conditional while-loop example types out the words "Python Programmer\'s
# Glossary Bible". As long as 'length' is less (<) than 'len' starting at "0", the while-loop
# will keep on looping until  'length' is equal to 'len'. The 'os.system('cls')' function
# clears the screen each cycle through the while-loop, and the 'time.sleep(.05)'
# function delays the while-loop in between cycles. This fun, little program example
# makes the printout on the screen appear as if it were actualy typing letters.

# Note: Python executes/runs programs starting from the top, downward. Be very
# careful on how you place statements. Some statements cannot execute right, even if
# they work. This is simply because of the order that Python executes/runs its program
# statements.

# Note: The 'import os' module and the 'import time' module must be imported first.

import os
import time

letters='\n"Python Programmer\'s Glossary Bible"'
length=0

while length<=len(letters):
    os.system('cls')
    print(letters[:length])
    time.sleep(.05)
    length+=1

'''----------------------------------------------------------------'''

# See what happens when you type and execute/run this guessing game program
# example below. Note: you must execute/run the program from the OS output screen,
# via double-clicking the Python program file itself.

# Save the Python file as 'Know Your Stuff'

import os

tc=(
    '\x1b[31m',
    '\x1b[32m',
    '\x1b[33m',
    '\x1b[34m',
    '\x1b[35m',
    '\x1b[36m',
    '\x1b[37m',
    'cls'
    )

question_prompts1=(
    f'{tc[2]}How many sides does a Triangle have?\n\n{tc[1]}(a) {tc[2]}four sides\n\
{tc[1]}(b) {tc[2]}three sides\n{tc[1]}(c) {tc[2]}two sides',
    
    f'{tc[2]}How many sides does a Square have?\n\n{tc[1]}(a) {tc[2]}Two sides\n\
{tc[1]}(b) {tc[2]}Three sides\n{tc[1]}(c) {tc[2]}Four sides',
    
    f'{tc[2]}How many sides does a Pentagon have?\n\n{tc[1]}(a) {tc[2]}four sides\n\
{tc[1]}(b) {tc[2]}five sides\n{tc[1]}(c) {tc[2]}Three sides',
    
    f'{tc[2]}How many sides does a Hexagon have?\n\n{tc[1]}(a) {tc[2]}six sides\n\
{tc[1]}(b) {tc[2]}five sides\n{tc[1]}(c) {tc[2]}two sides',
    
    f'{tc[2]}How many sides does a Octagon have?\n\n{tc[1]}(a) {tc[2]}four sides\n\
{tc[1]}(b) {tc[2]}six sides\n{tc[1]}(c) {tc[2]}eight sides',
    
    f'{tc[2]}How many sides does a Dodecagon have?\n\n{tc[1]}(a) {tc[2]}eight \
sides\n{tc[1]}(b) {tc[2]}three sides\n{tc[1]}(c) {tc[2]}twelve sides',
    
    f'{tc[2]}How many sides does a Hexadecagon have?\n\n{tc[1]}(a) {tc[2]}sixteen \
sides\n{tc[1]}(b) {tc[2]}eight sides\n{tc[1]}(c) {tc[2]}six sides'
    )

prompt=('b','c','b','a','c','c','a')

score=0
loop=0

while loop<=6:
    
    os.system(tc[7])
    button=input((tc[1])+'\nKnow Your Stuff!\n\n'+(tc[2])+'Know Your Polygons\n\n'+\
    question_prompts1[loop]+'\n\n'+(tc[0])+'READY:'+(tc[1])).strip()
    
    if button==(prompt[loop]):
        score+=1
        
    loop+=1
    
    os.system(tc[7])
    
print(f'\n{tc[2]}Know Your Polygons\n\n{tc[2]}You got \
{score}/{len(question_prompts1)} questions correct.\nCongratulations! Your total \
Prize Winnings: {tc[1]}${score*100*score:,}.00 {tc[2]}Dollars.\n\n{tc[0]}READY:')

input('\nEND OF PROGRAM! Press Enter to quit.')

'''----------------------------------------------------------------'''

# Let's have fun and learn how to raise some errors
# to test in Python programs.

try:
    print('Raising an Exception:')
    raise Exception
except Exception:
    print('Exception:')
finally:
    print('finally always executes no matter the outcome.')

try:
    print('Raising a ValueError:')
    raise ValueError
except ValueError:
    print('ValueError:')
finally:
    print('finally always executes no matter the outcome.')

try:
    print('Raising a TypeError:')
    raise TypeError
except TypeError:
    print('TypeError:')
finally:
    print('finally always executes no matter the outcome.')

try:
    print('Raising a NameError:')
    raise NameError
except NameError:
    print('NameError:')
finally:
    print('finally always executes no matter the outcome.')    
    
try:
    print('Raising a IndexError:')
    raise IndexError
except IndexError:
    print('IndexError:')
finally:
    print('finally always executes no matter the outcome.')

try:
    print('Raising a MemoryEorror:')
    raise MemoryError
except MemoryError:
    print('MemoryError:')
finally:
    print('finally always executes no matter the outcome.')    
    
'''----------------------------------------------------------------'''    

# Raise a list of possible errors to test in Python programs.

try:
    print('Raising a list of possible errors to test:')
    raise Exception
    raise ValueError
    raise TypeError
    raise NameError
    raise IndexError
    raise MemoryError
except Exception:
    print('Exception:')
except ValueError:
    print('ValueError:')    
except TypeError:
    print('TypeError:')
except NameError:
    print('NameError:')
except IndexError:
    print('IndexError:')
except MemoryError:
    print('MemoryError:')
finally:
    print('finally always executes no matter the outcome.')

'''----------------------------------------------------------------'''

# Here is a basic, skeletal structure of a Try: and Except: block.
# The 'Pass' statement ignores any empty code blocks, which are
# not used for now. In this case, only the skeletal structure of the
# program is clearly shown. Note:  you do not need to invoke the
# 'finally' statement into try: and Except: blocks, but they can be
# quite handy when you want to show any output on the screen,
# no matter the outcome of the program's execution/run.

try:
    pass
except Exception:
    pass
finally:
    pass

try:
    num=int(input('Type a Number: ').strip())
except ValueError:
    print('Sorry! Numbers only please.')
finally:
    print('finally always executes no matter the outcome.')
