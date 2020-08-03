'''Character Strings:'''

character_string_example='\nHello World!'

print(character_string_example)

'''
Character stings can be any name, letters or letters combined with numbers, \
starting with a letter first and then a number afterwards. Note: character strings \
must have different, unique names assign to them. Also note: character strings \
cannot contain numbers alone as character strings; a "can't assign to literal" error \
will occur. Character strings must be one, whole word only. Use the underscore key \
to make two or more words. Example: use 'character_string_example', instead of using \
'characterstringexample'. Character strings cannot contain two or more separate words \
with spaces in between them. Example: 'character string example' cannot be used as a \
string, but 'character_string_example' can be used as a string.

Character strings are used to hold important, key data information, which can be used \
over again and again throughout a program's execution/run. Using character strings also \
makes programming code very efficient, without manual redundancy on the programmer's part.
'''
'''Character String Variable Name Change Examples:'''

animal_canine='Fox'
animal_name='Ed'
animal_age='19'

print(f'\n{animal_name} the crazy {animal_canine} is {animal_age} years old.')

animal='Fox'
name='Ed'
age='19'

print(f'\n{name} the crazy {animal} is {age} years old.')

animal1='Fox'
name1='Ed'
age1='19'

print(f'\n{name1} the crazy {animal1} is {age1} years old.')

a='Fox'
n='Ed'
age='19'

print(f'\n{n} the crazy {a} is {age} years old.')

a1a='Fox'
n2n='Ed'
a55a='19'

print(f'\n{n2n} the crazy {a1a} is {a55a} years old.')

'''----------------------------------------------------------------'''

# Replace part of a string's value 'Ed the Fox is great!' with 'Ed the Canine is great!'
# example:

list_string_name='\nEd the Fox is great!'
my_replace_word=list_string_name.replace('Fox','Canine')

print(my_replace_word)

'''----------------------------------------------------------------'''

'''Numeric Strings:'''
'''
Numeric stings can be any name, letters or letters combined with numbers, starting \
with a letter first and then a number afterwards. Numeric strings do not contain quote \
('') marks around the values, like character strings do. Note: numeric strings must have \
different, unique names assign to them. Note: numeric strings cannot contain numbers \
alone as numeric strings; a "can't assign to literal" error will occur. Numeric strings must\
be one, whole word only. Use the underscore key to make two or more words. Example: \
use 'numeric_string_example', instead of using 'numericstringexample'. Numeric strings \
cannot contain two or more separate words with spaces in between them. Example: \
'numeric string example' cannot be used as a string, but 'numeric_string_example' can \
be used as a string.

Numeric strings are used to hold important, key data information, which can be used over \
again and again throughout a program's execution run. Using numeric strings also makes \
programming code very efficient, without manual redundancy on the programmer's part.

Numeric strings do not contain quote ('') marks, because they are not character strings. Numeric \
strings have to be able to do actual calculations throughout a program’s execution run.
'''
'''Numeric String Examples:'''

# BEDMAS! Order of Operation:

# All computers, and computer programs, which involve mathematics dictate the
# order of operation. BEDMAS:

# (Brackets) (Exponents) (Division) (Multiplication) (Addition) (Subtraction)

numeric_string1=3;numeric_string2=5

print(numeric_string1+numeric_string2*2+2)

# 5*2=10, 3+10+2 = 15

print(3+5*2+2)

# 3+10+2 = 15

num1=3
num2=5

print(num1+num2*2+2)

num1=3
num2=5
num3=2

print(num1+num2*num3+num3)

# num2*num3 = 10, num1+num2+num3 = 15

# Numbers can also used within the 'print' statement example as follows:

print('\nAlbert Einstein loves to count to',3+5*2+2,'using the order of operation.')

# New format example of the 'input' 'print' string statement: Note: the (f') format is now
# the standard in Python 3 and up.

num1=3
num2=5
num3=2

print(f'\nAlbert Einstein loves to count to \
{num1+num2*num3+num3} using the order of operation.')

# Non format example of the 'print' numeric string statement:

num1=3
num2=5
num3=2

print('\nAlbert Einstein loves to count to',(num1+num2*num3+num3),
      'using the order of operation.')

# Old format example of the 'print' numeric string statement: Now depreciated in
# Python 3 and up.

num1=3
num2=5
num3=2

print('\nAlbert Einstein loves to count to {} \
using the order of operation.'.format(num1+num2*num3+num3))

'''----------------------------------------------------------------'''

'''String Concatenation:'''
'''
Strings such as character strings and numeric strings can be concatenated or \
joined together, using the comma ',' or the plus sign '+'. Note: string concatenation \
is only needed in non-formatted command statements. However with the 'f' format \
function, there is no need for string concatenation. Consider the following:

numeric_string=2+2*4
character_string='printed text.'

print('Numeric string calculation',
      str(numeric_string),'mixed in with',character_string)
--------------------------------------------------------------------------------------------
numeric_string=2+2*4
character_string='printed text.'

print('Numeric string calculation '
      +str(numeric_string)+' mixed in with '+character_string)
--------------------------------------------------------------------------------------------
numeric_string=2+2*4
character_string='printed text.'

print(f'Numeric string calculation {str(numeric_string)} \
mixed in with {character_string}')
--------------------------------------------------------------------------------------------
numeric_string=2+2*4
character_string='printed text.'

print('Numeric string calculation {} \
mixed in with {}'.format(str(numeric_string),character_string))
--------------------------------------------------------------------------------------------
Notice how the 'f' format function and the old format command statements have no, such \
commas ',' or plus signs '+' needed for string concatenation. Curly braces '{}' are all that \
are needed for string concatenation, which makes it much simpler for the programmer in the long run.
''' 
# Here are some string concatenation program examples to practice with. See what
# happens when you type and execute/run each of these program examples below.

numeric_string=2+2*4
character_string='printed text.'

print('Numeric string calculation '
      +str(numeric_string)+' mixed in with '+character_string)

numeric_string=str(2+2*4)
character_string='printed text.'

print('Numeric string calculation '
      +(numeric_string)+' mixed in with '+character_string)

numeric_string=2+2*4
character_string='printed text.'

print('Numeric string calculation',
      str(numeric_string),'mixed in with',character_string)

numeric_string=str(2+2*4)
character_string='printed text.'

print('Numeric string calculation',
      (numeric_string),'mixed in with',character_string)

numeric_string=2+2*4
character_string='printed text.'

print(f'Numeric string calculation {str(numeric_string)} \
mixed in with {character_string}')

numeric_string=str(2+2*4)
character_string='printed text.'

print(f'Numeric string calculation {numeric_string} \
mixed in with {character_string}')

numeric_string=2+2*4
character_string='printed text.'

print('Numeric string calculation {} \
mixed in with {}'.format(str(numeric_string),character_string))

numeric_string=str(2+2*4)
character_string='printed text.'

print('Numeric string calculation {} \
mixed in with {}'.format(numeric_string,character_string))

'''----------------------------------------------------------------'''

# Let's have some fun with string concatenation. See what happens when you type
# and execute/run these program examples below.

p1=' "Pyt';p2='hon';p3='Pro';p4='gram'
p5="mer's";p6='Glos';p7='sary';p8='Bib';p9='le" '

print(p1+p2,p3+p4+p5,p6+p7,p8+p9,'\nBy Joseph C. Richardson')

'''----------------------------------------------------------------'''

# When commas ',' are used, they act as spaces in between strings. However, when
# plus signs '+' are used, there are no spaces in between strings. When using a plus
# sign '+' it is important to create spaces in the values themselves, example. p3=' Pro'.

p1=' "Pyt';p2='hon';p3=' Pro';p4='gram'
p5="mer's";p6=' Glos';p7='sary';p8=' Bib';p9='le" '

print(p1+p2+p3+p4+p5+p6+p7+p8+p9+'\nBy Joseph C. Richardson')

'''----------------------------------------------------------------'''

'''Tuple String Examples:'''
'''
Tuples are strings that can hold multiple values. Tuples are immutable, meaning they \
cannot be changed or modified once they are created. Tuple values are surrounded with \
round brackets '( )'. Tuple values always start at position '0', then position '1', and so on.
'''
# Example: tuple_string_name=('Position 0','Positon 1','Position 2')

# Tuple string examples are as follows.

# Non format example of the 'print' tuple string:

tuple_string_name=('Super Man','Bat Man','Spider Man')

print('\nMy name is '+(tuple_string_name[0])+' and I\'m a Super Hero.')

print('\nMy name is '+(tuple_string_name[1])+' and I\'m a Super Hero.')

print('\nMy name is '+(tuple_string_name[2])+' and I\'m a Super Hero.')

# New format example of the 'print' tuple string: Note: the (f') format is now the
# standard in Python 3 and up.

tuple_string_name=('Super Man','Bat Man','Spider Man')

print(f'\nMy name is {tuple_string_name[0]} and I\'m a Super Hero.')

print(f'\nMy name is {tuple_string_name[1]} and I\'m a Super Hero.')

print(f'\nMy name is {tuple_string_name[2]} and I\'m a Super Hero.')

# Old format example of the 'print' tuple string: Now depreciated in Python 3 and up.

tuple_string_name=('Super Man','Bat Man','Spider Man')

print('\nMy name is {} and I\'m a Super Hero.'.format(tuple_string_name[0]))

print('\nMy name is {} and I\'m a Super Hero.'.format(tuple_string_name[1]))

print('\nMy name is {} and I\'m a Super Hero.'.format(tuple_string_name[2]))

# Call up individual tuple values with the slice [::] emitter.

tuple_string=('Python','Programmer\'s','Glossary','Bible')

print(f' "{tuple_string[0]} {tuple_string[1]} {tuple_string[2]} {tuple_string[3]}" ')

'''----------------------------------------------------------------'''

# Loop through a tuple string with a for-loop.

tuple_string=('Python','Programmer\'s','Glossary','Bible')
for i in tuple_string:
    print(i)

'''----------------------------------------------------------------'''

# This tuple program example omits the 'min' and 'max' functions for each tuple set:
# 'min_num', and 'max_num'. The 'add_values' variable adds min_num and max_num'
# tuple values together which equals 11.

min_num=min(1,2,3,4,5,6,7,8,9,10)
max_num=max(1,2,3,4,5,6,7,8,9,10)
add_values=min_num+max_num

print(f'Numbers: (1,2,3,4,5,6,7,8,9,10)\n\nMinimum \
number= {min_num}\nMaximum number={max_num}\n\nMinimum \
number pluss maximum number={add_values}')

# Screen output:	Numbers: (1,2,3,4,5,6,7,8,9,10)

# 			Minimum number = 1
# 			Maximum number = 10

# 			Minimum number pluss maximum number = 11

'''----------------------------------------------------------------'''

'''List String Examples:'''
'''
Lists are strings that can hold multiple values. Lists are mutable, meaning they \
can be changed or modified once they are created. List values are surrounded \
with square brackets '[ ]'. List values always start at position '0', then position '1', and so on.
'''
# Example: list_string_name=['Position 0','Positon 1','Position 2']

# List string examples are as follows.

# Non format example of the 'print' list string:

list_string_name=['Super Man','Bat Man','Spider Man']

print('\nMy name is '+(list_string_name[0])+' and I\'m a Super Hero.')

print('\nMy name is '+(list_string_name[1])+' and I\'m a Super Hero.')

print('\nMy name is '+(list_string_name[2])+' and I\'m a Super Hero.')

# New format example of the 'print' list string: Note: the (f') format is now the standard
# in Python 3 and up.

list_string_name=['Super Man','Bat Man','Spider Man']

print(f'\nMy name is {list_string_name[0]} and I\'m a Super Hero.')

print(f'\nMy name is {list_string_name[1]} and I\'m a Super Hero.')

print(f'\nMy name is {list_string_name[2]} and I\'m a Super Hero.')

# Old format example of the 'print' list string: Now depreciated in Python 3 and up.

list_string_name=['Super Man','Bat Man','Spider Man']

print('\nMy name is {} and I\'m a Super Hero.'.format(list_string_name[0]))

print('\nMy name is {} and I\'m a Super Hero.'.format(list_string_name[1]))

print('\nMy name is {} and I\'m a Super Hero.'.format(list_string_name[2]))

# Loop through a list string with a for-loop.

list_string=['Python','Programmer\'s','Glossary','Bible']
for i in list_string:
    print(i)

'''----------------------------------------------------------------'''

'''List String Modification Examples:'''

# A list can always be changed or midified, but a tuple cannot be changed or midified.
# List values are mutable, whereas tuple values are immutable.The extra list value:
# 'Wonder Woman' is now appended or added to the string's name range:
# list_string_name.

list_string_name=['Super Man','Bat Man','Spider Man']
list_string_name.append('Wonder Woman')

print(f'\nMy name is {list_string_name[2]} and I\'m a Super Hero.')

'''----------------------------------------------------------------'''

# The inserted list value: 'The Tick' is now at position '0' where the list value: 'Super
# Man' was. The list value: 'Super Man' got moved from positon'0' into positon '1'
# instead.

list_string_name=['Super Man','Bat Man','Spider Man']
list_string_name.insert(0,'The Tick')

print(f'\nMy name is {list_string_name[1]} and I\'m a Super Hero.')

'''----------------------------------------------------------------'''

# The removed list value: 'Spider Man' is gone from the string's name range:
# list_string_name. Position '0', and position '1' are all that is left in the string's name
# range: list_string_name.

list_string_name=['Super Man','Bat Man','Spider Man']
list_string_name.remove('Spider Man')

print(f'\nMy name is {list_string_name[1]} and I\'m a Super Hero.')

'''----------------------------------------------------------------'''

# The popped list value: 'Super Man' at position '0' is now 'Bat Man' at position '0',
# where the value 'Super Man' was.

list_string_name=['Super Man','Bat Man','Spider Man']
list_string_name.pop(0)

print(f'\nMy name is {list_string_name[0]} and I\'m a Super Hero.')

'''----------------------------------------------------------------'''

# The sort list values: 'Super Man','Bat Man','Spider Man' get reversed as list values:
# 'Super Man','Spinder Man','Bat Man'. The sort list value 'Super Man' remains at
# position '0', while the other two values get reversed positions.

list_string_name=['Super Man','Bat Man','Spider Man']
list_string_name.sort(reverse=True)

print(f'\nMy name is {list_string_name[1]} and I\'m a Super Hero.')

'''----------------------------------------------------------------'''

# Note: the sorted list program example below only returns a preview of what the list
# would look like if it was sorted; it doesn't modify or change the actual characteristics
# of the list.

sorted(list_string_name)
print(list_string_name)

'''----------------------------------------------------------------'''

'''Two Dimensional List Examples:'''

# A two dimensional list is simply a list within another list. For example, a one
# dimensional list looks like this:

my_1d_list=['value 1','value 2']

# A two dimensional list looks like this:

my_2d_list=[
    ['value 1','value 2'],['value 3','value 4']
    ]

'''----------------------------------------------------------------'''

# A two dimensional list can hold as many list value blocks as one sees fit. For
# example: the my_2d_list variable has three list value blocks in it.

my_2d_list=[
    ['value 1','value 2'],['value 3','value 4'],['value 5','value 6']
    ]

# A two dimensional list can be numeric values as well as character values. Example:

my_2d_list=[
    [1,2],[3,4]
    ]

'''----------------------------------------------------------------'''

# Display a two dimensional list's character values to check them.

my_2d_list=[
    ['value 1','value 2'],['value 3','value 4']
    ]

print(my_2d_list)

# Screen output:	[['value 1', 'value 2'], ['value 3', 'value 4']]

'''----------------------------------------------------------------'''

# Display a two dimensional list's numeric values to check them.

my_2d_list=[
    [1,2],[3,4]
    ]

print(my_2d_list)

# Screen output:	[[1, 2], [3, 4]]

'''----------------------------------------------------------------'''

# Display a two dimensional list's character value pair to check them.

my_2d_list=[
    ['value 1','value 2'],['value 3','value 4']
    ]

print(my_2d_list[0])

# Screen output:	['value 1', 'value 2']

my_2d_list=[
    ['value 1','value 2'],['value 3','value 4']
    ]

print(my_2d_list[1])

# Screen output:	['value 3', 'value 4']

'''----------------------------------------------------------------'''

# Display a two dimensional list's numeric value pair to check them.

my_2d_list=[
    [1,2],[3,4]
    ]

print(my_2d_list[0])

# Screen output:	[1, 2]

my_2d_list=[
    [1,2],[3,4]
    ]

print(my_2d_list[1])

# Screen output:	[3, 4]

'''----------------------------------------------------------------'''

# Display a single character value from a two dimensional list. Examples:

my_2d_list=[
    ['value 1','value 2'],['value 3','value 4']
    ]

print(my_2d_list[0][0])

# Screen output:	value 1

my_2d_list=[
    ['value 1','value 2'],['value 3','value 4']
    ]

print(my_2d_list[1][0])

# Screen output:	value 3

my_2d_list=[
    ['value 1','value 2'],['value 3','value 4']
    ]

print(my_2d_list[0][1])

# Screen output:	value 2

my_2d_list=[
    ['value 1','value 2'],['value 3','value 4']
    ]

print(my_2d_list[1][1])

# Screen output:	value 4

'''----------------------------------------------------------------'''

# Display a single numeric value from a two dimensional list. Examples:

my_2d_list=[
    [1,2],[3,4]
    ]

print(my_2d_list[0][0])

# Screen output:	1

my_2d_list=[
    [1,2],[3,4]
    ]

print(my_2d_list[1][0])

# Screen output:	3

my_2d_list=[
    [1,2],[3,4]
    ]

print(my_2d_list[0][1])

# Screen output:	2

my_2d_list=[
    [1,2],[3,4]
    ]

print(my_2d_list[1][1])

# Screen output:	4

'''----------------------------------------------------------------'''

# Create a multiple two dimensional list, using letter and number values. Create a
# simple 'print' program example, which will use a two dimensional list.

name=[
     ['Tomy','Brian','Jim','Paul'],
     ['Mary','Terry','Jane','Patty'],
     [0,1,2,35,4,5,6,7,8,9],
     ['Dog','Cat','Bird','Fish']
     ]

print(f'My name is {name[0][0]} I am {name[2][3]} years old.')

print(f'I have a {name[3][0]}. My Sister {name[1][3]} wants a {name[3][2]}.')

print(f'{name[1][0]} loves {name[3][3]} so much. But {name[0][1]} \
wants a {name[3][1]} instead.')

'''----------------------------------------------------------------'''

'''Multiple String Variables and Multiple String Values Examples:'''
'''
Multiple tuple string variables and multiple tuple values can be stored right inside \
one, single 'print' statement. Note: multiple tuple strings and multiple tuple values \
must be the same; four tuple strings equals four tuple values. Also note that multiple \
tuple stings and multiple tuple values are always in the order they are given. For \
example, string (a) is always equal to the string value 'Andy' and string (b) is always \
equal to the string value 'Bob' and so on.
'''
# Multiple tuple string variables and multiple tuple values example:

a,b,c,d=('Andy','Bob','Chris','Dave')

print(a,b,c,d)

print(d,c,b,a)

print(c,b,a,d)

'''----------------------------------------------------------------'''

# The 'len' function is excellent at keeping track of how many tuple values or list values
# there are. Checking to see how many values there are in a tuple or list makes
# programming much more efficient, while the 'len' fuction checks exactly how many
# values there are. The printout on the screen will only show the number "8", not the
# actual tuple values or list values.

tuple_len=(
     'Value 0','Value 1',
     'Value 2','Value 3',
     'Value 4','Value 5',
     'Value 6','Value 7'
     )

print(len(tuple_len))

list_len=[
    'Value 0','Value 1',
    'Value 2','Value 3',
    'Value 4','Value 5',
    'Value 6','Value 7'
    ]

print(len(list_len))

'''----------------------------------------------------------------'''

'''Dictionary Examples:'''
'''
Dictionaries are like lists, but they hold "key" values that point to other values in the list. \
For example: the key value "animal" points to the list value "canine", and the key value "name" \
points to the list value "Mogie". The key value "age" points to the list value "13", and the key value \
"kind" points to the value "Husky/Chow mix". Lastly, the key value "colour" points to the list value \
"gold". Think of dictionaries as lists on heavy steroids. Dictionary values are surrounded with curly \
braces '{ }', which are also surrounded with round brackets '({ })'. Note: you can leave out the round \
brackets '()' if you like.
'''
# Type and execute/run this 'dictionary_list' dictionary program example:

dictionary_list=(
     {'animal':'canine',
      'name':'Mogie','age':13,
      'kind':'Husky/Chow mix',
      'colour':'gold'}
     )

print(dictionary_list['animal'])

print(dictionary_list['name'])

print(dictionary_list['age'])

print(dictionary_list['kind'])

print(dictionary_list['colour'])

'''----------------------------------------------------------------'''

# Update the dictionary_list values with the '.update' statement followed by the new
# dictionary_list:

# dictionary_list.update({'animal':'monkey','name':'Cheetah',
# 'age':20,'kind':'Chimpanzee','colour':'brown'})

dictionary_list=(
     {'animal':'canine','name':'Mogie','age':13,
      'kind':'Husky/Chow mix','colour':'gold'}
     )

dictionary_list.update(
     {'animal':'monkey','name':'Cheetah','age':20,'kind':'Chimpanzee','colour':'brown'}
     )

print(dictionary_list['animal'])

print(dictionary_list['name'])

print(dictionary_list['age'])

print(dictionary_list['colour'])

'''----------------------------------------------------------------'''

# This dictionary_list example illustrates how key values can point to multiple values,
# denoted by square brackets '[ ]' around the list value groups. For example: the key
# value 'Animals' has four list values assigned to it instead of just one list value, such
# as in the dictionary_list program example above illustrates.

dictionary_list=(
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

print(dictionary_list['Animals'][0])
print(dictionary_list['Animals'][1])
print(dictionary_list['Animals'][2])
print(dictionary_list['Animals'][3])

print(dictionary_list['Reptiles'][0])
print(dictionary_list['Reptiles'][1])
print(dictionary_list['Reptiles'][2])
print(dictionary_list['Reptiles'][3])

print(dictionary_list['Insects'][0])
print(dictionary_list['Insects'][1])
print(dictionary_list['Insects'][2])
print(dictionary_list['Insects'][3])

'''----------------------------------------------------------------'''

# Update the dictionary_list values with the '.update' statement followed by the new
# dictionary_list:

# dictionary_list.update({'Animals':['Wolf','Lion','Bat','Shark'],'
# Reptiles':['Tortoise','Alligator','Python','Toad'],'Insects':
# ['Moth','Cricket','Fly','Wasp']})

dictionary_list=(
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

dictionary_list.update(
     {'Animals':['Wolf','Lion','Bat','Shark'],'Reptiles':['Tortoise','Alligator','Python','Toad'],
      'Insects':['Moth','Cricket','Fly','Wasp']}
     )

print(dictionary_list['Animals'][0])
print(dictionary_list['Animals'][1])
print(dictionary_list['Animals'][2])
print(dictionary_list['Animals'][3])

print(dictionary_list['Reptiles'][0])
print(dictionary_list['Reptiles'][1])
print(dictionary_list['Reptiles'][2])
print(dictionary_list['Reptiles'][3])

print(dictionary_list['Insects'][0])
print(dictionary_list['Insects'][1])
print(dictionary_list['Insects'][2])
print(dictionary_list['Insects'][3])

'''----------------------------------------------------------------'''

# Display the dictionary key values to check them.

dictionary_list=(
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

print(dictionary_list.keys())

# Screen output:	dict_keys(['Animals', 'Reptiles', 'Insects'])

'''----------------------------------------------------------------'''

# Display the dictionary list values to check them.

dictionary_list=(
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

print(dictionary_list.values())

# Screen output:	dict_values([['Dog', 'Cat', 'Bird', 'Fish'], ['Turtle',
# 'Lizard','Snake', 'Frog'], ['Butterfly', 'Beetle', 'Ant', 'Bee']])

'''----------------------------------------------------------------'''

# Delete a dictionary key value and check it.

dictionary_list=(
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

del dictionary_list['Animals']

print(dictionary_list.keys())

# Screen output:	dict_keys(['Reptiles', 'Insects'])

'''----------------------------------------------------------------'''

# Delete a dictionary list value and check it.

dictionary_list=(
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

del dictionary_list['Animals'][0]

print(dictionary_list.values())

# Screen output:	dict_values([['Cat', 'Bird', 'Fish'], ['Turtle', 'Lizard',
# 'Snake', 'Frog'], ['Butterfly', 'Beetle', 'Ant', 'Bee']])

'''----------------------------------------------------------------'''

# Pop a dictionary key value and check it. The key value "Animals" is not deleted, but
# it's no longer in the dictionary list. However, it is returnable.

dictionary_list=(
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

pop_key=dictionary_list.pop('Animals')

print(dictionary_list.keys())

print(pop_key)

# Screen output:	dict_keys(['Reptiles', 'Insects'])

# Screen output:	['Dog', 'Cat', 'Bird', 'Fish']

'''----------------------------------------------------------------'''

# Display the length of dictionary key values to check them.

dictionary_list=(
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

print(len(dictionary_list))

print(dictionary_list.keys())

# Screen output:	3

# Screen output:	dict_keys(['Animals', 'Reptiles', 'Insects'])

'''----------------------------------------------------------------'''

# Display the length of dictionary list values to check them.

dictionary_list=(
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

print(len(dictionary_list['Animals']))

print(dictionary_list.values())

# Screen output:	4

# Screen output:	dict_values([['Dog', 'Cat', 'Bird', 'Fish'], ['Turtle',
# 'Lizard', 'Snake', 'Frog'], ['Butterfly', 'Beetle', 'Ant', 'Bee']])

'''----------------------------------------------------------------'''

# To add a new dictionary key value, simply use ['Set Key name example']='New Value'
# to display the length of dictionary list key values to check them. Note: one dictionary
# value must be created along with setting a new dictonary key value.

dictionary_list=(
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

dictionary_list['Fish']='Angelfish'

print(len(dictionary_list.keys()))

print(dictionary_list.keys())

# Screen output:	4

# Screen output:	dict_keys(['Animals', 'Reptiles', 'Insects', 'Fish'])

'''----------------------------------------------------------------'''

# To add new dictionary values, simply use ['Set Key name example']='Value','New
# Value','New Value',New Value' Display the length of dictionary list values to check
# them. Note: a dictionary key value must be [set] first, then add the new dictionary
# values.

dictionary_list=(
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

dictionary_list['Fish']='Angelfish','Devilfish','Catfish','Dogfish'

print(len(dictionary_list.values()))

print(dictionary_list.values())

# Screen output:	4

# Screen output:	dict_values([['Dog', 'Cat', 'Bird', 'Fish'], ['Turtle', 
# 'Lizard', 'Snake', 'Frog'], ['Butterfly', 'Beetle', 'Ant', 'Bee'], ('Angelfish', 
# 'Devilfish', 'Catfish', 'Dogfish')])

'''----------------------------------------------------------------'''

# To look for a dictionary key value, simply use the '.get' method to search for it.
# Display the dictionary key values to check them.

dictionary_list=(
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

print(dictionary_list.get('Fish'))

# Screen output:	None

# The screen output says None. However, by adding 'Not Found!' the screen output
# now looks like this:

dictionary_list=(
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

print(dictionary_list.get('Fish','Not Found!'))

# Screen output:	Not Found!

'''----------------------------------------------------------------'''

# This time, let's look for an actual key value and check it, using the 'get' methond. The
# screen output now looks like this:

dictionary_list=(
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

print(dictionary_list.get('Animals'))

# Screen output:	['Dog', 'Cat', 'Bird', 'Fish']
