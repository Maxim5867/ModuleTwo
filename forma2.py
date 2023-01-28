from tkinter import *
from graphics import create_triangle

window = Tk()
window.title('Треугольник')
canvas = Canvas(window,width=800,height=600,background='white')
create_triangle(canvas,100,50,100,200,400,200)
canvas.pack(expand=True,fill=BOTH)
window.mainloop()