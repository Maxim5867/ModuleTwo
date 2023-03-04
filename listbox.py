from tkinter import *

root = Tk()

lbox = Listbox(width=15,height=8,selectmode=EXTENDED)
lbox.pack()

for i in('один','два','три','четыре','пять','шесть','семь'):
    lbox.insert(END,i)

root.mainloop()