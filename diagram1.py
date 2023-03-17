from tkinter import *

root = Tk()

c = Canvas(width=1000,height=500)
c.pack()

c.create_oval(10,10,490,490,fill='lightgrey', outline='white')
c.create_arc(12,10,485,485,start=150, extent=60, fill='red', outline='black')
c.create_arc(12,10,485,485,start=210, extent=110, fill='orange', outline='black')
c.create_arc(12,10,485,485,start=320, extent=150, fill='purple', outline='black')
c.create_arc(12,10,485,485,start=470, extent=40, fill='green', outline='black')

c.create_text(648,40, text='Общее количество учеников равно 28', font='Arial 13')
c.create_text(715,80, text='Количество учеников, которые учатся на пять равно 3', font='Arial 13', fill='green')
c.create_text(731,120, text='Количество учеников, которые учатся на четыре равно 12', font='Arial 13', fill='purple')
c.create_text(712,160, text='Количество учеников, которые учатся на три равно 8', font='Arial 13', fill='orange')
c.create_text(714,200, text='Количество учеников, которые учатся на два равно 5', font='Arial 13', fill='red')
c.create_text(130,100, text='10,7%',font='Arial 13')
c.create_text(350,170, text='42,9%',font='Arial 13')
c.create_text(250,370, text='28,6%',font='Arial 13')
c.create_text(110,240, text='17,9%',font='Arial 13')

root.mainloop()
