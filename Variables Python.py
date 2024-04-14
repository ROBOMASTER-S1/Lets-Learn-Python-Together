# Auto Typing with Python for Advanced Python Programmers.
# These Python examples might be a bit tricky for beginners to fully
# understand. However, this is what Python programming is sometimes
# all about. These Python program examples below create fun auto
# typing text, using the 'len()' function within a while-loop to count the
# entire length of text, letter by letter, including empty spaces in between
# text words/sentences alike. Note: in these examples, we are going to
# learn some things the HARD WAY, such as string concatenation. This
# way you can learn what it's like to use the + plus sign to join strings
# and variables together without the use of the f' string. We are using
# raw string concatenation, is what I like to call it. Highlight, then copy
# and then paste this Python program into your preferred Python Idle.
# Save the program as 'Auto Type.py', then simply double click the
# Python program file to run it from the DOS window. See images below:

# Created by Joseph C. Richardson, GitHub.com

import os,time;from time import sleep as delay

clear_screen='cls'
line_break='\n'
indent=' '*2
auto_type_speed=.05
text,text_length=print,len

auto_text=(
    'Auto Backward Typing Text is so much fun to make.'[::-1],
    '.ekam ot nuf hcum os si txeT gnipyT drawkcaB otuA'[::-1])

length=0

while length<=text_length(auto_text[0]):
    os.system(clear_screen)
    text(line_break+indent+auto_text[0][:length]) # forward type reverse text
    delay(auto_type_speed);length+=1
    
delay(1)

length=0

while length<=text_length(auto_text[0]):
    os.system(clear_screen)
    text(line_break+indent+auto_text[0][length:]) # reverse type reverse text
    delay(auto_type_speed);length+=1

length=0

while length<=text_length(auto_text[1]):
    os.system(clear_screen)
    text(line_break+indent+auto_text[1][:length]) # forward type forward text
    delay(auto_type_speed);length+=1
    
delay(1)

length=0

while length<=text_length(auto_text[1]):
    os.system(clear_screen)
    text(line_break+indent+auto_text[1][length:]) # reverse type forward text
    delay(auto_type_speed);length+=1
