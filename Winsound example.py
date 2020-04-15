'''Python Wave Sounds:'''
'''
Python wave sounds are easy to create, because they are simply wave sounds you \
already have on your Windows computer system. Note: Python limits to wave sound \
format only. Wave sound files must be stored in the same folder/directory where your \
Python program files are also stored.
'''
# Type and execute/run the wave sound program example below. Use the name of the
# wave sound file only, such as 'SPEECH OFF' for example.

import winsound

winsound.PlaySound('SPEECH OFF',winsound.SND_ASYNC)

# The wave sound program below looks similar to the one above. The only difference
# is, the wave sound program below waits to play the wave sound before continuing
# on with the rest of the Python program. Type and execute/run the program example
# below and see what happends.

import winsound

winsound.PlaySound('SPEECH OFF',winsound.SND_ALIAS)
