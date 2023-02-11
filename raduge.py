from tkinter import *

root = Tk()

def color_name(c_n):
    if c_n==1:
        lab['text'] = 'красный'
        ent.delete(0,END)
        ent.insert(0,'#ff0000')
    elif c_n==2:
        lab['text'] = 'оранжевый'
        ent.delete(0,END)
        ent.insert(0,'#ff7300')
    elif c_n==3:
        lab['text'] = 'желтый'
        ent.delete(0,END)
        ent.insert(0,'##ffff00')
    elif c_n==4:
        lab['text'] = 'зеленый'
        ent.delete(0,END)
        ent.insert(0,'#00ff00')
    elif c_n==5:
        lab['text'] = 'голубой'
        ent.delete(0,END)
        ent.insert(0,'#007dff')
    elif c_n==6:
        lab['text'] = 'синий'
        ent.delete(0,END)
        ent.insert(0,'#0711FF')
    elif c_n==7:
        lab['text'] = 'фиолетовый'
        ent.delete(0,END)
        ent.insert(0,'#5C06FF')

ent = Entry(width=50,justify=CENTER)
lab = Label(width=48,anchor=CENTER)
but = Button(width=50,bg='#ff0000')
but1 = Button(width=50,bg='#ff7300')
but2 = Button(width=50,bg='#ffff00')
but3 = Button(width=50,bg='#00ff00')
but4 = Button(width=50,bg='#007dff')
but5 = Button(width=50,bg='#0711FF')
but6 = Button(width=50,bg='#5C06FF')

but.bind('<Button-1>',lambda event: color_name(1))
but1.bind('<Button-1>',lambda event: color_name(2))
but2.bind('<Button-1>',lambda event: color_name(3))
but3.bind('<Button-1>',lambda event: color_name(4))
but4.bind('<Button-1>',lambda event: color_name(5))
but5.bind('<Button-1>',lambda event: color_name(6))
but6.bind('<Button-1>',lambda event: color_name(7))

lab.pack()
ent.pack()
but.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
but5.pack()
but6.pack()

root.mainloop()