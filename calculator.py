from tkinter import *

root = Tk()

fr = Frame(root)
fr_but = Frame(root)
fr1 = Frame(root)

new_vvod = True
chislo = 0

def pr_nt(set):
    global new_vvod
    global chislo
    znak = '/ x - + = C'.split()
    if set in range(znak):
        chislo = ent.get()
        ent.delete()
    else:
        ent.insert(END,set)




    
ent= Entry(fr,width=15,justify=CENTER)
lab1 = Label(fr1,width=15)
b = Button(fr_but,width=1,height=1,text='1')
b1 = Button(fr_but,width=1,height=1,text='2')
b2 = Button(fr_but,width=1,height=1,text='3')
b3 = Button(fr_but,width=1,height=1,text='4')
b4 = Button(fr_but,width=1,height=1,text='5')
b5 = Button(fr_but,width=1,height=1,text='6')
b6 = Button(fr_but,width=1,height=1,text='7')
b7 = Button(fr_but,width=1,height=1,text='8')
b8 = Button(fr_but,width=1,height=1,text='9')
b9 = Button(fr_but,width=1,height=1,text='0')
b10 = Button(fr_but,width=1,height=1,text='/')
b11 = Button(fr_but,width=1,height=1,text='x')
b12 = Button(fr_but,width=1,height=1,text='-')
b13 = Button(fr_but,width=1,height=1,text='+')
b14 = Button(fr_but,width=1,height=1,text='=')
b15 = Button(fr_but,width=1,height=1,text='C')


b.bind('<Button-1>', lambda event: pr_nt(1))
b1.bind('<Button-1>', lambda event: pr_nt(2))
b2.bind('<Button-1>', lambda event: pr_nt(3))
b3.bind('<Button-1>', lambda event: pr_nt(4))
b4.bind('<Button-1>', lambda event: pr_nt(5))
b5.bind('<Button-1>', lambda event: pr_nt(6))
b6.bind('<Button-1>', lambda event: pr_nt(7))
b7.bind('<Button-1>', lambda event: pr_nt(8))
b8.bind('<Button-1>', lambda event: pr_nt(9))
b9.bind('<Button-1>', lambda event: pr_nt(0))
b10.bind('<Button-1>', lambda event: pr_nt('/'))
b11.bind('<Button-1>', lambda event: pr_nt('x'))
b12.bind('<Button-1>', lambda event: pr_nt('-'))
b13.bind('<Button-1>', lambda event: pr_nt('+'))
b14.bind('<Button-1>', lambda event: pr_nt('='))
b15.bind('<Button-1>', lambda event: pr_nt('C'))


fr.pack()
ent.pack()
fr_but.pack()
b6.grid(row=0,column=0)
b7.grid(row=0,column=1)
b8.grid(row=0,column=2)
b3.grid(row=1,column=0)
b4.grid(row=1,column=1)
b5.grid(row=1,column=2)
b.grid(row=2,column=0)
b1.grid(row=2,column=1)
b2.grid(row=2,column=2)
b9.grid(row=3,column=1)
b10.grid(row=0,column=3)
b11.grid(row=1,column=3)
b12.grid(row=2,column=3)
b13.grid(row=3,column=3)
b14.grid(row=3,column=2)
b15.grid(row=3,column=0)
fr1.pack()
lab1.pack()

root.mainloop()
