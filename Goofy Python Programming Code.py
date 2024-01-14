# Hardcore Goofy Python Programming Code that actually works

# I don't recommend that you program in this sort of fashion.
# The program does work fine, but other programmers wouldn't
# be able to make sense of it, when they have to take over the nightshift.
# Programmers call this type of coding: 'DIRTY CODE PROGRAMMING'

# Python is a very forgiving language that you can do this sort of thing
# as you can clearly see below. However, it looks quite confusing and
# very intimidating to new programmers, who want to learn to write code.
# So, execute/run this Python program below, but do not take it to school or
# work. However, this program will teach you some of the innereds of Python
# in general; the things you can do with it, as well as finding its own flaws.
# Python has some flaws in it, but they ony show up once in a while. Python
# executes from the top, downward; the same way the programmer had written
# it down on each line. Therefore, other commands might not execute right
# if some of the programming code is not in the right, top/down order the
# programming list has to be in for Python to work properly. You will learn
# this as you encounter it as you journey into computer programming, and
# beyond it.

x = []
line_brk='\n'
dline_brk='\n\n'
text=print,input
loop=range

sentence='type a list of five words: '.capitalize(),\
          'you have all'.capitalize(),'items in your list of words.'

for i in loop(1,6):message=text[1](sentence[0]).title().strip();x.append(message)

text[0]()
for j in loop(i):x.sort(),text[0](x[j],end=' ')

text[0](dline_brk+sentence[1],i,sentence[2])
