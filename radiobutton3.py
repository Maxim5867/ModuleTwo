from tkinter import *

def paint(color):
    lab['bg'] = color

class RBColor:
    def __init__(self,color,val):
        Radiobutton(
            text=color,
            command=lambda i=color: paint(i),
            indicatoron=0, #для изменения вида под кнопку
            variable=r_var,value=val
        ).pack()

root = Tk()

r_var = IntVar()
r_var.set(0)

RBColor('red',0)
RBColor('green',1)
RBColor('blue',2)

lab = Label(width=20,height=10,bg='red')

lab.pack()

root.mainloop()