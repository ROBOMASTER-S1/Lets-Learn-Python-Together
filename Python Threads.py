# Python Threading Python program examples

# Created by Joseph C. Richardson, GitHub.com

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE
'''
With todays computers, how fast and how much possessing speed they can handle.
Why not make the microprocessor do much more than do one thing at a time. Let's
make the computer do two things at the same time. Let's make the microprocessor
handle two or more things at once, using 'THREADING'. Threading allows a bunch
of functions to work at the very same time, making the computer do much more than
wait for the next instruction/instructions to come, while waiting for the code to finish
its instructions before the next bits of code get executed. With threading, you can
do much more with computer programming. To learn more, see Python examples
about threading. There are threads for processor only threads and Daemon threads
alike. For now, let's learn how to use these first. I myself am new to threads. I have
not much research about the others yet. I demonstrate things I actually use and have
used, such as my Raspberry Pi clock video. I make sure I do things so I can explain
things right without the fear of contradiction on my part as well. So get your lazy
computer to do more; it can handle a few def functions to play all at once. But like
anything, there is only so much you can make the computer do. Too many running
functions will eventually slow down your computer. Please keep that in mind.
'''
import os,time,datetime,threading
from time import sleep as delay

def text_input():
       while True:
              message=input(
                     'keep on Pressing "Enter" to see what happens.\nThe clock function(): while loop \
and the text_input function(): while loop will keep on going,\nno matter what the clock function(): \
while loop does.')
              print('The text_input(): function works at the exact same time the clock_function(): does')

def clock_function():
       while True:
              print(datetime.datetime.now().strftime('%I:%M:%S:%p'))
              print(datetime.datetime.now().strftime('%H:%M:%S'))
              print(datetime.datetime.now().strftime('%A %B %d,%Y'))
              print(datetime.datetime.now().strftime('Week %U'))
              print(datetime.datetime.now().strftime('Day %j'))
              delay(2)

a=threading.Thread(target=text_input)
b=threading.Thread(target=clock_function)

a.start()
b.start()
