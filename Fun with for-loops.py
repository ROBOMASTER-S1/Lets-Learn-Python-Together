# Create a right triangle shape with a for-loop, using a
# start value of 1.

for i in range(1,21):
    print('* '*i,i)
    
'''---------------------------------------------------------------------------------------------'''

# Create a right triangle shape with a for-loop, using a
# start value of 1 and a step value of 2.

for i in range(1,21,2):
    print('* '*i,i)
    
'''---------------------------------------------------------------------------------------------'''

# Create a for-loop that breaks when i==10.

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in nums:
    if i==10:
        print(f'{i}: I found number "{i}" ')
        break
    print(i)
    
'''---------------------------------------------------------------------------------------------'''

# Create a for-loop that continues on when i==10.

for i in nums:
    if i==10:
        print(f'{i}: I found number "{i}" ')
        continue
    print(i)
    
'''---------------------------------------------------------------------------------------------'''

# Loop through a tuple using a for-loop, along with
# a 'print' statement message 'I am number'

for i in tuple_loop:
    print('I am number '+i+'.')

'''---------------------------------------------------------------------------------------------'''

# Loop through a tuple using a for-loop.        

tuple_loop=(
    'One','Two',
    'Three','Four',
    'Five','Six',
    'Seven','Eight',
    'Nine','Ten'
    )

for i in tuple_loop:
    print(i,end=' ')
    
'''---------------------------------------------------------------------------------------------'''

# Create while-loops that can find numbers, then make them break
# or keep on incrementing 'i' until 'i=30. Type and execute/run the
# program examples below and see what happens.

i=1
while i<=30:
    print(i)
    i+=1
    if i==20:
        print(f'"{i}" I found number "{i}". I will break the loop now.')
        break
 
i=1
while i<=30:
    print(i)
    i+=1
    if i==20:
        print(f'"{i}" I found number "{i}". I will keep looping, until "i=30".')
        i+=1
        
'''---------------------------------------------------------------------------------------------'''

# Create a for-loop, using an 'input' statement that
# allows the user to input the number of the for-loop.

while True:
    try:
        enter_num=int(input('Please enter a number, or numbers '))    
        for i in range(1,enter_num+1):
            print('* '*i,i)
        break
    except ValueError:
        print(f'Sorry! Numbers only please.')
        
'''---------------------------------------------------------------------------------------------'''

# Create a for-loop, using an 'input' statement that
# allows the user to input the number of the for-loop.
# If a number doesn't exist, the for-loop breaks.

while True:
    try:
        enter_num=int(input('Enter any number up to 20 and I will find it. '))    
        for i in nums:
            if i==enter_num:
                print(f'{i}: I found number "{i}" ')
                break
            elif enter_num<1:
                print(f'Sorry! I cannot find "{enter_num}" ')
                break
            elif enter_num>20:
                print(f'Sorry! I cannot find "{enter_num}" ')
                break
            print(i)
        break
    except ValueError:
        print('Sorry! Numbers only please.')
