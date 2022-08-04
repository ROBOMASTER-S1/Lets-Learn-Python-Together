from time import sleep as delay;import os;os.system('title Binary Beat')

# For all you Hardcore Python Programmers out there,
# this One's for YOU! Welcome to the Binary Beat in
# Motion Python program example.

red='\x1b[31m'
green='\x1b[32m'
blue='\x1b[34m'
yellow='\x1b[33m'
purple='\x1b[35m'
white='\x1b[37m'

text=f'binary base 2, Octal base 8, hexadecimal \
base 16, decimal base 10 systems:\n'.title()

a=0
while True:
    print(purple+'\n'+' '*2+text+blue,'\n',' '*20,len(f'{a:b}'),green+\
          'binary digits: '.title()+yellow+f'{a:b} '+red+'=\n',' '*22+green+\
          ' octal digits: '.title()+yellow+f'{a:o} '+red+'=\n',' '*22+green+\
          ' hexadecimal: '.title()+yellow+f'{a:X} '+red+'= '+green,'\n',' '*22,
          f'decimal: '.title()+red+'= '+yellow+f'{a:d}')
    delay(.5)
    os.system('cls')
    a+=1
