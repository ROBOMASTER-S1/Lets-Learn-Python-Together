# Check to see if there are any duplicate names, using a set.
# Sets always display values in random order, such as this set_demo
# example below illustrates. This means that every time you execute/run
# the set_demo program example, the values will always be in random
# order. However, sets are designed to get rid of duplicate values. Note:
# sets do not use indexing, such as tuples and lists do.

set_demo={'Tom','Bob','John','Ron','Tom'}

print(set_demo)

# If you try to run this one-line 'print' statement, you will get a type error.
# message as illustrated below.

print(set_demo[1])

'''
Traceback (most recent call last):
  File "C:/Users/Brian D/Desktop/JCR/GITFiles/Sets Examples.py", line 16, in <module>
    print(set_demo[1])
TypeError: 'set' object is not subscriptable
'''

'''----------------------------------------------------------------'''

# Let's convert a set into a tuple, complete with indexing.

set_demo={'Tom','Bob','John','Ron','Tom'}

convert=tuple(set_demo)

print(convert[1])

# If you re-execute/run the set_demo program example above, it will still return
# a random value from the converted set, even though it has an index list range.
# To solve this problem, we need to use the 'sort()' function or the 'sorted() function.
# Also note that tuples cannot be changed or sorted, but lists can be changed and sorted.

'''----------------------------------------------------------------'''

# Let's convert a set into a sorted list, complete with indexing. The 'sorted()' function only
# affects the output of the list, not the actual list itself, whereas the 'sort()' function changes
# the actual list, such as in our next example shows.

set_demo={'Tom','Bob','John','Ron','Tom'}

convert=list(set_demo)

sorted_index=sorted(convert)

print(sorted_index)

'''----------------------------------------------------------------'''

# Here is almost the very same set_demo program example as illustrated above but with one
# exception, the actual list gets sorted, which in most cases, that's not always what you want.
# Therefore, the 'sorted()' function is used to prevent actual list modifications.

set_demo={'Tom','Bob','John','Ron','Tom'}

convert=list(set_demo)

convert.sort()

print(convert)

'''----------------------------------------------------------------'''

# The set_demo program example below does everything the above program example illustrated.
# The only difference, is that there are two sets, which we are going to extend both sets into one,
# single list. We will create two sets called set_demo1 and set_demo2 so we can extend them into
# one, single sorted list without duplicate values. We will also use what's called 'unpacking', which
# simply means to unpack two or more variables and two or more values, using just one '=' sign.

# convert1,convert2=list(set_demo1),list(set_demo2)

set_demo1={'Tom','Bob','John','Ron','Tom'}
set_demo2={'Tamy','Sandy','Mandy','Randy','Tamy'}

convert1,convert2=list(set_demo1),list(set_demo2)

convert1.extend(convert2)

sorted_index=sorted(convert1)

'''----------------------------------------------------------------'''

# Check the values first to make sure they are correctly sorted and such.

print(sorted_index)

# Let's create a sentence out of our sorted_index argument like this.

print(sorted_index[0],'is a great name.')

'''----------------------------------------------------------------'''

# Let's create a for-loop to loop through our sorted_index variable, and creat a sentence within our
# for-loop.

for i in sorted_index:
    print(i,'is a great name')

# Future examples comming soon.
