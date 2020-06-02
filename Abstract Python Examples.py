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

print(random.randrange(1, 9))

print(random.randrange(3, 9,2))

'''----------------------------------------------------------------'''

import random

print(random.random())

print(random.uniform(20, 60))

print(random.triangular(20, 60, 30))

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

print(random.choices(random_list, weights=[5, 10, 25,50],k=8))

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

state = random.getstate()

# print another random number:

print(random.random())

# restore the state:

random.setstate(state)

# and the next random number should be
# the same as when you captured the state:

print(random.random())

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
print(f'{x:,}') # =101 0's (ONE CENTILLION)

'''----------------------------------------------------------------'''

def myfunc():
  global x
  x = 'fantastic.'

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
