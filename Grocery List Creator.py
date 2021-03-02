'''
This is a full functional grocery list Python program example to add to my Python book.
Feel free to copy this Python program example if you like. See what you can do with it.
As time rolls on, I will make this an actual, working program, which the user can place
the price of a grocery list item, while it keeps track of what you will be spending at the
store. The user will also be able to clear the list items or clear just one single list item,
while the price part of the program will work as addition and subtraction of list pricing,
via items added or removed from the shopping list. You are all welcome to copy this
program and make it do and be anything you like. Maybe try and create the list, such as
what I want to make it do down the road. Please enjoy.
'''
import os

title='title Grocery List Creator'
clear_screen='cls'
single_line_break='\n'
double_line_break='\n\n'
indent=' '*2
dot_space='.'*3
create_list='vgl'
button1='y'
button2='n'
enter=''

os.system(title)

sentence=[
f'{single_line_break}{indent}Grocery List Creator', # index 0

f'''{double_line_break}{indent}Press "Enter" after each grocery list item typed.
{indent}Type "vgl", then press "Enter" to view your grocery list output.''', # index 1

f'{double_line_break}{indent}Please type your grocery list items: ', # index 2

f'{single_line_break}{indent}You have', # indext 3

'items in your grocery list.', # index 4

f'{double_line_break}{indent}Here is your grocery list output:', # index 5

f'''{single_line_break}{indent}Do you wish to add more items to your grocery list?
{indent}Press "y" or "n" to confirm: ''' # index 6
]

user_data=set()
user_data.add(enter)

def items_list():
    while True:
        os.system(clear_screen)
        grocery_list=input(sentence[0]\
        +sentence[1]+sentence[2]).strip()
        user_data.add(grocery_list)
        if grocery_list==create_list:
            user_data.remove(create_list)
            convert=list(user_data)
            convert.remove(enter)
            convert.sort()
            break

    while True:
        os.system(clear_screen)
        print(sentence[0]+sentence[5])

        x=1
        for i in convert:
            print(f'{single_line_break}{indent}{x}) {dot_space}',i.title())
            x+=1
            
        print(sentence[3],len(convert),sentence[4])
        grocery_list=input(sentence[6]).lower().strip()
        
        if grocery_list==button1:
            items_list()
            break
        elif grocery_list==button2:
            break
    
items_list()
input('end')
