from tkinter import *

class ChButton:
    def __init__(self,master,title):
        self.var = BooleanVar()
        self.var.set(0)
        self.title = title
        self.cb = Checkbutton(
            master,text=title,variable=self.var,
            onvalue=1,offvalue=0)
        self.cb.pack(side=LEFT)

def ch_on():
    for ch in checks:
        ch.cb.select()
    
def ch_off():
    for ch in checks:
        ch.cb.deselect()

root = Tk()

f1 = Frame()
f1.pack(padx=10,pady=10)

checks = []

for i in range(5):
    checks.append(ChButton(f1,i))

f2 = Frame()
f2.pack()

but_on = Button(f2,text='Выделить все',command=ch_on)
but_on.pack(side=LEFT)

but_off = Button(f2,text='Стереть все',command=ch_off)
but_off.pack(side=LEFT)

root.mainloop()