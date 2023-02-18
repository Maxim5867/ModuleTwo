from tkinter import *

root = Tk()

#fr_top = LabelFrame(root,text='Первый ряд')
#fr_bot = LabelFrame(root,text='Второй ряд')

l1 = Label(width=7,height=4,bg='yellow',text='1')
l2 = Label(width=7,height=4,bg='orange',text='2')
l3 = Label(width=7,height=4,bg='green',text='3')
l4 = Label(width=7,height=4,bg='blue',text='4')

#fr_top.pack(padx=10,pady=10)
#fr_bot.pack()

l1.place(x=0,y=0)
l2.place(x=60,y=0)
l3.place(x=0,y=70)
l4.place(x=60,y=70)

root.mainloop()