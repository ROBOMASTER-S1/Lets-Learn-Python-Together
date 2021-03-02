# Sometimes if you are going to be using and reusing small bits of Python code
# over and over again, you might want to consider using the 'exec' function.
# The 'exec' function can be used in such examples as these examples below.

redundant_code='''
print("Python Programmer's Glossary Bible")
print('This block of code can be used and reused again and again.')
'''

'''----------------------------------------------------------------'''

# Call the 'exec' function as many times as you please.

exec(redundant_code)
exec(redundant_code)
exec(redundant_code)

'''----------------------------------------------------------------'''

# Here is an example, using a for-loop to call the 'exec' function.

for i in range(3):
    exec(redundant_code)
