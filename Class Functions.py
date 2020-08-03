'''The Class Function:'''
'''
The class function in Python is like a super function, which can have multiple def functions right inside it. \
Class functions may consist of parent classes and child classes alike. The child classes inherit the parent \
classes, which means giving functions the ability to change their behavior outcome, throughout a program's \
execution run. You can use as many parent/upper classes you wish. However, only one child class can be used, \
which is always the last class act. You don't need to invoke def functions to use classes either. However, we \
are going to learn about both types such as this program example below, which doesn't invoke def functions at all.
'''

# Type and execute/run the program example below and see what
# happens.

class Grandma:
    gm='I\'m the Grandma class'

class Grandpa:
    gp='I\'m the Grandpa class'

class Mom:
    m='I\'m the Mom class'

class Dad:
    d='I\'m the Dad class'

class Child(Grandma,Grandpa,Mom,Dad):
    pass

print(Child.gm)
print(Child.gp)
print(Child.m)
print(Child.d)

# The 'pass' function tells the program to ignore the empty code block until later use,
# via the programmer's choice.

'''----------------------------------------------------------------'''

# Now let's place a 'print' statement where the 'pass' function was. Type and
# execute/run the program below and see what happens.

class Grandma:
    gm='I\'m the Grandma class'

class Grandpa:
    gp='I\'m the Grandpa class'

class Mom:
    m='I\'m the Mom class'

class Dad:
    d='I\'m the Dad class'

class Child(Grandma,Grandpa,Mom,Dad):
    print("The 'pass' function is now a print statement.")

print(Child.gm)
print(Child.gp)
print(Child.m)
print(Child.d)

'''----------------------------------------------------------------'''

# Sometimes a code block needs information, but you, the programmer does not wish
# to provide that, and that's where the 'pass' function comes in handy. Sometimes you
# don't want to use any code in a code block at all; that's the whole purpose of what
# the 'pass' function is all about. The 'pass' function ignores the code block and caries
# on its way, without the potential risk of errors. Here is an example of such an error.
# Type and execute/run the program examples below and see what happens.

class syntax_error:

# You will get a syntax error: 'expected an indented block'

class pass_function:
    pass

# The 'pass' function ignores the empty code block, which allows the programmer to
# decide what to do later on, or simply 'pass' the empty code block altogether. Use the
# 'pass' function in any type of empty code block to avoid potential errors from
# occurring.

'''----------------------------------------------------------------'''

# Classes can also be single classes, such as the program example below illustrates.
# Type and execute/run the program below and see what happens.

class Single_class:
    sc='I\'m a single class.'

print(Single_class.sc)

'''----------------------------------------------------------------'''

# Here is a simple Mom class and a simple Dad class, along with their simple Child
# class. Type and execute/run the program example below and see what happens.

class Mom:
    mom='I\'m Chid\'s Mom.'

class Dad:
    dad='I\'m Child\'s Dad.'

class Child(Mom,Dad):
    pass

print(Child.mom)
print(Child.dad)

# Let's call up the class function called 'Mom'.

print(Mom.mom)

# Let's call up the class function called 'Dad'.

print(Dad.dad)

# Let's call up Mom and Dad inside one, single 'print' statement.

print(Mom.mom,Dad.dad)

# Let's call up the Child class inside one, single 'print' statement.

print(Child.mom,Child.dad)

'''----------------------------------------------------------------'''

# Here is our very same Mom and Dad class program example, which uses list
# variables called 'mom' and 'dad'. Type and execute/run the program below and see
# what happens.

class Mom:
    mom=[
        'Class Mom with list item position [0]',
        'Class Mom with list item position [1]',
        'Class Mom with list item position [2]',
        ]
    
class Dad:
    dad=[
        'Class Dad with list item position [0]',
        'Class Dad with list item position [1]',
        'Class Dad with list item position [2]',
        ]
    
class Child(Mom,Dad):
    pass

print(f'The Child class inherits all classes:\n{Child.mom[0]}')
print(f'The Child class inherits all classes:\n{Child.dad[1]}')

'''----------------------------------------------------------------'''

# Now let's have some fun and change the words in the list. Let's also use double (")
# quote marks instead of single (') quote marks. Note: the (f') format function is not
# invoked inside the 'print' statements. However, you can still invoke the (f') format
# function if you like. Type and execute/run the program below and see what happens.

class Mom:
    mom=[
        "Mom's are the best!",
        "Mom's care so much!",
        "Mom's make dreams happen!",
        ]
    
class Dad:
    dad=[
        "Dad's are the best!",
        "Dad's care so much!",
        "Dad's make dreams happen!",
        ]
    
class Child(Mom,Dad):
    pass

print(Child.mom[0])
print(Child.dad[1])

'''----------------------------------------------------------------'''

# Tip: invoke the 'pass' function to make it much easier to create classes. Remove any
# 'pass' functions you no longer need, when adding code inside empty code blocks.
# Type and execute/run the program example below and see what doesn't happen.

class Mom:
    pass

class Dad:
    pass

class Child(Mom,Dad):
    pass

'''----------------------------------------------------------------'''

# The program above works just fine even if it shows no output on the screen. The
# reason that is, is simply because the 'pass' functions are just empty placeholders
# that occupy the empty code blocks, until the programmer decides to add code
# inside the empty code blocks.

# Type and execute/run the program example below and see what happens.

class Mom:
    mom='Mom'

class Dad:
    pass

class Child(Mom,Dad):
    pass

print(Mom.mom)
print(Child.mom)
print(Mom.mom,Child.mom)

'''----------------------------------------------------------------'''

# Now it's time to grow up and learn some more about classes, without Mom and Dad
# around. Classes don't need to be called Mom and Dad or Child to work. You can give
# classes any name you wish. Classes always start with an uppercase letter like
# 'Mom', 'Dad' and 'Child'. However, you can use lowercase letters if you like.

# The program example below illustrates a single class function, which invokes two
# def function blocks. Single class functions with two or more def function blocks work
# similar to parent and child class functions. Creating function classes simply means
# adding more versatility to functions in general. Type and execute/run the program
# below and see what happens.

class My_Shapes:
    def __init__(self,shape,sides):
        self.shape=shape
        self.sides=sides
        
    def shape_sides(self):
        return f'{self.shape} {self.sides}'
    
a=My_Shapes('Hexagon','Six Sides')
b=My_Shapes('Octagon','Eight Sides')
c=My_Shapes('Dodecagon','Twelve Sides')

print(f'{a.shape} {b.shape} {c.shape}')
print(f'{a.shape_sides()} {b.shape_sides()} {c.shape_sides()}')

'''----------------------------------------------------------------'''

# The program example below is the very same program example above. The only
# difference is, 'num' was added to create a third argument.

class Shapes:
    def __init__(self,shape,num,sides):
        self.shape=shape
        self.num=num
        self.sides=sides
        
    def shape_sides(self):
        return f'{self.shape} {self.num} {self.sides}'
    
a=Shapes('Hexagon',6,'sides')
b=Shapes('Octagon',8,'sides')
c=Shapes('Dodecagon',12,'sides')

print(f'{a.shape} {b.shape} {c.shape}')
print(f'{a.num} {b.num} {c.num}')
print(f'{a.shape_sides()} {b.shape_sides()} {c.shape_sides()}')

'''----------------------------------------------------------------'''

# The program example above uses a dunder method, which consists of two double
# underscores '__ __', called dunders. The dunder 'init' method is one of the most used
# methods. These special dunder methods are sometimes called 'Magic Methods', and
# these special methods allow us to emulate built-in data types or implement operator
# overloading. You probably didn't know it, but you've been using these dunder
# methods all along. These methods can be extremely powerful if they are used
# correctly. The dunder 'init' means to initialize a function. The word 'Dunder' simply
# means 'Double__Underscore'.

# These two 'print' statements below use the dunder method 'add', which is the same
# as the 'print' statements 'print(2+3)' and 'print('a'+'b')'. The 'int' function adds only
# integer numbers together, whereas the 'str' function concatenates/joins character
# strings together.

print(int.__add__(2,3))

# Screen output:	5

print(str.__add__('a','b'))

# Screen output:	ab

# Dunder methods assure functionality inside class functions. For example, you
# wouldn't use a dunder '__str__' method with integer values; likewise, you wouldn't
# use a dunder '__add__' method with character string values.

# Take a close look at these two program examples below. You notice there are
# yellow highlighted variables. These variables indicate how these two, very same
# program examples can be written. Both program examples do exactly the same
# thing, even though they look a wee bit different. Type and execute/run these two
# program examples below and see what happens.

# Program example 1:

class Dunder_add:
    def __init__(self,num):
        self.num=num
        
    def __add__(self,plus):
        return self.num+plus

a=Dunder_add(6)
b=Dunder_add(8)
c=Dunder_add(12)

print(a.num+b.num+c.num)

# Program example 2:

class Dunder_add:
    def __init__(self,num):
        self.num=num
        
    def __add__(self,plus):
        return self.num+plus.num

a=Dunder_add(6)
b=Dunder_add(8)
c=Dunder_add(12)

print(a+b+c.num)

# There are several types of dunder methods in Python. However, we will only focus
# on the ones we will learn for now.

# Take a close look at these two program examples below. You notice there are
# yellow highlighted variables. These variables indicate how these two, very same
# program examples can be written. Both program examples do exactly the same
# thing, even though they look a wee bit different. Type and execute/run these two
# program examples below and see what happens.

# Program example 1:

class Shapes:
    def __init__(self,shape,sides):
        self.shape=shape
        self.sides=sides
        
    def shape_sides(self):
        return f'{self.shape} {self.sides}'
    
    def __add__(self,add_num):
        return self.sides+add_num

a=Shapes('Hexagon',6)
b=Shapes('Octagon',8)
c=Shapes('Dodecagon',12)

print(a.sides+b.sides+c.sides)

print(a.shape_sides(),b.shape_sides(),c.shape_sides())

# Program example 2:

class Shapes:
    def __init__(self,shape,sides):
        self.shape=shape
        self.sides=sides
        
    def shape_sides(self):
        return f'{self.shape} {self.sides}'
    
    def __add__(self,add_num):
        return self.sides+add_num.sides

a=Shapes('Hexagon',6)
b=Shapes('Octagon',8)
c=Shapes('Dodecagon',12)

print(a+b+c.sides)

print(a.shape_sides(),b.shape_sides(),c.shape_sides())

'''----------------------------------------------------------------'''

# The program example below converts two integers into string characters, while still
# being able to calculate the result of the actual integer values themselves. Type and
# execute/run the program example below and see what happens.

class Dunder_str:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def __str__(self):
        return str(f'{self.num1}/{self.num2}, and I want more text')
    
dunder=Dunder_str(26,2+3)

print ("I want these integers to be a string, using 'str'.",str(dunder),'here.')

'''----------------------------------------------------------------'''

# The program example below uses the dunder method '__repr__', which follows the
# dunder method '__str__' as a fallback for programmers to see code as human,
# readable text. Type and execute/run the program example below and see what
# happens.

class Dunder_str:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def __str__(self):
        return str(f'{self.num1}/{self.num2}, and I want more text')
    
    def __repr__(self):
        return str(f'{self.num1},{self.num2}, and I want more text')
    
dunder=Dunder_str(26,2+3)

print("I want these integers to be a string, using 'str'.",str(dunder),'here.')

print("I want these integers to be an object, using 'repr'.",repr(dunder),'here.')

'''----------------------------------------------------------------'''

# Here is a multi-class function program that has multiple def statements in it. Each
# def statement has a different return math operation, such as addition, subtraction,
# multiplication, division, square and cube operations. The asterisk (*) is used for
# multiplying numbers together. Type and execute/run the program example below
# and see what happens.

class Math0:
    def addit(num1,num2):
        return num1+num2
    
class Math1:
    def subtr(num1,num2):
        return num1-num2
    
class Math2:
    def multi(num1,num2):
        return num1*num2
    
class Math3:
    def divis(num1,num2):
        return num1/num2
    
class Math4:
    def square(num1,num2):
        return num1**num2
    
class Math5:
    def cube(num1,num2):
        return num1**num2*num1
    
class Sum (
    Math0,Math1,
    Math2,Math3,
    Math4,Math5
    ):
    pass

print(Sum.addit(5,2))
print(Sum.subtr(5,2))
print(Sum.multi(5,2))
print(Sum.divis(5,2))
print(Sum.square(5,2))
print(Sum.cube(5,2))

# Let's add three class functions together inside the 'print' statement.

print(Sum.addit(5,2)+Sum.subtr(5,2)+Sum.cube(5,2))

'''----------------------------------------------------------------'''

# Now, let's create a list called 'x' and add all the class functions together inside the
# 'print' statement. Remember to use list indexing ie: [ ] starting at list index [0]. Also
# remember that Python always starts at index [0] with tuples, lists and dictionaries
# alike.

x=(
    Sum.addit(5,2),
    Sum.subtr(5,2),
    Sum.multi(5,2),
    Sum.divis(5,2),
    Sum.square(5,2),
    Sum.cube(5,2)
    )

print(x[0]+x[1]+x[2]+x[3]+x[4]+x[5])

# Let's call up all the actual functions, which are inside the multi-class function
# program example.

print(Math0.addit(5,2))

print(Math1.subtr(5,2))

print(Math2.multi(5,2))

print(Math3.divis(5,2))

print(Math4.square(5,2))

print(Math5.cube(5,2))

'''----------------------------------------------------------------'''

# The class function program example below works exactly the same as the class
# 'Shapes' function program example does. Type and execute/run the program and
# see what happens.

class Scientists:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def full_name(self):
        return f'{self.first_name} {self.last_name}' 
   
a=Scientists('Stephen','Hawking')
b=Scientists('Albert','Einstein')
c=Scientists('Isaac','Newton')
d=Scientists('Galileo','Galilei')

'''----------------------------------------------------------------'''

# Try these 'print' statement examples below and change the letter 'b' to the letter 'a'
# and try the letter 'c' and so on. Re-execute/run the program and see what happens.

print(f'{b.first_name}')
print(f'{b.last_name}')
print(f'{b.full_name()}')

# Make a sentence out of this 'print' statement program example:

print(f'{b.full_name()} loves science, and \
so does {a.full_name()}, along with {d.first_name}.')

'''----------------------------------------------------------------'''

# Type and execute/run the program example below and see what
# happens.

class Mathematics:
    def __init__(self,addition,subtraction,
                 multiplication,division):
        self.addition=addition
        self.subtraction=subtraction
        self.multiplication=multiplication
        self.division=division        
    def Math_Functions(self):
        return self.addition,self.subtraction
        return self.multiplication,self.division

nums=Mathematics(3+2,3-2,3*2,6/2)

names=Mathematics(
    'Stephen Hawking',
    'Albert Einstien',
    'Isaac Newton',
    'Galileo Galilei'
    )

print(
    f'{nums.addition}',f'{names.addition}\n'
    f'{nums.subtraction}',f'{names.subtraction}\n'
    f'{nums.multiplication}',f'{names.multiplication}\n'
    f'{int(nums.division)}',f'{names.division}'
    )
