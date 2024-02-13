# Typewriter Game Python program example.

# Created by Joseph C. Richardson, GitHub.com

# Note: you must execute/run the program from
# the OS output screen, via double-clicking the Python
# program file itself.

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

import os,time,winsound

text_colours=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

sounds=('TYPE')

text_words=(
    f'\n{text_colours[2]}Welcome to the Typewriter Game.\n\n{text_colours[1]}\
Type a sentence and I will retype whatever you type.\n\n{text_colours[3]}To \
begin, simply type a sentence or sentences,\nthen press (Enter) and I will retype \
whatever you type.\n\n{text_colours[0]}Press (F) to make the letters type \
forward/default.\nPress (R) to make the letters type reverse.\nPress (B) to make the \
letters type backwards.\nPress (Q) to quit.', # index 0 = text_words

    f'\n\n{text_colours[2]}Type sentence here: {text_colours[1]}', # index 1 = text_words

    f'\n{text_colours[3]}Press (Enter) to type again or\npress any \
one of the options above:{text_colours[0]}', # index 2 = text_words

    f'\n{text_colours[3]}Thanks for playing Typewriter Game.', # index 3 = text_words
    )

os_features=('cls','title Typewriter Game')

button=('f','r','b','q')

# type_intro

def type_intro():
    os.system(os_features[1])
    length=0
    while length<=len(text_words[0]):
        winsound.PlaySound(sounds,winsound.SND_ASYNC)
        print(text_words[0][:length])
        time.sleep(.05)
        os.system(os_features[0])
        length+=1

# forward type

    while True:
        os.system(os_features[0])
        letters=input(text_words[0]+text_words[1]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break

        length=0
        while length<=len(letters):
            winsound.PlaySound(sounds,winsound.SND_ASYNC)
            time.sleep(.05)
            os.system(os_features[0])
            print(text_words[0]+text_words[1]+letters[:length])
            length+=1

        letters=input(text_words[2]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break

def forward_type():
    while True:
        os.system(os_features[0])
        letters=input(text_words[0]+text_words[1]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break

        length=0
        while length<=len(letters):
            winsound.PlaySound(sounds,winsound.SND_ASYNC)
            time.sleep(.05)
            os.system(os_features[0])
            print(text_words[0]+text_words[1]+letters[:length])
            length+=1

        letters=input(text_words[2]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break

def reverse_type():
    while True:
        os.system(os_features[0])
        letters=input(text_words[0]+text_words[1]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break

        length=0
        while length<=len(letters):
            winsound.PlaySound(sounds,winsound.SND_ASYNC)
            time.sleep(.05)
            os.system(os_features[0])
            print(text_words[0]+text_words[1]+letters[length:])
            length+=1

        letters=input(text_words[2]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break

def backward_type():
    while True:
        os.system(os_features[0])
        letters=input(text_words[0]+text_words[1]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break

        length=0
        while length<=len(letters):
            winsound.PlaySound(sounds,winsound.SND_ASYNC)
            time.sleep(.05)
            os.system(os_features[0])
            print(text_words[0]+text_words[1]+letters[length::-1])
            length+=1

        letters=input(text_words[2]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break

def breakout():
    os.system(os_features[1])
    length=0
    while length<=len(text_words[3]):
        winsound.PlaySound(sounds,winsound.SND_ASYNC)
        print(text_words[3][:length])
        time.sleep(.05)
        os.system(os_features[0])
        length+=1

    print(text_words[3][:length])
    time.sleep(3)

def type_game():
    type_intro()

type_game()
