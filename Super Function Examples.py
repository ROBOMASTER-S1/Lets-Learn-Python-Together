# Let's learn what the 'super()' function does, when we want to use
# attributes from the Main class, if we want all our classes to be the
# same. Let's use the 'super()' function to get rid of redundant attribute
# code blocks, since they are all the same. Let's get real lazy now.

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

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
        print(self.first_name,'I have long',self.colour,self.hair,'and',self.eyes)

Parent_main('John','Smith',23)
Sub_child1('John','Smith',23,'Dog','Cat','Bird','Fish')
Sub_child2('Jane','Smith',23,'hair','blond','huge blue eyes.')

print(Main_class('John','Smith',23).first_name)
print(Sub_class1('John','Smith',23).last_name)
print(Sub_class2('John','Smith',23).age)
