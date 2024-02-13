# ASCII CODE TRANSLATOR Python program example.

# Created by Joseph C. Richardson, GitHub.com

# Note: you must execute/run the program from
# the OS output screen, via double-clicking the Python
# program file itself.

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

import os,math

text_features=(
    'cls', # index 0 = clear screen
    '\x1b[31m', # index 1 = red
    '\x1b[32m', # index 2 = green
    '\x1b[33m', # index 3 = yellow
    '\x1b[34m', # index 4 = blue
    '\x1b[37m'  # index 5 = red
    )

text_words=(
    f'\n{text_features[3]}ASCII CODE NUMERIC VALUE TRANSLATOR\n', # index 0 = text_words

    f'\n{text_features[3]}ASCII CODE CHARACTER VALUE TRANSLATOR\n', # index 1 = text_words

    f'\n{text_features[3]}ASCII CODE TRANSLATOR', # index 2 = text_words

    f'\n{text_features[3]}Thanks for choosing ASCII CODE TRANSLATOR', # index 3 = text_words

    'title ASCII CODE TRANSLATOR' # index 4 = text_words
    )

word_info=(
    f'{text_features[5]}Please type a number, then press \
(Enter) to confirm:{text_features[2]}', # index 0 = word_info

    f'{text_features[5]}Please type a letter key or a number key, then press \
(Enter) to confirm:{text_features[2]}', # index 1 = word_info

    f'\n{text_features[3]}Please choose which ASCII code translator you \
would like to use:\n\n{text_features[5]}Press (1) for ASCII code number \
values.\nPress (2) for ASCII code character values.\nPress \
(Q) to quit.{text_features[2]} ', # index 2 = word_info

    f'\n\n{text_features[3]}Do you wish to continue? Press \
(Enter) or press (Q) to quit:{text_features[2]}', # index 3 = word_info

    f'\n{text_features[1]}This is a Value Error!', # index 4 = word_info

    f'\n{text_features[1]}This is a Type Error!' # index 5 = word_info
    )

button=('1','2','q')

def ascii_codes():
    os.system(text_words[4])
    def subroutine1():
        while True:
            os.system(text_features[0])
            print(text_words[0])
            
            try:
                ascii_code=int(input(word_info[0]).strip())
                ascii_code=input(f'\n{text_features[2]}{chr(ascii_code)}\
{text_features[5]} = ASCII code: " {text_features[2]}{ascii_code}\
{text_features[5]} " {word_info[3]}').lower().lower().strip()
                if ascii_code==button[2]:
                    break
                
            except ValueError:
                print(word_info[4])
                time.sleep(2)

    def subroutine2():
        while True:
            os.system(text_features[0])
            print(text_words[1])
            
            try:
                ascii_code=input(word_info[1]).strip()
                ascii_code=input(f'\n{text_features[2]}{ascii_code}\
{text_features[5]} = ASCII code: " {text_features[2]}{ord(ascii_code)}\
{text_features[5]} " {word_info[3]}').lower().strip()
                if ascii_code==button[2]:
                    break
                
            except TypeError:
                print(word_info[5])                
                time.sleep(2)

    while True:
        os.system(text_features[0])
        print(text_words[2])
        
        butt=input(word_info[2]).lower().strip()
        if butt==button[0]:
            subroutine1()
        elif butt==button[1]:
           subroutine2()
           
        else:
            if butt==button[2]:
                os.system(text_features[0])
                print(text_words[3])
                time.sleep(3)
                break
            
ascii_codes()
