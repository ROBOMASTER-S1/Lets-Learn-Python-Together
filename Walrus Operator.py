# Walrus Operator Python program example.

# Created by Joseph C. Richardson, GitHub.com

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

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

# Use the := Walrus Operator to temporarily check for values in tuples,
# lists, dictionaries and sets. That way, you can be a bit lazy and
# not have to write two lines of code only to check for values. Note:
# default tuples won't work with the := walrus operator for indexing.
# Python cannot seem to see the values as either strings, nor integers
# when using the := walrus operator.

print(x := 1,2,3,4,5,6,7,8,9)  # x creates a default tuple of values

print(x[0]) # TypeError: 'int' object is not subscripted

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
# or the word Knowledge. Any words thereafter doesn't have quote marks;
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
