# Here is some MENTAL METAL PYTHON 'DEATH METAL' PROGRAMMING EXAMPLES
# to play with. I say no more...

# Note: not recommended for beginners. But why not?!

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

# Just discover and learn from these Python programming examples below.
# If you aren't sure what is happening. DO SOME HOMEWORK and figure
# these all out for yourself over the internet, such as YouTube is a GREAT
# START! That's the only place to start. I DID JUST THAT! I'm no hypocrite
# when it comes to this type of learning style; it's there. USE IT! I DO!! As a
# self taught Python programmer. I had to use VR teachers to teach me
# EVERYTHING I KNOW about Python in general. I'm as Human as You. I'm
# No one, nor am I BETTER THAN YOU! I had to learn all this Python stuff
# from VR teachers, mostly them. They are all on my channel, of those I
# recommend to others, who seek what I love to do. You can do it too...

# Just go and get it is all you have to do, and trust yourself and take the
# time to learn this kind of programming thing. Who knows? You might LOVE
# IT!
'''
Create three different integer sets that will combine/unionize all three sets into one
single set. Convert the single set into a list, using the list() function. Next, view the
contents of the list, along with the slice() function to set the range of list content
values to display on the screen.

Type and execute/run this Python program example below.
'''
# To reduce lines of code, create packed variables and their
# packed values.

x,y,z=(
    {1,2,3,4,9,6,7,8,5,9,10},
    {11,12,13,14,15,16,17},
    {18,19,20,21,22,23,24})

a=slice(24) # slice the set with the slice() function

# To reduce lines of code, create packed variables and their
# packed values.

length1,length2,length3=len(x),len(y),len(z)

unionize=x.union(y,z) # unionize x to y and z with the value v.union() function

convert=list(unionize) # cast the set to a list with the list() function

answer=length1,length2,length3

# Add the total values between length1, length2 and length3 with the sum()
# function.

total_sum=sum(answer) # add all three values of answer together with the sum() function

# View the contents of x, y and z in their combined, converted sets to a list.

print('View the value contents of the unionized list to check it:\n\n'+str(convert[a]))

# Create a variable called sentence_loop, along with all its values.

sentence_loop=(
    f'\nThe length of (x) = {length1}',f'The length of (y) = {length2}',
    f'The length of (z) = {length3}',f'\nThe total lengths of x+y+z = {total_sum}')

# Create a for loop that will loop through the sentence_loop variable, using a
# single print() function. The for loop will iterate until all the values are cycled
# through the sentence_loop variable.

for i in sentence_loop:print(i)

x={1,2,3,4,9,6,7,8,5,9}
y={10,11,15,13,14,12,16,17,18,19,19}
z={20,21,22,23,27,25,26,24,28,29,22}

unionize=x.union(y).union(z)

convert=list(unionize)

a=slice(20)

print(convert[a])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x={1,2,3,4,9,6,7,8,5,9}
y={10,11,15,13,14,12,16,17,18,19,19}
z={20,21,22,23,27,25,26,24,28,29,22}

unionize=x.union(y,z)

convert=list(unionize)

a=slice(20)

print(convert[a])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a=list()
for i in range(10):
    a.append(i)

b=set()
for i in range(10):
    b.add(i)

print(a)
print(b)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 | nums2) # Union

print(nums1.union(nums2)) # Union

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 & nums2) # Intersection

print(nums1.intersection(nums2)) # Intersection

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 - nums2) # Difference

print(nums1.difference(nums2)) # Difference

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1.symmetric_difference(nums2)) # Symmetric Difference

print(nums1 ^ nums2) # Symmetric Difference
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums1={0,1,2,3,1,3,4,10,5,6,6,7,8,9,10,23}
nums2={1,2,7,1,3,4,10,5,6,6,7,8,9,10,11,22}

print(nums1 | nums2) # Union
print(nums1 & nums2) # Intersection
print(nums1 - nums2) # Difference
print(nums1 ^ nums2) # Symmetric Difference

nums1=[1,2,3,1,3,4,10,5,6,6,7,8,9,10]
nums2=[1,2,3,1,3,4,10,5,6,6,7,8,9,10]

uniques1=set(nums1)
uniques2=set(nums2)

print(uniques1 | uniques2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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

1


1

COMPUTER SCIENCE & PYTHON PROGRAMMING EXAMPLES:
COMPUTER SCIENCE & PYTHON PROGRAMMING EXAMPLES:
2 weeks ago (edited)
# Here is some MENTAL METAL PYTHON 'DEATH METAL' PROGRAMMING EXAMPLES
# to play with. I say no more...

# Note: not recommended for beginners. But why not?!

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

# Just discover and learn from these Python programming examples below.
# If you aren't sure what is happening. DO SOME HOMEWORK and figure
# these all out for yourself over the internet, such as YouTube is a GREAT
# START! That's the only place to start. I DID JUST THAT! I'm no hypocrite
# when it comes to this type of learning style; it's there. USE IT! I DO!! As a
# self taught Python programmer. I had to use VR teachers to teach me
# EVERYTHING I KNOW about Python in general. I'm as Human as You. I'm
# No one, nor am I BETTER THAN YOU! I had to learn all this Python stuff
# from VR teachers, mostly them. They are all on my channel, of those I
# recommend to others, who seek what I love to do. You can do it too...

# Just go and get it is all you have to do, and trust yourself and take the
# time to learn this kind of programming thing. Who knows? You might LOVE
# IT!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
poem = ('''‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.'''[::-1],

'''.tneduts tsetaerg rieht era uoy roF !flesruoy ni eveileB
…su fo srehcaet tsetaerg eht ,suht era dnim eht dna traeh eht roF
.noitanigami ruo fo noitaerc s’maerd eht
,lla fo amolpid tsetaerg eht ot yek eht dloh dnim eht dna traeh eht roF
.rednow otni rednop ot yek eht si nettirw eb ot maxe ylno ehT
.dnim eht dna traeh eht era ,dedeen skoobtxet ylno ehT
!flesti dnim eht fo dna traeh eht fo noitnevni eerf a si
’egdelwonK‘'''[::-1])

print(poem[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(256):print(bin(i),hex(i),oct(i),i)

for i in range(256):print(f'{i:b} {i:x} {i:o} {i:d}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums = [i for i in range(1,11)];print(nums)

nums = [i+2 for i in range(1,11)];print(nums)

nums = [i-2 for i in range(1,11)];print(nums)

nums = [i*i for i in range(1,11)];print(nums)

nums = [i/2 for i in range(1,11)];print(nums)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums = [1,2,3,4,5,6,7,8,9,10]

num = [i if i>=5 else False for i in nums]

print(num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cubed = lambda x,y:x+y**3

print(cubed(10,10)) # 10*10*10 = 10 + 1000 = 1010
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cubed = lambda x,y:x**3+y

print(cubed(10,10)) # 10*10*10 = 1000 + 10 = 1010
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
full_name = lambda \
            first_name,middle_name,last_name:\
            first_name+' '+middle_name+' '+last_name

print(full_name('First','Middle','Last'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
auto_multi_dimensional_list = []

for i in range(1,11):
    auto_multi_dimensional_list.append(i)
    print(auto_multi_dimensional_list)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Almost six years later, and I'm still learning how to master
# Python. I'm always trying new ideas through others so I can
# learn what Python is truly all about.

# Use the enumerate() function to loop through a list, using
# only two lines of code; one for the for-index enumerate()
# function and the other for the 'print' statement.

name_list=['John','Bob','Rob','Tom']

# Here is a simple for-loop that will loop through the name_list
# values starting with index 0, followed by index 1 and then
# index 2, and finally index 3.

for index in name_list:
    print(index)

# The for-loop example above is fine, but it has its limitations
# when it comes to multi indexing through a tuple or list alike.
# With the enumerate() function, such things are possible.
# Try these enumerate() function Python program examples
# below and see what happens when you experiment with them.

for index,name in enumerate(name_list):
    print(index)

for index,name in enumerate(name_list):
    print(name)

for index,name in enumerate(name_list):
    print(index,name)

for index,name in enumerate(name_list,start=1):
    print(index,name)

name=['John','Bob','Rob','Tom']
pet=['Dog','Cat','Bird','Fish']
computer=['Desktop','Laptop','Cellphone','Notebook']

# Note: the zip() function only goes to the shortest length
# in a multi list. However, you can simply keep them the
# same size such as the list examples above, which shows
# three lists called name, pet and computer. Each list has
# four values in them. This way, every value gets called inside
# one, single 'print' statement. Try these different examples
# below. Note: you can rename the words 'index1, index2 and
# index3' to any names you wish. You can also rename the
# name variable if you like.

for index1,index2,index3 in zip(name,pet,computer):
    print(index1)

for index1,index2,index3 in zip(name,pet,computer):
    print(index2)

for index1,index2,index3 in zip(name,pet,computer):
    print(index3)

for index1,index2,index3 in zip(name,pet,computer):
    print(index1,index2,index3)

# Let's try the enumerate() function with a 2d-list.

my_2d_list=[
    ['John','Bob','Rob','Tom'],
    ['Desktop','Laptop','Cellphone','Notebook']]

for index,name in enumerate(my_2d_list):
    print(index)

for index,name in enumerate(my_2d_list):
    print(name[0])

for index,name in enumerate(my_2d_list):
    print(index,name[0])

for index,name in enumerate(my_2d_list,start=1):
    print(index,name[0])

# Let's try the zip() function with a 2d-list.

my_2d_list=[
    ['John','Bob','Rob','Tom'],
    ['Desktop','Laptop','Cellphone','Notebook']]

for index in zip(my_2d_list):
    print(index[0][0])

for index in zip(my_2d_list):
    print(index[0][0],index[0][1],index[0][2],index[0][3])

# Let's try some fun experiment examples with some of what
# we've learned so far about the enumerate() function. Let's
# create a program that uses a sentence for each value in the
# fun_list1,  fun_list2 and fun_list3 lists. Let's use the f' format
# to make string concatenations much easier to create.

fun_list1=['John','Bob','Rob','Tom']
fun_list2=['Dog','Cat','Bird','Fish']
fun_list3=['Desktop','Laptop','Cellphone','Notebook']

for index,name in enumerate(fun_list1):
    print(f"My name is {name}. I'm the value from the fun_list1, position {index}")

for index,name in enumerate(fun_list2):
    print(f"I am a {name}. I'm the value from the fun_list2, position {index}")

for index,name in enumerate(fun_list3):
    print(f"I am a {name}. I'm the value from the fun_list3, position {index}")

# These enumerate() function examples are great, but let's beef it up just a lot
# more with the zip() function, so we can create complex actions with all our
# fun_lists combined into complete, separate sentences, just simply using two
# lines of code. See what happens when you type and execute/run this Python
# program example below:

for list1,list2,list3 in zip(fun_list1,fun_list2,fun_list3):
    print(f"My name is {list1} and I have a {list2} picture on my {list3} screen.")

# The zip() function is very useful, but it can only reach as far as its shortest
# list length. That means, if you have two, three or more lists, the shortest list
# out of the three or more lists values will be cut off from the rest if one or more
# lists have extra values inside them. To avoid this from occurring, make all your
# lists the same size in each of their values. take a look at the example below:

fun_list1=['John','Bob','Rob','Tom'] # four values
fun_list2=['Dog','Cat','Bird','Fish'] # four values
fun_list3=['Desktop','Laptop','Cellphone','Notebook'] # four values

# The zip() function is sometimes better than a simple for-loop or a simple
# enumerate() function, in that it uses less lines of code and it can also achieve
# a far better programming style approach over program code redundancy on
# the programmer's part.

# Let's try one more example to prove this to be true. let's create another
# fun_list, zip() function Python program example. Type and execute/run
# this Python program below and see what happens with the output.

fun_list1=['John','Bob','Rob','Tom']
fun_list2=['Dog','Cat','Bird','Fish']
fun_list3=['Desktop','Laptop','Cellphone','Notebook']
fun_list4=['loves my','hates my','found my','lost my']
fun_list5=['fed his',"didn't feed his",'plays with his',"doesn't play with his"]

for list1,list2,list3,list4,list5 in zip(fun_list1,fun_list2,fun_list3,fun_list4,fun_list5):
    print(f'{list1} {list4} {list3} and {list5} {list2}.')

# Well, I think we pretty much learned what the enumerate() and zip() functions
# do. Now, it's practice, practice, practice and more practice, practice, practice...

'''
Create three different integer sets that will combine/unionize all three sets into one
single set. Convert the single set into a list, using the list() function. Next, view the
contents of the list, along with the slice() function to set the range of list content
values to display on the screen.

Type and execute/run this Python program example below.
'''
# To reduce lines of code, create packed variables and their
# packed values.

x,y,z=(
    {1,2,3,4,9,6,7,8,5,9,10},
    {11,12,13,14,15,16,17},
    {18,19,20,21,22,23,24})

a=slice(24) # slice the set with the slice() function

# To reduce lines of code, create packed variables and their
# packed values.

length1,length2,length3=len(x),len(y),len(z)

unionize=x.union(y,z) # unionize x to y and z with the value v.union() function

convert=list(unionize) # cast the set to a list with the list() function

answer=length1,length2,length3

# Add the total values between length1, length2 and length3 with the sum()
# function.

total_sum=sum(answer) # add all three values of answer together with the sum() function

# View the contents of x, y and z in their combined, converted sets to a list.

print('View the value contents of the unionized list to check it:\n\n'+str(convert[a]))

# Create a variable called sentence_loop, along with all its values.

sentence_loop=(
    f'\nThe length of (x) = {length1}',f'The length of (y) = {length2}',
    f'The length of (z) = {length3}',f'\nThe total lengths of x+y+z = {total_sum}')

# Create a for loop that will loop through the sentence_loop variable, using a
# single print() function. The for loop will iterate until all the values are cycled
# through the sentence_loop variable.

for i in sentence_loop:print(i)

x={1,2,3,4,9,6,7,8,5,9}
y={10,11,15,13,14,12,16,17,18,19,19}
z={20,21,22,23,27,25,26,24,28,29,22}

unionize=x.union(y).union(z)

convert=list(unionize)

a=slice(20)

print(convert[a])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x={1,2,3,4,9,6,7,8,5,9}
y={10,11,15,13,14,12,16,17,18,19,19}
z={20,21,22,23,27,25,26,24,28,29,22}

unionize=x.union(y,z)

convert=list(unionize)

a=slice(20)

print(convert[a])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a=list()
for i in range(10):
    a.append(i)

b=set()
for i in range(10):
    b.add(i)

print(a)
print(b)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 | nums2) # Union

print(nums1.union(nums2)) # Union

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 & nums2) # Intersection

print(nums1.intersection(nums2)) # Intersection

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 - nums2) # Difference

print(nums1.difference(nums2)) # Difference

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1.symmetric_difference(nums2)) # Symmetric Difference

print(nums1 ^ nums2) # Symmetric Difference
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums1={0,1,2,3,1,3,4,10,5,6,6,7,8,9,10,23}
nums2={1,2,7,1,3,4,10,5,6,6,7,8,9,10,11,22}

print(nums1 | nums2) # Union
print(nums1 & nums2) # Intersection
print(nums1 - nums2) # Difference
print(nums1 ^ nums2) # Symmetric Difference

nums1=[1,2,3,1,3,4,10,5,6,6,7,8,9,10]
nums2=[1,2,3,1,3,4,10,5,6,6,7,8,9,10]

uniques1=set(nums1)
uniques2=set(nums2)

print(uniques1 | uniques2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
