# Character Strings:

character_string_example='\nHello World!'

print(character_string_example)

'''
Character stings can be any name, letters or letters combined with numbers, \
starting with a letter first and then a number afterwards. Note: character strings \
must have different, unique names assign to them. Also note: character strings \
cannot contain numbers alone as character strings; a "can't assign to literal" \
error will occur. Character strings must be one, whole word only. Use the underscore \
key to make two or more words. Example: use 'character_string_example', instead \
of using 'characterstringexample'. Character strings cannot contain two or more \
separate words with spaces in between them. Example: 'character string example' \
cannot be used as a string, but 'character_string_example' can be used as a string.

Character strings are used to hold important, key data information, which can be used \
over again and again throughout a program's execution/run. Using character strings \
also makes programming code very efficient, without manual redundancy on the \
programmer's part.
'''
# Character String Variable Name Change Examples:

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

# Replace part of a string's value 'Ed the Fox is great!' with 'Ed the Canine is great!'
# example:

list_string_name='\nEd the Fox is great!'
my_replace_word=list_string_name.replace('Fox','Canine')

print(my_replace_word)

'''----------------------------------------------------------------'''

# Numeric Strings:
'''
Numeric stings can be any name, letters or letters combined with numbers, starting \
with a letter first and then a number afterwards. Numeric strings do not contain quote \
('') marks around the values, like character strings do. Note: numeric strings must have \
different, unique names assign to them. Note: numeric strings cannot contain numbers \
alone as numeric strings; a "can't assign to literal" error will occur. Numeric strings \
must be one, whole word only. Use the underscore key to make two or more words. \
Example: use 'numeric_string_example', instead of using 'numericstringexample'. \
Numeric strings cannot contain two or more separate words with spaces in between \
them. Example: 'numeric string example' cannot be used as a string, \
but 'numeric_string_example' can be used as a string.

Numeric strings are used to hold important, key data information, which can be used \
over again and again throughout a program's execution run. Using numeric strings also \
makes programming code very efficient, without manual redundancy on the programmer's part.

Numeric strings do not contain quote ('') marks, because they are not character strings. \
Numeric strings have to be able to do actual calculations throughout a program’s execution run.
'''
# Numeric String Examples:

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

# String Concatenation:
'''
Strings such as character strings and numeric strings can be concatenated or joined \
together, using the comma ',' or the plus sign '+'. Note: string concatenation is only \
needed in non-formatted command statements. However with the 'f' format function, \
there is no need for string concatenation. Consider the following:

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
Notice how the 'f' format function and the old format command statements have no,\
such commas ',' or plus signs '+' needed for string concatenation. Curly braces '{}' \
are all that are needed for string concatenation, which makes it much simpler for \
the programmer in the long run.
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

# When commas ',' are used, they act as spaces in between strings. However, when
# plus signs '+' are used, there are no spaces in between strings. When using a plus
# sign '+' it is important to create spaces in the values themselves, example. p3=' Pro'.

p1=' "Pyt';p2='hon';p3=' Pro';p4='gram'
p5="mer's";p6=' Glos';p7='sary';p8=' Bib';p9='le" '

print(p1+p2+p3+p4+p5+p6+p7+p8+p9+'\nBy Joseph C. Richardson')
