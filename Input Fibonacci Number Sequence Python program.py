# Input Fibonacci Number Sequence Python program example.

# Created by Joseph C. Richardson, GitHub.com

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

# Input Fibonacci Number Sequence example, using a set{}

num1,num2=0,1

fib={num1,num2}

words=(
    'is in the Fibonacci Sequence.',
    'is not in the Fibonacci Sequence.',
    'Please enter a correct Fibonacci Sequence Number: ',
    'Sorry! Numbers only.',
    'Memory Error!'
    )

try:
    x=int(input(words[2]).strip())

    for i in range(x):
        fib_num=num1+num2
        fib.add(fib_num)
        num1=num2
        num2=fib_num

    if x in fib:
        print(x,words[0])
        
    elif x not in fib:
        print(x,words[1])
        
except ValueError:
    print(words[3])
    
except MemoryError:
    print(words[4])
