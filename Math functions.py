# All computers, including your calculator follows the
# rules of BEDMAS, PEMDAS or BODMAS. Whatever you
# call these abbreviations', they still are the very same things.
# So, don't let the names of these abbreviations fool you; they
# are BEDMAS. Period!! Bedmas as I still call it means The Order
# of Operation. Multiplication and division always take
# dominants over addition and subtraction. Although,
# computers cannot do brackets () of any kind in Python.
# Python will still follow the order of operation regardless.
# Highlight and copy, then paste this Python code into your
# Python editor and see what happens when you execute/run
# these Python program examples.

# Here are the basic bracket sets you can use on paper, not in Python.

# You have to work inside the very first set of ( ) round brackets first.
# Next, you have to work inside the [ ] square backets. Then lastly,
# you have to work inside the curly braces { }

# Not shown here, you must also do any exponents if you have them
# in your math formulas. They have to be done FIRST, before any brackets
# get solved. After you break everything down. Always work from left to
# right. Look for any multiplication or division first. Then do your addition
# and subtraction last to get the correct answer.

# { [ ( ) ] }  {Third[Second(first)Second]Third} how this works {n+n[n(n+n)+n/n]-n*n}

bedmas_example1 = 2+3*3
bedmas_example2 = 3*3+2
bedmas_example3 = 2+3/3
bedmas_example4 = 3/3+2
bedmas_example5 = 3-2*3
bedmas_example6 = 3*3-2

print(bedmas_example1)
print(bedmas_example2)
print(bedmas_example3)
print(bedmas_example4)
print(bedmas_example5)
print(bedmas_example6)

# To create exponents in Python, you can do the following examples below:

# You can use a double asterisk **

exponent = 4**3

print(exponent)

# Or use the pow(num,num) function

exponent = pow(4,3)

print(exponent)

# Python has a square root function that finds the square
# root of a number. You have to import the math module
# for the sqrt() function to work. Invoke the integer function
# int() to stop floating point numbers from showing up.

import math

print(int(math.sqrt(9)))
