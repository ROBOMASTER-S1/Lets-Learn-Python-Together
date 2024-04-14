# Try this fun tkinter Python program example, I call LASER WARS

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
    
    x7=randint(-500,1920)
    y7=randint(-500,1920)
    x8=randint(-500,1920)
    y8=randint(-500,1920)
    
    x9=randint(-500,1920)
    y9=randint(-500,1920)
    x10=randint(-500,1920)
    y10=randint(-500,1920)

    x11=randint(-500,1920)
    y11=randint(-500,1920)
    x12=randint(-500,1920)
    y12=randint(-500,1920)

    x13=randint(-500,1920)
    y13=randint(-500,1920)
    x14=randint(-500,1920)
    y14=randint(-500,1920)

    x15=randint(-500,1920)
    y15=randint(-500,1920)
    x16=randint(-500,1920)
    y16=randint(-500,1920)

    x17=randint(-500,1920)
    y17=randint(-500,1920)
    x18=randint(-500,1920)
    y18=randint(-500,1920)

    x19=randint(-500,1920)
    y19=randint(-500,1920)
    x20=randint(-500,1920)
    y20=randint(-500,1920)
    
    random_width=randint(0,15)
    laser_canvas.create_line(x1,y1,x2,y2,fill=random_colour_code(),width=random_width)
    laser_canvas.create_line(x3,y3,x4,y4,fill=random_colour_code(),width=random_width)
    laser_canvas.create_line(x5,y5,x6,y6,fill=random_colour_code(),width=random_width)
    laser_canvas.create_line(x7,y7,x8,y8,fill=random_colour_code(),width=random_width)
    laser_canvas.create_line(x9,y9,x10,y10,fill=random_colour_code(),width=random_width)
    laser_canvas.create_line(x11,y11,x12,y12,fill=random_colour_code(),width=random_width)
    laser_canvas.create_line(x13,y13,x14,y14,fill=random_colour_code(),width=random_width)
    laser_canvas.create_line(x15,y15,x16,y16,fill=random_colour_code(),width=random_width)
    laser_canvas.create_line(x17,y17,x18,y18,fill=random_colour_code(),width=random_width)
    laser_canvas.create_line(x19,y19,x20,y20,fill=random_colour_code(),width=random_width)    

    laser_canvas.update()
    time.sleep(.08)
    laser_canvas.delete('all')

laser_wars.mainloop()
