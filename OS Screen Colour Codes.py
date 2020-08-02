'''Save the Python file as 'OS screen colours'''

# There are also OS screen colours, which also colours text. However, the OS screen
# These os screen colour codes colour individual text characters. See program examples
# below.

import os
os.system('')

text_colours=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

print(f'{text_colours[0]}The text is red')
print(f'{text_colours[1]}The text is green')
print(f'{text_colours[2]}The text is Yellow')

input(f'\n{text_colours[3]}End of Progream example 1. Press Enter.')

'''----------------------------------------------------------------'''

# There are also OS screen colours, which also colours text. However, the OS screen
# colours are not as flexible as text colours are. For example, If you try to make one
# line of text blue and try to make the next line of text green. When you execute/run the
# program, the next line of text you coloured green will override the blue text, making
# it green text too. Note: you must execute/run the program from the OS output
# screen, via double-clicking the Python program file itself.

import os
os.system('')

white=('color f')
blue=('color 9')
red=('color 4')
green=('color a')
cyan=('color b')
pink=('color c')

os.system(blue)
print('The text is blue')

input('\nEnd of Progream example 2. Press Enter')

os.system(green)
print('The text is green')

input('\nEnd of Progream examples. Press Enter to end the program.')
