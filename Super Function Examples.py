'''Ooh! The Super() Function. What does that do?'''

# Here is the simplest way, I had learned how to use the
# super() function in Python. I created separate python
# program examples to, not only walk you through the
# process of what the super() function is, but to also walk
# myself through it so I could know what it means and how
# to use it. Now, I hope I can turn 'can' into 'could' for others,
# such as myself, who watched different examples on Youtube,
# or in online Python programming text examples. But to
# truly understand what the super() function is, you have to
# start small, then gradually apply the super() function as you
# learn, or brush up on classes and class inheritance. Because
# when we learn to apply the super() function, you will have
# to fully understand what class inheritance is first. But believe
# it or not, it's quite easy to understand, but you need to start
# with small classes and class inheritance examples first to
# get you going. These super() function Python program
# examples were quite the puzzle to understand for me, and
# still are to this day; four years later, I'm still trying to master
# the super() function technique in Python. However, I hope
# I've helped others understand this super() function Python
# puzzle just a wee bit more than before, such as myself.

# Here are three separate, single classes with a simple function
# inside each of them. Each class is called by its own name, along
# with its own function name alike. Fore example: A.first(); A is the
# name of the class and first() is the name of the function. You can
# give any name you wish to classes and functions; they don't have
# to be called A, B or Mom, Dad or Child. However it's a grand start
# to teach yourself how to understand what classes and functions
# do in Python. Python is practically based on using functions,
# hence the term Object Oriented Programming.

class A:
    def first():
        print('A')

class B:
    def second():
        print('B')

class C:
    def third():
        print('C')

# Let's call each class by its own name and function name
# alike.

A.first()
B.second()
C.third()

# Let's add a child class so we can create a class inheritance,
# which will inherit each of these class attributes under one,
# single child class act; ABC is the child class, A, B and C are
# parent classes. Let's expand more about class inheritance
# in the next Python program examples, using the dunder
# init method: __init__ or constructor.

class ABC(A,B,C): # class inheritance
    pass

ABC.first()
ABC.second()
ABC.third()

# Let's try some of the same things, but with the use of the
# return statement that returns values from inside of functions.

class A:
    def first(letter):
        return letter

class B:
    def second(letter):
        return letter

class C:
    def third(letter):
        return letter

a=A.first('A')
b=B.second('B')
c=C.third('C')

print(a)
print(b)
print(c)

class ABC(A,B,C): # class inheritance
    pass

a=ABC.first('A')
b=ABC.second('B')
c=ABC.third('C')

# Let's try some more of the same things, with the use of the
# return statement that returns objects from inside of functions.

class A:
    def first(object):
        return 'A'

class B:
    def second(object):
        return 'B'

class C:
    def third(object):
        return 'C'

a=A.first(object)
b=B.second(object)
c=C.third(object)

print(a)
print(b)
print(c)

class ABC(A,B,C): # class inheritance
    pass

a=ABC.first(object)
b=ABC.second(object)
c=ABC.third(object)

print(a)
print(b)
print(c)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This Parent1, Parent2 and Child class example doesn't
# invoke the super() function at all. Each parent class gets
# called by their individual class names, via the Child class.
# The '__init__' method or constructor initiates the function's
# attributes so they can retrieve their values, such as the
# name attribute, which retrieves the values 'Bob' and 'Rob'.
# The word 'self' is simply telling the def function to call itself
# so it can retrieve its own attributes and values alike.

class Parent1:
    def __init__(self,name):
        print('Parent1 __init__',name)

class Parent2(Parent1):
    def __init__(self,name):
        print('Parent2 __init__',name)

class Child(Parent2):
    def __init__(self):
        Parent1.__init__(self,'Bob')
        Parent2.__init__(self,'Rob')

Child()

# Why not use this instead?

class Parent1:
    def __init__(self,name):
        print('Parent1 __init__',name)

class Parent2:
    def __init__(self,name):
        print('Parent2 __init__',name)

class Child(Parent1,Parent2): # kill two birds with one child class
    def __init__(self):
        Parent1.__init__(self,'Bob')
        Parent2.__init__(self,'Rob')

Child()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now use the super() function within our classes.
# The super() function calls Attributes from another class,
# which allow us to 'reuse our class attributes again and
# again. Remember, programmers hate to recreate code
# and they love to reuse code whenever possible. The
# super() function allows us to treat classes in the same
# fashion. Also, the super() function allows us to call class
# constructors ie: __init__ which cannot be called from other
# classes without using the super() function.

class Parent1:
    def __init__(self,name):        
        print('Parent1 __init__',name)

class Parent2(Parent1):
    def __init__(self,name):
        print('Parent2 __init__',name)
        super().__init__('Bob')
        
class Child(Parent2):
    def __init__(self):        
        super().__init__('Rob')
        
Child()

# Why not use this instead?

class Parent1:
    def __init__(self,name):        
        print('Parent1 __init__',name)

class Parent2:
    def __init__(self,name):
        print('Parent2 __init__',name)
        super().__init__('Bob')
        
class Child(Parent2,Parent1): # kill two birds with one child class
    def __init__(self):        
        super().__init__('Rob')
        
Child()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Base_Class_Attributes:
    def __init__(self,attribute1,attribute2,attribute3):
        self.attribute1=attribute1,
        self.attribute2=attribute2,
        self.attribute3=attribute3
        
        print('My',attribute1+',',attribute2,'and my',attribute3)

# These work just fine, but there is way too much base class calling
# redundancy. Three tips to remember. Never recreate code. Always
# reuse code. Keep it DRY (Don't Repeat Yourself)

Base_Class_Attributes('attribute value 1','attribute value 2','attribute value 3')
Base_Class_Attributes('Reuse my attribute1','Reuse my attribute2','Reuse my attribute3')
Base_Class_Attributes('Alright!','Enough is enough!','Redundancy is bad!')

# Why not consider using the super() function instead to avoid base
# class calling redundancy.

class Base_Class_Attributes:
    def __init__(self,attribute1,attribute2,attribute3):
        self.attribute1=attribute1,
        self.attribute2=attribute2,
        self.attribute3=attribute3
        
        print('My',attribute1+',',attribute2,'and my',attribute3)

class Call_Base_Class_Attributes(Base_Class_Attributes):
    def __init__(self):
        super().__init__('attribute value 1','attribute value 2','attribute value 3')
        super().__init__('Reuse my attribute1','Reuse my attribute2','Reuse my attribute3')
        super().__init__('Super!','Super!','Excellent!')

Call_Base_Class_Attributes() # No more redundant base class calling.

# Super Duper!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Pets:
    def __init__(self,dog,cat,bird,fish):
        self.dog=dog;self.cat=cat
        self.bird=bird;self.fish=fish
        
        print(f'My {dog}, my {cat}, my {bird} \
and my {fish} are GREAT pets to have.')

class Needs:
    def __init__(self,cage,food,water,love):
        self.cage=cage;self.food=food
        self.water=water;self.love=love

        print(f'You need a {cage}, some {food}, \
some {water} and some {love} are all you need.')

class Toys:
    def __init__(self,bones,ball,squeak_toy,mouse_toy):
        self.bones=bones;self.ball=ball
        self.squeak_toy=squeak_toy
        self.mouse_toy=mouse_toy

        print(f'Dogs need to chew {bones} and play \
with a {ball}. \nCats need to play with a {mouse_toy}; \
while birds love to play with {squeak_toy}.')

class Super1(Pets):
    def __init__(self):
         super().__init__('German Shepherd',
                          'Tabby','Parrot','Angelfish')

class Super2(Needs):
    def __init__(self):
        super().__init__('Cage','Food','Water',
                         'Unconditional Love')

class Super3(Toys):
    def __init__(self):
        super().__init__('Bones','Bouncy Ball',
                         'Squeaky Toys','Mouse Toys')

# Call each class called Super1(), Super2() and Super3()

Super1()
Super2()
Super3()

# Why not create a tuple that can loop through each class?

super_loop_tuple=(Super1,Super2,Super3)

# You can also call up any tuple elements in the super_loop_tuple
# starting at position zero, through positon two.

super_loop_tuple[0]()
super_loop_tuple[1]()
super_loop_tuple[2]()

# Create a for-loop that can loop through each class instead.
# Let's use our super_loop_tuple for this

for i in super_loop_tuple:
    (i())
