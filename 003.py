from tkinter import *

root = Tk()

def addFigur():
    fig = Toplevel()
    fig.title('Фигура')
    fig.resizable(0,0)

    Label(fig, text='x1').grid(row=0, column=1)
    x1 = Entry(fig, width=3)
    x1.grid(row=0, column=2)
    Label(fig, text='y1').grid(row=0, column=5)
    y1 = Entry(fig, width=3)
    y1.grid(row=0, column=6)

    Label(fig, text='x2').grid(row=5,column=1,pady=10)
    x2 = Entry(fig, width=3)
    x2.grid(row=5,column=2,pady=10)
    Label(fig, text='y2').grid(row=5,column=5,pady=10)
    y2 = Entry(fig, width=3)
    y2.grid(row=5,column=6,pady=10)

    v = IntVar()
    v.set(1)
    Radiobutton(fig, text='Прямоугольник', variable=v, value=1).grid(row=6,columnspan=7,pady=5)
    Radiobutton(fig, text='Овал', variable=v, value=0).grid(row=7,columnspan=3,pady=5)

    def paint():
        x = int(x1.get())
        y = int(y1.get())
        xx = int(x2.get())
        yy = int(y2.get())
        if v.get() == 0:
            c.create_oval(x, y, xx, yy, width=2)
        elif v.get() == 1:
            c.create_rectangle(x, y, xx, yy, width=2)
        fig.destroy()

    Button(fig, text='Нарисовать', command=paint).grid(row=9,columnspan=7,pady=5)

c = Canvas(width=300, height=300, bg='white')
c.pack()
Button(text='Добавить фигуру', command=addFigur).pack()

root.mainloop()