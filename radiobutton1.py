from tkinter import *

root = Tk()

r_var = BooleanVar()
r_var.set(0)

r1 = Radiobutton(text='Первый',variable=r_var,value=0)
r2 = Radiobutton(text='Второй',variable=r_var,value=1)

r1.pack()
r2.pack()

root.mainloop()
