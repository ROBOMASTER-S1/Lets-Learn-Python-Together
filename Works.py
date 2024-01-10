'''Minute Python Program Examples'''

# Let's learn what sets are and what they can do.
# Sets are powerful in ways you can't even begin
# to imagine and they get rid of any duplicate
# values as you can see in the screen output
# example below.

my_set={1,3,2,4,5,7,6,8,9,10,9,2,7}

print(my_set)

# screen output:   {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Sets can also hold text word values, but they will
# always be in random order, not sorted like our
# example above shows. Note: number values always
# remain sorted. For example:

my_set={'One','Two','Three','Four','Five','Five','Two'}

print(my_set)

# Notice how the screen output shows the values
# in random order. Yet the duplicate values are
# gone such as was in our first example.

# screen output:  {'Two', 'Five', 'One', 'Three', 'Four'}

# Note: sets do not contain indices '[0]' like lists
# and tuples do. Instead, sets are great at managing
# large array values that might be overlooked for
# duplicate array values on the programmer's part.
# So sets help prevent this from occurring. But you
# ask, if sets don't contain indices '[0]', how can we
# use their values? The answer is simple. For example:

my_set={'One','Two','Three','Four','Five','Five','Two'}

convert_my_set=list(my_set) # invoke the 'list()' function

print(convert_my_set) # use this variable to see the converted set.

# screen output:   ['Five', 'Four', 'Three', 'One', 'Two']

# But we then ask. How can we make the converted
# set become non-random and sorted. Again the
# answer is simple. For example:

my_set={'One','Two','Three','Four','Five','Five','Two'}

convert_my_set=list(my_set)

convert_my_set.sort() # sorts the actual list.

print(convert_my_set)

# screen output:   ['Five', 'Four', 'One', 'Three', 'Two']

# or:

my_set={'One','Two','Three','Four','Five','Five','Two'}

convert_my_set=list(my_set)

list_copy=sorted(convert_my_set) # sorts the list copy only.

print(list_copy)

# screen output:   ['Five', 'Four', 'One', 'Three', 'Two']

# Let's now call a value from our converted set,
# which we turned into a non-random, sorted list.
# For example:

my_set={'One','Two','Three','Four','Five','Five','Two'}

convert_my_set=list(my_set)

convert_my_set.sort() # sorts the actual list.

print(convert_my_set[0]) # indices '[0]'

# Let's call all the values on our converted set list.

print(convert_my_set[0])
print(convert_my_set[1])
print(convert_my_set[2])
print(convert_my_set[3])
print(convert_my_set[4])

# Let's use a for-loop to iterate through the indices
# with just a single 'print()' function.

for i in range(5):
    print(convert_my_set[i])

# or:

for i in convert_my_set:
    print(i)
'''----------------------------------------------------------------'''
# Sets can do much more than was shown, thus far.
# Let's learn how to unionize two sets together.
# For example:

my_set1={1,2,3,4,5,6,7,8,9,10,9,2}
my_set2={'One','Two','Three','Four','Five','Five','Two'}

unionize=my_set1.union(my_set2)

print(unionize)

# screen output:   {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Three', 'Four', 'Five', 'One', 'Two'}
'''----------------------------------------------------------------'''
# Let's learn how to intersect two sets.
# For example:

my_set1={1,2,3,4,5,6,7,8,9,10,9,2,'Five'}
my_set2={'One',4,'Two','Three','Four','Five','Five','Two'}

set_intersection=my_set1.intersection(my_set2)

print(set_intersection)

# screen output:   {'Five', 4} Five and 4 intersect

# Let's learn how to find the difference between sets.
# For example:

my_set1={1,2,3,4,5,6,7,8,9,10,9,2,'Six'}
my_set2={'One','Two','Three','Four','Five','Five','Two',3}

print(my_set1.difference(my_set2))

# screen output:   {1, 2, 4, 5, 6, 7, 8, 9, 10}
'''----------------------------------------------------------------'''
# Let's learn how to find the symmetric difference
# between sets. For example:

my_set1={1,2,3,4,5,6,7,8,9,10,'Five'}
my_set2={'One','Two','Three','Four','Five',2}

print(my_set1.symmetric_difference(my_set2))

# screen output:   {1, 3, 4, 5, 6, 7, 8, 9, 10, 'Three', 'One', 'Four', 'Two'}
'''----------------------------------------------------------------'''
# Below are the written set functions:

print(my_set1.union(my_set2)) # Union
print(my_set1.intersection(my_set2)) # Intersection
print(my_set1.difference(my_set2)) # Difference
print(my_set1.symmetric_difference(my_set2)) # Symmetric Difference

# Below are the symbol set functions:

print(my_set1 | my_set2) # Union
print(my_set1 & my_set2) # Intersection
print(my_set1 - my_set2) # Difference
print(my_set1 ^ my_set2) # Symmetric Difference
'''----------------------------------------------------------------'''
# Let's use the 'slice()' function to decide how far we want
# our set values to reach

my_set1={1,2,3,4,5,6,7,8,9,10,9,2}
my_set2={'One','Two','Three','Four','Five','Five','Two'}

unionize=my_set1.union(my_set2)

convert_my_set=list(unionize)

reach_limit=slice(14)

print(convert_my_set[reach_limit])

# screen output:   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''----------------------------------------------------------------'''
# Try these examples below:

x={1,2,3,4,9,6,7,8,5,9}
y={10,11,15,13,14,12,16,17,18,19,19}
z={20,21,22,23,27,25,26,24,28,29,22}

unionize=x.union(y).union(z)

convert=list(unionize)

a=slice(20)

print(convert[a])
'''----------------------------------------------------------------'''
x={1,2,3,4,9,6,7,8,5,9}
y={10,11,15,13,14,12,16,17,18,19,19}
z={20,21,22,23,27,25,26,24,28,29,22}

unionize=x.union(y,z)

convert=list(unionize)

a=slice(20)

print(convert[a])
'''----------------------------------------------------------------'''
a=list()
for i in range(10):
    a.append(i) # invoke the 'append()' function for lists

b=set()
for i in range(10):
    b.add(i) # invoke the 'add()' function for sets

print(a)
print(b)
'''----------------------------------------------------------------'''
nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 | nums2) # Union

print(nums1.union(nums2)) # Union

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 & nums2) # Intersection

print(nums1.intersection(nums2)) # Intersection

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 - nums2) # Difference

print(nums1.difference(nums2)) # Difference

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1.symmetric_difference(nums2)) # Symmetric Difference

print(nums1 ^ nums2) # Symmetric Difference
'''----------------------------------------------------------------'''
# Let's create a text word set and unionize them together and sort
# it. For example:

my_chr_set1={'a','b','c','d','e','f','g','h','i','j','k','l','m'}
my_chr_set2={'n','o','p','q','r','s','t','u','v','w','x','y','z'}

unionize=my_chr_set1 | my_chr_set2

convert_my_chr_sets=list(unionize) # invoke the 'list()' function

convert_my_chr_sets.sort() # sort the actual list

print(convert_my_chr_sets)

# screen output:   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Let's use the 'len()' function to see how many list values we have.

print(len(convert_my_chr_sets)) # prints how many values there are

# screen output:   26
'''----------------------------------------------------------------'''
# Let's turn two lists into a single set.

my_chr_set1=['a','b','c','d','e','f','g','h','i','j','k','l','m']
my_chr_set2=['n','o','p','q','r','s','t','u','v','w','x','y','z']

my_chr_set1.extend(my_chr_set2)

convert_to_set=set(my_chr_set1) # invoke the 'set()' function

print(convert_to_set)

# screen output:   {'j', 'o', 'f', 'q', 'n', 'v', 'l', 'e', 'z', 'u', 'g', 'm', 'y', 'w', 'b', 'k', 't', 'r', 'c', 'a', 'd', 's', 'p', 'x', 'h', 'i'}

print(len(convert_to_set)) # prints how many values there are

# screen output:   26
'''----------------------------------------------------------------'''
# Try these examples:

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 | nums2) # Union

print(nums1.union(nums2)) # Union
'''----------------------------------------------------------------'''
nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 & nums2) # Intersection

print(nums1.intersection(nums2)) # Intersection
'''----------------------------------------------------------------'''
nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 - nums2) # Difference

print(nums1.difference(nums2)) # Difference
'''----------------------------------------------------------------'''
nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1.symmetric_difference(nums2)) # Symmetric Difference

print(nums1 ^ nums2) # Symmetric Difference
'''----------------------------------------------------------------'''
nums1={0,1,2,3,1,3,4,10,5,6,6,7,8,9,10,23}
nums2={1,2,7,1,3,4,10,5,6,6,7,8,9,10,11,22}

print(nums1 | nums2) # Union
print(nums1 & nums2) # Intersection
print(nums1 - nums2) # Difference
print(nums1 ^ nums2) # Symmetric Difference

nums1=[1,2,3,1,3,4,10,5,6,6,7,8,9,10]
nums2=[1,2,3,1,3,4,10,5,6,6,7,8,9,10]

uniques1=set(nums1)
uniques2=set(nums2)

print(uniques1 | uniques2)

# Now you can clearly see just how powerful 'sets' are
# and they save a lot of time and headaches on the
# programmer's part. And now you have the proper
# tools to do the job well done...
