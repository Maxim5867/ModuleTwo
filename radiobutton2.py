from tkinter import *

def change():
    if r_var.get()==0:
        lab['bg']= 'red'
    elif r_var.get()==1:
        lab['bg'] = 'green'
    elif r_var.get()==2:
        lab['bg'] = 'blue'


root = Tk()

r_var = IntVar()
r_var.set(0)

r1 = Radiobutton(text='Красный',variable=r_var,value=0)
r2 = Radiobutton(text='Зеленый',variable=r_var,value=1)
r3 = Radiobutton(text='Синий',variable=r_var,value=2)
but = Button(text='Изменить', command=change)
lab = Label(width=20,height=10)

r1.pack()
r2.pack()
r3.pack()
but.pack()
lab.pack()

root.mainloop()