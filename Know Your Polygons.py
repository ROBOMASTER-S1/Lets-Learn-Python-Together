# Know Your Polygons

# Created by Joseph C. Richardson, GitHub.com

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

# See what happens when you type and execute/run this guessing
# game program example below. Note: you must execute/run the
# program from the OS output screen, via double-clicking the Python
# program file itself.

# Save the Python file as 'Know Your Polygons'

import os

tc=(
    '\x1b[31m',
    '\x1b[32m',
    '\x1b[33m',
    '\x1b[34m',
    '\x1b[35m',
    '\x1b[36m',
    '\x1b[37m',
    'cls'
    )

question_prompts1=(
    f'{tc[2]}How many sides does a Triangle have?\n\n{tc[1]}(a) {tc[2]}four sides\n\
{tc[1]}(b) {tc[2]}three sides\n{tc[1]}(c) {tc[2]}two sides',
    
    f'{tc[2]}How many sides does a Square have?\n\n{tc[1]}(a) {tc[2]}Two sides\n\
{tc[1]}(b) {tc[2]}Three sides\n{tc[1]}(c) {tc[2]}Four sides',
    
    f'{tc[2]}How many sides does a Pentagon have?\n\n{tc[1]}(a) {tc[2]}four sides\n\
{tc[1]}(b) {tc[2]}five sides\n{tc[1]}(c) {tc[2]}Three sides',
    
    f'{tc[2]}How many sides does a Hexagon have?\n\n{tc[1]}(a) {tc[2]}six sides\n\
{tc[1]}(b) {tc[2]}five sides\n{tc[1]}(c) {tc[2]}two sides',
    
    f'{tc[2]}How many sides does a Octagon have?\n\n{tc[1]}(a) {tc[2]}four sides\n\
{tc[1]}(b) {tc[2]}six sides\n{tc[1]}(c) {tc[2]}eight sides',
    
    f'{tc[2]}How many sides does a Dodecagon have?\n\n{tc[1]}(a) {tc[2]}eight \
sides\n{tc[1]}(b) {tc[2]}three sides\n{tc[1]}(c) {tc[2]}twelve sides',
    
    f'{tc[2]}How many sides does a Hexadecagon have?\n\n{tc[1]}(a) {tc[2]}sixteen \
sides\n{tc[1]}(b) {tc[2]}eight sides\n{tc[1]}(c) {tc[2]}six sides'
    )

prompt=('b','c','b','a','c','c','a')

score=0
loop=0

while loop<=6:
    
    os.system(tc[7])
    button=input((tc[1])+'\nKnow Your Polygons!\n\n'+(tc[2])+'Know Your Polygons\n\n'+\
    question_prompts1[loop]+'\n\n'+(tc[0])+'READY:'+(tc[1])).strip()
    
    if button==(prompt[loop]):
        score+=1
        
    loop+=1
    
    os.system(tc[7])    
print(f'\n{tc[2]}Know Your Polygons\n\n{tc[2]}You got \
{score}/{len(question_prompts1)} questions correct.\nCongratulations! Your total \
Prize Winnings: {tc[1]}${score*100*score:,}.00 {tc[2]}Dollars.\n\n{tc[0]}READY:')

input('\nEND OF PROGRAM! Press Enter to quit.')
