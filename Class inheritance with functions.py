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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
