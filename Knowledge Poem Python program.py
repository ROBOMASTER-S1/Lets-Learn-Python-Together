# Knowledge Poem Python program example.

# Created by Joseph C. Richardson, GitHub.com

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

# Note: after you save your file, you must double click this file to view it's cool coloured
# text and layout.

import time,os;os.system('title,Knowledge Poem')

text_colours=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

knowledge_poem=(
f'''\n{text_colours[5]}'Knowledge'
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream's creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.

THIS BELONGS TO EVERY MAN, WOMAN AND CHILD
Never give up your dream, no matter how far away it may seem to be, because that is when it is
ever so close to becoming true. If you dream of something long enough and strong enough, your
dream will come true, when you least expect it. Always remember, we are never too young or too
old to dream and use our imagination, for we only get one and it is ours forever. May your heart
be filled with courage and compassion, and your mind be as limitless and as wondrous as the
universe itself! If you dream it, you can be it. Believe it!\n'''
)

while True:
    os.system('cls')
    letter=input(f'{knowledge_poem}\n{text_colours[1]}Type a word or letter from this poem, and I will tell you how \
many times it\'s been used in it.\nNote: words and letters are case sensitive.\n\nType (quit) to close the program: ').strip()

    if letter=='quit':
        break

    elif len(letter)<=1:
        print(f'\n{text_colours[2]}The letter " {letter} " has been used {knowledge_poem.count(letter)} times in this poem.')
        time.sleep(2)

    elif len(letter)>=2:
        print(f'\n{text_colours[2]}The word " {letter} " has been used {knowledge_poem.count(letter)} times in this poem.')
        time.sleep(2)
