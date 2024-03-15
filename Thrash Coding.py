# Thrash Coding with Python for Advanced Python Programmers.
# These Python examples might be a bit tricky for beginners to fully
# understand. However, this is what Python is sometimes all about.
# These Python program examples below create fun auto typing
# text, using the 'len()' function within a while-loop to count the entire
# length of text, letter by letter, including empty spaces in between
# text words/sentences alike.

import os,time;from time import sleep as delay

clear_screen='cls'
line_break='\n'
indent=' '*2
auto_type_speed=.05
text,text_len=print,len

auto_text=(
    'Auto Backward Typing Text is so much fun to make.'[::-1],
    '.ekam ot nuf hcum os si txeT gnipyT drawkcaB otuA'[::-1])

length=0
while length<=text_len(auto_text[0]):
    os.system(clear_screen)
    text(line_break+indent+auto_text[0][:length]) # forward forward text
    delay(auto_type_speed)
    length+=1
delay(1)

length=0
while length<=text_len(auto_text[0]):
    os.system(clear_screen)
    text(line_break+indent+auto_text[0][length:]) # reverse forward text
    delay(auto_type_speed)
    length+=1

length=0
while length<=text_len(auto_text[1]):
    os.system(clear_screen)
    text(line_break+indent+auto_text[1][:length]) # forward backward text
    delay(auto_type_speed)
    length+=1
delay(1)

length=0
while length<=text_len(auto_text[1]):
    os.system(clear_screen)
    text(line_break+indent+auto_text[1][length:]) # reverse backward text
    delay(auto_type_speed)
    length+=1
delay(1)
