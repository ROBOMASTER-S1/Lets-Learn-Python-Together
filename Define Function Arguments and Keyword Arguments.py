# Created and written by Joseph C. Richardson, GitHub.com
'''
The define function() can contain arguments inside its parameters. The number of argument
variables must satisfy the equal number of argument placeholder values as well.
'''
def argument(argument1,argument2,argument3): # three argument variables        
    print('This is the nature of using arguments inside def function() parameters.')

# three argument variable placeholder values
argument('argument placeholder 1','argument placeholder 2','argument placeholder 3')
'''
The define function() can contain keyword arguments inside its parameters. The number
of keyword argument variables must satisfy the equal number of keyword argument variables
and their placeholder values as well.
'''
def keyword_argument(key,word,argument): # three keyword argument variables  
    print('This is the nature of using keyword arguments inside def function() parameters.')

# three keyword argument variables and their placeholder values
keyword_argument(key='key',word='word',argument='argument')
'''
Here are the very same set of Python define function() arguments and keyword arguments without
all the comments so we can see a much clearer picture of what the two look like.
'''
def argument(argument1,argument2,argument3):       
    print('This is the nature of using arguments inside def function() parameters.')

argument('argument placeholder 1','argument placeholder 2','argument placeholder 3')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def keyword_argument(key,word,argument):
    print('This is the nature of using keyword arguments inside def function() parameters.')

keyword_argument(key='key',word='word',argument='argument')
'''
When we use arguments and keyword arguments inside define function() parameters, there are
big differences between the two. With basic arguments, such as in the first and second examples
above, we can clearly see that with basic arguments, the arguments don't have repeated variables
and equal = signs. Whereas keyword arguments do need repeated variables and equal = signs.
Here are the two illustrations in comparison with one another, so we can clearly see where the two
types drastically differ from one another.
'''
argument('argument placeholder 1','argument placeholder 2','argument placeholder 3')

keyword_argument(key='key',word='word',argument='argument')
