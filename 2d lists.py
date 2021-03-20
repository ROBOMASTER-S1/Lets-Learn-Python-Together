# Let's fully understand what a 2d list is truly all about.
# A 2d list is a two dimensional array that can hold multiple
# 2d list array values under a single variable. For example:

my_2d_list=['2d list0'],['2d list0']

print(my_2d_list[0][0])
print(my_2d_list[1][0])

# If you create a really long 2d list such as this example below,
# you can force hard line-breaks, but you must use outer square
# brackets '[]' to surround the entire 2d list values. Note: you
# must use commas at the end of each 2d list array.

# Example 1:

my_2d_list=['2d list0'],['2d list0'],['2d list0'],['2d list0'],['2d list0'],['2d list0'],['2d list0']

print(my_2d_list[4][0])

# Example 2:

my_2d_list=[ # use a hard line-break make the 2d list look neat and tidy.
    ['2d list0'],['2d list0'],['2d list0'],
    ['2d list0'],['2d list0'],['2d list0'],
    ['2d list0']] # use a hard line-break to add more values to the 2d list.

print(my_2d_list[4][0])

# Create a multi-2d list array like this example below illustrates.

my_multi_2d_list=['Value0','Value1','Value2'],['Value0','Value1','Value2']

print(my_multi_2d_list[0][0])
print(my_multi_2d_list[0][1])
print(my_multi_2d_list[0][2])

print(my_multi_2d_list[1][0])
print(my_multi_2d_list[1][1])
print(my_multi_2d_list[1][2])

# You can create as many multi-2d list array values as you please.
# For example:

my_multi_2d_list=[
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2','Value3'],
    ['Value0','Value1','Value2','Value3','Value4']] # neat and tidy

print(my_multi_2d_list[0][2])
print(my_multi_2d_list[1][3])
print(my_multi_2d_list[2][4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's have some multi-2d list fun using a for-loop
# and see what happens when we execute/run this multi-2d
# list, for-loop example:

my_multi_2d_list=[
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2']] # neat and tidy

for i in my_multi_2d_list:
    print(i[0],i[1],i[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a real, working multi-2d list to see what
# they are truly all about in a real Python program scenario.
# We will call our multi-2d list, 'names'. Use the (f') format
# to make the 'print' statement easier to concatenate strings.

names=[
    ['Ron','Bob','Tom'],
    ['John','Mary','Terry'],
    ['Edie','Freddy','Teddy'],
    ['Charie','Marty','Harvey']] # neat and tidy

for i in names:
    print(f'{i[0]}, {i[1]} and {i[2]} went to the store.')

# Let's create a looping sentence tuple with our multi-2d list for-loop
# example and see what happens when we execute/run this Python
# program example below.

names=[
    ['Ron','Bob','Tom'],
    ['John','Mary','Terry'],
    ['Edie','Freddy','Teddy'],
    ['Charie','Marty','Harvey']] # neat and tidy

sentence=(
    ('went home to have dinner.',
    'went to the store to buy some food.',
    'wanted some pizza for breakfast.',
    'wanted computers for Christmas.',
    'love their computers.'))

for i in range(4):
        print(f'{names[i][0]}, {names[i][1]} \
and {names[i][2]} {sentence[i]}')
