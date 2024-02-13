# FANTASTIQUE PLASTIQUE Python program example.

# This Python program example truly does work in the real world.
# If you or anyone you know is into mixing glow in the dark powder
# and clear, liquid acrylic plastic mix. This Python program is a must.

# Created by Joseph C. Richardson, GitHub.com

# Note: you must execute/run the program from
# the OS output screen, via double-clicking the Python
# program file itself.

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

import os,math,winsound

text_colour=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[37m'  # index 4 = white 
    )

win_sound=(
    'Windows Notify System Generic', # index 0 = win_sound
    'Windows Background', # index 1 = win_sound
    'Windows Notify Email','BUZZ' # index 2 = win_sound
    )

text_words=(
    f'\n{text_colour[2]}FANTASTIQUE {text_colour[1]}PLASTIQUE \
{text_colour[2]}Easy {text_colour[1]}Mix {text_colour[2]}Converter', # index 0 = text_words

    f'\n{text_colour[4]}Liquid Acrylic Mix: 8.oz = (1) Cup', # index 1 = text_words

    f'\nLiquid Acrylic Mix: 4.oz = One Half Cup', # index 2 = text_words

    f'\nGlow Powder Pigment: 28.349523 Grams = (1) Ounce', # index 3 = text_words

    f'\nGlow Powder Pigment: 14.1747615 Grams = One Half Ounce', # index 4 = text_words

    f'\nLiquid Acrylic Mix and Glow Powder Pigment Ratios: \
(4 = Parts LAM) to (1 = Part GPP)', # index 5 = text_words

    f'\n1.0 Ounce = 28.349523 Grams or 28.35 Grams.' # index 6 = text_words
    )

text_info=(
    f'\n{text_colour[2]}Please Enter Ounce Amount:{text_colour[1]}', # index 0 = text_info

    f'\n{text_colour[4]}Press (Enter) to convert again or press (Q) to quit.{text_colour[1]}', # index 1 = text_info

    f'\n{text_colour[2]}Thanks for measuring with FANTASTIQUE \
PLASTIQUE Easy Mix Converter', # index 2 = text_info

    f'\n{text_colour[0]}ERROR! Input numbers only please.', # index 3 = text_info

    'title FANTASTIQUE PLASTIQUE Easy Mix Converter' # index 4 = text_info
    )

text_works=('cls','q') # clear screen, q = quit

ounce1=float()
ounce0=float()
grams0=float(28.349523)
grams1=round(28.349523,2)

def fan_plast():
    os.system(text_info[4])
    while True:
        os.system(text_works[0])
        winsound.PlaySound(win_sound[0],winsound.SND_ASYNC)
        
        for i in text_words:
            print(i)
            
        try:
            ounce0=float(input(text_info[0]).lower().strip())
            os.system(text_works[0])
            for i in text_words:
                print(i)
                
            winsound.PlaySound(win_sound[1],winsound.SND_ASYNC)
            
            print(f'\n{text_colour[2]}{ounce0} Ounce = {text_colour[1]}\
{ounce0*grams0} {text_colour[2]}Grams or {text_colour[1]}\
{ounce0*grams1} {text_colour[2]}Grams.')
            
            button=input(text_info[1]).lower().strip()
            if button==(''):
                continue
            elif button==(text_works[1]):
                os.system(text_works[0])
                winsound.PlaySound(win_sound[2],winsound.SND_ASYNC)
                print(text_info[2])
                time.sleep(3)
                break
            
        except ValueError:
            os.system(text_works[0])
            
            for i in text_words:
                print(i)
                
            winsound.PlaySound(win_sound[3],winsound.SND_ASYNC)
            
            print(text_info[3])
            
            time.sleep(2)
            
fan_plast()
