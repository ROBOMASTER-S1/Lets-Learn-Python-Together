from tkinter import*
root=Tk()
root.title('Majestic Calculator')
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_add():
    return

button1=Button(root,text='1',padx=40,pady=20,command=button_add)
button2=Button(root,text='2',padx=40,pady=20,command=button_add)
button3=Button(root,text='3',padx=40,pady=20,command=button_add)
button4=Button(root,text='4',padx=40,pady=20,command=button_add)
button5=Button(root,text='5',padx=40,pady=20,command=button_add)
button6=Button(root,text='6',padx=40,pady=20,command=button_add)
button7=Button(root,text='7',padx=40,pady=20,command=button_add)
button8=Button(root,text='8',padx=40,pady=20,command=button_add)
button9=Button(root,text='9',padx=40,pady=20,command=button_add)
button0=Button(root,text='0',padx=40,pady=20,command=button_add)
button_add=Button(root,text='+',padx=39,pady=20,command=button_add)
button_equal=Button(root,text='=',padx=91,pady=20,command=button_add)
button_clear=Button(root,text='Clear',padx=79,pady=20,command=button_add)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)

window_title='Frame Works'
window_size='197x374'
window_colour='#000000'
font_style='Arial Bold'
font_size=20
digit=0,1,2,3,4,5,6,7,8,9,'%','.','/','*','-','+','=','c'

black='#000000'
gray='#dddddd'
black_red='#550000'
white='#ffffff'
red='#ff0000'
yellow='#fff000'
blue='#000fff'
green='#00ff00'
pink='#ff00ff'
dark_pink='#880088'

root=Tk()

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
 
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
root.geometry("+{}+{}".format(positionRight, positionDown))

winfo_scw=root.winfo_screenwidth()
winfo_sch=root.winfo_screenheight()
win_width=1;win_height=600

x=(winfo_scw/2)-(win_width/2)
y=(winfo_sch/2)-(win_height/2)

root.configure(bg='#000000')
root.geometry('%dx%d+%d+%d'%(win_width,win_height,x,y))

def test():

    root.title(window_title)

    root.geometry(window_size)
    root.configure(bg=window_colour)
    root.resizable(width=False,height=False)

    entry=Entry(root,font=(font_style,font_size),
                bg=gray,fg=red,width=11,bd=15).place(x=0,y=0)
    
    b7=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[7]).place(x=0,y=68)

    b8=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[8]).place(x=50,y=68)

    b9=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[9]).place(x=100,y=68)

    b12=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[12]).place(x=150,y=68)

    b4=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[4]).place(x=0,y=130)

    b5=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[5]).place(x=50,y=130)

    b6=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[6]).place(x=100,y=130)

    b13=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[13]).place(x=150,y=130)

    b1=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[1]).place(x=0,y=192)

    b2=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[2]).place(x=50,y=192)

    b3=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[3]).place(x=100,y=192)

    b14=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[14]).place(x=150,y=192)

    b11=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[11]).place(x=0,y=254)

    b0=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[0]).place(x=50,y=254)

    b17=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[17]).place(x=100,y=254)

    b15=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=2,bd=5,text=digit[15]).place(x=150,y=254)

    b16=Button(root,font=(font_style,font_size),anchor=CENTER,bg=gray,
              fg=dark_pink,width=11,bd=3,text=digit[16]).place(x=0,y=317)

test()

root.mainloop()
