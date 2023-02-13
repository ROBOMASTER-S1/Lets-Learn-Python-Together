'''
Create three different integer sets that will combine/unionize all three sets into one
single set. Convert the single set into a list, using the list() function. Next, view the
contents of the list, along with the slice() function to set the range of list content
values to display on the screen.

Type and execute/run this Python program example below.
'''
# To reduce lines of code, create packed variables and their
# packed values.

x,y,z=(
    {1,2,3,4,9,6,7,8,5,9,10},
    {11,12,13,14,15,16,17},
    {18,19,20,21,22,23,24})

a=slice(24) # slice the set with the slice() function

# To reduce lines of code, create packed variables and their
# packed values.

length1,length2,length3=len(x),len(y),len(z)

unionize=x.union(y,z) # unionize x to y and z with the value v.union() function

convert=list(unionize) # cast the set to a list with the list() function

answer=length1,length2,length3

# Add the total values between length1, length2 and length3 with the sum()
# function.

total_sum=sum(answer) # add all three values of answer together with the sum() function

# View the contents of x, y and z in their combined, converted sets to a list.

print('View the value contents of the unionized list to check it:\n\n'+str(convert[a]))

# Create a variable called sentence_loop, along with all its values.

sentence_loop=(
    f'\nThe length of (x) = {length1}',f'The length of (y) = {length2}',
    f'The length of (z) = {length3}',f'\nThe total lengths of x+y+z = {total_sum}')

# Create a for loop that will loop through the sentence_loop variable, using a
# single print() function. The for loop will iterate until all the values are cycled
# through the sentence_loop variable.

for i in sentence_loop:print(i)
