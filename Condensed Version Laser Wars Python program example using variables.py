# Condensed Version: Laser Wars Python program example using variables

# Created by Joseph C. Richardson, GitHub.com

from time import sleep as wait
from random import*
from tkinter import*
laser_wars=Tk()

laser_wars.title('LASER WARS')

def random_colour_code():
    hex_chars=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code='#'

    for i in range(0,6):
        colour_code=colour_code+choice(hex_chars)
    return colour_code

colour = '#000000'
w,h = 1920,1080
r,c = 0,0
rand1,rand2 = 0,15
randint1,randint2 = -500,1920
loop = 20
seconds = .08

laser_canvas=Canvas(laser_wars,width=w,height=h,background=colour)
laser_canvas.grid(row=r,column=c)

while True:

    for i in range(loop): # increse the for loop value to add more lasers on the screen output
        random_width=randint(rand1,rand2)
        x = randint(randint1,randint2)
        laser_canvas.create_line(randint(randint1+x,randint2+x),randint(randint1+x,randint2+x),\
                                 randint(randint1+x,randint2+x),randint(randint1+x,randint2+x),\
                                 fill=random_colour_code(),width=random_width)

    laser_canvas.update();wait(seconds);laser_canvas.delete('all')

laser_wars.mainloop()
