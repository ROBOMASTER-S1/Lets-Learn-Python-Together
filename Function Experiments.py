# For when you get bored, try these two Python programming experiments out.

def get_value(name,program,book,author='by Joseph C. Richardson'):
    return name,program,book,author,'is GREAT!'

get_name=get_value('Python','Programmer\'s','Glossary Bible')

for i in get_name:
    print(i,end=' ')

# Try this global variables function experiment out and see what happens
# when you delete or comment out the 'science()' function call statement,
# using the '#' in front of it like this: # science(), or simply delete it.

a,e='atom','electron'

def science():
    global a,e
    a,e='Albert','Einstein'

science() # comment out, or delete this function call statement.
    
print(a,e)
