from tkinter import *

def vivod():
    if r_var.get()==0:
        lab['text'] = '+7 980 485 86 57'
    elif r_var.get()==1:
        lab['text'] = '+7 910 777 94 36'
    elif r_var.get()==2:
        lab['text'] = '+7 901 473 96 20'

root = Tk()
r_var = IntVar()
r_var.set(0)
frame = Frame()
fr = Frame()


r1 = Radiobutton(frame,text='Вася',indicatoron=0,variable=r_var,value=0,width=7,height=4,command=vivod)
r2 = Radiobutton(frame,text='Петя',indicatoron=0,variable=r_var,value=1,width=7,height=4,command=vivod)
r3 = Radiobutton(fr,text='Маша',indicatoron=0,variable=r_var,value=2,width=7,height=4,command=vivod)
lab = Label(width=20,height=10)

frame.pack()
r1.pack()
r2.pack()
r3.pack()
fr.pack()
lab.pack(side=RIGHT)

root.mainloop()