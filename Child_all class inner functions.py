# Type and execute/run this child_all class inner functions
# program example below and play around with different
# combinations of how to display the output.

class Math:
    def nums(num1,num2,num3):
        return num1**num2*num3    
    
class Reading:
    def words(word1,word2,word3):
        return word2
    
class Science:
    def people(person1,person2,person3):
        return person2

class Child_all(Math,Reading,Science):
    pass

'''----------------------------------------------------------------'''

# Try these different combination examples.

print(Math.nums(9,2,2))

print(Reading.words('word1','word2','word3'))

print(Science.people(
    'Albert Einstein',
    'Isaac Newton',
    'Stephen Hawking'))

# The 'Child_all' class inherits all the other classes,
# which means any of these class function values can
# be called.

print(Child_all.nums(9,2,2))

print(Child_all.words('word1','word2','word3'))

print(Child_all.people(
    'Albert Einstein',
    'Isaac Newton',
    'Stephen Hawking'))

# Create some strings to shorten your code.

m=Child_all.nums(9,2,2)

r=Child_all.words('word1','word2','word3')

s=Child_all.people(
    'Albert Einstein',
    'Isaac Newton',
    'Stephen Hawking')

print(m,r,s)

print(m*m,r,s)

# Old format:

print('{} counts to {} and uses {}'.format(s,m*m,r))

# New format with the 'f' function:

print(f'{s} counts to {m*m} and uses {r}')

'''---------------------------------------------------------------------------------------'''

# Type and execute/run this child_all class inner functions
# program example below and play around with different
# combinations of how to display the output.

class Addition:
    def nums1(num1,num2,num3):
        return num1+num2+num3
    
class Subtraction:
    def nums2(num1,num2,num3):
        return num1-num2-num3

class Multiplication:
    def nums3(num1,num2,num3):
        return num1*num2*num3

class Division:
    def nums4(num1,num2,num3):
        return num1/num2/num3

class Child_all(
    Addition,Subtraction,
    Multiplication,Division):
    pass

'''----------------------------------------------------------------'''

# Try these different combination examples.

print(Addition.nums1(1,2,3))

print(Subtraction.nums2(1,2,3))

print(Multiplication.nums3(1,2,3))

print(Division.nums4(1,2,3))

# The 'Child_all' class inherits all the other classes,
# which means any of these class function values can
# be called.

print(Child_all.nums1(1,2,3))

print(Child_all.nums2(1,2,3))

print(Child_all.nums3(1,2,3))

print(Child_all.nums4(1,2,3))

'''----------------------------------------------------------------'''

# Create some strings to shorten your code.

a=Addition.nums1(1,2,3)

b=Subtraction.nums2(1,2,3)

c=Multiplication.nums3(1,2,3)

d=Division.nums4(1,2,3)

print(a+b+c+d*3)

'''----------------------------------------------------------------'''

# Create some strings to shorten your code.

a=Child_all.nums1(1,2,3)

b=Child_all.nums2(1,2,3)

c=Child_all.nums3(1,2,3)

d=Child_all.nums4(1,2,3)

print(a+b+c+d*5)

'''---------------------------------------------------------------------------------------'''

# Pass name strings in functions and return
# their values.

def name(
    name1='"Python',
    name2='Programmer\'s',
    name3='Glossary',
    name4='Bible"'):

# Old format:

    return '{} {} {} {}'.format(name1,name2,name3,name4)

print(name())

def name(
    name1='"Python',
    name2='Programmer\'s',
    name3='Glossary',
    name4='Bible"'):

# New format with the 'f' function:

    return f'{name1} {name2} {name3} {name4}'

print(name())

'''---------------------------------------------------------------------------------------'''

# Now, let's pass some of our own string values '"Monty
# Python' and 'is the best' right inside the 'print' statement.

def name(
    name1='"Python',
    name2='Programmer\'s',
    name3='Glossary',
    name4='Bible"'):

# New format with the 'f' function:

    return f'{name1} {name2} {name3} {name4}'

print(name('"Monty Python','is the best'))

# Let's creat a string variable for our 'print' statement.

string=name('"Monty Python','is the best')

print(string)

'''---------------------------------------------------------------------------------------'''

# Create a class called 'All_names' which inherits
# all the properties of the 'Inherit' class

class Inherit:
    def person1(self):
        print('Albert Einstein')
        
    def person2(self):
        print('Isaac Newton')
        
    def person3(self):
        print('Stephen Hawking')

    def math(num1,num2):
        return num1+num2

class All_names(Inherit):
    pass

All_names.person1('')
All_names.person2('')
All_names.person3('')

print(All_names.math(2,8))

# Call the 'Inherit' class properties and notice
# how they have the very same property values
# as in the class 'All_names'.

Inherit.person1('')
Inherit.person2('')
Inherit.person3('')

print(Inherit.math(2,8))

'''---------------------------------------------------------------------------------------'''

# Create functions with for-loops inside them and then
# call the 'Inherit' class values and the 'All_loops' class
# values.

class Inherit:
    def loop1():
        for i in range(10):
            print('Number',i+1)
            
    def loop2():
        for i in range(10):
            print('Create another loop inside a function')
            
    def loop3():
        for i in range(1,11,1):
            print('* '*i,i)
            
class All_loops(Inherit):
    pass
            
All_loops.loop1()
All_loops.loop2()
All_loops.loop3()

# Call the 'Inherit' class properties and notice
# how they have the very same property values
# as in the class 'All_loops'.

Inherit.loop1()
Inherit.loop2()
Inherit.loop3()

'''---------------------------------------------------------------------------------------'''

# Below is a quick map example of what class inheritance
# looks like. The 'pass' function is just a simple function that
# occupies the empty code blocks, so that Python will ignore
# these empty code blocks.

class Inherit1:
    pass
class Inherit2:
    pass
class Inherit3:
    pass
class Inherit_all(Inherit1,Inherit2,Inherit3):
    pass

# Notice how the class inheritance program below is the same
# as our quick map example above. The empty code blocks now
# have some 'def' functions and some 'print' statements in them
# instead of the 'pass' function.

class Inherit1:
    def words1():
        print('Inherit1 prints out words1')
    def words2():
        print('Inherit1 prints out words2')
    def words3():
        print('Inherit1 prints out words3')
        
class Inherit2:
    def words4():
        print('Inherit2 prints out words4')
    def words5():
        print('Inherit2 prints out words5')
    def words6():
        print('Inherit2 prints out words6')
        
class Inherit3:
    def words7():
        print('Inherit3 prints out words7')
    def words8():
        print('Inherit3 prints out words8')
    def words9():
        print('Inherit3 prints out words9')
        
class Inherit_all(Inherit1,Inherit2,Inherit3):
    pass

# Call the 'Inherit1' class properties and notice how they have
# the very same property values as in the class 'Inherit_all'.

Inherit1.words1
Inherit1.words2
Inherit1.words3

Inherit2.words4
Inherit2.words5
Inherit2.words6

Inherit3.words7
Inherit3.words8
Inherit3.words9

# Call the 'Inherit_all' class properties and notice how they have
# the very same property values as in the class 'Inherit1' properties.

Inherit_all.words1()
Inherit_all.words2()
Inherit_all.words3()
Inherit_all.words4()
Inherit_all.words5()
Inherit_all.words6()
Inherit_all.words7()
Inherit_all.words8()
Inherit_all.words9()

'''----------------------------------------------------------------'''

# Now, let's create a 'tuple' for our class inheritance loop.

inherit_loop=(
    Inherit_all.words1(),Inherit_all.words2(),
    Inherit_all.words3(),Inherit_all.words4(),
    Inherit_all.words5(),Inherit_all.words6(),
    Inherit_all.words7(),Inherit_all.words8(),
    Inherit_all.words9()
    )

# Next, let's create a for-loop, which will loop through
# the 'tuple' values instead of having to manually type
# all that redundant code, line by line. The 'pass' function
# is just a simple function that occupies the empty code
# blocks, so that Python will ignore these empty code blocks.

for i in inherit_loop:
    pass

'''---------------------------------------------------------------------------------------'''

class First_Name:
    def first_name(self):
        return self

    def sec_name(self):
        return self

class Last_Name:
    def last_name(self):
        return self
    
class Full_Name(First_Name,Last_Name):
    pass

example1=First_Name.first_name('Example1')
example2=First_Name.sec_name('Example2')

example3=Last_Name.last_name('Example3')

a=Full_Name.first_name('Example1')
b=Full_Name.sec_name('Example2')
c=Full_Name.last_name('Example3')

print(example3)

'''---------------------------------------------------------------------------------------'''

class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f'Hi, I am {self.name}')

john=Person('John Smith')
bob=Person('Bob Smoth')

john.talk()
bob.talk()

'''---------------------------------------------------------------------------------------'''

class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    def bark(self):
        print('bark')

class Cat(Mammal):
    def be_annoying(self):
        print('annoying')

Dog().bark()
Dog().walk()
Cat().walk()
Cat().be_annoying()

'''---------------------------------------------------------------------------------------'''

class First_Class:
    def first():
        print('First Class')
        
class Second_Class:    
    def second():
        print('Second Class')
        
class Third_Class:
    def third():
        print('Third Class')
        
class Forth_Class:
    def forth():
        print('Forth Class')
        
class All_Classes(
    First_Class,
    Second_Class,
    Third_Class,
    Forth_Class
    ):pass

First_Class.first()
All_Classes.first()

'''---------------------------------------------------------------------------------------'''

class Book:    
    def book(
        name1='"Python',
        name2='Programmer\'s',
        name3='Glossary',
        name4='Bible"'
        ):

        return f'{name1} {name2} {name3} {name4}'
    
class Author:
    def author(
        name1='By',
        name2='Joesph',
        name3='C.',
        name4='Richardson'
        ):

        return f'{name1} {name2} {name3} {name4}'

class Full_Name(Book,Author):
    pass

a=Full_Name.book()
b=Full_Name.author()

print(a,b)

'''---------------------------------------------------------------------------------------'''

class Book:
    def __init__(self,book1,book2):
        self.book1=book1
        self.book2=book2

    def testing(book1,book2):
        return book1
    
a=Book.testing('test1','test2')

b=Book('test1','test2').book2

print(a,b)

'''---------------------------------------------------------------------------------------'''

class Main_class:
    def example1():
        print('Main_class')
        
class Second_class:
    def example2():
        print('Second_class')
        
class Third_class:
    def example3():
        print('Third_class')

class Full_class(Main_class,Second_class,Third_class):
    pass

Main_class.example1()
Second_class.example2()
Third_class.example3()

Full_class.example1()
Full_class.example2()
Full_class.example3()

'''---------------------------------------------------------------------------------------'''

class Class_one:
    def __init__(self,value1,value2,value3):
        self.value1=value1
        self.value2=value2
        self.value3=value3
        
class Class_two:
    def __init__(self,value1,value2,value3):
        self.value1=value1
        self.value2=value2
        self.value3=value3
        
class Class_three:
    def __init__(self,value1,value2,value3):
        self.value1=value1
        self.value2=value2
        self.value3=value3
        
class Class_all(Class_one,Class_two,Class_three):
    pass

a=Class_one(
    'Class_one value1',
    'Class_one value2',
    'Class_one value3'
    )

b=Class_two(
    'Class_two value1',
    'Class_two value2',
    'Class_two value3'
    )

c=Class_three(
    'Class_three value1',
    'Class_three value2',
    'Class_three value3'
    )

d=Class_all(
    'Class_all value1',
    'Class_all value2',
    'Class_all value3'
    )

e=Class_all(
    'Class_all value1',
    'Class_all value2',
    'Class_all value3'

    )
f=Class_all(
    'Class_all value1',
    'Class_all value2',
    'Class_all value3'
    )

print(a.value1)
print(b.value2)
print(c.value3)

print(d.value1)
print(e.value2)
print(f.value3)

'''---------------------------------------------------------------------------------------'''

class Class_one:
    def __init__(self,value1,value2,value3):
        self.value1=value1
        self.value2=value2
        self.value3=value3
        
    def get_return_value1(self):
        return self
    
class Class_two:
    def __init__(self,value1,value2,value3):
        self.value1=value1
        self.value2=value2
        self.value3=value3
        
    def get_return_value2(self):
        return self

class Class_three:
    def __init__(self,value1,value2,value3):
        self.value1=value1
        self.value2=value2
        self.value3=value3
        
    def get_return_value3(self):
        return self

class Class_all(Class_one,Class_two,Class_three):
    pass

a=Class_one('value1','value2','value3')
b=Class_all('value1','value2','value3')

print(b.value3)
