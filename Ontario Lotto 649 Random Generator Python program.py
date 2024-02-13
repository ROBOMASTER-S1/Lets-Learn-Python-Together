# ONTARIO LOTTO 6/49 RANDOM NUMBER GENERATOR Python program example.

# Created by Joseph C. Richardson, GitHub.com

# Note: you must execute/run the program from
# the OS output screen, via double-clicking the Python
# program file itself.

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

import os,time,math,random,winsound

text_colour=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

text_words=(
    f'\n{text_colour[1]}Welcome to ONTARIO LOTTO 6/49 \
RANDOM NUMBER GENERATOR. Good Luck!\n\nPress (Enter) \
to activate the ONTARIO LOTTO 6/49 RANDOM NUMBER GENERATOR:', # index 0 = text_words

    f'\n{text_colour[1]}ONTARIO LOTTO 6/49 RANDOM NUMBER \
GENERATOR is activated.\n\nONTARIO LOTTO 6/49 RANDOM NUMBER \
GENERATOR SEQUENCE:', # index 1 = text_words

    f'\n{text_colour[2]}Press (N) then press (Enter) to randomly \
pick a different set of Ontario Lotto 6/49 numbers.\n\nPress (Q) \
then press (Enter) to quit:{text_colour[1]}', # index 2 = text_words

    f'\n{text_colour[1]}Thanks for playing ONTARIO LOTTO 6/49 \
RANDOM NUMBER GENERATOR. Good Luck!', # index 3 = text_words

    'title ONTARIO LOTTO 6/49 RANDOM NUMBER GENERATOR' # index 4 = text_words
    )

random_num=(
    random.randint(1,9), # index 0 = random_num
    random.randint(10,17), # index 1 = random_num
    random.randint(18,25), # index 2 = random_num
    random.randint(26,33), # index 3 = random_num
    random.randint(34,41), # index 4 = random_num
    random.randint(42,49)  # index 5 = random_num
    )

win_sound='TYPE','Windows Notify Messaging'

text_fx=('cls','n','q') # clear screen, n = random number button, q = quit

def ont_lotto():
    os.system(text_words[4])
    random_num=(
        random.randint(1,9),
        random.randint(10,17),
        random.randint(18,25),
        random.randint(26,33),
        random.randint(34,41),
        random.randint(42,49)
        )

    y=0
    while y<=len(text_words[0]):
        winsound.PlaySound(win_sound[0],winsound.SND_ASYNC)
        print(text_words[0][:y])
        time.sleep(.06)
        os.system(text_fx[0])
        y+=1

    button=input(text_words[0]).lower().strip()

    y=0
    while y<=len(text_words[1]):
        winsound.PlaySound(win_sound[0],winsound.SND_ASYNC)
        print(text_words[1][:y])
        time.sleep(.06)
        os.system(text_fx[0])
        y+=1

    while True:
        winsound.PlaySound(win_sound[1],winsound.SND_ASYNC)
        print(
            f'{text_words[1]}{text_colour[0]}({random_num[0]}) \
({random_num[1]}) ({random_num[2]}) ({random_num[3]}) \
({random_num[4]}) ({random_num[5]})'
            )

        button=input(text_words[2]).lower().strip()

        os.system(text_fx[0])

        if button==(text_fx[1]):
            random_num=(
            random.randint(1,9),
            random.randint(10,17),
            random.randint(18,25),
            random.randint(26,33),
            random.randint(34,41),
            random.randint(42,49)
            )
        elif button==(text_fx[2]):
            break

    y=0
    while y<=len(text_words[3]):
        winsound.PlaySound(win_sound[0],winsound.SND_ASYNC)
        print(text_words[3][:y])
        time.sleep(.06)
        os.system(text_fx[0])
        y+=1

    print(text_words[3])
    time.sleep(3)

ont_lotto()
