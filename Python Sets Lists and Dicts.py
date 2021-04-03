# Have some fun with Python Sets.

animals1,animals2=(
    {'Dog','Cat','Bird','Fish','Dog','Bird'},
    {'Bat','Rat','Mouse','Monkey','Dog','Fish','Cat'})

animals1.update(animals2)

animals1.add('Frog')

animals1.discard('Rat')

print(animals1)

'''
.add()
.clear()
.copy()
.difference()
.difference_update()
.discard()
.intersection()
.intersection_update()
.isdisjoint()
.issubset()
.issuperset()
.pop()
.remove()
.symmetric_difference()
.symmetric_difference_update()
.union()
.update()
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
animals1,animals2=(
    {'Dog','Cat','Bird','Fish','Dog','Bird'},
    {'Bat','Rat','Mouse','Monkey','Dog','Fish','Cat'})

print(animals1.union(animals2)) # Union
print(animals1|animals2) # Union

print(animals1.intersection(animals2)) # Intersection
print(animals1 & animals2) # Intersection

print(animals1.difference(animals2)) # Difference
print(animals1 - animals2) # Difference

print(animals1 ^ animals2) # Symmetric Difference

x=animals1.symmetric_difference_update(animals2) # Symmetric Difference Update
print(animals1)

# Why not use these shortcuts instead.

print(animals1 | animals2)
print(animals1 & animals2)
print(animals1 - animals2)
print(animals1 ^ animals2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
animals1,animals2=(
    {'Dog','Cat','Bird','Fish','Dog','Bird'},
    {'Bat','Rat','Mouse','Monkey','Dog','Fish','Cat'})

x=animals1 | animals2
for i in x:
    print(i)

animals1.update(animals2)
for i in animals1:
    print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
animals1,animals2=(
    {'Dog','Cat','Bird','Fish','Dog','Bird'},
    {'Bat','Rat','Mouse','Monkey','Dog','Fish','Cat'})

animals1.update(animals2)

convert=list(animals1)

x=sorted(convert)
for i in x:
    print(i)

x=sorted(convert,reverse=True)
for i in x:
    print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Have some fun with Dictionaries.

animals={    
    'Dog':'Wolf',
    'Cat':'Lion',
    'Fish':'Shark',
    'Bird':'Eagle'
    }

print(animals.get('dog'))
print(animals.get('dog','Not Found!'))
print(animals.get('Dog','Not Found!'))

for key,value in animals.items():
    print(key)

for key,value in animals.items():
    print(value)

for key,value in animals.items():
    print(key,value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is some more fun with a return function along with
# a tuple called 'sentence', which will loop through each
# value within the for-loop, creating a complete, different
# sentence for each cycle through the for-loop. The 'names'
# variable also gets cycled through the for-loop until all its
# values get cycled through, which will end the for-loop.

def names(name1='Rob.',name2='Bob.',name3='Ron.'):
    return name1,name2,name3,'John.'

names=names()

sentence=(
    'Where did you get your rat?',
    'Where did you get your cat?',
    'Where did you get your hat?',
    'Where did you get your mat?')
    
for i in range(4):
    print('Hello',names[i],sentence[i]+'\n')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's have some fun with this positional arguments Python
# program example.

def keyword(first,second,third):
    print(
        '"Python Programmer\'s Glossary Bible"\nby '
        +first.capitalize()+second.capitalize()+third.capitalize())

keyword(third='richardson ',first='joseph ',second='c. ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's fully understand what a 2d list is truly all about.
# A 2d list is a two dimensional array that can hold multiple
# 2d list array values under a single variable. For example:

my_2d_list=['2d list0'],['2d list0']

print(my_2d_list[0][0])
print(my_2d_list[1][0])

# If you create a really long 2d list such as this example below,
# you can force hard line-breaks, but you must use outer square
# brackets '[]' or parentheses '()' to surround the entire 2d list
# values. Note: you must use commas at the end of each 2d list
# array.

# Example 1:

my_2d_list=['2d list0'],['2d list0'],['2d list0'],['2d list0'],['2d list0'],['2d list0'],['2d list0']

print(my_2d_list[4][0])

# Example 2:

my_2d_list=( # use a hard line-break make the 2d list look neat and tidy.
    ['2d list0'],['2d list0'],['2d list0'],
    ['2d list0'],['2d list0'],['2d list0'],
    ['2d list0']) # use a hard line-break to add more values to the 2d list.

print(my_2d_list[4][0])
'''
.insert()
.append()
.extend()
.index()
.remove()
.pop()
.clear()
.sort()
.sort(reverse = True)
.reverse()
.copy()
.count()
del list_item[n]
'''
# Create a multi-2d list array like this example below illustrates.

my_multi_2d_list=['Value0','Value1','Value2'],['Value0','Value1','Value2']

print(my_multi_2d_list[0][0])
print(my_multi_2d_list[0][1])
print(my_multi_2d_list[0][2])

print(my_multi_2d_list[1][0])
print(my_multi_2d_list[1][1])
print(my_multi_2d_list[1][2])

# You can create as many multi-2d list array values as you please.
# For example:

my_multi_2d_list=(
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2','Value3'],
    ['Value0','Value1','Value2','Value3','Value4']) # neat and tidy

print(my_multi_2d_list[0][2])
print(my_multi_2d_list[1][3])
print(my_multi_2d_list[2][4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's have some multi-2d list fun using a for-loop
# and see what happens when we execute/run this multi-2d
# list, for-loop example:

my_multi_2d_list=(
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2']) # neat and tidy

for i in my_multi_2d_list:
    print(i[0],i[1],i[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a real, working multi-2d list to see what
# they are truly all about in a real Python program scenario.
# We will call our multi-2d list, 'names'. Use the (f') format
# to make the 'print' statement easier to concatenate strings.

names=(
    ['Ron','Bob','Tom'],
    ['John','Mary','Terry'],
    ['Edie','Freddy','Teddy'],
    ['Charie','Marty','Harvey']) # neat and tidy

for i in names:
    print(f'{i[0]}, {i[1]} and {i[2]} went to the store.')

# Let's create a looping sentence tuple with our multi-2d list for-loop
# example and see what happens when we execute/run this Python
# program example below.

names=(
    ['Ron','Bob','Tom'],
    ['John','Mary','Terry'],
    ['Edie','Freddy','Teddy'],
    ['Charie','Marty','Harvey']) # neat and tidy

sentence=(
    ('went home to have dinner.',
    'went to the store to buy some food.',
    'wanted some pizza for breakfast.',
     'wanted computers for Christmas.',
     'love their computers.'))

for i in range(4):
        print(f'{names[i][0]}, {names[i][1]} \
and {names[i][2]} {sentence[i]}')
        
# Here are some simple return function examples to
# practice with.

def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def square(num1,num2):
    return num1**num2
def division(num1,num2):
    return num1/num2
def name(first_name,last_name,mc2=18600**2):
    return first_name+last_name+str(mc2)

a=addition(8,2)
s=subtraction(8,2)
m=multiplication(8,2)
d=division(8,2)
e=square(8,2)

nums=int(a+s+m+d+e)

name=name('Albert ','Einstein = ',nums)

# remove the 'nums' variable and see what happens when
# you re-execute/run the above Python program example.

print(name)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# How Parentheses, Square Brackets and Curly Braces
# work in Python.

# Parentheses: '()'
# Parentheses are used for 'Tuples', along with other uses,
# such as 'print' functions and functions alike.

# Square Brackets: '[]'
# Square Brackets are used for 'lists' and '2d lists', along
# with other uses, such as indexing character strings and
# values alike.

# Curly Braces: '{}'
# Curly Braces are used for 'sets' and 'dictionaries', along
# with other uses, such as formatted character strings.

# Here is a simple 'tuple' example:
# names=('John','Ron','Tom','Bob')

# Here is a simple 'list' example:
# names=['John','Ron','Tom','Bob']

# Here is a simple 'dictionary' example:
# names={1:'John',2:'Ron',3:'Tom',4:'Bob'}

# Here is a simple 'set' example:
# names={'John','Ron','Tom','Bob'}
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Variable Scope:

# L= Local
# E= Enclosing
# G= Global
# B=Built-in
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# predefined returned values to arguments example:

def values_example(value0,value1,value2,value3):
    return 0,1,2,3

print(values_example('Value0','Value1','Value2','Value3')[2])

# undefined returned values to arguments example:

# If you aren't sure how many returned values to variables
# are needed, use the '*args' function instead. You can name
# the word 'args' to any name you like, but the (*) is needed.
# For example: '*get_any_number_of_returned_values' works.
# However in python, programmers use the standard as '*args'
# short for (arguments). Use '*args' if you want to update the
# function's returned values, without the worry of how many
# actual argument variables are needed inside the 'print'
# statement, such as the example above illustrates.

# Example 1:

def args_example(*args):
    return args[0]

print(args_example(0,1,2,3,4,5,6,7,8,9))

# Example 2:

def args_example(*args):
    return 0,1,2,3,4,5,6,7,8,9

print(args_example()[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# undefined returned values to keyword arguments example:

# If you aren't sure how many returned values to variables are
# needed, use the '**kwargs' function instead. You can name the
# word 'kwargs' to any name you like, but the (**) is needed. For
# example: '**get_any_number_of_returned_values' works. However
# in python, programmers use the standard as '**kwargs' short for
# (keyword arguments). Use '**kwargs' if you want to update the
# function's returned values, without the worry of how many actual
# keyword argument variables are needed inside the 'return'
# statement.

def kwargs_example(**kwargs):
    return 0,1,2,3,4,5,6,7,8,9

print(kwargs_example()[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are the very same examples below, but with hard line
# breaks. In most cases, you must use parenthesis '()' to surround
# hard line breaks, such as these examples illustrate.

# Example 1:

def args_example(*args):
    return args[0]

print(args_example( # insert a hard line break if you like.
  'Test with numbers',0,1,2,3,4,5,6,7,8,9,'Example.'))

# Example 2:

def args_example(*args):
    return( # insert a hard line break if you like.
    'Test with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

print(args_example()[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def kwargs_example(**kwargs):
  return( # insert a hard line break if you like.
    'Test with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

print(kwargs_example()[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are the very same examples again, but with the use of
# variables to shorten our code a bit in the 'print' statements.

def args_example(*args):
  return args

args=args_example( # insert a hard line break if you like.
  'Test with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

print(args[0])

# Example 2:

def args_example(*args):
  return( # insert a hard line break if you like.
    'Test with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

args=args_example()

print(args[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def kwargs_example(**kwargs):
  return( # insert a hard line break if you like.
    'Test with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

kwargs=kwargs_example()

print(kwargs[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Using the knowledge we've learnt so far, let's create an
# arguments variable list loop using a for-loop.

def args_example(*args):
  return args

args=args_example( # insert a hard line break if you like.
  'Test with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

for i in args:
  print(i,end=' ') # add the 'end=' function to create single-line text output.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Using the knowledge we've learnt so far, let's create a
# keyword arguments variable list loop using a for-loop.

def kwargs_example(**kwargs):
  return( # insert a hard line break if you like.
    'Test with numbers',0,1,2,3,4,5,6,7,8,9,'Example.')

kwargs=kwargs_example()

for i in kwargs:
  print(i,end=' ') # add the 'end=' function to create single-line text output.
  
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in range(10)]

newlist = [x.upper() for x in fruits]

print("Yes") if 5 > 2 else print("No")

def fun(x):
    for i in x:
        if i == 4:
            fun(x)
        else:
            print(i)
    return;

x = [1,2,3,5,6]
fun(x)
