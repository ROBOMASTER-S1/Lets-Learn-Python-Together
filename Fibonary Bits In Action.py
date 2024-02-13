# Fibonary Bits In Action! Python program example.

# Created by Joseph C. Richardson, GitHub.com

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

# This is for advanced Python programmers, who want something a little bit saltier.
# Create this Fibonary Bits In Action! Python program using a single print() function.
# Use the backslash '\' to create line breaks within the print() function.

# Note: after you save your file, you must double click this file to view it's cool coloured
# text and layout.

import os;os.system('title fibonary bits in action! 3'.title())
from time import sleep as delay

red='\x1b[31m'
green='\x1b[32m'
blue='\x1b[34m'
yellow='\x1b[33m'
purple='\x1b[35m'
white='\x1b[37m'

title_text=f'fibonary bits in action! 3'.title(),'fibonacci natural number sequence'.title()
text=(' binary digits: ',' octal digits: ',' hexadecimal digits: ',' decimal digits:',
      ' fibonacci digits: '.title())

lb='\n';lbb='\n\n';elb=' =\n';eq=' = ';sp=' '

num1=0;num2=1
fib=[num1,num2]

pause=1

while True:
    os.system('cls')
    num3=num1+num2
    fib.append(num3)
    num1=num2;num2=num3
    
    b=f'{num3:b}';o=f'{num3:o}'
    x=f'{num3:X}';d=f'{num3:d}'

# old string formatted print() function example:

    print('{}{}{}{}{}{}{}{}{}{}{}'.format(
        white+lb+sp*16+title_text[0]+lb+red+lb+sp*4,
        len(b),green+text[0].title()+yellow+b+blue+elb+sp*4+
        green+red,len(o),green,text[1].title()+yellow+o+blue+
        elb+sp*4+green+red,len(x),green+text[2].title()+yellow+
        x,blue+eq+green+lb+sp*4+red,len(d),green+text[3].title()+
        blue+eq+yellow+d+lbb+white+sp*11+title_text[1]+lbb+green+
        sp*3+text[4]+yellow+f'{num3:,d}'))    
    delay(pause)
