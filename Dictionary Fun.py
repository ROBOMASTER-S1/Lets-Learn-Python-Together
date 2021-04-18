# Why not have some fun with Dictionaries. Try these
# Python program examples to get a feel of how dictionaries
# in Python work and how useful they truly are in programs.

# Let's create an animals dictionary so we can use its values.

animals={
    'Dog':'Wolf',
    'Cat':'Lion',
    'Bird':'Eagle',
    'Fish':'Shark'
    }

print(animals.get('dog'))
print(animals.get('dog','Not Found!'))
print(animals.get('Dog','Not Found!'))

for key,value in animals.items():
    print(key)

for key,value in animals.items():
    print(value)

for key,value in animals.items():
    print(key,value)

# Let's create some sentences out of our animals dictionary list.

d=animals.get('Dog')
c=animals.get('Cat')
b=animals.get('Bird')
f=animals.get('Fish')

print(f'My dog is really a {d}.')
print(f'My Cat is really a {c}.')
print(f'My Bird is really a {b}.')
print(f'My Fish is really a {f}.')

# Let's create some sentences out of our animals dictionary list
# using a 'for in' items() function to drastically reduce lines of
# code and code redundancy in our Python program example.

for keys,values in animals.items():
    print(f'My {keys} is really a {values}.')

# Rename the key and value variables if you wish.

for my_keys,my_values in animals.items():
    print(f'My {my_keys} is really a {my_values}.')

for animal_keys,animal_values in animals.items():
    print(f'My {animal_keys} is really a {animal_values}.')

# Try this dictionary Python program example below and recap
# what happens when you type and execute/run this program.

animals={
    'Dog':'Wolf',
    'Cat':'Lion',
    'Bird':'Eagle',
    'Fish':'Shark'}

people={              
    'Person1':'John',
    'Person2':'Bob',
    'Person3':'Rob',
    'Person4':'Tom'}

for key,value in animals.items():
    print(key,value)

for key,value in people.items():
    print(key,value)
