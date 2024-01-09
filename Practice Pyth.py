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
# These are the simplest ways, I can try to teach how to
# understand class inheritance of 'Why?' and 'How?' does
# it work. Below is an example of calling each class within
# the others below the very first class called, Main_class.

class Main_class:
    def my_function1():
        print('My function one')
    
class Sub_class1(Main_class): # class inheritance variable
    def my_function2():
        print('My function two')

class Sub_class2(Sub_class1): # class inheritance variable
    def my_function3():
        print('My function three')

Sub_class1.my_function1()
Sub_class1.my_function2()

Sub_class2.my_function1()
Sub_class2.my_function2()
Sub_class2.my_function3()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a parent class called, Main_class and two subclasses
# called Sub_class1 and Sub_class2. Then we must create a child
# class called, All_classes. If you look closely, this works exactly
# the same as the above class inheritance Python program example.
# The only difference is, that you need to add a child class, if you
# want to create class inheritance, without having to type all the
# class inheritance names in every subclass below the first one.
# Remember to kill two birds with one stone, as can be clearly
# seen below.

class Main_class:
    def my_function1():
        print('My function one')
    
class Sub_class1:
    def my_function2():
        print('My function two')

class Sub_class2:
    def my_function3():
        print('My function three')

class All_classes(Main_class,Sub_class1,Sub_class2): # class inheritance variables
    pass

All_classes.my_function1()
All_classes.my_function2()
All_classes.my_function3()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main_class:
    def my_function1():
        print('My function one')
    
class Sub_class1(Main_class):
    def my_function2():
        print('My function two')

class Sub_class2(Sub_class1):
    def my_function3():
        print('My function three')

Main_class.my_function1()

Sub_class1.my_function1()
Sub_class1.my_function2()

Sub_class2.my_function2()
Sub_class2.my_function3()

# How to understand class constructor/methods, using
# the dunder_method called __init__ with two underscores
# in each side of the 'init' word.

# Let's first learn how to create two, separate classes
# that will use the constructor method __init__. We will
# create two classes called 'Person and Description'.
# And after we learn how to do these, we will also learn
# how create Parent and Child class acts. How's that?

class Reuse_code_from_main_class_attributes:
    
    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age
        print(self.first_name,self.last_name,self.age)

class Sub_class(Reuse_code_from_main_class_attributes): # Inheritance variable
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age) # super() helps us reuse attributes from the main class
        print('Good Job',self.first_name)

Reuse_code_from_main_class_attributes('John','Smith',23).first_name
Sub_class('John','Smith',23).first_name

class Person:
    
    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

name_age1=Person('John','Smith',23).first_name
name_age2=Person('John','Smith',23).last_name
name_age3=Person('John','Smith',23).age

print(name_age1,name_age2,name_age3)

class Description:

     def __init__(self,hair_col,skin_col,eye_col):
         self.hair_colour=hair_col
         self.skin_colour=skin_col
         self.eye_colour=eye_col

description1=Description('Brown','White','Blue').hair_colour
description2=Description('Brown','White','Blue').skin_colour
description3=Description('Brown','White','Blue').eye_colour

print(description1,description2,description3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now create our Parent and Child Class Act. Let's create
# our two, separate clases we created and make them share
# all the atributes between them, so they become a class inheritance.
# The parent class will be called 'Person' and the child class will be
# called 'Description'.

class Person:
    
    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

class Description(Person): # Inheritance variable: Person
    pass

name_age1=Person('John','Smith',23).first_name
name_age2=Person('John','Smith',23).last_name

# The Description class has nothing in it. Yet the
# atributes from the Person class get passed onto
# the Description class.

name_age3=Description('John','Smith',23).age

print(name_age1,name_age2,name_age3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's make the Description class not only inherit all the properties.
# of the Parent class. But, let's also make the inherited class have
# some traits of its own as well.

class Person:
    
    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

class Description(Person): # Inheritance variable: Person
    
    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

name_age1=Person('John','Smith',23).first_name

# The Description class has direct access to the Person class atributes.

name_age2=Description('John','Smith',23).last_name

print(name_age1,name_age2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Person:
    
    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age
        print(self.first_name,self.last_name,self.age)

class Description(Person): # Inheritance variable: Person
    
    def __init__(self,fname,lname,age):
       super().__init__(fname,lname,age)

name_age1=Description('John','Smith',23).first_name

class Description(Person): # Inheritance variable: Person
    
    def __init__(self):
        super().__init__()
        
    def __init__(self,pet):
        self.pet=pet

def __init__(self,hair_col,skin_col,eye_col):
         super().__init__()
         self.hair_colour=hair_col
         self.skin_colour=skin_col
         self.eye_colour=eye_col
         
name_age1=Inheritance('John','Smith',23).first_name
name_age2=Inheritance('John','Smith',23).last_name
name_age3=Inheritance('John','Smith',23).age

description1=Inheritance('Brown','White','Blue').hair_colour
description2=Inheritance('Brown','White','Blue').skin_colour
description3=Inheritance('Brown','White','Blue').eye_colour

print(description1,description2,description3)

class Names:

    def __init__(self,fname,lname):
        self.first_name=fname
        self.last_name=lname

user_name=Names('John','Smith').first_name

print(user_name)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
user_name=Names('John','Smith').last_name

print(user_name)

# or this example if you like:

user_name=Names('John','Smith')

print(user_name.first_name)

user_name=Names('John','Smith')

print(user_name.last_name)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are some easy ways to understand how classes work.
# We will start with easy classes to understand how and why
# they work. Here is my way of understanding how to create
# different kinds of classes, along with their class objects;
# the 'def functions'. These class examples will show how
# to create classes, while being able to understand what
# they are and how they work, as well as what class inheritence
# means and how it works.

class Single_class:
    
    def function():
        print('You called function')
        
Single_class.function() # class name.function name
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Single_class:
    
    def function_argument(self):
        print('You called function')

Single_class.function_argument('argument placeholder') # class name.function name(argument placeholder)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create a parent and a child class so we
# can get access to all the classes with class inheritence.

class Parent_class:
    
    def function1():
        print('You called function1')

class Child_sub_class:
    
    def function2():
        print('You called function2')

class Class_all(Parent_class,Child_sub_class): # Class_all() contains parent and child classes
    pass

Class_all.function1()  # class name.function name
Class_all.function2()  # class name.function name
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Parent_class:
    
    def function_argument1(self):
        print('You called function1')

class Child_sub_class:
    
    def function_argument2(self):
        print('You called function2')

class Class_all(Parent_class,Child_sub_class): # Class_all() contains parent and child classes
    pass

Class_all.function_argument1('argument placeholder') # class name.function name(argument placeholder)
Class_all.function_argument2('argument placeholder') # class name.function name(argument placeholder)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Single_class:
    
    def function1():
        print('You called function1')

    def function2():
        print('You called function2')

    def function3():
        print('You called function3')

Single_class.function1() # class name.function name
Single_class.function2() # class name.function name
Single_class.function3() # class name.function name
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Single_class:
    
    def function_argument1(self):
        print('You called function1')

    def function_argument2(self):
        print('You called function2')

    def function_argument3(self):
        print('You called function3')

Single_class.function_argument1('argument placeholder') # class name.function name(argument placeholder)
Single_class.function_argument2('argument placeholder') # class name.function name(argument placeholder)
Single_class.function_argument3('argument placeholder') # class name.function name(argument placeholder)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create a parent and a child class so we
# can get access to all the classes with class inheritence.

class Parent_class:
    
    def function1():
        print('You called function1')

    def function2():
        print('You called function2')

    def function3():
        print('You called function3')

class Child_sub_class:
    
    def function4():
        print('You called function4')

    def function5():
        print('You called function5')

    def function6():
        print('You called function6')

class Class_all(Parent_class,Child_sub_class): # Class_all() contains parent and child classes
    pass

Class_all.function1() # class name.function name
Class_all.function2() # class name.function name
Class_all.function3() # class name.function name
Class_all.function4() # class name.function name
Class_all.function5() # class name.function name
Class_all.function6() # class name.function name
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Parent_class:
    
    def function_argument1(self):
        print('You called function1')

    def function_argument2(self):
        print('You called function2')

    def function_argument3(self):
        print('You called function3')

class Child_sub_class:
    
    def function_argument4(self):
        print('You called function4')

    def function_argument5(self):
        print('You called function5')

    def function_argument6(self):
        print('You called function6')

class Class_all(Parent_class,Child_sub_class): # Class_all() contains parent and child classes
    pass

Class_all.function_argument1('argument placeholder')  # class name.function name(argument placeholder)
Class_all.function_argument2('argument placeholder')  # class name.function name(argument placeholder)
Class_all.function_argument3('argument placeholder')  # class name.function name(argument placeholder)
Class_all.function_argument4('argument placeholder')  # class name.function name(argument placeholder)
Class_all.function_argument5('argument placeholder')  # class name.function name(argument placeholder)
Class_all.function_argument6('argument placeholder')  # class name.function name(argument placeholder)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Point.move()

num = int(input('Input a number: ').strip())

number = num%2

if number == 0:
    print(num,'is an Even Number.')
else:
    print(num,'is an Odd Number.')

# basic define functions() overview

def book(): # no argument variables
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book() # no argument values

def book(title): # one argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book('Python Book') # one argument values

def names(first,middle,last): # three argument variables
    print('by Joseph C. Richardson')

names('Python','Programmer\s','Glossary Bible') # three argument values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# basic return define functions() overview

def book(): # no argument variables
    return 'Python Programmer\'s Glossary Bible'

print(book()) # no argument values

def book(title): # one argument variable
    return 'Python Programmer\'s Glossary Bible'

print(book('by Joseph C. Richardson')) # one argument value

def names(first,middle,last): # three argument variables
    return 'Joseph C. Richardson'

print(names('Python','Programmer\'s','Glossary Bible')) # three argument values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# basic return define functions() numeric overview

def nums(num1,num2): # two argument variables
    return num1+num2-num1

print(nums(2,3)) # two argument values

def nums(num1,num2,num3): # three argument variables
    return num1+num2*num3 # return answer equals order of operation 2+(3*5) = 17

print(nums(2,3,5)) # three argument values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Let's learn what *args are all about. The word 'args' simply means the word
'arguments' for short. One asterisk * is used for *args. Use *args when you
don't know how many argument variables you want within your define function
parameters. Note: you do not need to call the word '*args' as args. However,
you will need to invoke the asterisk * to make *args work. Programmers
know the word as *args by standard definition, but you can use your own words.
'''
def book(*args): # one argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book('unknown number of argument values.','add another unknown argument value.') # two argument values

# Create your own *args function parameter variable as shown below.

def book(*my_unknown_num_arguments): # one argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book('unknown number of argument values.','add another unknown argument value.') # two argument values
'''
As shown in the other define function() examples above, how we needed the exact
number of argument values to the exact number of argument variables. However,
with *args you no longer have to worry about how many argument values you will
need to satisfy the number of argument variables within the define function parameters.
'''
# Let's do some more *args with return functions

def book(*args): # one argumant variable
    return 'Python Programmer\'s Glossary Bible'

print(book('by Joseph C. Richardson','add another unknown argument value.')) # two argument values

def nums(*args): # one argument variable
    return args

print(nums(2,3)) # two argument values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Let's learn what **kwargs are all about. The word 'kwargs' simply means the words
'keyword arguments' for short. Two asterisks ** are used for **kwargs. Use **kwargs
when you don't know how many keyword argument variables you want within your
define function parameters. Note: you do not need to call the word '**kwargs' as kwargs.
However, you will need to invoke two asterisks ** to make **kwargs work. Programmers
know the word as **kwargs by standard definition, but you can use your own words.
'''
def book(**kwargs): # one keyword argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book(keyword='keyword',argument='argument') # two keyword argument values

# This example is without any **kwargs at all; we have to name our keyword arguments.

def book(keyword_arg1,keyword_arg2): # two keyword argument variables
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book(keyword_arg1='keyword',keyword_arg2='argument') # two keyword argument values
'''
As shown in the define function() example above, how we needed the exact number of keyword
argument values to the exact number of keyword argument variables. However, with **kwargs
you no longer have to worry about how many keyword argument values you will need to satisfy
the number of keyword argument variables within the define function parameters.
'''
# Let's create some define functions that act like subroutines.
'''
Since there are no line numbers in Python, also means that we cannot create any such 'go to',
or 'go sub' commands at all with Python. So how can we create subroutines with Python?. How
can we create subroutines without making them jump to line numbers, like we did in the old days?
Well the answer is quite simple. Let's use define functions() with a while loop to create our subroutine
examples.
'''
def subroutine1():
    print('You picked subroutine1')

def subroutine2():
    print('You picked subroutine2')

def subroutine3():
    print('You picked subroutine3')

while True:
    message=input('Please type 1, 2 or 3 to select the subroutine you wish to \
display or type (q) to quit: ').strip()
    if message=='q':
        break
    while True:        
        if message=='1':
            subroutine1()
            break
        elif message=='2':
            subroutine2()
            break
        elif message=='3':
            subroutine3()
            break
        else:
            print('Sorry! No subroutine for that.')
            break
