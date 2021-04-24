# Let's create a dictionary that uses strings as keys and values, instead of
# of actual text, like we did before. Let's create two, simple tuples; one for
# the key tuple and one for the value tuple. We can also create them with or
# without parentheses, but a '\' backslash must be implemented in place of the
# parentheses. However, the Python programming standard shows only the
# constant use of parentheses, not backslashes, as you can see in the next
# example below.

key='dog','cat','mouse','bird','fish' # tuple by default

value=(
    'Grey Wolf','Huge Tigger',
    'Black Rat','Macaw Parrot',
    'Great White Shark') # create a tuple with '()' parentheses.

# Why use '()' parentheses when you can simply use the '\' backslash instead.
# Note: '\' is not the usual Python programming standard, but it works. Now,
# however, this only acts like a tuple by default, not a list as one would think.
# You cannot change or modify tuple values at all; they are immutable, not
# mutable like lists. Even though this works, it's not viable, especially when
# you need to create a mutable list, not an immutable tuple, as this example
# does by default. You must use either '()' parentheses for tuples, '[]' square
# brackets for lists and '{}' curly braces for dictionaries and sets alike.

key='dog','cat','mouse','bird','fish' # tuple by default

value=\
        'Grey Wolf','Huge Tigger',\
        'Black Rat','Macaw Parrot',\
        'Great White Shark' # tuple by default

dictionary={ # dictionary
    key[0]:value[0],
    key[1]:value[1],
    key[2]:value[2],
    key[3]:value[3],
    key[4]:value[4]
    }

# Non formatted examples with commas ',' and plus '+' signs

for keys,values in dictionary.items():
    print('My '+keys+' is really a '+values+'.')

for keys,values in dictionary.items():
    print('My',keys,'is really a',values+'.')

# Old formatted example: now depreciated in Python 3 and up.
# Can still be used in Python 3, thus far.

for keys,values in dictionary.items():
    print('My {} is really a {}.'.format(keys,values))

# New formatted example: Python 3 and up.

for keys,values in dictionary.items():
    print(f'My {keys} is really a {values}.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Things you can do with tuples and lists.

# Tuple Example:

variable_1='dog','cat','bird','guppy'

variable_2=(
    'Grey Wolf','Huge Tigger',
    'Macaw Parrot','Great White Shark')

variable_3='John','Rob','Ron','Bob'

variable_4='Mom','Dad','Brother','Sister'

variable_5='friend','girlfriend','boyfriend','neighbour'

for var1,var2,var3,var4,var5 in zip(variable_1,variable_2,variable_3,variable_4,variable_5):
    print(f'My {var4} and my {var5} {var3} says my {var1} is really a {var2}.')

# List Example:

variable_1=['dog','cat','bird','guppy']

variable_2=[
    'Grey Wolf','Huge Tigger',
    'Macaw Parrot','Great White Shark']

variable_3=['John','Rob','Ron','Bob']

variable_4=['Mom','Dad','Brother','Sister']

variable_5=['friend','girlfriend','boyfriend','neighbour']

for var1,var2,var3,var4,var5 in zip(variable_1,variable_2,variable_3,variable_4,variable_5):
    print(f'My {var4} and my {var5} {var3} says my {var1} is really a {var2}.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Test whether a value is true or false using the logical operators:

# " ==, <, >, <=, >=, != "

a=1;b=1

print(a==a) # True
print(a<a) # False
print(a>a) # False
print(a<=a) # True
print(a>=a) # True
print(a!=a) # False

print(b==b) # True
print(b<b) # False
print(b>b) # False
print(b<=b) # True
print(b>=b) # True
print(b!=b) # False

print(a==b) # True
print(a<b) # False
print(a>b) # False
print(a<=b) # True
print(a>=b) # True
print(a!=b) # False

print(b==a) # True
print(b<a) # False
print(b>a) # False
print(b<=a) # True
print(b>=a) # True
print(b!=a) # False

# Test whether a value is true or false using the Boolean conditionals:

# " True, False, and, or, not "

a=True;b=False

print(a and a) # True
print(b and b) # False
print(a and b) # False
print(b and a) # False

print(a and not a) # False
print(b and not b) # False
print(a and not b) # True
print(b and not a) # False

print(a or a) # True
print(b or b) # False
print(a or b) # True
print(b or a) # True

print(a or not a) # True
print(b or not b) # True
print(a or not b) # True
print(b or not a) # False

print(a is a) # True
print(b is b) # True
print(a is b) # False
print(b is a) # False

print(a is not a) # False
print(b is not b) # False
print(a is not b) # True
print(b is not a) # True

# Check to see if a variable contains a value.

numbers=1,2,3,4,5,6,7,8,9,10

print(1 in numbers) # True
print(9 in numbers) # True
print(11 in numbers) # False
print(11 not in numbers) # True
