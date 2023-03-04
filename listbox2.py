from tkinter import *

root = Tk()

def zamena():
    box = shop
    box


shop = ['яблоко морковь груша банан киви помидор огурец']

box = Listbox(selectmode=EXTENDED, command=zamena)
box1 = Listbox(selectmode=EXTENDED)
b1 = Button(text = '>>>')
b2 = Button(text = '<<<')

box.pack()
b1.pack()
b2.pack()
box1.pack()

root.mainloop()