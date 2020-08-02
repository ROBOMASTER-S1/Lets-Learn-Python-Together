'Python Clock Functions:'
'''
Python clock functions allow you to program the actual time in real time. \
Python clock functions work internally, in sync with the Windows clock. \
With Python clock functions; you can set the hour, minute, second, month, \
week, day and date. See Python clock function prefix descriptions below.

'%I'	12-hour prefix
'%H'	24-hour prefix
'%M'	Minutes prefix
'%S'	Seconds prefix
'%p'	AM/PM prefix
'%A'	Day of week prefix
'%B'	Month prefix
'%d'	Date prefix
'%Y'	Year prefix
'%U'	Weeks per year prefix
'%j'	Days per year prefix
'''
'''----------------------------------------------------------------'''

# Let's create a simple Python clock by invoking the Python clock function prefixes.
# First, however, we also need to import two modules; 'time' and 'datetime'. Type and
# execute/run the program example below and see what happens.

import time
import datetime

print(datetime.datetime.now().strftime('%I:%M:%S:%p'))
print(datetime.datetime.now().strftime('%H:%M:%S'))
print(datetime.datetime.now().strftime('%A %B %d,%Y'))
print(datetime.datetime.now().strftime('Week %U'))
print(datetime.datetime.now().strftime('Day %j'))

# Remember you can reduce balky code via, using string variables. Let's use 'timer' as
# the variable and use 'datetime.datetime.now()' as the value. Type and execute/run
# the program example below and see what happens.

import time
import datetime

timer=datetime.datetime.now()

print(timer.strftime('%I:%M:%S:%p'))
print(timer.strftime('%H:%M:%S'))
print(timer.strftime('%A %B %d,%Y'))
print(timer.strftime('Week %U'))
print(timer.strftime('Day %j'))

'''----------------------------------------------------------------'''

# Now, let's create a tuple variable called 'show_time' so we can reduce even more
# balky code, and also gain greater manipulative programming skills at the same time.
# Type and execute/run the program example below and see what happens.

import time
import datetime

show_time=(
    '%I:%M:%S:%p',
    '%H:%M:%S',
    '%A %B %d,%Y',
    'Week %U',
    'Day %j'
    )

timer=datetime.datetime.now()

print(timer.strftime(show_time[0]))    
print(timer.strftime(show_time[1]))    
print(timer.strftime(show_time[2]))    
print(timer.strftime(show_time[3]))
print(timer.strftime(show_time[4]))

'''----------------------------------------------------------------'''
 
# Now change and rearrange the tuple number values [0] through [4] in the program
# example above and re-execute/run the program and see what happens.

# Now, let's make our Python clock come to life. Let's also keep the code less balky
# and much more program manipulative at the same time. To make the Python clock
# come to life, we are simply going to use a while-loop to constantly refresh the screen
# output. A 'time.sleep()' function will also be implemented to create a one-second
# sleep delay in the screen output. Let's also implement the 'os.system()' function to
# clear the screen output right after every one-second 'time.sleep' delay. Type and
# execute/run the program example below and see what happens.

import os
import time
import datetime

show_time=(
    '%I:%M:%S:%p',
    '%H:%M:%S',
    '%A %B %d,%Y',
    'Week %U',
    'Day %j'
    )

while True:
    timer=datetime.datetime.now()
    print(timer.strftime(show_time[0]))
    print(timer.strftime(show_time[1]))
    print(timer.strftime(show_time[2]))
    print(timer.strftime(show_time[3]))
    print(timer.strftime(show_time[4]))
    
    time.sleep(1)
    os.system('cls')
    
'''----------------------------------------------------------------'''

# Now, let's use a while-loop and a for-loop to completely reduce our Python clock\
# program; remember to keep it (DRY): 'Don't Repeat Yourself' as shown in the examples \
# above with five repeated 'print' statements. If you notice the example below shows
# only one, single 'print' statement, not five repeated ones.

import os
import time
import datetime

show_time=(
    '%I:%M:%S:%p',
    '%H:%M:%S',
    '%A %B %d,%Y',
    'Week %U',
    'Day %j'
    )

while True:
    for i in show_time:
        timer=datetime.datetime.now()
        print(timer.strftime(i))
    time.sleep(1)
    os.system('cls')
