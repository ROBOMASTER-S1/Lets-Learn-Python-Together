'''
The only extensive way to truly understand Python
is to go deep, deep down that Rabbit Hole. So what
are you waiting for? Let's go...
'''
# 'str()' function example:

# 'str()' is short for 'string'

# 'str()' function turns integer numbers into character
# strings.

name='Tom'
age=400

print(name,'is',age+5,'years old.') # Non Formatted

print(name+' is '+str(age+5)+' years old.') # Non Formatted

print('{} is {} years old.'.format(name,age+5)) # Old Formatted

print(f'{name} is {age+5} years old.') # New Formatted
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 'int()' function example:

# 'int()' is short for 'integer'

# 'int()' function turns character strings into integer numbers

name='Tom'
age=int('400')

print(name,'is',age+5,'years old.') # non formatted

print(name+' is '+str(age+5)+' years old.') # non formatted

print('{} is {} years old.'.format(name,age+5)) # old formatted

print(f'{name} is {age+5} years old.') # new formatted
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 'min() and max()' function examples:

min_num=1,2,3,4,5,6,7,8,9,10

print(min(min_num)) # 1

max_num=1,2,3,4,5,6,7,8,9,10

print(max(max_num)) # 10

# Why not shorten the code inside the 'print()' function
# instead?

min_num=min(1,2,3,4,5,6,7,8,9,10)

print(min_num)

max_num=max(1,2,3,4,5,6,7,8,9,10)

print(max_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 'float()' function example:

float_num=float(5)

print(float_num) # 5.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 'round()' function example:

round_num=round(1.5)

print(round_num) # 2
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 'bool()' function examples:

george_boole=bool(1<1)

print(george_boole) # False

george_boole=bool(1>1)

print(george_boole) # False

george_boole=bool(1<=1)

print(george_boole) # True

george_boole=bool(1>=1)

print(george_boole) # True

george_boole=bool(1==1)

print(george_boole) # True

george_boole=bool(1!=1)

print(george_boole) # False
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The 'all()' and 'any()' functions examples:

# Displays Boolean logic 'True' and 'False' values only.

num=0,1

x=all(num)
print(x) # False

x=any(num)
print(x) # True
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 'abs()' function examples:

# 'abs()' is short for 'absolute value'

abs_num=abs(-5)

print(abs_num) # 5

print(abs_num+2) # 7
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 'tuple, list, dictionary and set examples:

# Check to make sure all the values are correct.

default_tuple_string='value1','value2','value3','value4' # without parentheses
print(default_tuple_string)

tuple_string=('value1','value2','value3','value4') # with parentheses
print(tuple_string)

list_string=['value1','value2','value3','value4'] # with sqaure brackets
print(list_string)

dictionary_string={1:'value1',2:'value2',3:'value3',4:'value4'} # with curly braces
print(dictionary_string)

set_string={'value1','value2','value3','value4','value3'} # with curly braces
print(set_string)

# Now we can use each of these checked values in
# our tuple, list, set and dictionary examples.

default_tuple_string='value1','value2','value3','value4'
print(default_tuple_string[0],'is from the default tuple string.')

tuple_string=('value1','value2','value3','value4')
print(tuple_string[1],'is from the tuple string.')

list_string=['value1','value2','value3','value4']
print(list_string[2],'is from the list string.')

dictionary_string={1:'value1',2:'value2',3:'value3',4:'value4'} # with curly braces
print(dictionary_string.get(3),'is from the dictionary string.')

# Check only the keys

print(dictionary_string.keys())

# Check only the values

print(dictionary_string.values())

print(dictionary_string.get(5,'Not Found!'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a set, then convert it to a tuple string
# without duplicate values.

set_string={'value1','value2','value3','value4','value3'}

convert_to_tuple=tuple(set_string)

print(convert_to_tuple)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a set, then convert it to a list string without
# duplicate values.

set_string={'value1','value2','value3','value4','value3'}

convert_to_list=list(set_string)

# Let's sort our converted list string with the 'sort()' function.

convert_to_list.sort() # sorts the actual converted list.

print(convert_to_list)

x=sorted(convert_to_list) # sorts only the variable 'x'.

print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a tuple string, then convert it to a list
# string so we can modify/change it. Next, we will
# reconvert our list string back to a modified tuple with
# one added value. With the 'list()' function, 'tuple()'
# function and along with the 'append()' function, we can
# achieve this feat.

tuple_string=('value1','value2','value3','value4')

convert_to_list=list(tuple_string)
convert_to_list.append('value5')
reconvert_to_tuple=tuple(convert_to_list)

print(reconvert_to_tuple)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 'dict()' function example:

dictionary_vars_and_values=dict(
    first_name='Tom',last_name='Thumb',age=str(400+5))

# Check to make sure everything is correct.

print(dictionary_vars_and_values)

# Check the keys.

print('keys:',dictionary_vars_and_values.keys())

# Check the values.

print('values:',dictionary_vars_and_values.values())

# Let's change our mind and convert the dictionary
# keys and the dictionary values to sets instead,
# using the 'set()' function.

convert_dictionary_vars_and_values=set(
    dictionary_vars_and_values.keys())

print(convert_dictionary_vars_and_values)

convert_dictionary_vars_and_values=set(
    dictionary_vars_and_values.values())

print(convert_dictionary_vars_and_values)

# Let's reconvert our dictionary keys and values back
# to sorted lists, using the 'list()' function, the 'sort()'
# and 'sorted()' functions.

convert_dictionary_vars_and_values=list(
    dictionary_vars_and_values.keys())

convert_dictionary_vars_and_values.sort()

print(convert_dictionary_vars_and_values)

convert_dictionary_vars_and_values=list(
    dictionary_vars_and_values.values())

convert_dictionary_vars_and_values.sort()

print(convert_dictionary_vars_and_values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The 'sorted()' function sorts only the variable 'x', not
# the actual list values.

convert_dictionary_vars_and_values=list(
    dictionary_vars_and_values.keys())

x=sorted(convert_dictionary_vars_and_values)

print(x)

convert_dictionary_vars_and_values=list(
    dictionary_vars_and_values.values())

x=sorted(convert_dictionary_vars_and_values)

print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The 'object()' function example:

def variables(object):
    return 'abcdefghijklmnopqrstuvwxyz'.upper()

print(variables(object),'are all uppercase letters.')

# Shorten the code inside the 'print()' function with a
# variable called 'x'.

x=variables(object)

print(x,'are all uppercase letters.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use what we learned and use these very same
# functions inside a 'tuple' and retrieve each value by
# its index[]. For example the 'print()' function can also
# be functs[0]('This Works!')

functs=(
    print,str,int,min,max,
    float,round,bool,abs,
    tuple,list,set,sorted,
    dict,all,any)

functs[0]('This Works!')

# Let's create a list of words and use them inside our
# 'print()' function along with our replacement 'print()'
# function 'functs[0]()'.

words=['word0','word1','word2','word3']

functs[0](words[0],words[1],words[2],words[3])

# Let's create the same thing using a for-loop instead.
# We will also invoke the end=' ' to make the printed
# output stay on the same line.

for i in words:
    functs[0](i,end=' ') # word0 word1 word2 word3
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try the 'str()' function using the replacement
# 'functs[1]()' and see what happens when you type
# and execute/run this program example.

x=functs[1](5+3)

functs[0](x,'This Works!')

functs[0](x+' This Also Works!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try the 'int()' function using the replacement
# 'functs[2]()' and see what happens when you type
# and execute/run this program example.

x=functs[2]('5')

functs[0](x+3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try the 'min()' function using the replacement
# 'functs[3]()' and see what happens when you type
# and execute/run this program example.

min_num=functs[3](1,2,3,4,5,6,7,8,9,10)

functs[0](min_num)

# Let's try the 'max()' function using the replacement
# 'functs[4]()' and see what happens when you type
# and execute/run this program example.

max_num=functs[4](1,2,3,4,5,6,7,8,9,10)

functs[0](max_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try the 'float()' function using the replacement
# 'functs[5]()' and see what happens when you type
# and execute/run this program example.

float_num=functs[5](5)

functs[0](float_num) # 5.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try the 'round()' function using the replacement
# 'functs[6]()' and see what happens when you type
# and execute/run this program example.

round_num=functs[6](1.5)

functs[0](round_num) # 2
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try the 'bool()' function using the replacement
# 'functs[7]()' and see what happens when you type
# and execute/run this program example.

george_boole=functs[7](1<1)

functs[0](george_boole) # False
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try the 'abs()' function using the replacement
# 'functs[8]()' and see what happens when you type
# and execute/run this program example.

abs_num=functs[8](-5)

functs[0](abs_num) # 5

functs[0](abs_num+2) # 7
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try the 'tuple()' function using the replacement
# 'functs[9]()' and see what happens when you type
# and execute/run this program example.

set_string={'value1','value2','value3','value4','value3'}

convert_to_tuple=functs[9](set_string)

functs[0](convert_to_tuple)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try the 'list()' and the 'sorted()' functions using
# the replacement 'functs[10]()', 'functs[12]()' and see
# what happens when you type and execute/run this
# program example.

set_string={'value1','value2','value3','value4','value3'}

convert_to_list=functs[10](set_string)

convert_to_list.sort()

functs[0](convert_to_list)

x=functs[12](convert_to_list)

functs[0](x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try the 'set()' function using the replacement
# 'functs[11]()' and see what happens when you type
# and execute/run this program example.

list_string=['value1','value2','value3','value4','value3']

convert_to_list=functs[11](set_string)

functs[0](convert_to_list)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try the 'dict()' and the 'str()' functions using the
# replacement 'functs[13]()', 'functs[1]()' and see what
# happens when you type and execute/run this program
# example.

dictionary_vars_and_values=functs[13](
    first_name='Tom',last_name='Thumb',age=functs[1](400+5))

# Check to make sure everything is correct.

functs[0](dictionary_vars_and_values)

# Check the keys.

functs[0]('keys:',dictionary_vars_and_values.keys())

# Check the values.

functs[0]('values:',dictionary_vars_and_values.values())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try the 'all()' and the 'any()' functions using the
# replacement 'functs[14]()', 'functs[15]()' and see what
# happens when you type and execute/run this program
# example.

num=0,1

x=functs[14](num)

functs[0](x) # False

x=functs[15](num)

functs[0](x) # True
