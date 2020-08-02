while True:
    try:
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
            
    except ValueError:
        print('\nThe \'try:\' and \'except ValueErorr:\' handlers prevent any unwanted \
value errors from occurring, via user input data.')
        
        print('\nIf the user presses any letter keys instead of pressing number keys, \
the \'try:\' and \'except:\'block executes/runs.')
        
print('This is the end of the entire conditional while-loop example:')

'''----------------------------------------------------------------'''

# This is a basic layout of the 'try and except', 'finally' program example. The program
# does work fine, but it does nothing. The program example below simply shows the
# basic layout of the 'try and except', 'finally' statements. The 'finally' statement is
# executed no matter the outcome the 'try and except' handler block does. Note: you
# can also leave out the 'finally' statement if you like, but it can come in handy if you
# want the final outcome to execute no matter what the 'try and except' handler block
# does. The 'pass' statements are just empty placeholders for the empty code blocks
# until they are needed, via the programmer.

try:
     pass
except:
     pass
else:
     pass
finally:
     pass
    
'''----------------------------------------------------------------'''

# Here is the very same 'try and except' program example below. Type and
# execute/run the program and see what happens.

try:
     message=int(input('Pick a number. ').lower().strip())
except ValueError:
     print('Numbers only please.')
else:
     print('You picked a number.')
finally:
     print("'finally' executed no matter what.")

# The 'finally' statement is executed no matter the outcome the 'try and except'
# handler block does

'''----------------------------------------------------------------'''

# These two 'input' statements in this program example asks the user their name and
# their age, using the 'try:' and 'except:' error handlers.

name=input('\nWhat is your name please? ').lower().strip()

try:
    age=int(input(f'\nHow old are you {name}? ').lower().strip())
    print(f'\n{name}. You are {age} years old.')
    
except ValueError:
    print('\nThe \'try:\' and \'except ValueError:\' block executes/runs whenever a letter \
key is pressed instead of a number key.')
    
'''----------------------------------------------------------------'''

# Now, put this very same program code above into a conditional while-loop and see
# what happens when the user tries to type letters, instead of typing numbers for their
# age. When the 'try:' statement is executed, the 'break' statement causes the
# conditional while-loop to break out and the 'print' statement ('End of program') is
# then executed.

name=input('\nWhat is your name please? ').lower().strip()

while True:
    try:
        age=int(input(f'\nHow old are you {name}? ').lower().strip())
        print(f'\n{name}. You are {age} years old.')
        break
    
    except ValueError:
        print('\nThe \'try:\' and \'except ValueError:\' block executes/runs whenever a \
letter key is pressed instead of a number key.')
