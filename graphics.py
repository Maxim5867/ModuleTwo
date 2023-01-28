from tkinter import *

def create_triangle(canvas,x1,y1,x2,y2,x3,y3):
    Vvod = input('Введите первую координату x')
    otv = input('Введите первую координату y')
    t = input('Введите вторую координату x')
    r = input('Введите вторую координату y')
    e = input('Введите третью координату x')
    n = input('Введите третью координату y')
    Vvod = Vvod.lower()
    otv = otv.lower()
    t = t.lower()
    r = r.lower()
    e = e.lower()
    n = n.lower()

    canvas.create_line(x1,y1,x2,y2)
    canvas.create_line(x1,y1,x3,y3)
    canvas.create_line(x3,y3,x2,y2)
