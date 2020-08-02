'''Print Statement Examples:'''
'''
Print statement values are encased with round brackets '()' on each end of the 'print' statement's value. \
Quotation marks (" ") denote what kind of 'print' statement value it is. If the value is a string, then no \
quotation marks are used inside the 'print' statement's value. However, quotation marks are used within the \
'print' statement's string value instead. Note: double quotation marks (" ") or single quotation marks (' ') \
can be used in 'print' statements, string values, tuples and lists alike. If the value is not a string, then \
quotation marks are used inside the 'print' statement's value itself, such as these two 'print' statement examples below.
'''
# Print statement examples:

# Double Quotation marks (" ")

print("Hello World!")

# Single Quotation marks (' ')
 
print('Hello World!') 

# Print statement string examples:

# Double Quotation marks (" ")

my_string_example="Hello World!"

print(my_string_example)

# Single Quotation marks (' ')

my_string_example='Hello World!'

print(my_string_example)

'''Fancy Print Statement Examples:'''
'''
All 'print' statements and all 'input' statements also support the '\n' line-break implementer, which acts like a normal \
line-break in between sentences. The '\n' line-break implementer can also be implemented into string values, tuple values \
and list values alike. From here on, the '\n' line-break implementer will be implemented into all 'print' statements, \
'input' statements, string values, tuple values and list values. The '\n' line-break implementer makes the screen printout \
much more cleaner and nicer looking with actual line-breaks in between sentences. Note: two '\n\n' or more '\n\n\n' \
line-break implementers can be implemented at once within a single 'print' statement.
'''
# Here are some 'print' statement examlples of the '\n' line-break implementer.

print('\nHello World!')

print('\n\nHello World!')

print('\n\n\nHello World!')

print('\n\n\n\nHello World!')

print('Hello world!\nHello world!\nHello world!\nHello world!')

# The upper() fuction turns the words 'hello world!' into the words 'HELLO WORLD!'
# example:

print('\nhello world!'.upper())

# The title() function turns the words 'hello world!' into the words 'Hello World!'
# example:

print('\nhello world!'.title())

# The lower() function turns the words 'HELLO WORLD!' into the words 'hello world!'
# example:

print('\nHELLO WORLD!'.lower())

# Make 'print' statement values in reverse by omitting the slice '[::]' emitter.

print('\nHello World!'[::-1])

'''----------------------------------------------------------------'''

# Try these 'print' statement value in reverse program examples, while using other
# combined functions.

print('\nhello world!'[::-1].upper())

print('\nhello world!'[::-1].title())

print('\nHELLO WORLD!'[::-1].lower())

# The slice [::] emitter can be omitted into tuples, lists, dictionaries and 'print'
# statements, such as in these 'print' statement program examples:

# The slice [::] emitter takes one to three positive or negative values. The 'print'
# statement's string value 'HELLO WORLD!' is sliced. When slicing a 'print' statement's
# string value, the values can be sliced from left to right, or from right to left. For
# example, the 'print' string value 'HELLO WORLD!' looks like these sliced 'print' string
# value examples:

#	0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
#	H,E,L,L,O, ,W,O,L,R,D,!

#	-12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1
#	H,E,L,L,O, ,W,O,L,R,D,!

# [ start value : end value : step value ]

# Note: step values must start at 1 not 0

# empty slice: no values

print('HELLO WORLD!'[:]) 

# Screen output:	HELLO WORLD!

# slice start value 0

print('HELLO WORLD!'[0:]) 

# Screen output:	HELLO WORLD!

# slice end value -1

print('HELLO WORLD! '[:-1]) 

# Screen output:	HELLO WORLD!

# slice start and slice end values 1 and -2

print('HELLO WORLD! '[1:-2])

# Screen output:	ELLO WORLD

# slice start, slice end and slice step 2

print('HELLO WORLD!'[0:-1:2])

# Screen output:	HLOWRD

'''----------------------------------------------------------------'''

# In this example, the start and end slice emitter values are positive. Notice how the
# screen output shows 'HE'.

# slice start and slice end values 0 and 2

print('HELLO WORLD! '[0:2])

# Screen output:	HE

'''----------------------------------------------------------------'''

# In this example, the start and end slice emitter values are negative. Notice how the
# screen output shows 'D!'.

# slice start and slice end values -3 and -1

print('HELLO WORLD! '[-3:-1])

# Screen output:	D!    

# Make this 'print' statement print 'Hello World!' 3 times.

print('Hello World! '*3)

'''----------------------------------------------------------------'''

# Make this 'print' statement print 'Hello World!' go in the top, middle of the screen.
# Note: use an emty space in between the single quotation marks (' '*45)

print(' '*45+'Hello World!')

# Try these 'print' statement program examples:

print('Hello World! '*3+'Python')

print('Python '*3+'Hello World!')

print('Python '*45+'Hello World!')

print('Python '*45)

# The 'len' function counts how many characters, including spaces there are inside of 
# a 'print' statement. The length of these two words "Hello World!", including the
# space in between 'Hello' and 'World!' are counted. For example: "Hello World!"
# including one space is twelve characters long. The printout on the screen will only
# show the number "12", not the actual words "Hello World!".

print(len('Hello World!'))
