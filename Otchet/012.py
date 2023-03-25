from tkinter import *

root = Tk()

def oval_func(event):
    if oval:
        c.delete(oval)
        c.create_text(80, 50, text='Овал')
    if oval1:
        c.delete(oval1)
        c.create_oval(30,10,130,80, fill='orange')

def rect_func(event):
    if tril:
        c.delete(tril)
        c.create_text(230, 50, text='Прямогульник')
    if tril1:
        c.delete(tril1)
        c.create_rectangle(180,10,280,80,fill='lightgreen')  

def triangle(event):
    if trian:
        c.delete(trian)
        c.create_text(380, 50, text='Треуг')
    if trian1:
        c.delete(trian1)
        c.create_polygon(330,80,380,10,430,80,fill='white',outline='black')

#def oval_func(event):
    #c.delete(oval)
    #c.create_text(80, 50, text='Овал')

#def oval1_func(event):
   # c.delete(oval1)
   # c.create_oval(30,10,130,80, fill='orange')

#def rect_func(event):
    #c.delete(tril)
    #c.create_text(230, 50, text='Прямогульник')

#def rect1_func(event):
   # c.delete(tril1)
  #  c.create_rectangle(180,10,280,80,fill='lightgreen')

#def triangle(event):
   # c.delete(trian)
   # c.create_text(380, 50, text='Треугольник')

#def triangle1(event):
   # c.delete(trian1)
   # c.create_polygon(330, 80,380,10,430,80,fill='white',outline='black')
   
c = Canvas(width=460, height=100, bg='grey')
c.pack()

oval1 = c.create_text(80, 50, text='Овал')
tril1 = c.create_text(230, 50, text='Прямогульник')
trian1 = c.create_text(380, 50, text='Треуг')

oval = c.create_oval(30,10,130,80, fill='orange')
tril = c.create_rectangle(180,10,280,80,fill='lightgreen')
trian = c.create_polygon(330,80,380,10,430,80,fill='white',outline='black')

c.tag_bind(oval,'<Button-1>', oval_func)
c.tag_bind(tril,  '<Button-1>', rect_func)
c.tag_bind(trian, '<Button-1>', triangle)

root.mainloop()