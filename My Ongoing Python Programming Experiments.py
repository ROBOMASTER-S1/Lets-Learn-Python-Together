# My Ongoing Python Programming Experiments

# You can do a lot with for loops. I practice Python everyday and I'm
# always tripping onto things, just by trial and error alone. I wasn't
# shown this at all. This is one of my own happy accidents. I got really
# bored and did this for us all.

names1 = ['Bob','Rob','dog','cat']
names2 = ['John','Tom','bird','fish']
names3 = ['Terry','Mary','turtle','monkey']

for i,x,y,z in names1,names2,names3:
    print('Hello',i+'. How are you? You bought a cute',y,'I see...')
    print('Hello',x+'. How are you? You bought a cute',z,'I see...')
    
''''''''''''''''''''''''''''''''''''''''''''''''''''''
names1 = ['Bob','Rob','dog','cat']
names2 = ['John','Tom','bird','fish']
names3 = ['Terry','Mary','turtle','monkey']

sentence= 'Hello','. How are you? You bought a cute','I see...'

for i,x,y,z in names1,names2,names3:
    print(sentence[0],i+sentence[1],y,sentence[2])
    print(sentence[0],x+sentence[1],z,sentence[2])

''''''''''''''''''''''''''''''''''''''''''''''''''''''
names1 = ['Bob','Rob','dog','cat']
names2 = ['John','Tom','bird','fish']
names3 = ['Terry','Mary','turtle','monkey']

sentence = 'Hello','. How are you? You bought a cute','I see...'

for i,x,y,z in names1,names2,names3:
    print('{} {} {} {}'.format(sentence[0],i+sentence[1],y,sentence[2])) # The old formated example:
    print('{} {} {} {}'.format(sentence[0],x+sentence[1],z,sentence[2]))

''''''''''''''''''''''''''''''''''''''''''''''''''''''
names1 = ['Bob','Rob','dog','cat']
names2 = ['John','Tom','bird','fish']
names3 = ['Terry','Mary','turtle','monkey']

sentence = 'Hello','. How are you? You bought a cute','I see...'

for i,x,y,z in names1,names2,names3:
    print(f'{sentence[0]} {i}{sentence[1]} {y} {sentence[2]}') # The new f' formated example:
    print(f'{sentence[0]} {x}{sentence[1]} {z} {sentence[2]}')

''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's play with the zip function()

list1 = ['zip 1','zip 2','zip 3','zip 4']
list2 = ['zip 5','zip 6','zip 7','zip 8']

zip_list = zip(list1,list2)

for i in zip_list:
    print(i)
    
# or this:

list1 = ['zip 1','zip 2','zip 3','zip 4']
list2 = ['zip 5','zip 6','zip 7','zip 8']

zip_list = zip(list1,list2)

for i in zip_list:
    print(i[0])

# or this:

list1 = ['zip 1','zip 2','zip 3','zip 4']
list2 = ['zip 5','zip 6','zip 7','zip 8']

zip_list = zip(list1,list2)

for i in zip_list:
    print(i[1])

# or this:

list1 = ['zip 1','zip 2','zip 3','zip 4']
list2 = ['zip 5','zip 6','zip 7','zip 8']

zip_list = zip(list1,list2)

for i in zip_list:
    print(i[0])
    print(i[1])

''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's play with the enumerate function()

list1 = ['enumerate 1','enumerate 2','enumerate 3','enumerate 4']
list2 = ['enumerate 5','enumerate 6','enumerate 7','enumerate 8']

x,y = enumerate(list1),enumerate(list2)

print(tuple(x))
print(list(y))

# or this:

list1 = ['enumerate 1','enumerate 2','enumerate 3','enumerate 4']
list2 = ['enumerate 5','enumerate 6','enumerate 7','enumerate 8']

x,y = enumerate(list1),enumerate(list2)

print(dict(x))
print(set(y))
