import random

# This is a continuation of the use of def fuctions(). We are doing
# the very same things we did before, but we are now going to
# create a for loop that will iterate all through the tuple() indexes
# instead of calling each one at a time by human hand. Let's use
# a for loop to make things happen, without the help of human hands.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_tuple = (function_one,function_two,function_three)

for i in my_functions_tuple:
    i()  
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same thing, but with a list[].

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_list = [function_one,function_two,function_three]

for i in my_functions_list:
    i()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same thing, but with a dictionary{}.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_dictionary = {1:function_one,2:function_two,3:function_three}

for i in my_functions_dictionary:
    my_functions_dictionary.get(i)()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same thing, using a casting tuple() function with a set{}.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_set = {function_one,function_two,function_three}

my_cast = tuple(my_functions_set) # use the casting tuple function

for i in my_cast:
    i()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same thing, using a casting list() function with a set{}.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_set = {function_one,function_two,function_three}

my_cast = list(my_functions_set) # use the casting tuple function

for i in my_cast:
    i()
input()

# I use def functions() most of the time. These are used for either
# calling code through them, or they can be used as simple subroutines.
# You can also use them within lists, which is what these Python
# program examples shows. You can create a list[] of function
# calls, a tuple() a dictionary{} and a set{}. Note: sets{} do not use
# indexing like tuples and lists do. Sets{} only get rid of duplicate
# values, whereas lists[], tuples and dictionaries don't. We learn
# all of the above with these Python program def functions() examples.

# Let's create three def functions() called 'function_one', 'function_two'
# and 'function_three'.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

# Let's call each def function, one by one so we can see what's going on.
# To call a function, you have to call it like this:

function_one()     # do not use the colon : to call functions

function_two()     # do not use the colon : to call functions

function_three()  # do not use the colon : to call functions
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's try placing these same functions inside a tuple().
# Remember that tuples and lists always start at index[0].

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_tuple = (function_one,function_two,function_three)

my_functions_tuple[0]()  # index[0] is function_one

my_functions_tuple[1]()  # index[1] is function_two

my_functions_tuple[2]()  # index[2] is function_three

# When calling up a function through a tuple(), do not include the () parentheses
# right after the function call. The () parentheses go at the very end of the index[]()
# box: my_functions_tuple[0](). Now, let's move onto using def functions() within
# a list[], which is similar to a tuple(). But tuples() are not mutible, wheras lists[]
# are mutible, meaning they can be changed or modified; tuples cannot be
# changed or modified at all, meaning they are not mutible.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's try placing these same functions inside a list[].
# Remember that tuples and lists always start at index[0].

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_list = [function_one,function_two,function_three]

my_functions_list[0]()  # index[0] is function_one

my_functions_list[1]()  # index[1] is function_two

my_functions_list[2]()  # index[2] is function_three

# When calling up a function through a list[], do not include the () parentheses
# right after the function call. The () parentheses go at the very end of the index[]()
# box: my_functions_list[0](). Now, let's move onto using def functions() within
# a dictionary{} of values.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's try placing these same functions inside a dictionary{}.
# The dictionary 'keys' will be numbers or text if you like. But we are going to
# use numbers for the 'key's and make the values be the names of the functions
# we are using so the 'keys' will '.get' each of the values we call up, within our
# dictionary{}.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_dictionary = {1:function_one,2:function_two,3:function_three}

my_functions_dictionary.get(1)()  # "I'm Function One."

my_functions_dictionary.get(2)()  # "I'm Function Two."

my_functions_dictionary.get(3)()  # "I'm Function Three"

# When calling up a function through a dictionary{}, do not include the () parentheses
# right after the function call. The () parentheses go at the very end of the .get(n)(),
# my_functions_dictionary.get(1)(). Now, let's move onto using def functions() within
# a set of values. Note: sets{} get rid of duplicate values. They will also be in random
# order when using text values, instead of number values. Set{} do not produce
# output directly onto the screen at execute/run time. Instead you have to cast the
# values to a built-in tuple(), a built-in list() or a built-in dict() function.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's try placing these same functions inside a set{} in which we have to
# cast into a tuple() function, a list() function or a dict() function. We are only
# going to cast the set into a tuple() and a list() function for now.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_set = {function_one,function_two,function_three}

my_cast = tuple(my_functions_set)

my_cast[0]()

my_cast[1]()

my_cast[2]()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
my_functions_set = {function_one,function_two,function_three}

my_cast = list(my_functions_set)

my_cast[0]()

my_cast[1]()

my_cast[2]()

# Use the := Walrus Operator to create the following Python prgram
# examples, using tuples(), lists[] and dictionaries{}.

if my_tuple := (
    'Value 0','Value 1','Value 2',
    'Value 3','Value 4','Value 5'):pass

for value in my_tuple:print(value)

if my_list := [
    'Value 0','Value 1','Value 2',
    'Value 3','Value 4','Value 5']:pass

for value in my_list:print(value)

if my_dictionary := {
    1:'Value 1',2:'Value 2',3:'Value 3',
    4:'Value 4',5:'Value 5',6:'Value 6'}:pass

for value in my_dictionary:print(
    my_dictionary.get(value+1,f"There are no more values to loop \
through after 'Value {value}'."))

input()

# Look what you can do with Python's print() function.

# Use three single ''' quotes to make string concatenation much easier
# and much more text oriented.

print('''That's 'GREAT' to "TRIPPLE QUOTES" ''')

# Use three double " quotes to make string concatenation much easier
# and much more text oriented.

print("""That's 'GREAT' to "TRIPPLE QUOTES" """)

# Use Python's Error Handlers to not only stop errors from occurring.
# But you can also use Error Handlers to manipulate Python code flow
# of control. As you may notice, I used the walrus := operator to write
# less lines of code. Play around with the values within these program
# examples and call wrong indexes, and wrong strings together to force
# these exception handlers to do their work, which is to stop programs
# from crashing, and they are also used for program manipulation
# purposes to change program flow control.

if x := (0,1,2,3,4,5):
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')

# The 'pass' prefix is for code place holding if you don't wish to write
# any code blocks underneath expressions that use code blocks, such
# as the Python program above shows in our first example.

if x := (0,1,2,3,4,5):
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        pass

# Without the use of the walrus := operator.

x = (0,1,2,3,4,5)

if x == x:
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')

# With the 'pass' prefix placeholder for code blocks.

x = (0,1,2,3,4,5)

if x == x:
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        pass

# Let's use one 'try:' and two exception handlers, alongside the walrus
# := operator. We will use one 'IndexError:' handler and one 'TypeError:'
# handler to create some programming manipulation within our Python
# program examples below.

if x := (0,1,2,3,4,5):
    try:
        print(x[6],'is in the "x" variable tuple().')
        print(x[4]+'character string')       
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')
    except TypeError:
        print('The TypeError handler stops Type errors from occurring.')

# Python executes/runs its programs from the top downward, as the
# very same way you can see the code order. Each instruction is first
# to execute, is the first to be serviced. In most cases multiple exception
# handlers can only execute one or the other, depending on the code order.

if x := (0,1,2,3,4,5):
    try:
        print(x[4]+'character string text.')
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')
    except TypeError:
        print('The TypeError handler stops Type errors from occurring.')

input()
# Use the := Walrus Operator to tempararly check for values in tuples,
# lists, dictionaries and sets. That way, you can be a bit lazy and
# not have to write two lines of code only to check for values. Note:
# default tuples won't work with the := walrus operator for indexing.
# Python cannot seem to see the values as either strings, nor integers
# when using the := walrus operator.

print(x := 1,2,3,4,5,6,7,8,9)  # x creates a default tuple of values

print(x[0]) # TypeError: 'int' object is not subscriptable

print(x := (1,2,3,4,5,6,7,8,9))  # x creates a tuple of values

print(x[0]) # tuple index[0] is the value '1'

print(x := [1,2,3,4,5,6,7,8,9])  # x creates a list of values

print(x[0]) # list index[0] is the value '1'

print(x := {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9})  # x creates a dictionary of values

print(x.get(1,'Not Found!'))

print(x := {1,2,3,4,5,6,7,8,9})  # x creates a set of values

x = sum([1,2,3,4,5,6,7,8,9])
y = sum([10,11,12,13,14,15,16,17,18,19])

print(f'x = {x} and y = {y}. x+y = {x+y}') # x = 45 and y = 145. x+y = 190

# The 'is' and 'not' prefixes are the very same things as '==' and '!='.
# The prefix 'is' is a literal '==', meaing that 'is' is goes deeper into
# Python's scope of the '==' prefix. The 'not' prefix simply means
# 'not' equal to, which is exactly the same as the '!=' prefix. These
# prefixes are mainly used for logical expressions as these Python
# program examples clearly shows. Note: you will get a SyntaxWarning
# message. This is because Python is asking you if you mean this '=='
# or 'is', which is used only for logical expressions. Remember that
# the 'is' prefix goes deeper into the Python scope than '==' does.

# Warning (from warnings module):
#   File "C:\Users\mogie54321\Desktop\How To Copy.py", line 17
#    print(2 is y) # True because y = 2
# SyntaxWarning: "is" with a literal. Did you mean "=="?

x = 1
y = 2

print(1 == x) # True because x = 1
print(2 == y) # True because y = 2

print(1 is x) # True because x = 1
print(2 is y) # True because y = 2

print(1 != x) # False because x = 1
print(2 != y) # False because y = 2

print(not x) # False because x = 1
print(not y) # False because y = 2

# Check the 'animals' variable list of values to see how many values
# contain like 'letters'. For example, the letter 'i' is in three values:
# Bird, Fish and Lizard. The for loop will only show text output with
# letters that also belong inside the other values, as shown in this
# Python program example.

animals = ['Cat','Dog','Bird','Fish','Lizard']

for i in animals:
    if 'k' in i:
        print(f'The word "{i}" has {len(i)} letters in it.')

# The logical 'in' is great to use if you want to know if a value
# is 'in' a list[ ], a tuple( ), a dictionary{ }, a set() and a print( ) function.
# in our first example, we are only using logical text as a single
# value placeholder for the 'abc' variable. If a letter or value does
# not belong to the 'abc' variable, the 'else:' clause will execute.
# If a letter or value does belong to the 'abc' variable, the 'if'
# clause will execute.

abc = 't' # change the value 't' and re-execute this Python program example.

if abc in 'If a letter appears in this logical text.':  # logical text won't show screen output
    print(abc,'appears in the logical text.')
    
else:
    print(abc,'does not appear in the logical text.')

# Let's use the logical 'in' to check if a tuple value is present or not.
# Note: when creating tuples( ), a default tuple is a tuple without ( )
# parentheses. That means you cannot modify, change the tuple
# values in logical expressions. Whereas lists[ ] can be changed,
# modified; meaning tuples are immutable and lists are mutable.

my_default_tuple = 'text',1,3,4,5,'more text'  # change the values and re-execute the program.

if 'more text' in my_default_tuple:
    print('appears in the default tuple.')

else:
    print('does not appear in the default tuple.')

# This is a tuple( ). Not a default tuple.

my_tuple = ('text',1,3,4,5,'more text')  # change the values and re-execute the program.

if 'more text' in my_tuple:
    print('appears in the tuple.')

else:
    print('does not appear in the tuple.')

# Let's create a list of values and check them with the logical 'in'.

my_list = ['text',1,3,4,5,'more text']  # change the values and re-execute the program.

if 'more text' in my_list:
    print('appears in the list.')

else:
    print('does not appear in the list.')

input()
# Here is something else we can do with the Walrus := operator.
# Here are two Python program examples that will show you the
# 'if' statement, using the none walrus := operator, and the use
# of the walrus := operator with the 'if' statement.

x = 3

if x == 3:print(x)

# Notice how the very same Python code above is exactly the
# very same Python code as below. As you can clearly see, the
# walrus := operator reduces the usual two lines of Python code
# down to just one, single line of Python code.

if x := 3:print(x) # the walrus := operator makes x act as if it were named first.

# You don't have to create a variable first, to then place it within an
# 'if' statement using the walrus := operator.

# Welcome to the the split() function. This split() function has a dot '. '
# in front of it that joins the variable, 'poem' to the split() function
# using another variable called, 'text'. What the split() function does
# is turns any text paragraphs into an actual list of words, which you
# can then use their indexes [index] to pick out words within the poem.

poem = '''‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.'''

# For example: the first word in the poem is 'Knowledge', which is
# index[0] with the single quote marks as in no spaces in between them
# or the word Knowledge. Any words therafter dosen't have quote marks;
# only the title of the poem as in normal poems, sometimes you want
# quote marks in a title or word/words alike.

text = poem.split()

print(text[0]) # index[0] is the word with single quote marks: 'Knowledge'

poem = '''‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.'''

# Here, we can use Python's Walrus Operator := to check our list of words
# within the poem right on the spot and on one, single line of Python code
# at that.

print(text := poem.split())

# Here is the old way, I taught you, as others had taught you. Let's check our
# list of words without the help of the walrus := operator and see how we have
# to use two lines of Python code to create the same thing as we did above
# using the walrus := operator. When you are happy with your list of words,
# you can throw away only one line of Python code, instead throwing away
# two lines of Python code. The walrus := operator makes this a single line
# snap that you can just throw away one line of Python code.

text = poem.split()

print(text)

# Now that I'm happy with my list. I can start picking out words, via their indexes.

print(text[1]) # index[1] is the word: is

# Let's use a for loop to call up all the words to the poem, without showing ugly
# commas ' , ' and index[ ] brackets.

for i in text:print(i)

input()
'''
Did you know you can create variables for some of these Python
commands/functions? This will give us much more opertunities
to use variables as Python code in a for loop that loops through
a list of values, which are actual Python commands/functions.
You can create two or more Python commands/functions with
just one for loop alone. Let's explore what these variables can
do for us, using actual Python code itself.
'''
absolute_num = abs
add_nums = sum
ascii_character = ascii
ascii_character_num = ord
ascii_character_value = chr
binary_base_2 = bin
character_string = str
convert_to_list = list
convert_to_set = set
convert_to_tuple = tuple
dictionary = dict
float_num = float
George_Boole = bool
hexadecimal_base_16 = hex
index_error = IndexError
integer_num = int
maximum_num = max
memory_error = MemoryError
minimum_num = min
redundant_code = exec
round_num = round
super_function = super
text_input = input
text_print = print
value_error = ValueError
value_length = len

# Let's try a simple print() command/function and see what this does
# We will also create a variable to be a text placeholder, so we don't
# have to keep rewriting text sentences over and over again.

text = "This was Python's print() command/function."

# this:

print("This was Python's print() command/function.")

# or this:

text_print(text) # use variables instead if you like

# Let's try a few more to get the hange of things. Let's add some numbers
# together with the sum() command/function, we renamed to 'add_nums'
# using a variable to store the actual sum() command/function. We also
# need to create a variable we'll call nums, so we can store a default tuple
# of numbers without any parenthesese, ie: (1,2,3,4,5,6,7,8,9)

nums = 1,2,3,4,5,6,7,8,9 # this is a tuple by default, without parentheses ' () ' 

# this:

print(sum(nums))

# or this:

text_print(add_nums(nums))

# Let's try a simple input() command/function and see what this does We will
# create a variable to be a text placeholder, so we don't have to keep rewriting
# text sentences over and over again. We also have to create an 'user_input'
# variable so the user can type into it.

input_text = "This was Python's input() command/function."

# this:

user_input = input("This was Python's input() command/function.")

# or this:

user_input = text_input(input_text)

# Let's use a for loop to loop through a tuple of variables, which are actual Python
# commands/functions. Let's creat our tuple called loop.

loop = integer_num,binary_base_2,hexadecimal_base_16

for i in loop:
    text_print(f'{i(255)}. You only need one print statement with a list of variables.')
