'''TKINTER:'''
'''
Welcome to tkinter, the canvas part of Python. With tkinter you can draw lines and
shapes such as ovals, arcs and rectangles. You can also create some wild digital
string-art designs with for-loops. With tkinter you can also create buttons and input
boxes. We will get into all this and more about tkinter, the fun part of Python programming.
'''
# Let's create a simple tkinter window. Type and execute/run this tkinter program
# example below and see what happens.

from tkinter import*

root=Tk()

'''----------------------------------------------------------------'''

# This simple tkinter program will create an empty window, which is 500 X 500 pixels.
# Type and execute/run this tkinter program example below and see what happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500)

draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# So far the tinkter window is empty; no canvas colours or anything, but a simple
# grayed out, empty tkinter window. Now, let's add colour to our empty tkinter window
# to sort of see where we are going with tkinter. Type and execute/run the tkinter
# program example below and see what happens when we add the colour black to our
# empty tkinter window.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')

draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Now that we have our empty tkinter window, which is now a black, empty tkinter
# window. Let's add a simple, blue diagonal line drawing inside our black, empty
# tkinter window and see what happens when you execute/run the tkinter program
# example below.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')

draw.create_line(0,0,500,500,fill='blue')

draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Note: hexadecimal values can also be used with the tkinter canvas colour as well as
# the tkinter graphics colour scheme alike. All hexadecimal values in Python start with
# the '#' number sign, then preceding with a six digit hexadecimal number to the right,
# for example '#000000' = black, '#ffffff' = white. See below, a basic hexadecimal RGB
# colour codes list as follows:

# Black = '#000000'
# White = '#ffffff'
# Red = '#ff0000'
# Green = '#00ff00'
# Blue = '#000fff'
# Yellow = '#fff000'
# Pink = '#ff00ff'
# Cyan = '#00ffff'

# Now let's add another diagonal line in the tkinter window and colour it red and
# change the background colour to the hexadecimal colour code, black. type and
# execute/run the tkinter program example below and see what happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='#000000')

draw.create_line(0,0,500,500,fill='blue')
draw.create_line(0,500,500,0,fill='red')

draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Let's now draw a complete yellow square right in the middle of our X-shaped lines
# and see what happens when you execute/run the tkinter program example below.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')

draw.create_line(0,0,500,500,fill='blue')
draw.create_line(0,500,500,0,fill='red')
draw.create_line(50,50,450,50,450,50,450,450,50,450,50,50,fill='yellow')

draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Now let's make all the lines in our tkinter drawing thicker. Type and execute/run the
# tkinter program example below and see what happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')
draw.create_line(0,0,500,500,fill='blue',width=5)
draw.create_line(0,500,500,0,fill='red',width=5)
draw.create_line(50,50,450,50,450,50,450,450,50,450,50,50,fill='yellow',width=5)

draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Let's draw a simple rectangle with tkinter's 'rectangle' command. Type and
# execute/run the tkinter program example below and see what happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')

draw.create_rectangle(150,100,340,400,outline='cyan',width=5)

draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Let's fill the inside of the rectangle with the colour red. Type and execute/run the
# tkinter program example below and see what happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')

draw.create_rectangle(150,100,340,400,fill='red',outline='cyan',width=5)

draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Let's draw a simple oval with tkinter's 'oval' command. Type and execute/run the
# tkinter program example below and see what happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')

draw.create_oval(150,100,340,400,fill='red',outline='cyan',width=5)

draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Let's draw a simple arc with tkinter's 'arc' command. Type and execute/run the
# tkinter program below and see what happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')

draw.create_arc(120 ,120,400,400,extent=180,fill='red',outline='cyan',width=5)

draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Now let's create a tkinter digital string-art design using a for-loop. Type and
# execute/run the tkinter program example below and see what happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')

for i in range(0,400,3):
    draw.create_line(50+i,50+i,450,50,450,50,450,450,50,450,50+i,50+i,fill='cyan')
    
draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Now let's create a tkinter digital string-art design using tkinter's 'rectangle'
# command with a for-loop. Type and execute/run the tkinter program example below
# and see what happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')

for i in range(0,96,5):
    draw.create_rectangle(150+i,100+i,340-i,400-i,outline='cyan')
    
draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Now let's create a tkinter digital string-art design using tkinter's 'oval' command with
# a for-loop. Type and execute/run the tkinter program example below and see what
# happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')

for i in range(0,96,5):
    draw.create_oval(150+i,100+i,340-i,400-i,outline='cyan')
    
draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Now let's create a tkinter digital string-art design using tkinter's 'arc' command with
# a for-loop. Type and execute/run the tkinter program example below and see what
# happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')

for i in range(0,140,5):
    draw.create_arc(120+i ,120+i,400-i,400-i,extent=180,outline='cyan')
    
draw.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Let's import an image from your computer with tkinter. See what happens when you
# type and execute/run the tkinter program example below.

from tkinter import*

root=Tk()

photo=PhotoImage(file='C:\\Users\\JCR\\Documents\\Pictures\\image.jpg')

label=Label(root,image=photo)

label.pack()

root.mainloop()

'''----------------------------------------------------------------'''

# Let's set the canvas width and the canvas height, then import an image from your
# computer with tkinter. See what happens when you type and execute/run the tkinter
# program example below.

from tkinter import*

root=Tk()

canvas=Canvas(width=600,height=600,bg='blue')

canvas.pack()

photo=PhotoImage(file='C:\\Users\\JCR\\Documents\\Pictures\\image.jpg')

canvas.create_image(300,300,image=photo)

root.mainloop()

'''----------------------------------------------------------------'''

# Let's add anchoring to an image and position it in the center of the canvas. The
# anchor emitter has up to nine positional value settings: CENTER, N, S, E, W, NW, NE,
# SW, SE. See what happens when you type and execute/run the tkinter program
# example below.

from tkinter import*

root=Tk()

canvas=Canvas(width=600,height=600,bg='blue')

canvas.pack()

photo=PhotoImage(file='C:\\Users\\JCR\\Documents\\Pictures\\image.jpg')

canvas.create_image(300,300,image=photo,anchor=CENTER)

root.mainloop()

'''----------------------------------------------------------------'''

# Let's create a button with tkinter and see what happens when you type and
# execute/run the tkinter program example below.

from tkinter import*

button=Tk()

button.geometry('500x500')
button_1=Button(button,text='Click Me!')

button_1.pack()

button.mainloop()

'''----------------------------------------------------------------'''

# Let's create a label for our tkinter button and see what happens when you type and
# execute/run the tkinter program example below.

from tkinter import*

button=Tk()

button.geometry('500x500')
label_1=Label(button,text=' "Python Programmer\'s Glossary Bible" ')
button_1=Button(button,text='Click Me!')

label_1.pack()

button_1.pack()

button.mainloop()

'''----------------------------------------------------------------'''

# Let's make the tkinter button call the label with a 'def' function. Every time the 'Click
# Me!' button is clicked, the 'def' function gets called and the label is desplayed again.
# See what happens when you type and execute/run the tkinter program example
# below.

from tkinter import*

button=Tk()

def call_the_def_function():
    label_1=Label(button,text=' "Python Programmer\'s Glossary Bible" ')
    
    label_1.pack()

button.geometry('500x500')
button_1=Button(button,text='Click Me!',command=call_the_def_function)

button_1.pack()

button.mainloop()

'''----------------------------------------------------------------'''

# Let's reposition the tkinter button and its label by invoking the 'side=TOP' statement
# for the label and the 'side=LEFT' statement for the tkinter button. See what happens
# when you type and execute/run the tkinter program example below.

from tkinter import*

button=Tk()

def call_the_def_function():
    label_1=Label(button,text=' "Python Programmer\'s Glossary Bible" ')
    
    label_1.pack(side=TOP)

button.geometry('500x500')
button_1=Button(button,text='Click Me!',command=call_the_def_function)

button_1.pack(side=LEFT)

button.mainloop()

# More Tkinter examples still to come, as I learn more and more, each and every day.
