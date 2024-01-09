'''
My Class Function Examples of the way I tinkered around to learn
what they are and how they work. But I had to know why they worked
first of all. I hope this can help others out as well. I actually explained
all this to myself, just like these Python class act examples below
show. When learning anything, you have to do it as well. Well, here
is my way of doing it as well as learning it.

The class function in Python is like a super function, which can have
multiple def functions right inside it. Class functions may consist of
parent classes and child classes alike. The child classes inherit the
parent classes, which means giving functions the ability to change
their behavior outcome, throughout a program's execution run. You
can use as many parent/upper classes you wish. However, only one
child class can be used, which is always the last class act. You don't
need to invoke def functions to use classes either. However, we are
going to learn about both types such as this program example below,
which doesn't invoke def functions at all.
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

# The 'pass' function tells the program to ignore the empty code
# block until later use, via the programmer's choice.

# Now let's place a 'print' statement where the 'pass' function was.
# Type and execute/run the program below and see what happens.

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

# Sometimes a code block needs information, but you, the programmer
# does not wish to provide that, and that's where the 'pass' function
# comes in handy. Sometimes you don't want to use any code in a code
# block at all; that's the whole purpose of what the 'pass' function is all
# about. The 'pass' function ignores the code block and caries on its
# way, without the potential risk of errors. Here is an example of such an
# error. Type and execute/run the program examples below and see what
# happens.

class syntax_error:

# You will get a syntax error: 'expected an indented block'

class pass_function:
    pass

# The 'pass' function ignores the empty code block, which allows the
# programmer to decide what to do later on, or simply 'pass' the empty
# code block altogether. Use the 'pass' function in any type of empty
# code block to avoid potential errors from occurring.

# Classes can also be single classes, such as the program example
# below illustrates. Type and execute/run the program below and see
# what happens.

class Single_class:
    sc='I\'m a single class.'

print(Single_class.sc)

# Here is a simple Mom class and a simple Dad class, along with
# their simple Child class. Type and execute/run the program
# example below and see what happens.

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

# Here is our very same Mom and Dad class program example,
# which uses list variables called 'mom' and 'dad'. Type and
# execute/run the program below and see what happens.

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
