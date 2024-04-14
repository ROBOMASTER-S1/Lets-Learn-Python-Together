'''
Tkinter Borders

'flat'
'solid'
'raised'
'sunken'
'ridge'
'groove'
'''
from tkinter import*
window=Tk()
window.geometry('500x600')
label1=Label(window,text='Hello World',fg='blue',font='arial 32',width=10)
label1.pack()

import tkinter as tk
import time as tm

window=tk.Tk()
window.config(bg='black')

def display_time():
    current_time=tm.strftime('%H:%M:%S:%p')
    clock_label['text']=current_time
    window.after(1000,display_time)

window.title('TIMERNATOR')
timern=tk.Label(window,font='arial 45 bold',text='TIMERNATOR',bg='black',fg='red')
clock_label=tk.Label(window,font='arial 50',bg='black',fg='#00ffff')
clock_label.grid(row=1,column=0)
timern.grid(row=0,column=0)

display_time()
window.mainloop()

import tkinter as tk
import time as tm

window=tk.Tk()
window.title('TIMERNATOR')
current_time=tm.strftime(' %H:%M:%S:%p ')

clock_label=tk.Label(window,font='arial 80',bg='black',fg='red',text=current_time)
clock_label.grid(row=0,column=0)

window.mainloop()
    
import time as tm
current_time1=tm.strftime('%I:%M:%S')
current_time2=tm.strftime('%I:%M:%S:%p')
print(current_time2)

import tkinter as tk
window=tk.Tk()

window.title('Colour Choice')

window.geometry('400x400+400+200')

def red_colour():
    window['bg']='#ff0000'    
def green_colour():
    window['bg']='#00ff00'
def blue_colour():
    window['bg']='#0000ff'
def Cyan_colour():
    window['bg']='#00ffff'
def Pink_colour():
    window['bg']='#ff00ff'
def Yellow_colour():
    window['bg']='#fff000'

text_variables_tuple=('Red','Green','Blue','Cyan','Pink','Yellow','Colour')

window.config(bg=text_variables_tuple[0])    
menubar=tk.Menu(window)

dropdown_menu=tk.Menu(menubar,tearoff=False)
dropdown_menu.add_command(label=text_variables_tuple[0],command=red_colour)
dropdown_menu.add_separator()
dropdown_menu.add_command(label=text_variables_tuple[1],command=green_colour)
dropdown_menu.add_separator()
dropdown_menu.add_command(label=text_variables_tuple[2],command=blue_colour)
dropdown_menu.add_separator()
dropdown_menu.add_command(label=text_variables_tuple[3],command=Cyan_colour)
dropdown_menu.add_separator()
dropdown_menu.add_command(label=text_variables_tuple[4],command=Pink_colour)
dropdown_menu.add_separator()
dropdown_menu.add_command(label=text_variables_tuple[5],command=Yellow_colour)

menubar.add_cascade(label=text_variables_tuple[6],menu=dropdown_menu)
window.config(menu=menubar)
window.mainloop()


import tkinter as tk
window=tk.Tk()

def red_colour():
    window['bg']='red'
def green_colour():
    window['bg']='green'
def blue_colour():
    window['bg']='blue'


menublock=tk.Menu(window)
menublock.add_command(label='Red',command=red_colour)
menublock.add_command(label='Green',command=green_colour)
menublock.add_command(label='blue',command=blue_colour)

window.config(menu=menublock)
window.mainloop()

import tkinter as tk
window=tk.Tk()

def quit_app():
    window.destroy()

def change_colour():
    window['bg']='red'

menublock=tk.Menu(window)
menublock.add_command(label='Quit',command=quit_app)
menublock.add_command(label='Colour',command=change_colour)
window.config(menu=menublock)
window.mainloop()

import tkinter as tk
window=tk.Tk()

menublock=tk.Menu(window)
menublock.add_command(label='Quit')
menublock.add_command(label='Colour')
window.config(menu=menublock)
window.mainloop()

def demo_fn():
    global x
    global y
    x='Hello'
    y='Word'
    print(x,y)
    print(dir())

demo_fn()
print(dir())
print(x,y)

from tkinter import*
window=Tk()

class DrawLineApp():
    def __init__(self,contain,width,height,colour,row,column):
        self.canvas=Canvas(contain,width=width,height=height,bg=colour)
        self.canvas.grid(row=row,column=column)
        self.canvas.bind('<Button-1>',self.draw_line)
        self.click_number=0
        self.x1=0
        self.y1=0
        self.x2=0
        self.y2=0
        
    def draw_line(self,event):
        if self.click_number==0:
            self.x1=event.x
            self.y1=event.y
            self.click_number=1
        else:
            self.x2=event.x
            self.y2=event.y
            self.canvas.create_line(self.x1,self.y1,self.x2,self.y2,fill='black',width=10)
            
my_draw_line1=DrawLineApp(window,width=400,height=300,colour='white',row=0,column=0)
my_draw_line2=DrawLineApp(window,width=400,height=300,colour='yellow',row=0,column=1)       
my_draw_line3=DrawLineApp(window,width=400,height=300,colour='red',row=0,column=2)       

window.mainloop()


from tkinter import*
import time
from random import*
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
    
    random_width=randint(0,8)
    my_canvas.create_line(x1,y1,x2,y2,fill=random_colour_code(),width=random_width)
    my_canvas.create_line(x3,y3,x4,y4,fill=random_colour_code(),width=random_width)
    my_canvas.create_line(x5,y5,x6,y6,fill=random_colour_code(),width=random_width)

    my_canvas.update()
    time.sleep(.05)
    my_canvas.delete('all')

my_window.mainloop()


from tkinter import*
window=Tk()

def draw_line(event):
    global click_number
    global x1,y1
    if click_number==0:
        x1=event.x
        y1=event.y
        click_number=1
    else:
        x2=event.x
        y2=event.y
        canvas.create_line(x1,y1,x2,y2,fill='black',width=10)
        click_number=0

canvas=Canvas(window,width=400,height=400,bg='white')
canvas.grid(row=0,column=0)
canvas.bind('<Button-1>',draw_line)
click_number=0
window.mainloop()


from random import*
from tkinter import*

window=Tk()

def random_line(event):
    x1=randint(0,400)
    y1=randint(0,400)
    x2=randint(0,400)
    y2=randint(0,400)
    canvas.create_line(x1,y1,x2,y2,fill=f'#{randint(0,0xffffff):06x}',width=20)
    
def delete_lines(event):
    canvas.delete('all')

canvas=Canvas(window,width=400,height=400,bg='white')
canvas.bind('<Button-1>',random_line)
canvas.bind('<Button-3>',delete_lines)
canvas.grid(row=0,column=0)
window.mainloop()


from random import*
from tkinter import*

window=Tk()

def random_line():
    x1=randint(0,400)
    y1=randint(0,400)
    x2=randint(0,400)
    y2=randint(0,400)
    canvas.create_line(x1,y1,x2,y2,fill=f'#{randint(0,0xffffff):06x}',width=20)
    
def delete_lines():
    canvas.delete('all')

canvas=Canvas(window,width=400,height=400,bg='white')
button1=Button(window,text='Click for a randome coloured line',command=random_line)
button2=Button(window,text='Click to clear coloured lines',command=delete_lines)

canvas.grid(row=0,column=0)
button1.grid(row=1,column=0)
button2.grid(row=2,column=0)
window.mainloop()

from tkinter import*
import time
from random import*
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
    
    random_width=randint(0,5)
    my_canvas.create_line(x1,y1,x2,y2,fill=random_colour_code(),width=random_width)
    my_canvas.create_line(x3,y3,x4,y4,fill=random_colour_code(),width=random_width)
    my_canvas.create_line(x5,y5,x6,y6,fill=random_colour_code(),width=random_width)

    my_canvas.update()
    time.sleep(.05)
    my_canvas.delete('all')

my_window.mainloop()


from random import*
from tkinter import*

my_window=Tk()

def random_colour_code():
    hex_chars=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code='#'
    
    for i in range(0,6):
        colour_code=colour_code+choice(hex_chars)
    return colour_code

my_canvas=Canvas(my_window,width=400,height=400,background='#000000')
my_canvas.grid(row=0,column=0)

while True:
    x1=randint(0,400)
    y1=randint(0,400)
    x2=randint(0,400)
    y2=randint(0,400)    
    random_width=randint(1,25)
    
    my_canvas.create_line(x1,y1,x2,y2,fill=random_colour_code(),width=random_width)
    my_canvas.update()
    
my_window.mainloop()


from random import*
from tkinter import*
my_window=Tk()

def random_colour_code():
    hex_chars=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code='#'
    for i in range(0,6):
        colour_code=colour_code+choice(hex_chars)
    return colour_code

my_canvas=Canvas(my_window,width=400,height=400,background='white')
my_canvas.grid(row=0,column=0)
my_canvas.create_line(0,0,400,400,fill=random_colour_code(),width=10)
my_window.mainloop()


from random import*

def random_colour_code():
    hex_chars=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code='#'
    for i in range(0,6):
        colour_code=colour_code+choice(hex_chars)
    return colour_code

print('The hexadecimal colour code generated is:',random_colour_code())

from random import choice

hex_chars=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

colour_code='#'
for i in range(0,6):
    colour_code=colour_code+choice(hex_chars)
print('The hexadecimal colour code gerated is:',colour_code)

from random import choice

hex_chars=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

colour_code='#'
colour_code=colour_code+choice(hex_chars)
colour_code=colour_code+choice(hex_chars)
colour_code=colour_code+choice(hex_chars)
colour_code=colour_code+choice(hex_chars)
colour_code=colour_code+choice(hex_chars)
colour_code=colour_code+choice(hex_chars)
print('The hexadecimal colour code gerated is:',colour_code)


from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')
for i in range(0,400,3):
    draw.create_line(50+i,50+i,450,50,450,50,450,450,50,450,50+i,50+i,fill='cyan')
draw.pack()

root.mainloop()


from tkinter import*
my_window=Tk()

my_canvas1=Canvas(my_window,width=100,height=100,bg='red')
my_canvas2=Canvas(my_window,width=100,height=100,bg='orange')
my_canvas3=Canvas(my_window,width=100,height=100,bg='yellow')
my_canvas4=Canvas(my_window,width=100,height=100,bg='green')

my_canvas1.grid(row=0,column=0)
my_canvas2.grid(row=0,column=1)
my_canvas3.grid(row=1,column=0)
my_canvas4.grid(row=1,column=1)

my_window.mainloop()


from tkinter import*
my_window=Tk()

width_value=my_window.winfo_screenwidth()
height_value=my_window.winfo_screenheight()
my_window.geometry(f'{width_value}x{height_value}+0+0')
my_window.mainloop()

from tkinter import*
my_window=Tk()

width_value=my_window.winfo_screenwidth()
height_value=my_window.winfo_screenheight()
my_window.geometry('{}x{}+0+0'.format(width_value,height_value))
my_window.mainloop()

from tkinter import*
my_window=Tk()

my_window.geometry('%dx%d+0+0'%(my_window.winfo_screenwidth(),my_window.winfo_screenheight()))
my_window.mainloop()

from tkinter import*

my_window=Tk()

width=my_window.winfo_screenwidth()
height=my_window.winfo_screenheight()
my_window.geometry('%dx%d+0+0'%(width,height))

my_window.mainloop()

from tkinter import*
my_window=Tk()

my_window.geometry('300x300')
my_window.configure(bg='blue',padx='10',pady='10')

class HelloNameFrame(Frame):    
    def __init__(self,thing):
        Frame.__init__(self,thing)
        self.users_name=StringVar()
        self.display_string=StringVar()

        self.friendly_label=Label(self,text='Enter yur name')
        self.name_entry=Entry(self,textvariable=self.users_name)
        self.button=Button(self,text='Click Me!',command=self.display_output)
        self.display_label=Label(self,textvariable=self.display_string,relief='solid')

        self.friendly_label.grid(row=0,column=0)
        self.name_entry.grid(row=0,column=1)
        self.button.grid(row=1,column=0)
        self.display_label.grid(row=1,column=1)

    def display_output(self):
        self.display_string.set('Hello '+self.users_name.get())        

frameA=HelloNameFrame(my_window)
frameA.grid(row=0,column=0)
my_window.mainloop()

from tkinter import*

my_window=Tk()

class RedFrame(Frame):
    def __init__(self,window):
        Frame.__init__(self,master=window)
        self['height']=150
        self['width']=150
        self['relief']='raised'
        self['bd']=10
        self['bg']='red'
        
frame_a=RedFrame(my_window)
frame_b=RedFrame(my_window)
frame_a.grid(row=0,column=0)
frame_b.grid(row=0,column=1)

my_window.mainloop()


from tkinter import*

print(help(Frame))

from tkinter import*



class RedFrame(Frame):
    def __init__(self,blank):
        super().__init__()
        print('The id of self is',id(self))
        self['height']=150
        self['width']=150
        self['relief']=RAISED
        self['bd']=8
        self['bg']='red'
        
frame_a=RedFrame(my_window)
print('The id of frame_a is',id(frame_a))
frame_b=RedFrame(my_window)
print('The id of frame_b is',id(frame_b))
frame_a.grid(row=0,column=0)
frame_b.grid(row=0,column=1)

my_window.mainloop()


from tkinter import*

my_window=Tk()

class RedFrame(Frame):
    def __init__(self,window):
        super().__init__()
        self['height']=150
        self['width']=150
        self['relief']=RAISED
        self['bd']=8
        self['bg']='red'
        
class YellowFrame(Frame):
    def __init__(self,window):
        super().__init__()
        self['height']=150
        self['width']=150
        self['relief']=RAISED
        self['bd']=8
        self['bg']='Yellow'
        
frame_a=RedFrame(my_window)
frame_b=RedFrame(my_window)

frame_a.grid(row=0,column=0)
frame_b.grid(row=0,column=1)

print('The id of frame_a is',id(frame_a))
print('The type of frame_a is',type(frame_a))

my_window.mainloop()


from tkinter import*

my_window=Tk()

entry_a=Entry(my_window,bg='red')
entry_b=Entry(my_window,bg='yellow')
entry_c=Entry(my_window,bg='white')

label_a=Label(my_window,text='First Name')
label_b=Label(my_window,text='Middle Name')
label_c=Label(my_window,text='Last Name')

entry_a.grid(row=0,column=1)
entry_b.grid(row=1,column=1)
entry_c.grid(row=2,column=1)

label_a.grid(row=0,column=0)
label_b.grid(row=1,column=0)
label_c.grid(row=2,column=0)

entry_a.focus()
my_window.mainloop()


from tkinter import*

my_window=Tk()

celsius=StringVar()
fahrenheit=StringVar()

def convert():
    F=float(fahrenheit_entry.get())
    C=(F-32)*5/9
    celsius.set(str(C))

friendly_label_1=Label(my_window,text='Enter Fahrenheit')
friendly_label_2=Label(my_window,text='Celsius Temperature')
display_celsius_label=Label(my_window,textvariable=celsius)
fahrenheit_entry=Entry(my_window,textvariable=fahrenheit)
convert_button=Button(my_window,text='Convert',command=convert)

friendly_label_1.grid(row=0,column=0)
fahrenheit_entry.grid(row=0,column=1)
friendly_label_2.grid(row=1,column=0)
display_celsius_label.grid(row=1,column=1)
convert_button.grid(row=2,column=0)

fahrenheit_entry.focus()

my_window.mainloop()


from tkinter import*

my_window=Tk()

def convert():
    F=float(fahrenheit_entry.get())
    C=(F-32)*5/9
    display_celsius_label['text']=str(C)

friendly_label_1=Label(my_window,text='Enter Fahrenheit')
friendly_label_2=Label(my_window,text='Celsius Temperature')
display_celsius_label=Label (my_window)
fahrenheit_entry=Entry(my_window)
convert_button=Button(my_window,text='Convert',command=convert)

friendly_label_1.grid(row=0,column=0)
fahrenheit_entry.grid(row=0,column=1)
friendly_label_2.grid(row=1,column=0)
display_celsius_label.grid(row=1,column=1)
convert_button.grid(row=2,column=0)

fahrenheit_entry.focus()

my_window.mainloop()

from tkinter import*

learn=Tk()

class RedFrame(Frame):
    def __init__(self,things):
        super(). __init__()
        self['height']=150
        self['width']=150
        self['relief']=RAISED
        self['bd']=8
        self['bg']='red'

frame_a=RedFrame(learn)
frame_b=RedFrame(learn)
frame_a.grid(row=0,column=0)
frame_b.grid(row=0,column=1)

learn.mainloop()


from tkinter import*

learn=Tk()

frame_a=Frame(learn,
              height=150,
              width=150,             
              relief=RAISED,
              bd=8,bg='red')

frame_b=Frame(learn,
              height=150,
              width=150,
              relief=GROOVE,
              bd=8,bg='green')

frame_c=Frame(learn,
              height=150,
              width=150,             
              relief=RIDGE,
              bd=8,bg='yellow')
frame_d=Frame(learn,
              height=150,
              width=150,             
              relief=SUNKEN,
              bd=8,bg='blue')

frame_a.grid(row=0,column=0)
frame_b.grid(row=0,column=1)
frame_c.grid(row=0,column=2)
frame_d.grid(row=0,column=3)

from tkinter import*

learn=Tk()

frame1=Frame(learn)
frame2=Frame(learn)

label1=Label(frame1,text='First Name')
label2=Label(frame1,text='Middle Name')
label3=Label(frame1,text='Last Name')

label4=Label(frame2,text='First Line')
label5=Label(frame2,text='Town')
label6=Label(frame2,text='Country')

entry1=Entry(frame1)
entry2=Entry(frame1)
entry3=Entry(frame1)

entry4=Entry(frame2)
entry5=Entry(frame2)
entry6=Entry(frame2)

butt1=Button(frame1,text='Submit',padx='5')
butt2=Button(frame2,text='Submit',padx='5')

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)

label4.grid(row=0,column=0)
label5.grid(row=1,column=0)
label6.grid(row=2,column=0)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)

entry4.grid(row=0,column=1)
entry5.grid(row=1,column=1)
entry6.grid(row=2,column=1)

butt1.grid(row=3,columnspan=2)
butt2.grid(row=3,columnspan=2)

frame1.grid(row=0,column=0)
frame2.grid(row=0,column=1)

learn.mainloop()


from tkinter import*

learn=Tk()

frame=Frame(learn)

labelf=Label(frame,text='First Name')
labelm=Label(frame,text='Middle Name')
labell=Label(frame,text='Last Name')

entryf=Entry(frame)
entrym=Entry(frame)
entryl=Entry(frame)

butt=Button(frame,text='Submit',padx='8')

labelf.grid(row=0,column=0)
labelm.grid(row=1,column=0)
labell.grid(row=2,column=0)

entryf.grid(row=0,column=1)
entrym.grid(row=1,column=1)
entryl.grid(row=2,column=1)

butt.grid(row=3,columnspan=2)

frame.grid(row=1,column=0)

from tkinter import*

learn=Tk()

label_a=Label(learn,text='First Name')
label_b=Label(learn,text='Middle Name')
label_c=Label(learn,text='Last Name')

entry_a=Entry(learn,bg='red',bd=2)
entry_b=Entry(learn,bg='yellow',bd=2)
entry_c=Entry(learn,bg='white',bd=2)

label_a.grid(row=0,column=0,padx='3',pady='5')
label_b.grid(row=1,column=0,padx='3',pady='5')
label_c.grid(row=2,column=0,padx='3',pady='5')

entry_a.grid(row=0,column=1,padx='3',pady='5')
entry_b.grid(row=1,column=1,padx='3',pady='5')
entry_c.grid(row=2,column=1,padx='3',pady='5')

entry_a.focus()

learn.mainloop()


from tkinter import*

my_window=Tk()

def convert():
    F=float(fahrenheit_entry.get())
    C=(F-32)*5/9
    display_celsius_label['text']=str(C)

friendly_label_1=Label(my_window,text='Enter Fahrenheit')
friendly_label_2=Label(my_window,text='Celsius Temperature')
display_celsius_label=Label (my_window)
fahrenheit_entry=Entry(my_window)
convert_button=Button(my_window,text='Convert',command=convert)

friendly_label_1.grid(row=0,column=0)
fahrenheit_entry.grid(row=0,column=1)
friendly_label_2.grid(row=1,column=0)
display_celsius_label.grid(row=1,column=1)
convert_button.grid(row=2,column=0)

fahrenheit_entry.focus()

my_window.mainloop()


def say_hello():
    name_of_us=entry_1.get()
    string_to_display='Hello'+name_of_user
    label_2=Label(learn)
    label_2['text']=string_to_display
    label_2.grid(row=1,column=1)

def say_hello():
    name_of_us=entry_1.get()
    string_to_display='Hello'+name_of_user
    label_2['text']=string_to_display

def say_hello():
    name_of_us=entry_1.get()
    string_to_display='Hello'+name_of_user
    var_1.set(string_to_display)

def say_hello():
    name_of_us=entry_1.get()
    var_1.set('Hello '+name_of_user)    

from tkinter import*

learn=Tk()

learn.title('The Hello Machine')
learn.geometry('450x100+400+300')
learn.configure(bg='green')
learn.resizable(width=False,height=False)

def call_def_function():
    name_of_user=entry1.get()
    string_to_display='Hello '+name_of_user.title()+'!'.strip()
    var1.set(string_to_display)

var1=StringVar()

label1=Label(learn,bg='yellow',
             fg='blue',
             font='Arial 12 bold',
             text='Please enter your name:',
             padx='5', pady='5')

entry1=Entry(learn,
             bd=5,
             relief='sunken',
             bg='#555555',
             fg='#00ff00',
             font='Arial 14 bold')

label2=Label(learn,
             bg='green',
             fg='yellow',
             font='Mistral 30 bold',
             textvariable=var1,
             padx='5', pady='5')

butt1=Button(learn,
             bd=5,
             relief='raised',
             bg='cyan',
             fg='red',
             font='Arial 12 bold',
             text='Hello Button!',
             padx='5', pady='5',
             command=call_def_function)

label1.grid(row=0,column=0)
label2.grid(row=1,column=1)

entry1.focus()
entry1.grid(row=0,column=1)
butt1.grid(row=1,column=0)

learn.mainloop()


from tkinter import*

learn=Tk()

def say_hi():
    name_of_user=entry1.get()
    string_to_display='Hello '+name_of_user
    label2['text']=string_to_display

label1=Label(learn,text='Please enter your name:')
entry1=Entry(learn)
butt1=Button(learn,text='Click me to enter name',command=say_hi)
label2=Label(learn)

label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
butt1.grid(row=1,column=0)
label2.grid(row=1,column=1)

learn.mainloop()


from tkinter import*

learn=Tk()

def label_red():
    label1['bg']='red'
def label_green():
    label1['bg']='green'
def label_blue():
    label1['bg']='blue'

label1=Label(learn,width='20',height='3',bg='white')
butt1=Button(learn,text='red',width=6,command=label_red)
butt2=Button(learn,text='green',width=6,command=label_green)
butt3=Button(learn,text='blue',width=6,command=label_blue)

label1.grid(row=0,column=1)
butt1.grid(row=1,column=0)
butt2.grid(row=1,column=1)
butt3.grid(row=1,column=2)

learn.mainloop()


from tkinter import*

learn=Tk()

label1=Label(learn,width='20',height='3',bg='red')
label2=Label(learn,width='20',height='3',bg='green')
label3=Label(learn,width='20',height='3',bg='blue')

butt1=Button(learn,text='Click Me! 1')
butt2=Button(learn,text='Click Me! 2')
butt3=Button(learn,text='Click Me! 3')

label1.grid(row=0,column=0)
label2.grid(row=1,column=1)
label3.grid(row=0,column=2)

butt1.grid(row=1,column=0)
butt2.grid(row=0,column=1)
butt3.grid(row=1,column=2)

learn.mainloop()


from tkinter import*

learn=Tk()

label1=Label(learn,width='20',height='3',bg='red')
label2=Label(learn,width='20',height='3',bg='green')
label3=Label(learn,width='20',height='3',bg='blue')

button1=Button(learn,text='Click Me!')
label1.grid(row=0,column=0)

button1.grid(row=1,column=0)


from tkinter import*

learn=Tk()

label1=Label(learn,width='20',height='3',bg='red')
label2=Label(learn,width='20',height='3',bg='green')
label3=Label(learn,width='20',height='3',bg='blue')
label4=Label(learn,width='20',height='3',bg='white')
label5=Label(learn,width='20',height='3',bg='black')
label6=Label(learn,width='20',height='3',bg='grey')
label7=Label(learn,width='20',height='3',bg='#4477af')
label8=Label(learn,width='20',height='3',bg='#997755')
label9=Label(learn,width='20',height='3',bg='#ccff44')

label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)
label4.grid(row=1,column=0)
label5.grid(row=1,column=1)
label6.grid(row=1,column=2)
label7.grid(row=2,column=0)
label8.grid(row=2,column=1)
label9.grid(row=2,column=2)

learn.mainloop()

from tkinter import*

learn=Tk()

label1=Label(learn,
             width='20',
             height='3',
             bg='red')

label2=Label(learn,
             width='20',
             height='3',
             bg='green')

label1.grid(row=0,column=0)
label2.grid(row=0,column=1)

learn.mainloop()


from tkinter import*

learn=Tk()

def add_label():
    label1=Label(learn,text='Hello World')

    label1.pack()

learn.geometry('200x100')

button1=Button(learn,
               text='Click Me!',
               command=add_label)

button1.pack()

learn.mainloop()


from tkinter import*

learn=Tk()

var1=StringVar()

label1=Label(learn,
             relief='solid',
             font='Times 22 bold',
             text='Hello World')
label2=Label(learn,
             relief='solid',
             font='Times 22 bold',
             textvar=var1)

label1['text']='Text put here using key/value pairs approach'
var1.set('Using textvariable and StringVar()')

label1.pack()
label2.pack()

learn.mainloop()


import time;from tkinter import*

learn=Tk()

var1=StringVar()

label1=Label(learn,
             relief='solid',
             font='Times 22 bold',
             text='Hello World')
label2=Label(learn,
             relief='solid',
             font='Times 22 bold',
             textvar=var1)

var1.set('Hi')
label1.pack()
label2.pack()

learn.mainloop()


import time;from tkinter import*

learn=Tk()

var1=StringVar()

label1=Label(learn,
             relief='solid',
             font='Times 22 bold',
             textv=var1)

var1.set('Hi')
label1.pack()

learn.mainloop()

from tkinter import*

learn=Tk()
var1=StringVar()

label1=Label(learn,
             relief='solid',
             font='Times 22 bold')

label1.pack()

learn.mainloop()

from tkinter import*
learn=Tk()
label1=Label(learn,
             relief='solid',
             font='Times 22 bold')

label1.pack()

learn.mainloop()

from tkinter import*
learn=Tk()
label1=Label(learn,
             bd=8,
             relief='solid',
             font='Times 22 bold',
             bg='red',
             fg='white',
             text='Hello World')

label1.pack()
for item in label1.keys():
    print(item,':',label1[item])

learn.mainloop()

from tkinter import*
learn=Tk()
label1=Label(learn,
             bd=8,
             relief='solid',
             font='Times 22 bold',
             bg='red',
             fg='white',
             text='Hello World')

label1.pack()
print(label1.keys())
learn.mainloop()

from tkinter import*

learn=Tk()
learn.title('Thank you for Teaching Us!-:)')
learn.geometry('530x130+400+200')
learn.configure(bg='blue')
label1=Label(learn)

label1['bd']=16
label1['relief']='ridge'
label1['font']='Mistral 32 bold'
label1['bg']='#ff00ff'
label1['fg']='#00ffff'
label1['text']='Thank you for Teaching Us!-:)'
label1['padx']=16
label1['pady']=16

label1.pack()

learn.mainloop()

learn=Tk()
learn.title('Hello')
learn.geometry=('400x250')

label1=Label(learn,
             bd=8,
             relief='solid',
             bg='red',
             fg='white',
             text='Hello World')

label1.pack()
label1['bg']='blue'

learn.mainloop()

from tkinter import*

learn=Tk()
learn.title('Hello')
learn.geometry=('400x250')

label1=Label(learn,bd=8,relief='solid',
             bg='red',fg='white',text='Hello World')

label1.pack()
print(label1['bd'])
print(label1['relief'])
print(label1['font'])
print(label1['bg'])
print(label1['fg'])
print(label1['text'])

from tkinter import*

learn=Tk()
learn.title('Hello')
learn.geometry=('400x250')

label1=Label(learn,
             text='Text\nText Text\nText Text Text',
             bd=1,
             relief='sunken',
             fg='blue',
             font='Times 20',
             justify=RIGHT)

label1.pack()

learn.mainloop()

from tkinter import*

learn=Tk()
learn.title('Hello')
learn.geometry=('400x250')

label1=Label(learn,
             text='spacer')

label2=Label(learn,
             text='Hello World\nHello World',
             bd=1,
             relief='solid',
             font='Times 32',
             width=15,
             height=4,
             anchor=CENTER)

label1.pack()
label2.pack()

learn.mainloop()

from tkinter import*

learn=Tk()
learn.title('Hello')

label1=Label(learn,
             text='Text Verdana Font\ntesting testing',
             bd=10,
             relief='ridge',
             bg='red',
             fg='white',
             font='Verdana 20 bold',
             width=30,
             height=4)

label2=Label(learn,
             text='Text Times Font',
             bd=10,
             relief='flat',
             bg='green',
             fg='white',
             font='Times 20 bold italic',
             width=40)

label3=Label(learn,
             text='Text Arial Font',
             bd=10,
             relief='sunken',
             fg='blue',
             font='Arial 20 bold italic')

label1.pack()
label2.pack()
label3.pack()

learn.mainloop()


from tkinter import*

learn=Tk()
learn.title('Hello')

label1=Label(learn,
             text='Text Verdana Font\ntesting testing',
             bd=10,
             relief='solid',
             bg='red',
             fg='white',
             font='Verdana 20 bold',
             width=30,
             height=4)

label2=Label(learn,
             text='Text Times Font',
             bd=10,
             relief='groove',
             bg='green',
             fg='white',
             font='Times 20 bold italic',
             width=40)

label3=Label(learn,
             text='Text Arial Font',
             bd=10,
             relief='raised',
             fg='blue',
             font='Arial 20 bold italic')

label1.pack()
label2.pack()
label3.pack()

learn.mainloop()

from tkinter import*

learn=Tk()
learn.title('Hello')

label1=Label(learn,
             text='Text Verdana Font\ntesting testing',
             bd=10,
             relief='solid',
             bg='red',
             fg='white',
             font='Verdana 20 bold',
             width=30,
             height=4)

label2=Label(learn,
             text='Text Times Font',
             bd=10,
             relief='raised',
             bg='green',
             fg='white',
             font='Times 20 bold italic',
             width=40)

label3=Label(learn,
             text='Text Arial Font',
             bd=10,
             relief='sunken',
             fg='blue',
             font='Arial 20 bold italic')

label1.pack(),label2.pack()
label2.pack(),label3.pack()

learn.mainloop()

from tkinter import*

learn=Tk()
learn.title('Hello')
label1=Label(learn,
             text='Text Verdana Font\ntesting testing',bg='red',fg='white',font='Verdana 20 bold',width=30)
label2=Label(learn,
             text='Text Times Font',bg='green',fg='white',font='Times 20 bold italic',width=40)
label3=Label(learn,
             text='Text Arial Font',fg='blue',font='Arial 20 bold italic')

label1.pack()
label2.pack()
label2.pack()
label3.pack()

learn.mainloop()

import time;from tkinter import*

learn=Tk()
learn.title('Hello')
learn.geometry('500x100')
learn.resizable(width=False,height=False)

label1=Label(learn,text='Hello World',fg='black',font='Times 32 bold italic')
label2=Label(learn,text='Testing Testing')

label1.pack()
label2.pack()
learn.mainloop()

from tkinter import*
learn=Tk()

width=500
height=500

scrn_w=learn.winfo_screenwidth()
scrn_h=learn.winfo_screenheight()

x=(scrn_w/2)-(width/2)
y=(scrn_h/2)-(height/2)

learn.geometry('%dx%d+%d+%d'%(width,height,x,y))
learn.mainloop()

from tkinter import*
learn=Tk()
learn.title('Learn Tkinter')
learn.geometry('200x100+0+0')
learn.resizable(width=True,height=False)
learn.mainloop()

from tkinter import*
learn=Tk()
learn.title('Learn Tkinter')
learn.geometry('200x100+0+0')
learn.resizable(width=False,height=False)
learn.mainloop()

from tkinter import*
learn=Tk()
learn.title('Learn Tkinter')
learn.geometry('200x100+0+0')
learn.mainloop()

from tkinter import*
learn=Tk()
learn.title('Learn Tkinter')
learn.geometry('200x100')
learn.mainloop()

from tkinter import*
learn=Tk()
learn.title('Learn Tkinter')
learn.configure(width=200,height=100)
learn.mainloop()

from tkinter import*
learn=Tk()
learn.title('Learn Tkinter')
learn.configure(width=200,height=100,bg='#ff00ff')
learn.mainloop()

from tkinter import*
learn=Tk()
learn.title('Learn Tkinter')
learn.configure(width=400,height=200,bg='#ff00ff')
learn.mainloop()

from tkinter import*
learn=Tk()
learn.title('Learn Tkinter')
learn.configure(bg='#ff00ff')
learn.mainloop()

from tkinter import*
learn=Tk()
learn.title('Learn Tkinter')
learn.configure(bg='red')
learn.mainloop()
'''
from tkinter import*

my_window=Tk()

 code goes here

my_window.mainloop()
'''

for i in range(1000):
    print(i)
    print(i*2)
    print(i*3)
    print(i**2)

first_name=input('Please enter your first name ')
second_name=input('Please enter your surname ')
full_name=first_name+' '+second_name
print('Hello',full_name)

from tkinter import*

testing=Tk()
testing.title('Demo')

from tkinter import*

my_window=Tk()

def convert():
    F=float(fahrenheit_entry.get())
    C=(F-32)*5/9
    display_celsius_label['text']=str(C)

friendly_label_1=Label(my_window,text='Enter Fahrenheit')
friendly_label_2=Label(my_window,text='Celsius Temperature')
display_celsius_label=Label (my_window)
fahrenheit_entry=Entry(my_window)
convert_button=Button(my_window,text='Convert',command=convert)

friendly_label_1.grid(row=0,column=0)
fahrenheit_entry.grid(row=0,column=1)
friendly_label_2.grid(row=1,column=0)
display_celsius_label.grid(row=1,column=1)
convert_button.grid(row=2,column=0)

fahrenheit_entry.focus()

my_window.mainloop()


from tkinter import*

my_window=Tk()

class RedFrame(Frame):
    def __init__(self,the_window):

        super().__init__()
        self['height']=150
        self['width']=150
        self['relief']=RAISED
        self['bd']=8
        self['bg']='red'

frame_a=RedFrame(my_window)
frame_b=Frame(my_window,
              height=150,width=150,
              relief=RIDGE,bd=8)

frame_c=RedFrame(my_window)
frame_d=Frame(my_window,
              height=150,width=150,
              relief=RIDGE,bd=8)

frame_a.grid(row=0,column=0)
frame_b.grid(row=0,column=1)
frame_c.grid(row=1,column=0)
frame_d.grid(row=1,column=1)

my_window.mainloop()


from tkinter import*

my_window=Tk()

class RedFrame(Frame):
    def __init__(self,the_window):
        super().__init__()
        self['height']=150
        self['width']=150
        self['relief']=RAISED
        self['bd']=8
        self['bg']='red'

frame_a=RedFrame(my_window)
frame_b=RedFrame(my_window)
frame_c=RedFrame(my_window)
frame_d=RedFrame(my_window)

frame_a.grid(row=0,column=0)
frame_b.grid(row=0,column=1)
frame_c.grid(row=1,column=0)
frame_d.grid(row=1,column=1)

my_window.mainloop()


from tkinter import*

my_window=Tk()

class RedFrame(Frame):
    def __init__(self,the_window):
        super().__init__()
        self['height']=150
        self['width']=150
        self['relief']=RAISED
        self['bd']=8
        self['bg']='red'

frame_a=RedFrame(my_window)
frame_b=RedFrame(my_window)

frame_a.grid(row=0,column=0)
frame_b.grid(row=0,column=1)

my_window.mainloop()


from tkinter import*

my_window=Tk()

class RedFrame(Frame):
    def __init__(self,the_window):
        super().__init__()
        self['height']=150
        self['width']=150
        self['relief']=RAISED
        self['bd']=8
        self['bg']='red'

frame_a=RedFrame(my_window)
frame_a.grid(row=0,column=0)

my_window.mainloop()


from tkinter import*
my_window=Tk()
frame_a=Frame(my_window,height=150,width=150,relief=RAISED,bd=8,bg='red')
frame_a.grid(row=0,column=0)
my_window.mainloop()


from tkinter import*

my_window=Tk()

frame_a=Frame(my_window,height=150,width=150,relief=RAISED,bd=8,bg='red')
frame_b=Frame(my_window,height=150,width=150,relief=SUNKEN,bd=8,bg='green')

frame_a.grid(row=0,column=0)
frame_b.grid(row=0,column=1)

my_window.mainloop()


from tkinter import*

my_window=Tk()

frame_name=Frame(my_window)

label_first=Label(frame_name,text='First Name:')
label_middle=Label(frame_name,text='Middle Name:')
label_surname=Label(frame_name,text='Surname:')

entry_first=Entry(frame_name)
entry_middle=Entry(frame_name)
entry_surname=Entry(frame_name)

button_submit_name=Button(frame_name,text='Submit')

label_first.grid(row=0,column=0)
label_middle.grid(row=1,column=0)
label_surname.grid(row=2,column=0)

entry_first.grid(row=0,column=1)
entry_middle.grid(row=1,column=1)
entry_surname.grid(row=2,column=1)

button_submit_name.grid(row=3,columnspan=2)

frame_name.grid(row=0,column=0)
my_window.mainloop()


from tkinter import*

my_window=Tk()

entry_a=Entry(my_window,bg='red')
entry_b=Entry(my_window,bg='yellow')
entry_c=Entry(my_window,bg='white')

label_a=Label(my_window,text='First Name')
label_b=Label(my_window,text='Middle Name')
label_c=Label(my_window,text='Last Name')

entry_a.grid(row=0,column=1)
entry_b.grid(row=1,column=1)
entry_c.grid(row=2,column=1)

label_a.grid(row=0,column=0)
label_b.grid(row=1,column=0)
label_c.grid(row=2,column=0)

entry_a.focus()
my_window.mainloop()


from tkinter import*

my_window=Tk()

def sayhi():
    name_of_user=entry1.get()
    string_to_display='Hello',name_of_user
    var1.set(string_to_display)
var1=StringVar()

label1=Label(my_window,text='Please enter your name:')
entry1=Entry(my_window)
button1=Button(my_window,text='Click me to enter name',command=sayhi)
label2=Label(my_window,textvariable=var1)

label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
button1.grid(row=1,column=0)
label2.grid(row=1,column=1)

my_window.mainloop()


from tkinter import*

my_window=Tk()

def sayhi():
    name_of_user=entry1.get()
    string_to_display='Hello',name_of_user
    label2=Label(my_window)
    label2['text']=string_to_display
    label2.grid(row=1,column=1)

label1=Label(my_window,text='Please enter your name:')
entry1=Entry(my_window)
button1=Button(my_window,text='Click me to enter name',command=sayhi)

label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
button1.grid(row=1,column=0)

my_window.mainloop()


from tkinter import*

my_window=Tk()

def label_red():
    label1['bg']='red'
def label_green():
    label1['bg']='green'
def label_blue():
    label1['bg']='blue'

label1=Label(my_window,width='20',height='3')
button1=Button(my_window,text='red',width=6,command=label_red)
button2=Button(my_window,text='green',width=6,command=label_green)
button3=Button(my_window,text='blue',width=6,command=label_blue)

label1.grid(row=0,column=1)
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

my_window.mainloop()


from tkinter import*
my_window=Tk()
label1=Label(my_window,width='20',height='3',bg='red')
label2=Label(my_window,width='20',height='3',bg='green')
label3=Label(my_window,width='20',height='3',bg='blue')

button1=Button(my_window,text='Click Me 1')
button2=Button(my_window,text='Click Me 2')
button3=Button(my_window,text='Click Me 3')

label1.grid(row=0,column=0)
label2.grid(row=1,column=1)
label3.grid(row=0,column=2)

button1.grid(row=1,column=0)
button2.grid(row=0,column=1)
button3.grid(row=1,column=2)
my_window.mainloop()


from tkinter import*
my_window=Tk()
label1=Label(my_window,width='20',height='3',bg='red')
label2=Label(my_window,width='20',height='3',bg='green')
label3=Label(my_window,width='20',height='3',bg='blue')

button1=Button(my_window,text='Click Me 1')
button2=Button(my_window,text='Click Me 2')
button3=Button(my_window,text='Click Me 3')

label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
my_window.mainloop()


from tkinter import*
my_window=Tk()
label1=Label(my_window,width='20',height='3',bg='red')
label2=Label(my_window,width='20',height='3',bg='green')
label3=Label(my_window,width='20',height='3',bg='blue')
label4=Label(my_window,width='20',height='3',bg='white')
label5=Label(my_window,width='20',height='3',bg='black')
label6=Label(my_window,width='20',height='3',bg='grey')
label7=Label(my_window,width='20',height='3',bg='#4477af')
label8=Label(my_window,width='20',height='3',bg='#997755')
label9=Label(my_window,width='20',height='3',bg='#ccff44')

label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)
label4.grid(row=1,column=0)
label5.grid(row=1,column=1)
label6.grid(row=1,column=2)
label7.grid(row=2,column=0)
label8.grid(row=2,column=1)
label9.grid(row=2,column=2)

my_window.mainloop()


from tkinter import*
my_window=Tk()
label1=Label(my_window,width='20',height='3',bg='red')
label2=Label(my_window,width='20',height='3',bg='green')
label3=Label(my_window,width='20',height='3',bg='blue')
label4=Label(my_window,width='20',height='3',bg='white')
label5=Label(my_window,width='20',height='3',bg='black')
label6=Label(my_window,width='20',height='3',bg='grey')

label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)
label4.grid(row=1,column=0)
label5.grid(row=1,column=1)
label6.grid(row=1,column=2)
my_window.mainloop()


from tkinter import*
my_window=Tk()
label1=Label(my_window,
             width='20',
             height='3',
             bg='red')
label2=Label(my_window,
             width='20',
             height='3',
             bg='green')
label3=Label(my_window,
             width='20',
             height='3',
             bg='blue')
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)

my_window.mainloop()


from tkinter import*
def label():
    label1=Label(my_window,
                 text='Hello World')
    label1.pack()
my_window=Tk()
my_window.geometry('200x100')
button1=Button(my_window,
               text='Click Me',
               command=label)
button1.pack()
my_window.mainloop()


from tkinter import*
my_window=Tk()
my_window.geometry('200x100')
button1=Button(my_window,
                 text='Click Me!')
button1.pack()
my_window.mainloop()


from tkinter import*
my_window=Tk()
var1=StringVar()
label1=Label(my_window,
             relief='solid',
             font='Times 22 bold',
             text='Hello World')
label2=Label(my_window,
             relief='solid',
             font='Times 22 bold',
             textvariable=var1)
label1.pack()
label2.pack()
label1['text']='Text put here using key/value pairs approach'
var1.set('Using textvariable and StringVar()')
my_window.mainloop()


from tkinter import*
my_window=Tk()
var1=StringVar()
label1=Label(my_window,
             relief='solid',
             font='Times 22 bold',
             textvariable=var1)
label1.pack()
var1.set('Hi')
my_window.mainloop()


from tkinter import*
my_window=Tk()
my_window.configure(height=500,width=500)

label1=Label(my_window,text='I am label one',bg='blue',fg='green',font='arial 32 bold',width=20)
label2=Label(my_window,text='I am label two',bg='black',fg='green',font='times 12 bold italic',width=30)
label3=Label(my_window,text='I am label three\nInline break',bg='yellow',fg='green',font='times 32 bold italic',width=40)
label4=Label(my_window,text='I am label three',bd=2,relief='solid',bg='yellow',fg='green',font='times 32 bold italic')
label4=Label(my_window,text='I am label three',bd=8,relief='raised',fg='green',font='times 12 bold italic')
label4=Label(my_window,text='I am label three',bd=8,relief='sunken',fg='green',font='times 20 bold italic')
label4=Label(my_window,text='I am label three',bd=8,relief='ridge',fg='green',font='times 20 bold italic')
label4=Label(my_window,text='I am label three',bd=8,relief='groove',fg='green',font='times 20 bold italic')
label4=Label(my_window,text='I am label three',bd=8,relief='flat',fg='green',font='times 20 bold italic')
label4=Label(my_window,
             text='I am label three\ntesting\ntesting',
             bd=1,
             relief='solid',
             fg='green',
             font='times 20 bold italic',
             width=15,
             height=4,
             anchor=CENTER)

label1.pack()
label2.pack()
label3.pack()
label4.pack()
label1['font']='arial'
label1['fg']='white'
label1['text']='white'

my_window.mainloop()


from tkinter import*
my_window=Tk()
my_canvas=Canvas(my_window,width=400,height=300,background='white')
my_canvas.grid(row=0,column=0)
my_canvas.create_line(10,30,390,30,fill='blue',arrow='last',width=4)
my_canvas.create_line(10,100,390,100,fill='blue',arrow='last',arrowshape=(64,80,24),width=4)
my_canvas.create_line(10,170,390,170,fill='blue',arrow='last',arrowshape=(70,40,24),width=4)
my_canvas.create_line(10,240,390,240,fill='blue',arrow='last',arrowshape=(100,100,24),width=4)
my_window.mainloop()


from tkinter import*
my_window=Tk()
width=500
height=500
screen_width=my_window.winfo_screenwidth()
screen_height=my_window.winfo_screenheight()
x=(screen_width/2)-(width/2)
y=(screen_height/2)-(height/2)
my_window.geometry('%dx%d+%d+%d' % (width,height,x,y))
my_window.mainloop()


from tkinter import*
root=Tk()
root.configure(height=500,width=500)
root.resizable(width=False,height=False)
root.mainloop()


from tkinter import*
root=Tk()
root.configure(height=500,width=500)
root.mainloop()


from tkinter import*
root=Tk()
root.geometry('500x500')
root.mainloop()


from tkinter import*
root=Tk()
root.geometry('500x500+0+0')
root.mainloop()


from tkinter import*
root=Tk()
draw=Canvas(root,height=500,width=500)
draw.pack()
root.mainloop()


from tkinter import*

root=Tk()
root.title('Strying Art')

draw=Canvas(root,height=500,width=500,bg='black')
for i in range(0,400,3):
    draw.create_line(50+i,50+i,450,50,450,50,450,450,50,450,50+i,50+i,fill='cyan')
draw.pack()

root.mainloop()
