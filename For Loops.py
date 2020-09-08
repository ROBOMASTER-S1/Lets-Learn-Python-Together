'''For-Loop Examples:'''
'''
Loops are instructions, which tells the computer to iterate/repeat a part of a \
program a certain numbers of times before it stops. When a loop reaches its \
final iteration, it stops and comes to an end. Loops make programming code \
very efficient, without the manual redundancy on the programmer's part. Loops \
can also manipulate data by incrementing it or decrementing it.
'''
# The 'for i in range(5):' for-loop causes the 'print' statement value to print 'Hello
# World!' five times:

for i in range(5):
    print('\nHello World!')
    
'''----------------------------------------------------------------'''

# Here is a manual, redundant example of this tuple string code without using a for-
# loop:

tuple_string_name=('Super Man','Bat Man','Spider Man')

print(f'\nMy name is {tuple_string_name[0]} and I\'m a Super Hero.')

print(f'\nMy name is {tuple_string_name[1]} and I\'m a Super Hero.')

print(f'\nMy name is {tuple_string_name[2]} and I\'m a Super Hero.')

# Here is a manual, redundant example of this list string code without using a for-loop:

list_string_name=['Super Man','Bat Man','Spider Man']

print(f'\nMy name is {list_string_name[0]} and I\'m a Super Hero.')

print(f'\nMy name is {list_string_name[1]} and I\'m a Super Hero.')

print(f'\nMy name is {list_string_name[2]} and I\'m a Super Hero.')

'''----------------------------------------------------------------'''

# Here is a non manual example of this very same code, using a for-loop: The for-loop
# also increments the string's data values, which makes the code more efficient, without
# the manual redundancy on the programmer's part.

tuple_string_name=('Super Man','Bat Man','Spider Man')

for i in range(3):
    print(f'\nMy name is {tuple_string_name[i]} and I\'m a Super Hero.')

list_string_name=['Super Man','Bat Man','Spider Man']

for i in range(3):
    print(f'\nMy name is {list_string_name[i]} and I\'m a Super Hero.')

# The new 'list_string_name' value 'Halk' is appended/added at the end of the for-loop.

list_string_name=['Super Man','Bat Man','Spider Man']

list_string_name.append('Halk')

for i in range(4):
    print(f'\nMy name is {list_string_name[i]} and I\'m a Super Hero.')
    
'''----------------------------------------------------------------'''

# This for-loop example loops by using the string's variable, instead of using the range
# values.

list_string_name=['Super Man','Bat Man','Spider Man']

list_string_name.append('Halk')

for i in list_string_name:
        print(f'\nMy name is {i} and I\'m a Super Hero.')
        
'''----------------------------------------------------------------'''

# How to make a for-loop count, starting from 0 to 9 with a 'print' statement using the
# (f') format along with the words 'Count Loop!', with # a loop range # equal to 10.

for i in range(10):
    print(f'\nCount Loop! "{i}" ')
    
'''----------------------------------------------------------------'''

# Here is a fun list looping program example with the for-loop. The animal_list variable
# gets incremented by (i) each cycle through the for-loop. The animal_list variable will
# keep iterating in the for-loop, until the values in animal_list gets completely cycled
# through the for-loop.

animal_list=['dog','cat','bird','duck','chicken']

for i in animal_list:
    print(f'\nI would love to own a {i}. I just love {i}s so much!')
    
'''----------------------------------------------------------------'''

# In this example the for-loop will cycle through the nums list, containing real integer
# values. When it encounters the 'if i==5:' statement, the 'print' statement (f'{i}: I found
# number "{i}" ') will execute followed by the 'break' statement. When the 'break'
# statement is executed, the for-loop stops iterating through the rest of the nums list
# values.

nums=[1,2,3,4,5,6,7,8,9]

for i in nums:
    if i==5:
        print(f'\n{i}: I found number "{i}" ')
        break
    print(f'\n{i}')
    
'''----------------------------------------------------------------'''

# In this example the for-loop will cycle through the nums list, containing real integer
# values. When it encounters the 'if i==5:' statement, the 'print' statement (f'\n{i}: I
# found number "{i}" ') will execute followed by the 'continue' statement. When the
# 'continue' statement is executed, the for-loop runs its complete iteration through the
# nums list values.

nums=[1,2,3,4,5,6,7,8,9]

for i in nums:
    if i==5:
        print(f'\n{i}: I found number "{i}" ')
        continue
    print(f'\n{i}')
    
'''----------------------------------------------------------------'''

# In this example the for-loop will cycle through the dictionary_list key value's values.
# The key value "Animals" points to four values ['Dog','Cat','Bird','Fish]. When the first
# for-loop ends, the second for-loop will cycle through the key value "Reptiles", which
# points to four values ['Turtle','Lizard','Snake','Frog']. When the second for-loop ends, 
# the third for-loop will cycle through the key value "Insects", which points to four
# values ['Butterfly','Beetle','Ant','Bee'].

dictionary_list=(
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

for values in range(4):
    print(dictionary_list['Animals'][values])
    
for values in range(4):
    print(dictionary_list['Reptiles'][values])
    
for values in range(4):
    print(dictionary_list['Insects'][values])
    
'''----------------------------------------------------------------'''

# In this example the for-loop will cycle through each of the dictionary_list key value's
# only. The 'print' statement 'print(key,value[0])' only prints out the first item of every
# key value's value. For example: the key value 'Animals' will only access the value 
# 'Dog', then the for-loop will cycle over again to the next key value 'Reptiles', which
# again will only access the value 'Turtle'. The final for-loop will cycle through the
# dictionary_list key value 'Insects', which, once again will only access the value
# 'Butterfly'. However each of these key values are also printed along the left side of
# the values; example: "Animals Dog", "Reptiles Turtle", "Insects Butterfly". If you 
# change the 'print' statement's value 'value[0]' to 'value[1]' the for-loop will only
# access the values "Animals Cat", "Reptiles Lizard", "Insects Beetle". Now, if you
# change the 'print' statement's value to 'value[2]' the "Animals key value will become
# "Animals Bird" and "Reptiles key value will become "Reptiles Snake" and Insects
# key value will become "Insects Ant". If you change the 'print' statement's value to
# 'value[3]', the last items in the key value's value will look like this:

# "Animals Fish", "Reptiles Frog" and "Insects Bee". Try changing the 'print'
# statement 'value[number]' and see what happens when you execute/run the
# program.

dictionary_list=(
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

for key,value in dictionary_list.items():
    print(key,value[0])
    
'''----------------------------------------------------------------'''

# Take a very close look at the program example below. It's like a for-loop but it's a
# manual-loop. You decide how long this manual-loop will manually be. Take a close
# look at the highlighted 'iter' function and the highlighted 'next' function in the 'print'
# statements. These functions are what make this manual-loop possible. However, if
# you want to add more 'print' statements with 'next' functions in them, you also need
# to add more values inside the variable. For example, the variable 'book' has the
# values of the name of this book. Type and execute/run the program example below;
# add more values, change values and see what happens each time you re-xecute/run
# the program.

book=('Python',"Programmer's",'Glossary','Bible')

manual_loop=iter(book)
print(next(manual_loop),end=' ')
print(next(manual_loop),end=' ')
print(next(manual_loop),end=' ')
print(next(manual_loop))

'''----------------------------------------------------------------'''

# For-loops can have other for-loops nested inside them, called a 'Nest'. The main,
# outer for-loop repeats one whole cycle through, while the nested, inner for-loop
# repeats its entire cycles through on each cycle of the main, outer for-loop. On the
# next cycle of the main, outer for-loop, the nested, inner for-loop repeats its entire
# cycles all over again.

for i in range(3):
    print(f'\nRepeat main loop "for i in range({i}):" cycles.\n')
    for x in range(4):
        print(f'Repeat nest loop "for x in range({x}):" cycles.')
