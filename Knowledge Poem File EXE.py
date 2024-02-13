import os
from FileMenuExample import file_menu

os.system('title J.C.R Soft~Choice')

sounds=(
    'Ring08','Alarm05','Windows Proximity Notification'
    )

text_features=(
    'cls', # index 0 = clear screen
    '*'*118, # index 1 = 118 asterisks
    '\x1b[31m', # index 2 = red
    '\x1b[32m', # index 3 = green
    '\x1b[33m', # index 4 = yellow
    '\x1b[34m', # index 5 = blue
    '\x1b[35m', # index 6 = purple
    '\x1b[36m', # index 7 = cyan
    '\x1b[37m'  # index 8 = white
    )

knowledge_poem=(
    f'''\n{text_features[7]}‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.

THIS BELONGS TO EVERY MAN, WOMAN AND CHILD
Never give up your dream, no matter how far away it may seem to be, because that is when it is ever so
close to becoming true. If you dream of something long enough and strong enough, your dream will come
true, when you least expect it. Always remember, we are never too young or too old to dream and use our
imagination, for we only get one and it is ours forever. May your heart be filled with courage and
compassion, and your mind be as limitless and as wondrous as the universe itself!
If you dream it, you can be it. Believe it!\n'''
    )

logo=(
    f'\njoshua.computers.read/information', # index 0 = logo
    f'\n\nall rights reserved.' # index 1 = logo
    )

text_info=(f'\nPress (ENTER) to begin:')

class Knowledge:
    def ponder():
        os.system(text_features[0])
        print(knowledge_poem)
    def jcr():
        print(f'{text_features[2]}{text_features[1]}{text_features[8]}{logo[0].upper()}{logo[1].title()}')
        input(text_info).lower().strip()
        file_menu()
      
Knowledge.ponder()
Knowledge.jcr()
