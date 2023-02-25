from tkinter import *

def ins_text():
    t = 'Привет, мир!'
    text.insert(1.0,t)

def g_text():
    t = text.get(1.0,END)
    lab['text'] = t

def del_text():
    text.delete(1.0,END)
    
root = Tk()

text = Text(width=20,height=7)
text.pack()

frame = Frame()
frame.pack()

Button(frame,text='Вставить',command=ins_text).pack(side=LEFT)
Button(frame,text='Взять',command=g_text).pack(side=LEFT)
Button(frame,text='Удалить',command=del_text).pack(side=LEFT)

lab = Label()
lab.pack()

root.mainloop()

