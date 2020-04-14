# This program example has three, separate conditional while-loops, each of them
# compares data against user input data. The first while-loop asks for the user's first
# name. The second while-loop asks for the user's last name, and the third while-loop
# asks for the user's age. In the first and second while-loop, the user's first name and
# user's last name are compared by how many letters the user types. The 
# '<str([first_name])' statement makes the user type in text only, not integers.

# Note: Python executes/runs programs starting from the top, downward. Be very
# careful on how you place statements. Some statements cannot execute right, even if
# they work. This is simply because of the order that Python executes/runs its
# program statements.

while True:
    first_name=input('\nWhat is your name please? ').strip()
    
    if first_name<str([first_name]):
        print('\nError: text only please!')
        
    elif len(first_name)<3:
        print('\nYour first name must be over 2 characters long.')
        
    elif len(first_name)>10:
        print('Your first name must be under 10 characters long.')
        
    else:
        break

while True:
    last_name=input(f'\nNice to meet you {first_name.title()}. \
What is your last name please? ').strip()
    
    if last_name<str([last_name]):
        print('\nError: text only please!')
        
    elif len(last_name)<3:
        print('\nYour last name must be over 2 characters long.')
        
    elif len(last_name)>10:
        print('\nYour last name must be under 10 characters long.')
        
    else:
        break

while True:
    try:
        age=int(input(f'\nHow old are you {first_name.title()}? ').strip())
        break
    
    except ValueError:
        print('\nError: integers only please!')
        
print(f'\nYour first name = {first_name.title()}:\nYour last name = \
{last_name.title()}:\nYour age = {age}:\n')
