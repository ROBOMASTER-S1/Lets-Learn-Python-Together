'''Minute Python Program Examples'''

# Python's Random Generator Module

# Created by Joseph C. Richardson, GitHub.com

# Let's have some random fun with Python's Random Generator Module
# But first, let's 'import' the random generator module so we can use it
# and have some fun with it.

# Please note: numpy random generator functions aren't shown here.
# Only those that use Python's built-in Random Generator are shown here.

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

import random

# Let's call a random number with our first random generator example,
# using the 'random.randint()' function.

random_num=random.randint(1,9)
print(random_num)

# Let's try the 'random.shuffle()' function

shuffle_nums_list=[1,2,3,4,5,6,7,8,9]
rand_shuffle=random.shuffle(shuffle_nums_list)
print(shuffle_nums_list[0])

# Let's try using words in our 'random.shuffle()' function and see what
# happens.

shuffle_words_list=[
    'Random Value 1',
    'Random Value 2',
    'Random Value 3',
    'Random Value 4',
    'Random Value 5']

rand_shuffle=random.shuffle(shuffle_words_list)
print(shuffle_words_list[0])

# Let's try the 'random.choice()' function

random_nums_choice_list=[1,2,3,4,5,6,7,8,9]
random_choice=random.choice(random_nums_choice_list)
print(random_choice)

# Let's try using words in our 'random.choice()' function and see what
# happens.

random_words_choice_list=[
    'Random Value 1',
    'Random Value 2',
    'Random Value 3',
    'Random Value 4',
    'Random Value 5']

random_choice=random.choice(random_words_choice_list)
print(random_choice)

# Now, let's try the 'random.choices()' function

random_nums_choice_list=[1,2,3,4,5,6,7,8,9]

print(random.choices(random_nums_choice_list,
weights=[100,80,70,60,50,40,30,20,10],k=8)[0])

# Let's try using words in our 'random.choices()' function and see what
# happens.

random_words_choices_list=[
    'Random Value 1',
    'Random Value 2',
    'Random Value 3',
    'Random Value 4',
    'Random Value 5']

print(random.choices(random_words_choices_list,
weights=[100,80,70,60,50],k=8)[0])

# The beauty of the 'random.choices()' function is that you can increase
# or decrease the odds of how many times a random value will show up
# in the screen output verses the random values, who's odds are much
# lower, due to the 'weights' implementer.

# Other uses of Python's Random Generator are as follows:

random.seed(10)
print(random.random())

random.seed(10)
print(random.getstate())

print(random.getrandbits(4))

print(random.random())

# capture the state:

state=random.getstate()

# print another random number:

print(random.random())

# restore the state:

random.setstate(state)

# and the next random number should be
# the same as when you captured the state:

print(random.random())
'''----------------------------------------------------------------'''
# This conditional while-loop example compares a random number
# against user input data. If the user picks the right number by luck
# alone, the while-loop will break out and the program ends. If the
# user picks the wrong number, the less (<) than or greater (>) than
# 'random_num' variable gets conditioned and the while-loop keeps
# on iterating until the right number is picked, via user input data.

# Note: Python executes/runs programs starting from the top, downward.
# Be very careful on how you place statements. Some statements
# cannot execute right, even if they work. This is simply because of
# the order that Python executes/runs its program statements.

# Note: The 'import random' module must be imported first.

import random

random_num=random.randint(1,10)

while True:
    try:
        pick_num=int(input('\nWhat number am I thinking of? Hint! It\'s \
between 1 and 10: ').strip())
        
        if pick_num<random_num:
            print('\nThe number I\'m thinking of is too low!')
            
        elif pick_num>random_num:
            print('\nThe number I\'m thinking of is too high!')
            
        elif pick_num==random_num:
            print(f'\nCongratulations! You won. "{random_num}" was the \
number I was thinking of.')
            break
        
    except ValueError:
        print('\nYou must type integers only please!')
'''----------------------------------------------------------------'''
# This very same program example as above works exactly the same
# way, but with one major difference; the while loop will only iterate three
# times. If the user picks the right number, the while loop breaks. If the
# user doesn't pick the right number after three times, the 'else' statement
# executes and says 'Sorry! You lost.', which ends the program.

# Note: the 'import random' module must be imported first.

import random

random_num=random.randint(1,10)

i=0

while i<3:
    try:
        pick_num=int(input('\nWhat number am I thinking of? Hint! It\'s \
between 1 and 10: ').strip())
        
        i+=1
        
        if pick_num<random_num:
            print('\nThe number I\'m thinking of is too low!')
            
        elif pick_num>random_num:
            print('\nThe number I\'m thinking of is too high!')
            
        elif pick_num==random_num:
            print(f'\nCongratulations. You won! "{random_num}" was the number \
I was thinking of.')            
            break
        
    except ValueError:
        print('\nYou must type integers only please!')
        
else:
    print('\nSorry. You lost!')
'''----------------------------------------------------------------'''
# Once again, this is the very same program example as above before.
# However, this time the loop iterates in reverse instead of forward and
# the user is shown how many guesses they have left before they win or
# lose.

# Note: the 'import random' module must be imported first.

import random

random_num=random.randint(1,10)

i=3

while i>0:
    try:
        pick_num=int(input(f'\nWhat number am I thinking of? Hint! It\'s \
between 1 and 10:\n\nYou have {i} gesses left. ').strip())
        
        i-=1
        
        if pick_num<random_num:
            print('\nThe number I\'m thinking of is too low!')
            
        elif pick_num>random_num:
            print('\nThe number I\'m thinking of is too high!')
            
        elif pick_num==random_num:
            print(f'\nCongratulations. You won! "{random_num}" was the number \
I was thinking of.')
            break
        
    except ValueError:
        print('\nYou must type integers only please!')
        
else:
    print('\nSorry. You lost!')
