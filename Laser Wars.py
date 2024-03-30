# Try this fun tkinter Python program example, I call LASER WARS

# Created by Joseph C. Richardson, GitHub.com

import time
from random import*
from tkinter import*
my_window=Tk()

my_window.title('LASER WARS')

def random_colour_code():
    hex_chars=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code='#'
    
    for i in range(0,6):
        colour_code=colour_code+choice(hex_chars)
    return colour_code

my_canvas=Canvas(my_window,width=1920,height=1080,background='#000000')
my_canvas.grid(row=0,column=0)

while True:
    x1=randint(-500,1920)
    y1=randint(-500,1920)
    x2=randint(-500,1920)
    y2=randint(-500,1920)

    x3=randint(-500,1920)
    y3=randint(-500,1920)
    x4=randint(-500,1920)
    y4=randint(-500,1920)

    x5=randint(-500,1920)
    y5=randint(-500,1920)
    x6=randint(-500,1920)
    y6=randint(-500,1920)
    
    random_width=randint(0,10)
    my_canvas.create_line(x1,y1,x2,y2,fill=random_colour_code(),width=random_width)
    my_canvas.create_line(x3,y3,x4,y4,fill=random_colour_code(),width=random_width)
    my_canvas.create_line(x5,y5,x6,y6,fill=random_colour_code(),width=random_width)

    my_canvas.update()
    time.sleep(.08)
    my_canvas.delete('all')

my_window.mainloop()
