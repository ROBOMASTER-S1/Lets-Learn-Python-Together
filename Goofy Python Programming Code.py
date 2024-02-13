# Hardcore Goofy Python Programming Code that actually works

# I don't recommend that you program in this sort of fashion.
# The program does work fine, but other programmers wouldn't
# be able to make sense of it, when they have to take over the nightshift.
# Programmers call this type of coding: 'DIRTY CODE PROGRAMMING'

# Python is a very forgiving language that you can do this sort of thing
# as you can clearly see below. However, it looks quite confusing and
# very intimidating to new programmers, who want to learn to write code.
# So, execute/run this Python program below, but do not take it to school or
# work. However, this program will teach you some of the innards of Python
# in general; the things you can do with it, as well as finding its own flaws.
# Python has some flaws in it, but they only show up once in a while. Python
# executes from the top, downward; the same way the programmer had written
# it down on each line. Therefore, other commands might not execute right
# if some of the programming code is not in the right, top/down order the
# programming list has to be in for Python to work properly. You will learn
# this as you encounter it as you journey into computer programming, and
# beyond it.

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

x = []
line_brk='\n'
dline_brk='\n\n'
text=print,input
loop=range

sentence='type a list of five words: '.capitalize(),\
          'you have all'.capitalize(),'items in your list of words.'

for i in loop(1,6):message=text[1](sentence[0]).title().strip();x.append(message)

text[0]()
for j in loop(i):x.sort(),text[0](x[j],end=' ')

text[0](dline_brk+sentence[1],i,sentence[2])
'''
Grocery List Creator Python program

Created by Joseph C. Richardson, GitHub.com

This is a full functional grocery list Python program example to add to my Python book.
Feel free to copy this Python program example if you like. See what you can do with it.
Please enjoy.
'''
import os

text_colours=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

title='title grocery list creator'
clear_screen='cls'
single_line_break='\n'
double_line_break='\n\n'
indent=' '*2
dot_space='.'*3
create_list='vgl'
enter=0
decimal_point=100
button1='y'
button2='n'

textp=print
textm=input

length=len
flt=float
rnd=round

verror=ValueError
ierror=IndexError

sentence=[
f'{single_line_break}{indent}grocery list creator', # index 0

f'''{double_line_break}{indent}Press "Enter" after each grocery list item typed.
{indent}Type "vgl", then press "Enter" to view your grocery list output.''', # index 1

f'{double_line_break}{indent}Please type your grocery list items: ', # index 2

f'{double_line_break}{indent}Please type your grocery list item price: $', # index 3

f'{double_line_break}{indent}{text_colours[5]}You have', # indext 4

'items in your grocery list.', # index 5

f'{double_line_break}{indent}Here is your grocery list output:', # index 6

f'{single_line_break}{indent}Your grocery list total:', # index 7

f'''{single_line_break}{indent}Do you wish to add more items to your grocery list?
{single_line_break}{indent}Press "y" or "n" to confirm: ''', # index 8

f'{single_line_break}{indent}Thank you for choosing Grocery List Creator... \
Press "Enter" to exit.', # index 9
]

user_textm_item_data,user_textm_price_data=[],[]

user_textm_item_data.append(enter)
user_textm_price_data.append(enter)

os.system(title.title())

def items_list():

    while True:
        os.system(clear_screen)
        grocery_list=textm(text_colours[5]+sentence[0].title()
        +sentence[1]+sentence[2]).strip()
        user_textm_item_data.append(grocery_list)

        if grocery_list==create_list:
            user_textm_item_data.remove(create_list)
            item=user_textm_item_data
            item.remove(enter);break

        try:
            os.system(clear_screen)
            item_price=flt(textm(sentence[0].title()
            +sentence[1]+sentence[3]).strip())
            user_textm_price_data.append(item_price)
        except verror:user_textm_price_data.append(0)

    while True:
        os.system(clear_screen)
        textp(sentence[0].title()+sentence[6])

        try:            
            x=1
            for i in item:
                textp(f'{single_line_break}{indent}{x}) {dot_space} {i} \
${user_textm_price_data[x]/decimal_point}'.title())
                x+=1
        except ierror:item.remove(enter)

        total_sum=user_textm_price_data
        
        textp(f'{sentence[7]}{text_colours[1]} ${sum(total_sum)/decimal_point}',
              sentence[4],length(item),sentence[5])

        grocery_list=textm(sentence[8]).lower().strip()

        user_textm_item_data.append(enter)

        if grocery_list==button1:items_list();break
        
        elif grocery_list==button2:break

items_list()
os.system(clear_screen)
textm(text_colours[6]+sentence[9])
