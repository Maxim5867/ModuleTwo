from tkinter import *

root = Tk()


fr = Frame(root)

def color_name(n):
    if n==1:
        lab['text'] = 'красный'
        ent.delete(0,END)
        ent.insert(0,'#ff0000')
    elif n==2:
        lab['text'] = 'оранжевый'
        ent.delete(0,END)
        ent.insert(0,'#ff7300')
    elif n==3:
        lab['text'] = 'желтый'
        ent.delete(0,END)
        ent.insert(0,'##ffff00')
    elif n==4:
        lab['text'] = 'зеленый'
        ent.delete(0,END)
        ent.insert(0,'#00ff00')
    elif n==5:
        lab['text'] = 'голубой'
        ent.delete(0,END)
        ent.insert(0,'#007dff')
    elif n==6:
        lab['text'] = 'синий'
        ent.delete(0,END)
        ent.insert(0,'#0711FF')
    elif n==7:
        lab['text'] = 'фиолетовый'
        ent.delete(0,END)
        ent.insert(0,'#5C06FF')

ent = Entry(width=30,justify=CENTER)
lab = Label(width=30,anchor=CENTER)
but = Button(fr,width=2,bg='#ff0000')
but1 = Button(fr,width=2,bg='#ff7300')
but2 = Button(fr,width=2,bg='#ffff00')
but3 = Button(fr,width=2,bg='#00ff00')
but4 = Button(fr,width=2,bg='#007dff')
but5 = Button(fr,width=2,bg='#0711FF')
but6 = Button(fr,width=2,bg='#5C06FF')



but.bind('<Button-1>',lambda event: color_name(1))
but1.bind('<Button-1>',lambda event: color_name(2))
but2.bind('<Button-1>',lambda event: color_name(3))
but3.bind('<Button-1>',lambda event: color_name(4))
but4.bind('<Button-1>',lambda event: color_name(5))
but5.bind('<Button-1>',lambda event: color_name(6))
but6.bind('<Button-1>',lambda event: color_name(7))



lab.pack()
ent.pack()
fr.pack()
but.pack(side=LEFT)
but1.pack(side=LEFT)
but2.pack(side=LEFT)
but3.pack(side=LEFT)
but4.pack(side=LEFT)
but5.pack(side=LEFT)
but6.pack(side=LEFT)

root.mainloop()