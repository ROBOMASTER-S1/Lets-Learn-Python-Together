# Fibonacci Natural Number Sequence Python program example.

# Created by Joseph C. Richardson, GitHub.com

# Note: you must execute/run the program from
# the OS output screen, via double-clicking the Python
# program file itself.

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

import os,time,winsound

os.system(f'title Fibonacci Natural Number Sequence')

text_colours=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

text_words=(
    f'{text_colours[1]}Fibonacci Natural Number Sequence in Action...',

    f'\n\n{text_colours[2]}Fibonacci Natural Number Sequence example: \
[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610...]',

    f'\n\n{text_colours[5]}Fibonacci Natural Numbers go on forever!',
    f'\n\nFibonacci Natural Numbers can only be found in \
nature, such as plants and animals...'
    )

sounds=('Ring03','Speech Off')

def Fib_Num():
    winsound.PlaySound(sounds[0],winsound.SND_ASYNC)

    for i in range(25):
        print('\n',' '*i,text_words[0])
        time.sleep(.25)
        os.system('cls')

    num1=0
    num2=1
    fib=[num1,num2]

    while True:
        num3=num1+num2
        fib.append(num3)
        num1=num2
        num2=num3
        clock=(time.asctime())

        print('\n',' '*25,text_words[0],text_words[1],text_words[2])

        print(f'\nFibonacci Natural Number Sequence: {text_colours[2]}\
{num1} {text_colours[5]}+ {text_colours[2]}{num2}{text_colours[5]} = \
({text_colours[0]}{num1+num3}{text_colours[5]}){text_colours[5]}\n\n\
Fibonacci Natural Numbers: "{text_colours[0]}{num1+num3:,}{text_colours[5]}\
"\n\n{text_colours[0]}Date & Time:\n\n{clock}')

        winsound.PlaySound(sounds[1],winsound.SND_ALIAS)
        os.system('cls')

Fib_Num()
