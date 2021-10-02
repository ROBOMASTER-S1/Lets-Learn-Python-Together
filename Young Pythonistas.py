# This is for much younger Pythonistas to be. lol

# With computers, numbers always follow the order of operation
# or BEDMAS: 'Brackets, Exponents, Division, Addition and
# Subtraction.

# Here are some Python examples that clearly show the order
# of operation.

print(3*4+5+3) # 12+8 = 20

num1=3*4
num2=5+3

print(num1+num2) # 12+8 = 20
print(num1-num2) # 12-8 = 4

# To create an integer on the screen output instead of a float,
# use the int() function. For example: 20.0 is a float, 20 is an
# integer number without a decimal point. In some cases, a
# floating point number can occur when you don't want to
# display an ugly floating point number on the screen output.

print(int(24/2+5+3)) # 12+8 = 20

num1=int(24/2)
num2=int(5+3)

print(num1+num2) # 12+8 = 20
print(num1-num2) # 12-8 = 4
'''----------------------------------------------------------------------------------------------------------------------'''
# Add the sum of all the numbers in a numbers list.

numbers=0,1,2,3,4,5,6,7,8,9

print(sum(numbers)) # sum = 45
'''----------------------------------------------------------------------------------------------------------------------'''
# Minimum and maximum number example:

min_max=0,1,2,3,4,5,6,7,8,9

print(min(min_max)) # min = 0
print(max(min_max)) # max = 9

# To keep things simpler. Why not do this:

min_num=min(0,1,2,3,4,5,6,7,8,9)
max_num=max(0,1,2,3,4,5,6,7,8,9)

print(min_num)
print(max_num)
'''----------------------------------------------------------------------------------------------------------------------'''
# Round numbers with the 'round()' function

round_up=round(85.5) # round = 86

print(round_up)

round_up=round(85.56,1) # round = 85.6

print(round_up)
'''----------------------------------------------------------------------------------------------------------------------'''
# The 'abs()' function returns a negative integer into a
# positive number.

positive_num=abs(-3)

print(positive_num) # abs = 3
'''----------------------------------------------------------------------------------------------------------------------'''
# Float function example:

float_num=float(4) # float = 4.0

print(float_num)
'''----------------------------------------------------------------------------------------------------------------------'''
# Floor division example:

import math

floor_num=math.floor(8.5) # floor = 8

print(floor_num)
'''----------------------------------------------------------------------------------------------------------------------'''
# Ceil division example:

import math

ceil_num=math.ceil(8.5) # ceil = 9

print(ceil_num)
'''----------------------------------------------------------------------------------------------------------------------'''
# Modulus division example:

import math

mod_num=5%3 # modulus '%' = 2 as the remainder

print(mod_num)
'''----------------------------------------------------------------------------------------------------------------------'''
# Try and Except Error Handler Examples:

# The basic layout of the Try and except error handler.

try:
    pass # empty placeholder for code, until needed.
except ValueError:
    pass
finally: # optional: executes no matter the outcome.
    pass

# This is a working example of the Try and except error handler.

try:
    message=int(input('Please enter a number: ').strip())
except ValueError: # catches non integer values
    print('Error! Numbers only please.')
finally: # optional: executes no matter the outcome.
    print('finally: always executes no matter the outcome.')
'''----------------------------------------------------------------------------------------------------------------------'''
# Dictionary, nested for-loop sentence example:

# Create three dictionaries called person_name, pet_name
# and pet.

person_name={1:'Rob',2:'Bob',3:'Tom',4:'John'}
pet_name={1:'Spot',2:'Sylvester',3:'Goergy',4:'Polly'}
pet={1:'Dog',2:'Cat',3:'Rat',4:'Bird'}

# Create three lists called person_name_list, pet_name_list
# pet_list to get all the dictionary values.

person_name_list=[
person_name.get(1),person_name.get(2),
person_name.get(3),person_name.get(4)]

pet_name_list=[
pet_name.get(1),pet_name.get(2),
pet_name.get(3),pet_name.get(4)]

pet_list=[
pet.get(1),pet.get(2),
pet.get(3),pet.get(4)]

# Create a his_her variable to add more programming
# creativity within the nested for-loop.

his_her=['his','her']

# Use the (f') format() function to combine strings together,
# without the worry about proper string concatenation.

for i in range(2):
    for j in range(4):
        print(f'My name is {person_name_list[j]}. \
I love my {pet_list[j]} and {his_her[i]} name is {pet_name_list[j]}.')

# You can still use of the depreciated old format() function:

for i in range(2):
    for j in range(4):
        print('My name is {}. I love my {} and {} name is {}.\
'.format(person_name_list[j],pet_list[j],his_her[i],pet_name_list[j]))
'''----------------------------------------------------------------------------------------------------------------------'''
# Create a set that will check and get rid of duplicated
# letters. Note: sets don't do indexing; you must 'cast'
# the set into a list first with the list() function.

alphaset={
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','k',
'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','v',
's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a','a'}

# Convert the set into a list, while sorted without actually
# sorting the real alphalist values.

alphalist=list(sorted(alphaset)) # cast with the list() function

# Create a for-loop to loop through the alphalist values,
# while calling the upper() function to turn the letters
# into uppercase letters.

for i in alphalist:
    print(i.upper(),end=' ') # end=' ' forces same line printout

# Use the len() function to count how many letters there
# are inside the alphalist variable. Insert a new line with '\n'.

print('\n',len(alphalist))

# or this:

# Use the str() function to concatenate strings with a '+' sign.

print('\n'+str(len(alphalist)))

# have some fun, while calling the lower() function to turn
# the uppercase sentence into a lowercase sentence.

print('\n'+str(len(alphalist)),'LETTERS IN THE ALPHABET.'.lower())

# Create a variable for the sentence instead.

sentence='LETTERS IN THE ALPHABET.'

print('\n'+str(len(alphalist)),sentence.lower())

'''Python 3 and up:'''

# Use the (f') format() function to combine strings together,
# without the worry about proper string concatenation.

print(f'\n{len(alphalist)} {sentence}'.lower())

'''Python 1, and 2 versions'''

# You can still use of the depreciated old format() function:

print('\n{} {}'.format(len(alphalist),sentence.lower()))

# Call the alphalist with a slice index [:]

print(alphalist[0:26])
print(alphalist[5:26])

# Print a single letter from the alphalist variable.

print(alphalist[0].upper())

# Create a for-loop to print out the whole alphabet by using
# the variable 'alphalist' instead of using a range(n,n)

for i in alphalist:
    print(i.upper(),end=' ')

# Print the whole alphabet using a slice index [:] within
# a for-loop.

for i in range(26):
    print(alphalist[i].upper(),end=' ')

# Print the whole alphabet backwards using a slice
# index [:] within a reverse for-loop.

for i in range(25,-1,-1):
    print(alphalist[i].upper(),end=' ')

# Show off your Python skills with some fancy footwork to
# keep things straight. Make the three for-loop examples
# above, read like these three examples below.

for i in alphalist:print(i.upper(),end=' ')

for i in range(26):print(alphalist[i].upper(),end=' ')

for i in range(25,-1,-1):print(alphalist[i].upper(),end=' ')
'''----------------------------------------------------------------------------------------------------------------------'''
# How to shrink down lines of code, using a simicolon ' ; '
# along with the colon ' : '

# Please note: some Python code won't allow the use of
# the simicolon ' ; ' to be able to completely shrink down
# Python code. In for-loops and while loops, the colon ' : '
# cannot be used for nested loops or beside lists.
# This simple Python code is as shrunk down as it can
# physically allow.

for i in range(1,11):print(i)

x=[0,1,2,3,4,5,6,7,8,9]
for i in x:print(i)

x=1
while x<=10:print(x);x+=1

x=3
while True:
    if x==4:print(x,'Breaks out of the loop.');break
    elif x==5:print('Continue as we loop forever!');continue
    else:print('else: and break broke you out of the loop anyway.');break
'''----------------------------------------------------------------------------------------------------------------------'''
# Shorten functions down examples:

def func1():print('Function 1')
def func2():print('Function 2')
def func3():print('Function 3')

# Call each function from the funcs list with a for-loop.

funcs=[func1,func2,func3]

for i in funcs:i()
'''----------------------------------------------------------------------------------------------------------------------'''
