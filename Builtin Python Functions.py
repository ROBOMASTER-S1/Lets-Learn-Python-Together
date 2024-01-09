# I've never ever tried this Walrus := Operator before. What this
# actually does, is allow you to create variable expressions
# right inside print(functions), like these examples below. They
# can do a lot more as well. Let's see what this Walrus Operator
# does. The walrus operator looks like this := as if his head is
# sideways. It even looks just like the face of a walrus at that;
# the big teeth, and its nose. The walrus operator consists of
# one : colon and one = equals sign, side by side ' := '

print(x := 'The Walrus Operator :=')  # create variable expressions right inside print() functions

# You can also call the variable in a print() function, as if you
# created it like this old, two line Python code example:

x = 'Old Way'

print(x)

# Now, let's use the walrus operator and reduce this Python
# code down to only one, single line of Python code.

print(x := 'The New Walrus Way')  # create variable expressions right inside print() functions

# We can also use the very same variable 'x' inside another
# print() function, as if using the old way.

print(x := 'The New Walrus Way')  # create variable expressions right inside print() functions

# You can reuse walrus variables all throughout your Python code.
# The variable 'x' will always show the value, as if you created it like
# I taught you to create them, and had also others taught you, as well
# as they once taught me much about Python. We are going to have
# some more fun with this walrus operator := to improve our code to
# be more efficient and practical.

print(x,'can be reused as if it were an actual variable outside the print() function.')

# Create a list out of the walrus := operator and then call the variable 'x'
# inside another, separate print() function and see it behave as the old
# way of doing things. But the walrus := operator will be a huge game
# changer for us from here onward.

print('Check your list:',x := [0,1,2,3,4,5])  # screen output: [0,1, 2, 3, 4, 5]

print(x[3])  # screen output: 3

print('Check your tuple:',x := (0,1,2,3,4,5))  # screen output: (0,1, 2, 3, 4, 5)

print(x[3])  # screen output: 3

print('Check your set:',x := {0,1,2,3,4,5})  # screen output: {0,1, 2, 3, 4, 5}
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's see what happens when we use the walrus := operator with a
# dictionary.

print('Check your dictionary:',my_dict := {1:'Value 1',2:'Value 2',3:'Value 3'})

print(my_dict.get(1))  # screen output: Value 1

# See how we can dramatically reduce code, using the walrus := operator?
# I will try other things to teach us what else this walrus := operator can do
# for us to help make our Python code that much more tight and efficient.

input()
# Here is what some of Python's built-in functions can do for
# us. Let's see what some of them do, so we can make them
# do some fun things. W3schools.com is going help us here.
# This is their writing, I just placed the name of the function
# into their writings was all.

print(abs(-10+4))  # abs() returns the absolute value of a number

# The all() function returns True if all items in an iterable are
# true, otherwise it returns False.

x = [1,2,3]

print(all(x))  # screen output: True

x = [0,2,3]

print(all(x))  # screen output: False

x = [1,2,0]

print(all(x))  # screen output: False
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# any() returns True if any item in an iterable are true, otherwise
# it returns False.

x = [1,2,3]

print(any(x))  # screen output: True
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The ascii() function returns a readable version of any object
# (Strings, Tuples, Lists, etc).

x = 'Python'

print(ascii(x))

# The ascii() function will replace any non-ascii characters with
# escape characters:

x = 'Pythonå' # å will be replaced with \xe5.

print(ascii(x))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The bin() function returns the binary version of a specified
# integer number. The result will always start with the prefix 0b.

x = 255

print(bin(x))  # screen output: 0b100100
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The bool() function returns the boolean value of a specified object.
# The object will always return True, unless:

# The object is empty, like [], (), {}
# The object is False
# The object is 0
# The object is None

x = 1

print(bool(x))  # screen output: True

x = 0

print(bool(x))  # screen output: False
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The bytearray() function returns a bytearray object. It can convert objects
# into bytearray objects, or create empty bytearray object of the specified size.

x = 4

print(bytearray(x))  # screen output: bytearray(b'\x00\x00\x00\x00')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Complete Built-in Python Functions() List:
# These built-in functions are very powerful all throughout
# Python in general, such as the print() function and the input()
# function. Now imagine all these others we get to monkey
# around with to help us do our Fancy Dancy Python Footwork.
# Explore what these commands do. If you aren't sure, just do
# a bit of research and you will find what all these are. There
# are most I don't even know what they do, but having a list
# of these built-in Python Functions() can make it a snap to know
# what you are wielding, when it comes to Python in general.

abs()
all()
any()
ascii()
bin()
bool()
bytearray()
bytes()
callable()
chr()
classmethod()
compile()
complex()
delattr()
dict()
dir()
divmod()
enumerate()
eval()
exec()
exit()
filter()
float()
format()
frozenset()
getattr()
globals()
hasattr()
hash()
help()
hex()
id()
input()
int()
isinstance()
issubclass()
iter()
len()
list()
locals()
map()
max()
memoryview()
min()
next()
object()
oct()
open()
ord()
pow()
print()
property()
range()
repr()
reversed()
round()
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
tuple()
type()
vars()
zip()
