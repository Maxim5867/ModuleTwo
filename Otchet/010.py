from tkinter import *
 
 
def red_label():
    label['bg'] = 'red'
 
 
def green_label():
    label['bg'] = 'green'
 
 
def blue_label():
    label['bg'] = 'blue'
 
 
root = Tk()
 
var = IntVar()
var.set(0)
Radiobutton(text="Красный", command=red_label,
            variable=var, value=0).pack()
Radiobutton(text="Зеленый", command=green_label,
            variable=var, value=1).pack()
Radiobutton(text="Синий", command=blue_label,
            variable=var, value=2).pack()
label = Label(width=20, height=10, bg='red')
label.pack()
 
root.mainloop()