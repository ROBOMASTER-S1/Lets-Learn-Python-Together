'''While-loop Examples:'''
'''
While-loops are conditional loops that end when a certain condition is met, or when \
a certain value is found to be true. In Python, while-loops also work in conjunction \
with 'If' and 'Elif' and 'Else' statements.
'''
# Here is just one example of a conditional while-loop, which counts, starting from 0 to
# 9 with a 'print' statement using the (f') format along withthe words 'Count Loop!', with
# a loop conditional value of 10. As long # as (i) is less (<) than 10, the while-loop will
# keep on looping until (i) is equal to 10.

i=0
while i<10:
    print(f'\nCount Loop! "{i}" ')
    i+=1
    
'''-----------------------------------------------------------------------------'''

# This conditional while-loop example will never ever stop looping, until the user
# presses either "y" or "n" followed by pressing the "Enter" key to confirm. If the user
# presses any other key except "y" or "n", the conditional while loop will keep on
# looping forever. After the while-loop gets broken, the final 'print' statement ('"Yay!"
# You broke the while-loop example.') will execute/run, which ends the conditional
# while-loop example. You can add as many 'if' and 'elif' statements you like within a 
# while-loop. Note: these two 'break' statements causes the while-loop to stop looping.
# If the 'break' statements weren't used, the while-loop would just keep on going
# forever, making the user press the same keys forever. All loops must come to an
# end, such as for-loops and conditional while-loops alike. If a loop is infinite, running
# away, the program and/or computer will eventually crash. It's important to make 
# sure loops always break out or end when a certain condition is met, such as in this
# conditional while-loop example.

# The '.strip()' function clears away unwanted white spaces, via user input data.

while True:
    Letter=input('\nYou must press "y" or "n" then press (ENTER) to break out of this \
conditional while-loop example: ').strip()
    
    if Letter==('y'):
        print('\nThe "y" key was pressed and the while-loop breaks.')
        break
    
    elif Letter==('n'):
        print('\nThe "n" key was pressed and the while-loop breaks.')
        break
    
print('\n"Yay!" You broke out of the while-loop example.')

'''-----------------------------------------------------------------------------'''

# This conditional while-loop example will never ever stop looping, until the user
# presses "y" followed by the "Enter" key to confirm. If the user presses any other key
# except "y", the conditional while-loop will keep on looping forever. After the while-
# loop gets broken, the final 'print' statement (f'You gave me "{letter}", so I broke out
# of the conditonal while loop example.') will execute/run. Now if the user doesn't
# press the right key, either less (<) than "y" or greater (>) than "y", the key 
# mapping range will always execute/run the 'print' statement (f'Oops! You give me
# "{letter}", so I won\'t stop this condional while-loop example, until you give me "y".'),
# and the loop keeps on iterating over and over, until the user presses 'y'. After the
# while-loop gets broken, the final 'print' statement ('This is the end of the entire
# conditional while-loop example.') will execute/run.

# Note: Python executes/runs programs starting from the top, downward. Be very
# careful on how you place statements. Some statements cannot execute right, even if
# they work. This is simply because of the order that Python executes/runs its program
# statements.

while True:
    letter=input('\nGive Me "y": ').strip()
    if letter=='y':
        print(f'\nYou gave me "{letter}", so I broke out of the conditonal \
while-loop example.')
        break
    
    elif letter<'y' or letter>'y':
        print(f'\nOops! You give me "{letter}", so I won\'t stop this condional \
while-loop example, until you give me "y".')
        
print('\nThis is the end of the entire conditional while-loop example:')

'''-----------------------------------------------------------------------------'''

# This conditional while-loop example will never ever stop looping, until the user types
# the number "10" followed by pressing the "Enter" key to confirm. If the user types
# any other number keys except "10", the conditional while-loop will keep on looping
# forever. After the while-loop gets broken, the final 'print' statement ('This is the end
# of the entire conditional while-loop example.') will execute/run.

# Note: the 'int' statement is for integer values only.

# Note: Python executes/runs programs starting from the top, downward. Be very
# careful on how you place statements. Some statements cannot execute right, even if
# they work. This is simply because of the order that Python executes/runs its
# program statements.

while True:
    number=int(input('\nGive Me "10": ').strip())
    if number==10:
        print(f'\nYou gave me "{number}", so I broke out of the conditonal \
while-loop example.')
        break
    
    elif number<10:
        print(f'\nOops! You give me "{number}", which is too small. I won\'t \
stop this condional while-loop example, until you give me "10".')
        
    elif number>10:
        print(f'\nOops! You give me "{number}", which is too big. I won\'t stop \
this condional while-loop example, until you give me "10".')

print('\nThis is the end of the entire conditional while-loop example:')
