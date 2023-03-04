from tkinter import *

def show():
    s = f'{var1.get()},' \
        
    lab['text'] = s


root = Tk()

frame = Frame()
frame.pack(side=LEFT)

var1 = BooleanVar()
var1.set(0)

c1 = Checkbutton(frame,text='Первый',
                 variable=var1,
                 onvalue=1,offvalue=0,
                 command=show)
c1.pack()

lab = Label()
