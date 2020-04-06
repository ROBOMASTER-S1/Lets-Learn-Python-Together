# This little flip flop game is a great example of how the conditional while-loop works.
# The 'else' statement executes/runs when the user types the wrong keys, and the
# while-loop iterates/repeats over again while ignoring the 'break' statement.

print('\nWelcome to Flip! Flop!')

print('\nPlease type the words "flip" or "flop", then press (ENTER)')

print('\nWhen you give up, press (ENTER) to quit playing Flip! Flop!')

while True:
    flip=input('\nFlip? or Flop? ').strip()
    
    if flip=='flip':
        print('\nFlop!')
        
    elif flip=='flop':
        print('\nFlip!')
        
    elif flip=='':
        print('\nThanks for playing Flip! Flop!')
        break
    
    else:
        print('\nYou can\'t cheat now! Do you flip? or do you flop?')
        
input('\nEnd of program. Press Enter to quit.')
