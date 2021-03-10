# Some class return function experiments to tinker with. Because
# this time, I'm not going to teach anything here. Just tinker away
# like I had to when I created these Mad Computer Science Python
# programming experiment examples to add to my collection for
# others to learn Python with me too.

class Python_book:    
    def python_book(
        value1,value2,value3,value4='bible'.title()):
        return value1+value2+value3+value4
    
    book=python_book(
        'python '.title(),"Programmer's ",'glossary '.title())

class Author:    
    def name(
        first_name,middle_name,last_name):
        return first_name+middle_name+last_name
    
    author=name('joseph ','c. ','richardson')

class Birthday:    
    def birthdate(
        month,day,year=' sorry! i can\'t tell you that.'):
        return month+day+year

    birthday=birthdate('december ',str(9),',0000')

class Data_record(
    Python_book,Author,Birthday):
    pass

cat='book: ','author: ','birthday: '

get_data_records=(
    cat[0].title()+Data_record.book,
    cat[1].title()+Data_record.author.title(),
    cat[2].title()+Data_record.birthday.upper())

for i in get_data_records:
    print(i,'\n')

input('Press "Enter" to continue these program examples.\n')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Scientists:
    def __init__(
        self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def full_name(self):
        return f'{self.first_name} {self.last_name}' 

class Mathematics:    
    def addition(num1,num2):
        return num1+num2    
    def subtraction(num1,num2):
        return num1-num2
    def multiplication(num1,num2):
        return num1*num2
    def division(num1,num2):
        return num1/num2
    def square(num1,num2):
        return num1**num2
    
class Smart_data(Scientists,Mathematics):
    pass

a=Smart_data('stephen','hawking')
b=Smart_data('albert','einstein')
c=Smart_data('isaac','newton')
d=Smart_data('galileo','galilei')

e=Smart_data.addition(10,5)
f=Smart_data.subtraction(10,5)
g=Smart_data.multiplication(10,5)
h=Smart_data.division(10,5)
i=Smart_data.square(10,5)

loop_first_name=(
    a.first_name,b.first_name,
    c.first_name,d.first_name,)

loop_last_name=(
    a.last_name,b.last_name,
    c.last_name,d.last_name)

loop_full_name=(
    a.full_name,b.full_name,
    c.full_name,d.full_name)
    
loop_mathematics=[e,f,g,h,i]

for i in loop_full_name:
    print(f'physicist, {i()}'.title(),'was a Mathematician.\n')

for i in loop_mathematics:
    print(f'print smart: {i:,}\n'.title())
       
input('Press "Enter" to close the prompt window.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
