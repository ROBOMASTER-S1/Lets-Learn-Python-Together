import os,time;os.system('')

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
    f'\n"Python Programmer\'s Glossary Bible" by Joseph C. Richardson','cls'
    )

length=0
while length<=len(text_words[0]):
    for i in text_colours:
        print(i+text_words[0][:length])
        time.sleep(.05)
        os.system(text_words[1])
        length+=1

print(i+text_words[0])

input('\nPress Enter to exit.')
