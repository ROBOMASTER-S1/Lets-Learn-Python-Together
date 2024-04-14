# Python class objects with def functions() and more.

# Created and written by Joseph C. Richardson, GitHub.com

# Let's create a class object with def functions() inside it, then learn how to
# chain them together by invoking the (self) parameter, along with return 'self'.
# Next we will create a def functions() list and call each function() with a for
# loop. Next, we will create the very same class object as before. But this time
# we will also place the class object functions() inside a list. And lastly, we
# will use a for loop to call up all the class object's functions() with a for loop.

class Functs:

    def function1():
        print("I'm function() 1")

    def function2():
        print("I'm function() 2")

    def function3():
        print("I'm function() 3")

    def function4():
        print("I'm function() 4")

Functs.function1()
Functs.function2()
Functs.function3()
Functs.function4()

# Let's chain all these same functions() together. If you want function() 5
# to work, you will need to invoke the 'self' parameter, along with return self.

class Functs:

    def function1(self):
        print("I'm chained function() 1")
        return self

    def function2(self):
        print("I'm chained function() 2")
        return self

    def function3(self):
        print("I'm chained function() 3")
        return self

    def function4(self):
        print("I'm chained function() 4")
        return self

    def function5():
        print("You need the (self) parameter and return 'self' to use me in a function chain.")     

Functs().function1().function2().function3().function4()

# or this:

functions = Functs() # use a variable instead if you like

functions.function1().function2().function3().function4()

Functs.function5()

# You can use the hard return backslash \ to chain the functions() over top of
# one another.

functions.\
            function1().\
            function2().\
            function3().\
            function4()

# Let's place ordinary def functions() in a list instead of a class.

def function1():
        print("I'm function() 1")

def function2():
    print("I'm function() 2")

def function3():
    print("I'm function() 3")

def function4():
    print("I'm function() 4")

functs_list = [
    function1,
    function2,
    function3,
    function4
    ]

functs_list[2]() # call a functs_list index[x]

# Let's shorten the code using a for loop

for i in functs_list:
    i()

# or this:

for i in functs_list:i()

# Let's place our class object def functions() in a list.

class Functs:

    def function1():
        print("I'm function() 1")

    def function2():
        print("I'm function() 2")

    def function3():
        print("I'm function() 3")

    def function4():
        print("I'm function() 4")
        
class_functs_list = [
    Functs.function1,
    Functs.function2,
    Functs.function3,
    Functs.function4
    ]

class_functs_list[2]() # call a class_functs_list index[x]

# Let's shorten the code using a for loop

for i in class_functs_list:
    i()

# or this:

for i in class_functs_list:i()

# Note: you can call 'self' any word you like, but Python programmers use the
# word 'self' as standard programming practice. the 'self' prefix means to make
# a def function() call itself back up, which is known as RECURSION. In computer
# programing, the word 'recursion' is mentioned a lot. So keep this in mind. In
# some cases, recursion can be a bad thing; you have to know when to use it, and
# when not to use it. Never use recursion in for loops, even if they look like
# they work. because errors could occur. For loops have to have a proverbial end
# by nature. Never use recursion in for loops to avoid possible program execution
# errors from happening. Always know when and where you can use recursion; def
# functions() love recursion more than anything.
