# The exc() Function Python program examples

# Created by Joseph C. Richardson, GitHub.com

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

# Sometimes if you are going to be using and reusing small bits of Python code
# over and over again, you might want to consider using the 'exec()' function.
# The 'exec()' function can be used in such examples as these examples below.

redundant_code='''
print("Python Programmer's Glossary Bible")
print('This block of code can be used and reused again and again.')
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Call the 'exec()' function as many times as you please.

exec(redundant_code)
exec(redundant_code)
exec(redundant_code)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is an example, using a for-loop to call the 'exec()' function.

for i in range(3):
    exec(redundant_code)

# Let's create a for loop inside an exec() function and see what happens when
# execute/run this Python program example:

reuse_code='''
for i in range(10):print(i)
'''
exec(reuse_code) # call the exec() function as many times as you wish
exec(reuse_code)
exec(reuse_code)
