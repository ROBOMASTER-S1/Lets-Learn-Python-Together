# Copy then save the file as 'Def Funk Demo.py'
# Next double-click to open the file called 'Def Funk Demo'
# to see how the os colours work with text.

# Import the os module

import os

# The os module sets the os.system colours with the
# following code. You can also use os.system(''), without
# a title. You can name the title any name you wish, but
# you must invoke the word 'title', along with the chosen
# name

os.system('title Functions and OS Colour Demo')

# The variable 'text_colours' stores 7 os colour values.
# along with their commented indexes and their os colour
# values descriptions.

text_colours=(   
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

#1 Def example with text

def name(
    name1='Python',
    name2='Programmer\'s',
    name3='Glossary',
    name4='Bible'
    ):

    return f'\n{text_colours[0]}{name1} \
{text_colours[1]}{name2} {text_colours[2]}{name3} \
{text_colours[3]}{name4} {text_colours[4]}is the best.'

print(name())

print(name('Monty Python'))

print(name('Monty Python','the program'))

#2 Def example with integers

def math(num1,num2,name='Integers'):
    return f'\n{text_colours[2]}{name} {text_colours[1]}\
{num1+num2} {text_colours[0]}and {text_colours[3]}\
{num1-num2}'

print(math(4,3))

print(math(4,3,'Numbers'))

# to stop the file from closing on its own after program
# execution, simply use an 'input' function so you can deside
# when you want to let the program close.

input(f'\n{text_colours[6]}Press (Enter) to close the idle window.')
