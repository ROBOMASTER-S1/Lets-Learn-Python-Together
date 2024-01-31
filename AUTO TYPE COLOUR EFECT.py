# AUTO TYPE COLOUR EFECT Python program example.

# Created by Joseph C. Richardson, GitHub.com

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

# Note: after you save your file, you must double click this file to view it's cool coloured
# text and layout.

import os,time,winsound

text_colours=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

clear_screen='cls'
single_line_break='\n'
double_line_break='\n\n'
indent=' '*2
wave_sound='TYPE'

text_words=(
f'{single_line_break}{indent}"Python Programmer\'s Glossary Bible" \
{single_line_break}{indent}by Joseph C. Richardson{double_line_break}{indent}\
My Python Programmer\'s Glossary Bible has everything you need to get{single_line_break}\
{indent}started. Because great programming always starts with a great programmer’s\
{single_line_break}{indent}manual.{double_line_break}{indent}You can find \
all you need to learn about Python programming on GitHub.com{double_line_break}\
{indent}While you\'re at it, why not try out all my Robomaster S1 Python program\
{single_line_break}{indent}examples, including my Robomaster S1 Comes to Life Python \
program exercise.{double_line_break}{indent}For those who are into the Famous \
Raspberry Pi 4, I also have quite a few{single_line_break}{indent}Python program \
exercises to choose from.{double_line_break}{indent}Simply visit my YouTube channel \
or my GitHub.com profile page to learn{single_line_break}{indent}more. Look for username: \
ROBOMASTER-S1 to get started. Let\'s get into it...',

f'{single_line_break}{indent}Since the age of robotics began in the early \
part of the twenty-first{single_line_break}{indent}century, early roboticists had also \
scrambled about the concept of what{single_line_break}{indent}a robot should be and \
do predictably. However, there is one man, who{single_line_break}{indent}wanted to \
clarify that fact with a bit of a different abstract approach{single_line_break}{indent}to the \
concept of what a robot should be and do. His solution is to create{single_line_break}{indent}\
a robot with unpredictability, via the Random Generator. While roboticists{single_line_break}\
{indent}in general still hash out the same old concepts of what a robot is supposed\
{single_line_break}{indent}to be and do, this one man has set a revolutionary concept of what \
a robot{single_line_break}{indent}isn\'t supposed to be and do. His approach is to create a \
robot that is{single_line_break}{indent}unpredictable, meaning each behavior the robot\'s \
programming consists of,{single_line_break}{indent}it\'s the random generator that gives the \
appearance of a real, living thing{single_line_break}{indent}that is as unpredictable as any \
other real, living being alike.{double_line_break}{indent}I now bring you into the wonderful \
world of robotics and computer science,{single_line_break}{indent}combined with dash of \
imagination.{double_line_break}{indent}And I now welcome you to the awesome Robomaster \
S1 Comes to Life concept in{single_line_break}{indent}robotics science...','cls')

length=0

while length<=len(text_words[0]):
    for i in text_colours:
        print(i+text_words[0][:length])
        winsound.PlaySound(wave_sound,winsound.SND_ASYNC)
        time.sleep(.06)
        os.system(text_words[2])
        length+=1

print(text_colours[6]+text_words[0]);time.sleep(3)

length=0

while length<=len(text_words[1]):    
    print(text_colours[5]+text_words[1][:length])
    winsound.PlaySound(wave_sound,winsound.SND_ASYNC)
    time.sleep(.06)
    os.system(text_words[2])
    length+=1

print(text_colours[6]+text_words[1]);time.sleep(3)
