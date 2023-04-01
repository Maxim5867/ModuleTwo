from tkinter import *

root = Tk()

def oval_func(event):
    c.delete(oval)
    c.create_text(80, 50, text='Овал',tags='oval1')

def oval_func1(event):
    c.delete('oval1')
    c.create_oval(30,10,130,80, fill='orange')

def rect_func(event):
    c.delete(tril)
    c.create_text(230, 50, text='Прямогульник',tags='rect')

def rect_func1(event):
    c.delete('rect')
    c.create_rectangle(180,10,280,80,fill='lightgreen')

def triangle(event):
    c.delete(trian)
    c.create_text(380,50,text='Треугольник',tags='triang')

def triangle1(event):
    c.delete('triang')
    c.create_polygon(330,80,380,10,430,80,fill='white',outline='black')

c = Canvas(width=460, height=100, bg='grey')
c.pack()

oval = c.create_oval(30,10,130,80, fill='orange')
tril = c.create_rectangle(180,10,280,80,fill='lightgreen')
trian = c.create_polygon(330,80,380,10,430,80,fill='white',outline='black')

c.tag_bind(oval,'<Button-1>', oval_func)
c.tag_bind(tril,  '<Button-1>', rect_func)
c.tag_bind(trian, '<Button-1>', triangle)
c.tag_bind('oval1','<Button-1>', oval_func1)
c.tag_bind('rect',  '<Button-1>', rect_func1)
c.tag_bind('triang', '<Button-1>', triangle1)

root.mainloop()
