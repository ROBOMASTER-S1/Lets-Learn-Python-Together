# Did You Know Python program example.

# Created by Joseph C. Richardson, GitHub.com

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE
'''
Did you know you can create variables for some of these Python
commands/functions? This will give us much more opportunities
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
george_boole = bool
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
you_quitter = quit
must_exit = exit

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
# of numbers without any parentheses, ie: (1,2,3,4,5,6,7,8,9)

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
