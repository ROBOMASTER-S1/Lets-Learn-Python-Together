
#  These super class examples are also my own tinkering
#  from other such examples. However, super() and __init__
#  constructors are still very new to me. So please don't ask
#  me how to understand what I made, because I honestly don't.
#  Well, I understand classes and functions, but the super() function
#  is very new to me. But, I'm pretty darn sure I will figure it all out in
#  due time...

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

print(f'{a[0].value1} is {a[0].value3} years old, and he loves his {a[0].value2} very much.')

for i in super_class_string:
    print(f'{i.value1} is {i.value3} years old, and he loves his {i.value2} very much.')
