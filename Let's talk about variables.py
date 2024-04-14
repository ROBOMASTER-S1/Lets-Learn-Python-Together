# Created and written by Joseph C. Richardson, GitHub.com
'''
Let's talk about variables for a moment. What are variables? Variables are letters or
a bunch of letters that can make short words, for example 'c' can equal the value 'cat'
or 'cat' can equal the value 'catfish' if you like. You can create variable names of any
choice you like. However, by programming standards, variables are not capitalized.
but you can capitalize them if you want, or make them all capitalized if you like. But
as a programming standard, you do not capitalize variables. What are variables used
for, you ask? Variables save time and energy on the programmer's part. Let's say you
do a whole bunch of print() functions, but you got someone's name wrong. Without
variables, you would have to manually make sure you corrected that mistake in some-
-one's name, which would be a huge nightmare. Variables also make programming less
redundant on the programmer's part. Here are what you can do with variables.
'''
print('Hello Tommy. How are you?') # no variables at all.

name = 'Tommy'

print(f'Hello {name}. How are you?') # with a variable called 'name'

# Since Python 3 and up uses the formatted f' string, we will use this f' format to make
# string concatenation much, much easier. Here is the old way, I once had to use.

print('Hello {}. How are you?'.format(name)) # old formatted string example before Python 3

# Another great use for using variables is with numbers. For example:

num1 = 3
num2 = 4

print(num1 + num2)
print(num2 - num1)
print(num1 * num2)
print(num2 / num1)

# The new f' format string examples:

print(f'I love to add numbers {num1 + num2}')
print(f'I love to subtract numbers {num2 - num1}')
print(f'I love to multiply numbers {num1 * num2}')
print(f'I love to divide numbers {num2 / num1}')

# The old format string examples:

print('I love to add numbers {}'.format(num1 + num2))
print('I love to subtract numbers {}'.format(num2 - num1))
print('I love to multiply numbers {}'.format(num1 * num2))
print('I love to divide numbers {}'.format(num2 / num1))

# Let's do some more string concatenation, using a person's name and numbers

name = 'Tommy'
num1 = 3
num2 = 4

# The new f' format string examples:

print(f'{name} loves to add numbers {num1 + num2}')
print(f'{name} loves to subtract numbers {num2 - num1}')
print(f'{name} loves to multiply numbers {num1 * num2}')
print(f'{name} loves to divide numbers {num2 / num1}')

# The old format string examples:

print('{} loves to add numbers {}'.format(name,num1 + num2))
print('{} loves to subtract numbers {}'.format(name,num2 - num1))
print('{} loves to multiply numbers {}'.format(name,num1 * num2))
print('{} loves to divide numbers {}'.format(name,num2 / num1))

# Let's pack variables with their packed values, using just one equals = sign.

name,num1,num2 = 'Tommy',3,4

# The new f' format string examples:

print(f'{name} loves to add numbers {num1 + num2}')
print(f'{name} loves to subtract numbers {num2 - num1}')
print(f'{name} loves to multiply numbers {num1 * num2}')
print(f'{name} loves to divide numbers {num2 / num1}')

# The old format string examples:

print('{} loves to add numbers {}'.format(name,num1 + num2))
print('{} loves to subtract numbers {}'.format(name,num2 - num1))
print('{} loves to multiply numbers {}'.format(name,num1 * num2))
print('{} loves to divide numbers {}'.format(name,num2 / num1))

'''
Now, let's ratchet things up a bit and do some non formatted string examples. These non
formatted string examples evolve some fancy footwork on the programmer's part. Note:
you do not need to use such things, but they were all I had when I first started Python
programming, when I didn't want to use the old formatted string examples. Let's now set
up our variables and our values. The 'str()' function means string function; please keep
this in mind. The str() function helps to create string concatenation in non formatted text
strings. Because string variables and numeric variables do not get along at all; they fight
like cats and dogs. So the str() function makes them get along not matter what! When I
show how to use the '+' sign to concatenate strings together, instead of using a comma ','
you will see why we will need the 'str()' function.
'''
num1 = 3
num2 = 4

# The non format string examples:

print('I love to add numbers',num1 + num2)
print('I love to subtract numbers',num2 - num1)
print('I love to multiply numbers',num1 * num2)
print('I love to divide numbers',num2 / num1)

# Let's add a name variable to our non formatted string examples

name = 'Tommy'
num1 = 3
num2 = 4

# The non format string examples:

print(name,'loves to add numbers',num1 + num2)
print(name,'loves to subtract numbers',num2 - num1)
print(name,'loves to multiply numbers',num1 * num2)
print(name,'loves to divide numbers',num2 / num1)

# Let's pack variables with their packed values, using just one equals = sign.

name,num1,num2 = 'Tommy',3,4

# The non format string examples:

print(name,'loves to add numbers',num1 + num2)
print(name,'loves to subtract numbers',num2 - num1)
print(name,'loves to multiply numbers',num1 * num2)
print(name,'loves to divide numbers',num2 / num1)

# Let's place sentences inside a list[ ] and then concatenate its variable indexes[x]

name = 'Tommy'
num1 = 3
num2 = 4

my_sentences = [
    'loves to add numbers',
    'loves to subtract numbers',
    'loves to multiply numbers',
    'loves to divide numbers'
    ]

# The non format string examples:

print(name,my_sentences[0],num1 + num2)
print(name,my_sentences[1],num2 - num1)
print(name,my_sentences[2],num1 * num2)
print(name,my_sentences[3],num2 / num1)

# Let's pack variables with their packed values, using just one equals = sign.

name,num1,num2 = 'Tommy',3,4

my_sentences = [
    'loves to add numbers',
    'loves to subtract numbers',
    'loves to multiply numbers',
    'loves to divide numbers'
    ]

# The non format string examples:

print(name,my_sentences[0],num1 + num2)
print(name,my_sentences[1],num2 - num1)
print(name,my_sentences[2],num1 * num2)
print(name,my_sentences[3],num2 / num1)

# Now, let's use the much needed 'str() function. We will need this while using the '+' sign
# instead of a comma ','

num1 = 3
num2 = 4

# The non format string examples:

print('I love to add numbers '+str(num1 + num2))
print('I love to subtract numbers '+str(num2 - num1))
print('I love to multiply numbers '+str(num1 * num2))
print('I love to divide numbers '+str(num2 / num1))

# Let's add a name variable to our non formatted string examples

name = 'Tommy'
num1 = 3
num2 = 4

# The non format string examples:

print(name+' loves to add numbers '+str(num1 + num2))
print(name+' loves to subtract numbers '+str(num2 - num1))
print(name+' loves to multiply numbers '+str(num1 * num2))
print(name+' loves to divide numbers '+str(num2 / num1))

# Let's pack variables with their packed values, using just one equals = sign.

name,num1,num2 = 'Tommy',3,4

# The non format string examples:

print(name+' loves to add numbers '+str(num1 + num2))
print(name+' loves to subtract numbers '+str(num2 - num1))
print(name+' loves to multiply numbers '+str(num1 * num2))
print(name+' loves to divide numbers '+str(num2 / num1))

# Let's place sentences inside a list[ ] and then concatenate its variable indexes[x]

name = 'Tommy'
num1 = 3
num2 = 4

my_sentences = [
    ' loves to add numbers ',
    ' loves to subtract numbers ',
    ' loves to multiply numbers ',
    ' loves to divide numbers '
    ]

# The non format string examples:

print(name+my_sentences[0]+str(num1 + num2))
print(name+my_sentences[1]+str(num2 - num1))
print(name+my_sentences[2]+str(num1 * num2))
print(name+my_sentences[3]+str(num2 / num1))

# Let's pack variables with their packed values, using just one equals = sign.

name,num1,num2 = 'Tommy',3,4

my_sentences = [
    ' loves to add numbers ',
    ' loves to subtract numbers ',
    ' loves to multiply numbers ',
    ' loves to divide numbers '
    ]

# The non format string examples:

print(name+my_sentences[0]+str(num1 + num2))
print(name+my_sentences[1]+str(num2 - num1))
print(name+my_sentences[2]+str(num1 * num2))
print(name+my_sentences[3]+str(num2 / num1))
'''
Here is where variables truly shine. Let's use a variable to condense our print()
funtion to only one, using a for loop to loop through a list[ ] of names of people,
along with the words '. How are you?'. Remember the plus '+' sign is also used
for string concatenation, instead of using a comma ',' that creates a space, which
is something you don't always want. If you need a space, but don't want to make
two spaces, you must add a space within your 'text' as shown in the example
below. Now you know just how vital variables are in computer programming as a
whole. Because without them, we would have to do a lot of manual redundant
programming on our part. And that would be a total drag. Wouldn't it?
'''
names = ['Ron','Bob','Tom','John','Mandy','Sandy']

for i in names:
    print('Hello',i+'. How are you?')
