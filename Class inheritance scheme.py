# Play around with this class inheritance scheme
# Python program example.

class Math: # parent class Math:

    global a,b # use global variables inside classes and functions alike:
    a,b=6,2 # use a multivariable, since it's too small to be a tuple or a list.

    def addition(num1,num2):
        return num1+num2

    def subtraction(num1,num2):
        return num1-num2

    def multiplication(num1,num2):
        return num1*num2

    def exponent(num1,num2):
        return num1**num2

    def division(num1,num2):
        return num1/num2

class People: # parent class People:

    global names # use global variables inside classes and functions alike:
    names=(
        ['Galileo','Galilei'], # use a 2d list:
        ['Isaac','Newton'],
        ['Albert','Einstein'],
        ['Stephen','Hawking'])

    def name(fname,lname):
        return f'{fname} {lname} loves Physics.' # Tip: use the f' format for easier string concatenation.

class Both(Math,People): # child class Both with Math and People classes:
    pass

# Look very carefully at these class inheritance schemes,
# you notice the class names Math, People and Both. Each
# of these following examples visually show how class
# inheritance works. The class Both inherits the all the
# properties of the Math class and the People class.

print(Math.addition(a,b))
print(Math.subtraction(a,b))
print(Math.multiplication(a,b))
print(Math.exponent(a,b))
print(Math.division(a,b))

print(People.name(names[0][0],names[0][1]))
print(People.name(names[1][0],names[1][1]))
print(People.name(names[2][0],names[2][1]))
print(People.name(names[3][0],names[3][1]))

print(Both.addition(a,b))
print(Both.subtraction(a,b))
print(Both.multiplication(a,b))
print(Both.exponent(a,b))
print(Both.division(a,b))

print(Both.name(names[0][0],names[0][1]))
print(Both.name(names[1][0],names[1][1]))
print(Both.name(names[2][0],names[2][1]))
print(Both.name(names[3][0],names[3][1]))

# Instead, why not shorten your code in the 'print()' function,
# using strings.

num1=Math.addition(a,b)
name1=People.name(names[0][0],names[0][1])

num2=Both.addition(a,b)
name2=Both.name(names[0][0],names[0][1])

print(num1)
print(name1)

print(num2)
print(name2)

# If you have lots of code in your classes, you can create
# a tuple or a list for them to shorten the code inside the
# 'print()' function. You can also notice how each tuple
# example has its own parent and child class attributes.

math1=(
    Math.addition(a,b),
    Math.subtraction(a,b),
    Math.multiplication(a,b),
    Math.exponent(a,b),
    Math.division(a,b))

math2=(
    Both.addition(a,b),
    Both.subtraction(a,b),
    Both.multiplication(a,b),
    Both.exponent(a,b),
    Both.division(a,b))

print(math1[0])
print(math2[0])

names1=(
    People.name(names[0][0],names[0][1]),
    People.name(names[1][0],names[1][1]),
    People.name(names[2][0],names[2][1]),
    People.name(names[3][0],names[3][1]))

names2=(
    Both.name(names[0][0],names[0][1]),
    Both.name(names[1][0],names[1][1]),
    Both.name(names[2][0],names[2][1]),
    Both.name(names[3][0],names[3][1]))

print(names1[0])
print(names2[0])

math_and_people1=(
    Math.addition(a,b),
    Math.subtraction(a,b),
    Math.multiplication(a,b),
    Math.exponent(a,b),
    Math.division(a,b),
    People.name(names[0][0],names[0][1]),
    People.name(names[1][0],names[1][1]),
    People.name(names[2][0],names[2][1]),
    People.name(names[3][0],names[3][1]))

for i in math_and_people1:
    print(i)

# Let's use the class name variable 'Both' and combine
# all our function calls inside a single tuple, then we will
# create a for-loop to call them all.

math_and_people2=(
    Both.addition(a,b),
    Both.subtraction(a,b),
    Both.multiplication(a,b),
    Both.exponent(a,b),
    Both.division(a,b),
    Both.name(names[0][0],names[0][1]),
    Both.name(names[1][0],names[1][1]),
    Both.name(names[2][0],names[2][1]),
    Both.name(names[3][0],names[3][1]))

for i in math_and_people2:
    print(i)
