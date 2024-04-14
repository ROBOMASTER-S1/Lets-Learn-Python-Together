# Condensed Version: Laser Wars Python program example

# Created by Joseph C. Richardson, GitHub.com

import time
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

laser_canvas=Canvas(laser_wars,width=1920,height=1080,background='#000000')
laser_canvas.grid(row=0,column=0)

while True:    

    for i in range(20):
        random_width=randint(0,15)
        x = randint(-500,1920)
        laser_canvas.create_line(randint(-500+x,1920+x),randint(-500+x,1920+x),randint(-500+x,1920+x),\
                                 randint(-500+x,1920+x),fill=random_colour_code(),width=random_width)

    laser_canvas.update()
    time.sleep(.08)
    laser_canvas.delete('all')

laser_wars.mainloop()
