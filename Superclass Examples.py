# These superclass examples are also my own tinkering from other such examples. However, super() and __init__
# constructors are still very new to me. So please don't ask me how to understand what I made, because I honestly don't.
# Well, I understand classes and functions, but the super() function is very new to me. But, I'm pretty darn sure I
# will figure it all out in due time...

class Super_class:
    def super1(self):
        print('Super1')

    def super2(self):
        print('Super2')

    def super3(self):
        print('Super3')

class Class_all(Super_class):
    def get_values(self):
        super().super1()
        super().super2()
        super().super3()

Class_all().get_values()

'''-----------------------------------------------------------------------------'''

class Super:
    def person(self):
        print('person(self) is from Super class')

    def home(self):
        print('home(self) is from Super class')
        
class Sub:
    def pet(self):
        print('pet(self) is from Sub class')

    def toys(self):
        print('toys(self) is from Sub class')

class Class_all(Super,Sub):
    def get_all(self):
        super().person()
        super().home()
        super().pet()
        super().toys()

Class_all().get_all()

'''-----------------------------------------------------------------------------'''

class Super_class:
    def __init__(self,value1,value2,value3):
        self.value1=value1
        self.value2=value2
        self.value3=value3
        
class Super_sub(Super_class):
    def __init__(self,value1,value2,value3):
        super().__init__(value1,value2,value3)

a=Super_class('value1','value2','value3')


print(f'{a.value1}, {a.value2} and {a.value3}')

'''-----------------------------------------------------------------------------'''

class Super_class:
    def __init__(self,value1,value2,value3):
        self.value1=value1
        self.value2=value2
        self.value3=value3
        
class Super_sub(Super_class):
    def __init__(self,value1,value2,value3):
        super().__init__(value1,value2,value3)

super_class_string=[
    Super_class('John','dog',4),
    Super_class('Tom','cat',7),
    Super_class('Bob','bird',4),
    Super_class('Ron','fish',9)
    ]

print(f'{super_class_string[0].value1} is {super_class_string[0].value3} \
years old, and he loves his {super_class_string[0].value2} very much.')

a=super_class_string

print(f'{a[0].value1} is {a[0].value3} years old, and he loves his {a[0].value2} \
very much.')

for i in super_class_string:
    print(f'{i.value1} is {i.value3} years old, and he loves his {i.value2} very much.')

'''-----------------------------------------------------------------------------'''

class Super1:
    def __init__(self,value1,value2,value3,value4):
        self.var1=value1
        self.var2=value2
        self.var3=value3
        self.var4=value4

class Super2(Super1):
    def __init__(self,var1,var2,var3,var4):
        super().__init__(var1,var2,var3,var4)

class Super3(Super1):
    def __init__(self,var1,var2,var3,var4):
        super().__init__(var1,var2,var3,var4)

class Super4(Super1):
    def __init__(self,var1,var2,var3,var4):
        super().__init__(var1,var2,var3,var4)

print(Super1('value1','value2','value3','value4').var1)
print(Super2('value1','value2','value3','value4').var2)
print(Super3('value1','value2','value3','value4').var3)
print(Super4('value1','value2','value3','value4').var4)
       
a=Super1('value1','value2','value3','value4')
b=Super2('value1','value2','value3','value4')
c=Super3('value1','value2','value3','value4')
d=Super4('value1','value2','value3','value4')

print(a.var1,b.var2,c.var3,d.var4)

'''-----------------------------------------------------------------------------'''

class Student_body:
    def __init__(
        self,value1,
        value2,value3,
        value4,value5):
            
        self.var1=value1
        self.var2=value2
        self.var3=value3
        self.var4=value4
        self.var5=value5

class First_name(Student_body):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)
    
class Middle_name(Student_body):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)
        
class Last_name(Student_body):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)
        
class Student_age(Student_body):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)
        
class Student_grade(Student_body):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)
    
class Students(Student_body):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)
        
a=First_name(
    'First name1',
    'First name2',
    'First name3',
    'First name4',
    'First name5'
    )
b=Middle_name(
    'Middle name1',
    'Middle name2',
    'Middle name3',
    'Middle name4',
    'Middle name5'
    )
c=Last_name(
    'Last name1',
    'Last name2',
    'Last name3',
    'Last name4',
    'Last name5'
    )
    
d=Student_age(22,18,17,20,19)
e=Student_grade(12,10,12,11,9)

print(e.var1)

'''-----------------------------------------------------------------------------'''

class Student_body:
    def __init__(
        self,value1,
        value2,value3,
        value4,value5):
            
        self.var1=value1
        self.var2=value2
        self.var3=value3
        self.var4=value4
        self.var5=value5

class First_name(Student_body):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)
    
class Middle_name(Student_body):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)
        
class Last_name(Student_body):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)
        
class Student_age(Student_body):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)
        
class Student_grade(Student_body):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)
    
class Students(Student_body):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)

list_args=[
    First_name(
        'First name1','First name2',
        'First name3','First name4',
        'First name5'),
    Middle_name(
        'Middle name1','Middle name2',
        'Middle name3','Middle name4',
        'Middle name5'),
    Last_name(
        'Last name1','Last name2',
        'Last name3','Last name4',
        'Last name5'),
        
    Student_age(22,18,17,20,19),
    Student_grade(12,10,12,11,9)
    ]

print(f'Student {list_args[0].var1} {list_args[1].var1}. {list_args[2].var1}')
print(f'Student age:{list_args[3].var1} Student grad:{list_args[4].var1}')

'''-----------------------------------------------------------------------------'''

class Super_dooper:
    def __init__(
        self,value1,
        value2,value3,
        value4,value5):
        self.var1=value1
        self.var2=value2
        self.var3=value3
        self.var4=value4
        self.var5=value5
    
class Super1(Super_dooper):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)
        
class Super2(Super_dooper):
    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4,var5)
        
a=Super2('value1','value2','value3','value4','value5')

print(a.var5)

'''-----------------------------------------------------------------------------'''

class A(object):
    def __init__(self):
        print('first')
        
class B(object):
    def __init__(self):
        print('second')
        
class C(A,B):
    def __init__(self):
        super().__init__()
        print('third')
        
My_object=C()

'''-----------------------------------------------------------------------------'''

class Super1:
   def first(self):
       print('Super1')
       
class Super2:
   def second(self):
       print('Super2')
       
class Super3:
   def third(self):
       print('Super3')
       
class Super4:
   def forth(self):
       print('Super4')
       
class Child(Super1,Super2,Super3,Super4):
    def allclass(self):
        print('lets call all the classes at once.')
        super().first()
        super().second()
        super().third()
        super().forth()
        
Child().allclass()
