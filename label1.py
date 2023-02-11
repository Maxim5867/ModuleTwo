from tkinter import *

def change():
    lab['text'] = 'Выдано'
    b1['bg'] = '#000000'
    lab1['fg'] = '#0F0'
    lab['fg'] = '#34eba4'

root = Tk()

lab1 = Label(text='Пункт выдачи')
b1 = Button(text='Получить', command = change)
lab1.pack()
lab = Label(width=10,height=1)
b1.pack()
lab.pack()

root.mainloop()