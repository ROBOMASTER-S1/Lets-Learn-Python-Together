
from time import sleep as delay;import os;os.system('title Binary Beat')

# Created by Joseph C. Richardson, GitHub.com

red='\x1b[31m'
green='\x1b[32m'
blue='\x1b[34m'
yellow='\x1b[33m'
purple='\x1b[35m'
white='\x1b[37m'
os.system('cls')
n=0
while True:
    print(white+'\n'+' '*6+'welcome to the binary beat in motion python program example'.title()
          +yellow+'\n\n'+' '*6+'1     1    1    1    1   1   1   1 = eight bits or one byte'
          +'\n\n'+' '*6+'128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = decimal number: 255''\n\n'+' '*2
          +'binary base: 2, octal base: 8, hexadecimal base: 16, decimal base: 10'.title()
          +'\n\n'+' '*3+yellow,len(f'{n:b}'),green+'binary digits: '.title()
          +yellow+f'{n:b} '+red+'=\n\n'+' '*3+yellow,len(f'{n:o}'),green+'octal digits: '.title()
          +yellow+f'{n:o} '+red+'=\n\n'+green+' '*3+yellow,len(f'{n:x}'),green+'hexadecimal digits: '.title()
          +yellow+f'{n:X} '+red+'= '+green+'\n\n'+' '*3+yellow,len(f'{n:d}'),green+'decimal digits: '.title()
          +red+'= '+yellow+f'{n:d}');delay(1);os.system('cls');n+=1
