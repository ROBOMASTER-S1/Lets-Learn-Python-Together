# Here is how I am trying to understand what threading
# is all about. It seems as if each def function runs each
# threaded instruction starting from the top downward
# on each of the def function's instructions. The delay(n)
# function shows how the threads work, as if looking at
# them in a slow motion time lapse to show how they
# work with each def function call thread. Threading gives
# the illusion that each of the four def functions are running
# at the same time, when really, they aren't.

from time import sleep as delay;import threading

def function1():
       print('print commands 1')
       delay(1)
       print('print commands 2')
       delay(1)
       print('print commands 3')
       delay(1)
       print('print commands 4')
       delay(1)

def function2():
       print('print commands 1')
       delay(1)
       print('print commands 2')
       delay(1)
       print('print commands 3')
       delay(1)
       print('print commands 4')
       delay(1)

def function3():
       print('print commands 1')
       delay(1)
       print('print commands 2')
       delay(1)
       print('print commands 3')
       delay(1)
       print('print commands 4')
       delay(1)

def function4():
       print('print commands 1')
       delay(1)
       print('print commands 2')
       delay(1)
       print('print commands 3')
       delay(1)
       print('print commands 4')
       delay(1)

# Call the thread functions example 1:

threading.Thread(target=function1).start()
threading.Thread(target=function2).start()
threading.Thread(target=function3).start()
threading.Thread(target=function4).start()

# Call the thread functions example 2:

a=threading.Thread(target=function1)
b=threading.Thread(target=function2)
c=threading.Thread(target=function3)
d=threading.Thread(target=function4)

a.start()
b.start()
c.start()
d.start()
       
# For-loop example:

my_threads=(
   threading.Thread(target=function1),
   threading.Thread(target=function2),
   threading.Thread(target=function3),
   threading.Thread(target=function4))

for i in my_threads:
   i.start()
