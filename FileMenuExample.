# You will need to import your own files to correctly make this Python \
# file menu program example work. You can also use some of my program \
# examples to create a working Python file menu of your very own.

import os,time,winsound
from secpoem import secret_poem
from ASCIIcharacterguide import ascii_codes
from FantastiquePlastique import fan_plast
from MajesticCalculator import maj_cal
from ONTARIOLOTO import ont_lotto
from TypeGame import type_game

text_features=(
    'cls', # index 0 = clear screen
    ' '*45, # index 1 = 45 spaces
    '*'*118, # index 2 = 118 asterisks
    '\x1b[31m', # index 3 = red
    '\x1b[32m', # index 4 = green
    '\x1b[33m', # index 5 = yellow
    '\x1b[34m', # index 6 = blue
    '\x1b[37m'  # index 7 = white
    )

sounds=('Ring05','Ring06')

text_words=(
    f'\n{text_features[1]}{text_features[5]}J.C.R \
Soft{text_features[4]}~{text_features[5]}Choice', # index 0 = text_words

    f'\n{text_features[4]}{text_features[2]}', # index 1 = text_words

    f'\n{text_features[5]}To open a choice, press any one of \
the selected number keys below, then press \
({text_features[3]}ENTER{text_features[5]}) to confirm.', # index 2 = text_words

    f'\n({text_features[4]}1{text_features[5]}): ASCII CODE \
TRANSLATOR', # index 3 = text_words

    f'\n({text_features[4]}2{text_features[5]}): FANTASTIQUE \
PLASTIQUE Easy Mix Converter', # index 4 = text_words

    f'\n({text_features[4]}3{text_features[5]}): Majestic Calculator', # index 5 = text_words

    f'\n({text_features[4]}4{text_features[5]}): ONTARIO LOTTO \
6/49 RANDOM NUMBER GENERATOR', # index 6 = text_words

    f'\n({text_features[4]}5{text_features[5]}): Typewriter Game', # index 7 = text_words

    f'\nPress ({text_features[3]}Q{text_features[5]}) to \
exit J.C.R Soft~Choice.' # index 8 = text_words
    )

text_info=(
    f'\n{text_features[3]}READY:{text_features[4]}', # index 0 = text_info

    f'\n{text_features[5]}Thanks for choosing J.C.R Soft~Choice.', # index 1 = text_info

    'title J.C.R Soft~Choice', # index 2 = text_info
    
    'knowledge' # index 3 = text_info
    )

choice=('1','2','3','4','5','q') # choices, q = quit

def file_menu():
    winsound.PlaySound(sounds[0],winsound.SND_ASYNC)
    
    while True:
        os.system(text_info[2])
        os.system(text_features[0])
        for i in text_words:
            print(i)
            
        button=input(text_info[0]).lower().strip()

        if button==(text_info[3]):
            secret_poem()        
        elif button==(choice[0]):
            ascii_codes()
        elif button==(choice[1]):
            fan_plast()
        elif button==(choice[2]):
            maj_cal()
        elif button==(choice[3]):
            ont_lotto()             
        elif button==(choice[4]):
            type_game()        
        elif button==(choice[5]):
            os.system(text_features[0])
            winsound.PlaySound(sounds[1],winsound.SND_ASYNC)        
            print(text_info[1])            
            time.sleep(3)            
            break
     
file_menu()
