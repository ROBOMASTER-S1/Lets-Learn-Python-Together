'''
Here is some really easy Python program examples for those
who want to learn programming, but are too afraid they aren't
smart enough. To be very honest. NO! You do not have to know
rocket science to understand programming. All you really need
is the desire to want to learn it. Like anything, if you are not into
programming, then learning it by force would only hold you back.
I wouldn't be very good at sports, thus I would have a very hard
time and the stress of doing something you don't like is not good
for anyone. But for those who might become curious with computer
programming, then I can start you off really easy with simple print()
function examples to help you understand computer programming,
even just a wee bit is enough to help you expand through others
as well as myself. Here is some really get your feet wet easy Python
program examples, using the print() function.
'''
print('Helo World!')

# Let's use a variable with any name we like. Let's use the word
# 'text' as our variable name, so we can call it back up in our print()
# function.

text = 'Helo World!'

print(text) # call up the 'text' variable inside the print() function

# Let's use a variable with any name we like. Let's use the word
# 'addition' as our variable name, so we can call it back up in our
# print() function.

addition = 1 + 9 # this variable will add these numbers together

print(addition) # call up the 'addition' variable inside the print() function

# Simply remember that the = equal sign is just a pointer to the value;
# it has nothing to do with an = equal sign in arithmetic. This kind of =
# sign is simply assigning values to variables, not for math problems.

# Here are some more examples of variables within print() functions.

subtraction = 9 - 8 # this variable will subtract these numbers

print(subtraction) # call up the 'subtraction' variable inside the print() function

# Note: the asterisk * is used for multiplication in programming.

multiplication = 12 * 12 # this variable will multiply these numbers together

print(multiplication) # call up the 'multiplication' variable inside the print() function

# Note: the backslash / is used for devision in programming.

devision = 12 / 12 # this variable will devide these numbers

print(devision) # call up the 'devision' variable inside the print() function

# If you want to get rid of floating point values, such as the example above
# illustrates. You can use the 'integer' function to create integer numbers
# instead of floating point values etc. 1.0 becomes integer number 1 with
# the integer function: int().

print(int(devision)) # call up the 'devision' variable inside the print() function

# If you know what BEDMAS or PEMDAS is, which some teachers call it. This
# simply means the ORDER OF OPERATION. Both multiplication and devision
# take presence over addition and subtraction. Brackets take presence over
# exponents as, such what multiplication and devision are to addition and
# subtraction. Brackets and exponents take presence over multiplication,
# devision, addition and subtraction. The abreviation for BEDMAS and PEMDAS
# are as follows:

# BEDMAS:

# B = Brackets ()
# E = Exponents
# D = Devison
# M = Multiplication
# A = Addition
# S = Subtraction

# PEMDAS:

# P = Parentheses ()
# E = Exponents
# M = Multiplication
# D = Division
# A = Addition
# S = Subtraction

# Note: BEDMAS and PEMDAS are the very same thing, they just have different
# names that some teachers use to explain how the ORDER OF OPERATON
# works with arithmetic, as well as with computers alike. For example:

# 2(3+2) = 2 X (3+2) = 2 X 5 = 10

# when a number such as 2(num), anything with numbers right in front of
# brackets, means MULTIPLY what's inside the added total of 3+2 = 5.
# You must do the brackets first, before you can do anything else.
# However, Python can't do BEDMAS, such as expressing it with brackets
# like with human written expressions with symbles on paper. But here
# is how Python does basic BEDMASS.

print(3+2*2/2-2) # 3.0

print(int(3+2*2/2-2)) # 3

# This is how we do exponents with Python using just two asterisks, called
# a double asterisk etc. 3**2 = 9, not 6

print(3**2)

# Let's see what computer BEDMAS does for us, using exponents **.

print(3**2*2) # 18, 3 X 3 = 9, 9 X 2 = 18

# Let's increase the expenent by 3 this time.

print(3**3*2) # 54, 3 X 3 X 3 = 27, 27 X 2 = 54

# Please give me a like if you want to see what variables do when you have
# more than one value with only one variable. For example:

text = 'Helo World!','How are you?'

print(text[0],text[1])
'''
Here are easy ways to understand Python dictionaries. This was
how I taught myself back in my early days of Python: (OOP) Object
Oriented Programming or (POOP) Python Object Oriented Programming.
'''
# This dictionary below has just two values, Canada and Ottawa.
# The Canada value is called the KEY value, and the Ottawa value
# is the value that gets called. This is the value you see on the
# screen output, when you run your Python program below.

my_easy_dictionary = {'Canada':'Ottawa'}

print(my_easy_dictionary.get('Canada'))

# If a key value cannot be found. You will see the word 'None' on the
# screen output.

print(my_easy_dictionary.get('country'))

# If you want to make this program a bit more detailed, you can do
# this instead.

print(my_easy_dictionary.get('country','Sorry! Not found.')) # Optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's expand this dictionary to more key values and value pairs.

my_easy_dictionary = {'Canada':'Ottawa','America':'Woshington D.C.'}

print(my_easy_dictionary.get('America','Sorry! Not found.')) # Optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# You can use ordenary numbers as key values with value pairs:

my_easy_dictionary = {1:'Ottawa',2:'Woshington D.C.'}

print(my_easy_dictionary.get(2,'Sorry! Not found.')) # Optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# You can use ordenary numbers as key values with numbers for value
# pairs:

my_easy_dictionary = {1:10,2:9}

print(my_easy_dictionary.get(1,'Sorry! Not found.')) # Optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# As you can clearly see how dictionary key values can be text strings
# and number strings as well as their value pairs alike.

my_easy_dictionary = {'Number 10':10,'Number 9':9}

print(my_easy_dictionary.get('Number 10','Sorry! Not found.')) # Optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# You can create as many dictionary key values and their pairs to any
# length you wish. The illustrations above were aimed at showing only
# two key values and two value pairs so the learner can grasp this, just
# exactly the same way I show these dictionary examples here. Use a
# colon  :  to separate key values and their value pairs. Use a comma ,
# to separate key values and their grouped value pairs.

my_easy_dictionary = {'Key Value 1':'Value Pair 1','Key Value 2':'Value Pair 2'}

print(my_easy_dictionary.get('Key Value 1','Sorry! Not found.')) # Optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a for loop, with the key values being integer numbers so
# the for loop will count through the dictionary key values to show their
# value pairs.

my_easy_dictionary = {
        0:'Zero',1:'One',
        2:'Two',3:'Three',
        4:'Four',5:'Five'}

for i in my_easy_dictionary:
        print(my_easy_dictionary.get(i,'Sorry! Not found.')) # Optional

# or this:

for i in my_easy_dictionary:print(my_easy_dictionary.get(i,'Sorry! Not found.')) # Optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's update the dictionary with the update() method:

my_easy_dictionary = {
        0:'Zero',1:'One',
        2:'Two',3:'Three',
        4:'Four',5:'Five'}

my_easy_dictionary.update({6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten'})

for i in my_easy_dictionary:
        print(my_easy_dictionary.get(i,'Sorry! Not found.')) # Optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's remove a key value with the pop() method.

my_easy_dictionary = {
        0:'Zero',1:'One',
        2:'Two',3:'Three',
        4:'Four',5:'Five'}

my_easy_dictionary.pop(4)

for i in my_easy_dictionary:
        print(my_easy_dictionary.get(i,'Sorry! Not found.')) # Optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The pop() method can also be used to call the value, that you
# removed from the dictionary. All you need to do us use a variable
# name to recall the returned item you deleted, or removed tempararly.

my_easy_dictionary = {
        0:'Zero',1:'One',
        2:'Two',3:'Three',
        4:'Four',5:'Five'}

popped_item = my_easy_dictionary.pop(4)

print('Popped item',popped_item,'is returned.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Completly delete an item from the dictionary with the 'del' emplementor.

my_easy_dictionary = {
        0:'Zero',1:'One',
        2:'Two',3:'Three',
        4:'Four',5:'Five'}

del my_easy_dictionary[0]

print(my_easy_dictionary) # check the dictionary to make sure you deleted the right key value pairs
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Clear all dictionary items.

my_easy_dictionary = {
        0:'Zero',1:'One',
        2:'Two',3:'Three',
        4:'Four',5:'Five'}

clear_dictionary = my_easy_dictionary.clear()

print(clear_dictionary) # returns None

# Straight up class inheritance Python program examples: how to
# create inheritance classes as easy as these examples illustrate.

class Main:
        def a(x):
                print(x,x,x,x) # add as many argument values you like.

class Sub(Main): # class inheritance variable
        def b(y):
                print(y,y,y)  # add as many argument values you like.

Main.a('argument value')

Sub.a('argument value')
Sub.b('argument value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
        def a(x,y):
                print(x,y,y,y)  # add as many argument values you like.

class Sub(Main): # class inheritance variable
        def b(y,x):
                print(y,x,x)  # add as many argument values you like.

Main.a('argument value1','argument value2')

Sub.a('argument value1','argument value2')
Sub.b('argument value1','argument value2')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
        def a(x):
                print(x,x,x,x) # add as many argument values you like.

class Sub():
        def b(y):
                print(y,y,y)  # add as many argument values you like.

class Child(Main,Sub): # The Child class inherits both the Main class and the Sub class
        pass

Main.a('argument value')

Sub.b('argument value')

Child.a('argument value')
Child.b('argument value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
        def a(x,y):
                print(x,y,y) # add as many argument values you like.

class Sub():
        def b(y,x):
                print(y,x,x)  # add as many argument values you like.

class Child(Main,Sub): # The Child class inherits both the Main class and the Sub class
        pass

Main.a('argument value1','argument value2')

Sub.b('argument value1','argument value2')

Child.a('argument value1','argument value2')
Child.b('argument value1','argument value2')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Try these simple define functions to learn how to do them as they progress in each
Python program pactice example. Try doing diffent things to them and see what
happens every time you execute/run any of these Python program examples.
'''
def my_func1(fname,lname): # two parameter variables

        print(fname,lname)

def my_func2(pet): # one parameter variable

        print(pet)

my_func1('John','Smith') # two argument values
my_func2('Dog') # one argument value
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Try these simple define functions to learn how to do them as they progress in each
Python program pactice example. Try doing diffent things to them and see what
happens every time you execute/run any of these Python program examples.

def my_func():

        print('This screen output text is the output of the my_function() def function.')

my_func() # call the my_function to display the screen output.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def my_func(parameter_var1,parameter_var2,parameter_var3): # three parameter variables

        print(parameter_var1,parameter_var2,parameter_var3)

# call the my_function to display the screen output.

my_func('argument value 1','argument value 2','argument value 3') # three argument values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def my_func(parameter_var1,parameter_var2,parameter_var3): # three parameter variables

       return 'argument value 1' ' argument value 2' ' argument value 3' # returns argument values

# call the my_function to display the screen output.

print(my_func('argument placeholder 1','argument placeholder 2','argument placeholder 3'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def my_func(parameter_var1,parameter_var2,parameter_var3): # three parameter variables

       return 'argument value 1' ' argument value 2' ' argument value 3' # returns argument values

# store the my_function inside the args variable to save printed coding space on your screen.

args=my_func('argument placeholder 1','argument placeholder 2','argument placeholder 3')

print(args) # call the args variable instead to display the screen output.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Do some math with our 'return' statement.

def arithmetic():

        return 1+2*3+3/2 # returns a decimal float value

print(arithmetic())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def arithmetic():

        return (1+2*3+3)/2 # returns a float value

print(arithmetic())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def arithmetic():

        return int((1+2*3+3)/2) # returns an integer value

print(arithmetic())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This time, we can make up values and see what happens when
# we re-execute/run our Python program example below.

def arithmetic(num1,num2,num3): # three parameter variables

        return int((num1+num2*num3+num3)/num2) # returns an integer value

print(arithmetic(1,2,3)) # create any three, separate number values in each argument placeholder
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# These classes do exactly the same things as other examples
# showed. The only real difference is, this time we are going to
# use 'ATTRIBUTES' for our classes. Attributes are these:

ATTRIBUTES:

self.first_name=fname
self.last_name=lname
self.age=age

# Classes and 'def functions()' can use attributes to create names,
# such as a person's first name; their last name, and their age. Note:
# these attributes are all the same for all classes to make things a
# bit easier to understand, when we learn the 'super()' function.

class Main_class:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

class Sub_class1:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

class Sub_class2:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

class All_classes(Main_class,Sub_class1,Sub_class2): # child class inheritance variables
    pass

print(Main_class('John','Smith',23).first_name)
print(Sub_class1('John','Smith',23).last_name)
print(Sub_class2('John','Smith',23).age)

print(All_classes('John','Smith',23).first_name)
print(All_classes('John','Smith',23).last_name)
print(All_classes('John','Smith',23).age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main_class:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age
        print(self.first_name)

class Sub_class1:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age
        print(self.last_name)

class Sub_class2:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age
        print(self.age)

class All_classes(Main_class,Sub_class1,Sub_class2): # child class inheritance variables
    pass

Main_class('John','Smith',23)
Sub_class1('John','Smith',23)
Sub_class2('John','Smith',23)
All_classes('John','Smith',23)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what the 'super()' function does, when we want to use
# attributes from the Main class, if we want all our classes to be the
# same. Let's use the 'super()' function to get rid of redundant attribute
# code blocks, since they are all the same. Let's get real lazy now.

class Main_class:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

class Sub_class1(Main_class): # class inheritance variable

     def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age) # super() calls the __init__ method

class Sub_class2(Main_class): # class inheritance variable

    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)

print(Main_class('John','Smith',23).first_name)
print(Sub_class1('John','Smith',23).last_name)
print(Sub_class2('John','Smith',23).age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main_class:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age
        print(self.first_name)

class Sub_class1(Main_class): # class inheritance variable

     def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age) # super() calls the __init__ method
        print(self.last_name)

class Sub_class2(Main_class): # class inheritance variable

    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)
        print(self.age)

Main_class('John','Smith',23)
Sub_class1('John','Smith',23)
Sub_class2('John','Smith',23)

# Notice how everything is exactly the same, except for the attributes
# and the super() function, which allows you to get rid of redundant attribute
# code blocks? Now you can use the super() function with classes.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the super() function with some of the attributes that we will
# need with the others with different attribute names. We will also create
# each class to have their very own attribute characteristics.

class Parent_main:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age
        print(self.first_name)

class Sub_child1(Parent_main): # class inheritance variable

     def __init__(self,fname,lname,age,dog,cat,bird,fish):
        super().__init__(fname,lname,age)
        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish
        print(self.first_name,'I love my',self.dog,self.cat,'and my',self.bird)

class Sub_child2(Parent_main): # class inheritance variable

    def __init__(self,fname,lname,age,hair,colour,eyes):
        super().__init__(fname,lname,age)
        self.hair=hair
        self.colour=colour
        self.eyes=eyes
        print(self.first_name,'I have long',self.colour,self.hair,'and',self.eyes )

Parent_main('John','Smith',23)
Sub_child1('John','Smith',23,'Dog','Cat','Bird','Fish')
Sub_child2('Jane','Smith',23,'hair','blond','huge blue eyes.')


print(Main_class('John','Smith',23).first_name)
print(Sub_class1('John','Smith',23).last_name)
print(Sub_class2('John','Smith',23).age)

print(All_classes('John','Smith',23).first_name)
print(All_classes('John','Smith',23).last_name)
print(All_classes('John','Smith',23).age)
