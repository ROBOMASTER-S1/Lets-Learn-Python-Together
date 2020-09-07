# Advanced List and Dictionary examples

# Please note: these list and dictionary examples don't
# have any comments, other than these seven comments
# only. However, I will be adding lots of comments to these
# advanced list and dictionary examples when I update my
# Python book: "Python Programmer's Glossary Bible". Until
# then, experiment with these list and dictionary examples.

dictionary_list={
    'Animals':['Dog','Cat','Bird','Fish'],
    
    'Reptiles':['Turtle','Lizard','Snake','Frog'],
    
    'Insects':['Butterfly','Beetle','Ant','Bee']
    }

for values in range(4):
    print(dictionary_list['Animals'][values])
    
for values in range(4):
    print(dictionary_list['Reptiles'][values])
    
for values in range(4):
    print(dictionary_list['Insects'][values])
    
'''----------------------------------------------------------------'''

dictionary_list={
    'Animals':['Dog','Cat','Bird','Fish'],
    
    'Reptiles':['Turtle','Lizard','Snake','Frog'],
    
    'Insects':['Butterfly','Beetle','Ant','Bee']
    }

for key,value in dictionary_list.items():
    print(key,value[2])

'''----------------------------------------------------------------'''

min_nums_list=min(0,1,2,3,4,5,6,7,8,9)

print(min_nums_list)

max_nums_list=max(0,1,2,3,4,5,6,7,8,9)

print(max_nums_list)

'''----------------------------------------------------------------'''

enumerate_list=[
    'Value index ','Value index ',
    
    'Value index ','Value index '
    ]

for index,value in enumerate(enumerate_list):
    print(value,index)

'''----------------------------------------------------------------'''

search_in_list=[
    'Value 0','Value 1',
    
    'Value 2','Value 3'
    ]

print('Value 1' in search_in_list)

'''----------------------------------------------------------------'''

extend_list1=[
    'Value 0','Value 1',
    
    'Value 2','Value 3'
    ]

extend_list2=[
    'Value 4','Value 5',
    
    'Value 6','Value 8'
    ]

extend_list1.extend(extend_list2)

print(extend_list1)

'''----------------------------------------------------------------'''

append_list1=[
    'Value 0','Value 1',
    
    'Value 2','Value 3'
    ]

append_list2=[
    'Value 4','Value 5',
    
    'Value 6','Value 8'
    ]

append_list1.append(append_list2)

print(append_list1)

'''----------------------------------------------------------------'''

clear_list_value=[
    'Value 0','Value 1',
    
    'Value 2','Value 3'
    ]

clear_list_value.clear()

print(clear_list_value)

'''----------------------------------------------------------------'''

del_list_value=[
    'Value 0','Value 1',
    
    'Value 2','Value 3'
    ]

del del_list_value[2]

print(del_list_value)

'''----------------------------------------------------------------'''

remove_list_value=[
    'Value 0','Value 1',
    
    'Value 2','Value 3'
    ]

remove_list_value.remove('Value 2')

print(remove_list_value)

'''----------------------------------------------------------------'''

pop_list_value=[
    'Value 0','Value 1',
    
    'Value 2','Value 3'
    ]

pop_list_value.pop()

print(pop_list_value)

'''----------------------------------------------------------------'''

insert_list_value=[
    'Value 0','Value 1',
    
    'Value 2','Value 3'
    ]

insert_list_value.insert(4,'Value 4')

print(insert_list_value)

'''----------------------------------------------------------------'''

sort_list_value=[
    'Value 0','Value 1',
    
    'Value 2','Value 3'
    ]

sort_list_value.sort()

print(sort_list_value)

'''----------------------------------------------------------------'''

sorted_list_value=[
    'Value 0','Value 1',
    
    'Value 2','Value 3'
    ]

sorted_list_value=sorted(sorted_list_value)

print(sorted_list_value)

'''----------------------------------------------------------------'''

reverse_list_value=[
    'Value 0','Value 1',
    
    'Value 2','Value 3'
    ]

reverse_list_value.reverse()

print(reverse_list_value)

'''----------------------------------------------------------------'''

reverse_list_value=[
    'Value 0','Value 1',
    
    'Value 2','Value 3'
    ]

reverse_list_value.sort(reverse=True)

print(reverse_list_value)

reverse_list_value.sort(reverse=False)

print(reverse_list_value)

'''----------------------------------------------------------------'''

split_string="Let's split up a string"

print (split_string.split('split'))

'''----------------------------------------------------------------'''

split_list='split split split split'

print (split_list.split('split',0))
print (split_list.split('split',1))
print (split_list.split('split',2))
print (split_list.split('split',3))
print (split_list.split('split',4))

'''----------------------------------------------------------------'''

list_set=[
    'string value1',
    'string value2',
    'string value3']

print(list_set)

join_string='--join--'.join(list_set)

print(join_string)

'''----------------------------------------------------------------'''

# Create a tuple list with an 'IndexError' handler. If a value is not
# found, then the 'try' and 'except IndexError' handler will execute.
# If a value is found, the 'try' and 'except IndexError' handler are
# ignored, but the 'finally' statement will always execute no matter
# the outcome.

tuple_list=(
    'Value pos:0','Value pos:1',
    'Value pos:2','Value pos:3',
    'Value pos:4','Value pos:5',
    'Value pos:6','Value pos:7',
    'Value pos:8','Value pos:9',
    'Value pos:10','Value pos:11',
    'Value pos:12','Value pos:13',
    'Value pos:14','Value pos:15'
    )

try:
    print(tuple_list[16])
except IndexError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')
    
'''---------------------------------------------------------'''

# Create a single list with an 'IndexError' handler. If a value is not
# found, then the 'try' and 'except IndexError' handler will execute.
# If a value is found, the 'try' and 'except IndexError' handler are
# ignored, but the 'finally' statement will always execute no matter
# the outcome.

single_list=[
    'Value pos:0','Value pos:1',
    'Value pos:2','Value pos:3',
    'Value pos:4','Value pos:5',
    'Value pos:6','Value pos:7',
    'Value pos:8','Value pos:9',
    'Value pos:10','Value pos:11',
    'Value pos:12','Value pos:13',
    'Value pos:14','Value pos:15'
    ]

try:
    print(single_list[16])
except IndexError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')

'''---------------------------------------------------------'''

# Extend the single_list1 and the single_list2 with the '.extend()'
# function. Once again, If a value is not found, then the 'try' and
# 'except IndexError' handler will execute. If a value is found, the
# 'try' and 'except IndexError' handler are ignored, but the 'finally'
# statement will always execute no matter the outcome.

single_list1=[
    'Value pos:0','Value pos:1',
    'Value pos:2','Value pos:3',
    'Value pos:4','Value pos:5',
    'Value pos:6','Value pos:7',
    'Value pos:8','Value pos:9',
    'Value pos:10','Value pos:11',
    'Value pos:12','Value pos:13',
    'Value pos:14','Value pos:15'
    ]

single_list2=[
    'Value pos:0','Value pos:1',
    'Value pos:2','Value pos:3',
    'Value pos:4','Value pos:5',
    'Value pos:6','Value pos:7',
    'Value pos:8','Value pos:9',
    'Value pos:10','Value pos:11',
    'Value pos:12','Value pos:13',
    'Value pos:14','Value pos:15'
    ]

single_list1.extend(single_list2)

try:
    print(single_list1[32])
except IndexError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')

'''---------------------------------------------------------'''

# Create a multi dimensional list with an 'IndexError' handler. If a
# value is not found, then the 'try' and 'except IndexError' handler
# will execute. If a value is found, the 'try' and 'except IndexError'
# handler are ignored, but the 'finally' statement will always execute
# no matter the outcome.

multi_dim_list=[
    ['Value pos:0','Value pos:1','Value pos:2','Value pos:3'],
    ['Value pos:4','Value pos:5','Value pos:6','Value pos:7'],
    ['Value pos:8','Value pos:9','Value pos:10','Value pos:11'],
    ['Value pos:12','Value pos:13','Value pos:14','Value pos:15']
    ]

try:
    print(multi_dim_list[0][4])
except IndexError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')
    
'''---------------------------------------------------------'''

import os;os.system('')

text_colours=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

knowledge_poem=(
f'''\n{text_colours[5]}‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.

THIS BELONGS TO EVERY MAN, WOMAN AND CHILD
Never give up your dream, no matter how far away it may seem to be, because that is when it is ever so
close to becoming true. If you dream of something long enough and strong enough, your dream will come
true, when you least expect it. Always remember, we are never too young or too old to dream and use our
imagination, for we only get one and it is ours forever. May your heart be filled with courage and
compassion, and your mind be as limitless and as wondrous as the universe itself!
If you dream it, you can be it. Believe it!\n'''
)

print(knowledge_poem)

letter=input(f'{text_colours[1]}Type a word or letter from this poem, and I will tell you how many \
times it\'s been used in it.\nNote: words and letters are case sensitive. ')

if len(letter)>=2:
    print(f'\n{text_colours[2]}The word " {letter} " has been used {knowledge_poem.count(letter)} times in this poem.')

elif len(letter)<=2:
    print(f'\n{text_colours[2]}The letter " {letter} " has been used {knowledge_poem.count(letter)} times in this poem.')   
    
input(f'\n{text_colours[6]}End of knowledge_poem.count program example. Press Enter to close.')

'''---------------------------------------------------------'''

# Create a dictionary with a 'KeyError' handler. If a value is not found,
# then the 'try' and 'except KeyError' handler will execute. If a value is
# found, the 'try' and 'except IndexError' handler are ignored, but the
# 'finally' statement will always execute no matter the outcome.

dict_key={
    'key:0':'Value:0','key:1':'Value:1',
    'key:2':'Value:2','key:3':'Value:3',
    'key:4':'Value:4','key:5':'Value:5'
    }

try:
    print(dict_key['key:6'])
except KeyError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')

'''---------------------------------------------------------'''

# The '.get()' function does exactly the same thing as the 'try' and 'except
# KeyError' handler does. However, the '.get()' function works with
# dictionaries only.

dict_key={
    'key:0':'value:0','key:1':'value:1',
    'key:2':'value:2','key:3':'value:3',
    'key:4':'value:4','key:5':'value:5'
    }

print(dict_key.get('key:6','Value not found.'))

'''---------------------------------------------------------'''

# The '.update({})' function updates the dictionary's keys and values alike.
# Notice how the '.get()' function is still being used instead of the 'try' and
# 'except KeyError' handler. However, in some cases it's a good idea to use
# error handlers.

dict_key.update({
    'key:0':'New value','key:1':'value:1',
    'key:2':'value:2','key:3':'value:3',
    'key:4':'value:4','key:5':'value:5'
    })

print(dict_key.get('key:0','Value not found.'))

'''---------------------------------------------------------'''

# key example 1:

key_example={
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

print(key_example[1])
print(key_example[2])
print(key_example[3])
print(key_example[4])
print(key_example[5])
print(key_example[6])
print(key_example[7])
print(key_example[8])


# key example 2:

key_example={
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

print(key_example[1],end=' ')
print(key_example[2],end=' ')
print(key_example[3],end=' ')
print(key_example[4],end=' ')
print(key_example[5],end=' ')
print(key_example[6],end=' ')
print(key_example[7],end=' ')
print(key_example[8],end=' ')

'''---------------------------------------------------------'''

# Get key example 1:

key_example={
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

print(key_example.get(1))
print(key_example.get(2))
print(key_example.get(3))
print(key_example.get(4))
print(key_example.get(5))
print(key_example.get(6))
print(key_example.get(7))
print(key_example.get(8))

print(key_example.get(9))

print(key_example.get(9,'Key Not Found!'))

'''---------------------------------------------------------'''

# Get key example 2:

key_example={
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

print(key_example.get(1),end=' ')
print(key_example.get(2),end=' ')
print(key_example.get(3),end=' ')
print(key_example.get(4),end=' ')
print(key_example.get(5),end=' ')
print(key_example.get(6),end=' ')
print(key_example.get(7),end=' ')
print(key_example.get(8),end=' ')

print(key_example.get(9),end=' ')

print(key_example.get(9,'Key Not Found!'),end=' ')

'''---------------------------------------------------------'''

# For-loop key example 1:

key_example={
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,9):
    print(key_example[i])

'''---------------------------------------------------------'''

# For-loop key example 2:

key_example={
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,9):
    print(key_example[i],end=' ')

'''---------------------------------------------------------'''

# For-loop get key example 1:

key_example={
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,11):
    print(key_example.get(i,'Key Not Found!'))
    
'''---------------------------------------------------------'''

# For-loop get key example 2:

key_example={
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,11):
    print(key_example.get(i,'Key Not Found!'),end=' ')
    
'''---------------------------------------------------------'''

# For-loop get key example 3:

key_example={
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,11):
    print(key_example.get(i,'Key '+str(i)+' Key Not Found!'),end=' ')

'''---------------------------------------------------------'''

# For-loop get key example 4:

key_example={
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,11):
    print(key_example.get(i,'Key {} Key Not Found!'.format(i)),end=' ')
    
'''---------------------------------------------------------'''

# For-loop get key example 5:

key_example={
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,11):
    print(key_example.get(i,f'Key {i} Key Not Found!'),end=' ')
    
'''---------------------------------------------------------'''

# Unpack multi-dictionary key example:

key_nums,key_letters,key_words=(

{0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9},

{'a':'a','b':'b','c':'c','d':'d','e':'e',
 'f':'f','g':'g','h':'h','i':'i','j':'j','k':'k',
 'l':'l','m':'m','n':'n','o':'o','p':'p',
 'q':'q','r':'r','s':'s','t':'t','u':'u',
 'v':'v','w':'w','x':'x','y':'y','z':'z'},

{'P1':'"Python','P2':"Programmer's",
 'G':'Glossary','B':'Bible"'}
)

print(key_nums[5])

print(key_nums.get(5)) # Add optional custom keyword/keywords.

print(key_nums.get(5,'Not Found!'))

print(key_letters['a'])

print(key_letters.get('a')) # Add optional custom keyword/keywords. 

print(key_letters.get('a','Not Found!'))

print(
    key_words['P1'],
    key_words['P2'],
    key_words['G'],
    key_words['B']
    )

print(
    key_words.get('P1','Not Found!'),
    key_words.get('P2','Not Found!'),
    key_words.get('G','Not Found!'),
    key_words.get('B','Not Found!')
    )

'''---------------------------------------------------------'''

# Unpack multi-dictionary key for-loop example:

key_nums,key_letters,key_words=(

{0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9},

{'a':'a','b':'b','c':'c','d':'d','e':'e','f':'f',
 'g':'g','h':'h','i':'i','j':'j','k':'k', 'l':'l',
 'm':'m','n':'n','o':'o','p':'p', 'q':'q','r':'r',
 's':'s','t':'t','u':'u','v':'v','w':'w','x':'x',
 'y':'y','z':'z'},

{'P1':'"Python','P2':"Programmer's",
 'G':'Glossary','B':'Bible"'}
)

for i in key_nums,key_letters,key_words:
    print(i)
