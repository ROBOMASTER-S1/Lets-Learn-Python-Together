# Let's make some Mad Python Code, that works great, but it won't cut
# it in the real world when most words, including ones you can create
# yourself must be a standard for other programmers to understand
# when they take over the night shift. Since there isn't any such things
# on my part, being self taught on Python is a blessing in disguise to me
# and to 'You!', The learner. So let's get started with some Mad Python Code
# and see what kind of Python madness we can conjure up, while we have
# fun learning Python at the same time. Please note, it's a good idea if you
# understand basic Python. And if you don't, you can still have fun learning
# all about it on your own. Try these fun Python program examples out and
# have some fun with them, even if you don't understand Python at all.

# Let's make a function that doesn't use the word 'self', but it will still
# understand what 'self' is, no matter what we call it.

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

class Correct_Python_Code:
    def __init__(self,name,age):
        self.name=name
        self.age=age

a=Correct_Python_Code('Bob',40)

print(a.name,'is',a.age,'years old.')

# This works, but it's not the correct Python way of doing things in the programming
# world. But, sometimes it's a good idea to see what code does when you alter it;
# you will only get one of two things that will happen, either you will get an error, or
# the program will still work as if no code was altered.

class Mad_Python_Code:
    def __init__(fles,eman,ega):
        fles.eman=eman
        fles.ega=ega
        
a=Mad_Python_Code('Rob',50)

print(a.eman,'is',a.ega,'years old.')

# Why not have some fun with Dictionaries. Try these
# Python program examples to get a feel of how dictionaries
# in Python work and how useful they truly are in programs.

# Let's create an animals dictionary so we can use its values.

animals={
    'Dog':'Wolf',
    'Cat':'Lion',
    'Bird':'Eagle',
    'Fish':'Shark'
    }

print(animals.get('dog'))
print(animals.get('dog','Not Found!'))
print(animals.get('Dog','Not Found!'))

for key,value in animals.items():
    print(key)

for key,value in animals.items():
    print(value)

for key,value in animals.items():
    print(key,value)

# Let's create some sentences out of our animals dictionary list.

d=animals.get('Dog')
c=animals.get('Cat')
b=animals.get('Bird')
f=animals.get('Fish')

print(f'My dog is really a {d}.')
print(f'My Cat is really a {c}.')
print(f'My Bird is really a {b}.')
print(f'My Fish is really a {f}.')

# Let's create some sentences out of our animals dictionary list
# using a 'for in' items() function to drastically reduce lines of
# code and code redundancy in our Python program example.

for keys,values in animals.items():
    print(f'My {keys} is really a {values}.')

# Rename the key and value variables if you wish.

for my_keys,my_values in animals.items():
    print(f'My {my_keys} is really a {my_values}.')

for animal_keys,animal_values in animals.items():
    print(f'My {animal_keys} is really a {animal_values}.')

fun_list1=['John','Bob','Rob','Tom']
fun_list2=['Dog','Cat','Bird','Fish']
fun_list3=['Desktop','Laptop','Cellphone','Notebook']

for list1,list2,list3 in zip(fun_list1,fun_list2,fun_list3):
    print(f"My name is {list1} and I have a {list2} picture on my {list3} screen.")

# pet=['Dog','Cat','Bird','Fish']

name_list=[['John','Bob','Rob','Tom'],['Desktop','Laptop','Cellphone','Notebook']]

for index,name in enumerate(name_list):
    print(name[0],name[1],name[2],name[3])

name_list=['John','Bob','Rob','Tom']

for index,name in enumerate(name_list):
    print(index)

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

# Let's hurt our brain just a wee bit and create a class inheritance
# with two functions inside it. First, we will start off with creating
# two functions called student1 and student2. Next we will create
# two, separate classes called Student1 and Student2 and place
# our two functions inside them. After that, we will create our class
# inheritance called Students with our two classes inside it. Note:
# to be sure that each programming step works, type and execute/
# run each program example first, before you proceed to the next
# programming steps.

def student1(fname,lname,grade,marks):
        if marks>50 and marks<80:
            print('Congrats!',fname,lname,'passed.')
        elif marks>=80:
            print('Congrats!',fname,lname,'passed with an A++.')
        else:
            print('Sorry!',fname,lname,'failed grade',str(grade)+'.')

def student2(fname,lname,grade,marks):
        if marks>50 and marks<80:
            print('Congrats!',fname,lname,'passed.')
        elif marks>=80:
            print('Congrats!',fname,lname,'passed with an A++.')
        else:
            print('Sorry!',fname,lname,'failed grade',str(grade)+'.')

student1('John','Smith',11,80) # call the student1 function
student2('Jane','Smith',12,30) # call the student2 function

# Let's place our functions, student1 and student2 inside each
# of these two classes, Student1 and Student2. Note: to be sure
# that each programming step works, type and execute/run each
# program example first, before you proceed to the next
# programming steps.

class Student1:

    def student1(fname,lname,grade,marks):
        if marks>50 and marks<80:
            print('Congrats!',fname,lname,'passed.')
        elif marks>=80:
            print('Congrats!',fname,lname,'passed with an A++.')
        else:
            print('Sorry!',fname,lname,'failed grade',str(grade)+'.')

class Student2:

    def student2(fname,lname,grade,marks):
        if marks>50 and marks<80:
            print('Congrats!',fname,lname,'passed.')
        elif marks>=80:
            print('Congrats!',fname,lname,'passed with an A++.')
        else:
            print('Sorry!',fname,lname,'failed grade',str(grade)+'.')

Student1.student1('John','Smith',11,80) # call the Student1 class
Student2.student2('Jane','Smith',12,30) # call the Student2 class
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, finally let's create our class inheritance called Students.

# class Students(Student1,Student2):

class Student1:

    def student1(fname,lname,grade,marks):
        if marks>50 and marks<80:
            print('Congrats!',fname,lname,'passed.')
        elif marks>=80:
            print('Congrats!',fname,lname,'passed with an A++.')
        else:
            print('Sorry!',fname,lname,'failed grade',str(grade)+'.')

class Student2:

    def student2(fname,lname,grade,marks):
        if marks>50 and marks<80:
            print('Congrats!',fname,lname,'passed.')
        elif marks>=80:
            print('Congrats!',fname,lname,'passed with an A++.')
        else:
            print('Sorry!',fname,lname,'failed grade',str(grade)+'.')

class Students(Student1,Student2): # class inheritance of Student1 and Student2
    pass # use 'pass' as an empty placeholder.

Students.student1('John','Smith',11,80) # call the Students inheritance class
Students.student2('Jane','Smith',12,30) # call the Students inheritance class
