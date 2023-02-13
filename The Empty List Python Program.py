'''
Create an empty list using a for loop and the append() function to create
ten numbers from 1 to 10. After that, use the sum() function to add up all
the numbers from 1 through 10.

Type and execute/run this Python program example below.
'''
value=1,11
empty_num_list = []

# increment the empty list, using a for loop and the append() function.

for i in range(value[0],value[1]):empty_num_list.append(i)

print('\nMy list loop',empty_num_list) # view the scope contents of the empty list

# Try these three formatted print() functions to concatenate strings together.
    
print('\nMy list loop sum = '+str(sum(empty_num_list))) # non formatted string

print('\nMy list loop sum = {}'.format(str(sum(empty_num_list)))) # old formatted string

print(f'\nMy list loop sum = {sum(empty_num_list)}') # new formatted f' string
