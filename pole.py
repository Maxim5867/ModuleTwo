from tkinter import *

root = Tk()

def change_side(event):
    if ent.get().isdigit():
        box['width'] = ent.get()
    elif ent1.get().isdigit():
        box['height'] = ent1.get()

def white_color(event):
    box['bg'] = 'white'

def grey_color(event):
    box['bg'] = 'lightgrey'

f = Frame()
f1 = Frame()
f2 = Frame()

ent = Entry(width=2)
ent1 = Entry(width=2)
but = Button(text='Изменить')
box = Text()

f.pack()
f1.pack(side=LEFT)
ent.pack()
ent1.pack()
but.pack()
f2.pack()
box.pack()



root.mainloop()