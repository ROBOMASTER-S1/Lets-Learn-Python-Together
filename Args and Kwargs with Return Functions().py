# Created by Joseph C. Richardson, GitHub.com

# Try these *args and **kwargs with return functions() Python program examples

def arguments(arg1,arg2):
    return 'Return my arguments.'

print(arguments('placeholder value 1','placeholder value 2'))

def arguments(*args):
    return 'Return my *args.'

print(arguments('placeholder value 1','placeholder value 2'))

def arguments(num1,num2):
    return num1 * num2

print(arguments(2,4))

def arguments(*args):
    return 2 * 4

print(arguments('placeholder value 1','placeholder value 2'))

def keyword_arguments(kwarg1,kwarg2):
    return 'Return my keyword arguments.'

print(keyword_arguments(kwarg1='placeholder value 1',kwarg2='placeholder value 2'))

def keyword_arguments(**kwargs):
    return 'Return my **kwargs.'

print(keyword_arguments(kwarg1='placeholder value 1',kwarg2='placeholder value 2'))

def keyword_arguments(num1,num2):
    return num1 * num2

print(keyword_arguments(num1=2,num2=4))

def keyword_arguments(**kwargs):
    return 2 * 4

print(keyword_arguments(num1='placeholder value 1',num2='placeholder value 2'))
