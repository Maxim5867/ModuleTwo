from tkinter import *
root = Tk()
def left(e):
 x = -20
 y = 0
 c.move(ball, x, y)

def right(e):
 x = 20
 y = 0
 c.move(ball, x, y)

def up(e):
 x = 0
 y = -20
 c.move(ball, x, y)

def down(e):
 x = 0
 y = 20
 c.move(ball, x, y)

# Bind the move function
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

c = Canvas(width=400,height=400,bg='white')
c.pack()
ball = c.create_oval(10,10,30,30, fill='green', outline='black')

root.mainloop()
