from tkinter import *
root = Tk()

def plus(event):
    x1 = ent.get()
    x1 = (x1)
    x2 = unt.get()
    x2 = (x2)
    y = str(x1+x2)
    if (x1 == 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяqwertyuiopasdfghjklzxcvbnm') or (x2 != 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяqwertyuiopasdfghjklzxcvbnm'):
        lab['text'] = 'Ошибка'
    else:
        lab['text'] = y
def minus(event):
    x3 = ent.get()
    x3 = (x3)
    x4 = unt.get()
    x4 = (x4)
    i = str(x3-x4)
    if (x3 == 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяqwertyuiopasdfghjklzxcvbnm') or (x4 != 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяqwertyuiopasdfghjklzxcvbnm'):
        lab['text'] = 'Ошибка'
    else:
        lab['text'] = i

def proizv(event):
    x5 = ent.get()
    x5 = (x5)
    x6 = unt.get()
    x6 = (x6)
    q = str(x5*x6)
    if (x5 == 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяqwertyuiopasdfghjklzxcvbnm') or (x6 != 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяqwertyuiopasdfghjklzxcvbnm'):
        lab['text'] = 'Ошибка'
    else:
        lab['text'] = q

def delen(event):
    x7 = ent.get()
    x7 = (x7)
    x8 = unt.get()
    x8 = (x8)
    w = str(x7/x8)
    if (x7 == 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяqwertyuiopasdfghjklzxcvbnm') or (x8 != 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяqwertyuiopasdfghjklzxcvbnm'):
        lab['text'] = 'Ошибка'
    else:
        lab['text'] = w

ent = Entry(width=20)
unt = Entry(width=20)
but = Button(text='+')
bute = Button(text='-')
buto = Button(text='*')
butu = Button(text='/')
lab = Label(width=20,bg='black',fg='white')

but.bind('<Button-1>',plus)
bute.bind('<Button-1>',minus)
buto.bind('<Button-1>',proizv)
butu.bind('<Button-1>',delen)

ent.pack()
unt.pack()
but.pack()
bute.pack()
buto.pack()
butu.pack()
lab.pack()

root.mainloop()