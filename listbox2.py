from tkinter import  *

root = Tk()

fr_1 = Frame()

def sellect1():
    select1 = box.curselection()

    for i in select1:
        box1.insert(END, box.get(i))

    for i in reversed(select1):
        box.delete(i)


def sellect2():
    select2 = box1.curselection()

    for i in select2:
        box.insert(END, box1.get(i))

    for i in reversed(select2):
        box1.delete(i)


    

shop = ['огурец', 'помидор', 'груша', 'банан', 'киви', 'морковь' , 'яблоко','свити','лук','чеснок', 'слива', 'малина','черника']

box  = Listbox(selectmode=EXTENDED,height=10)
box1 = Listbox(selectmode=EXTENDED,height=10)

scroll = Scrollbar(command=box.yview)
scroll.pack(side=LEFT,fill=Y)
box.config(yscrollcommand=scroll.set)

b1  = Button(fr_1,text  = '>>>')
b2  = Button(fr_1,text  =  '<<<')

scroll = Scrollbar(command=box1.yview)
scroll.pack(side=RIGHT,fill=Y)
box1.config(yscrollcommand=scroll.set)

for i in shop:
    box.insert(0,i)

b1.bind('<Button-1>',lambda event:sellect1())
b2.bind('<Button-1>',lambda event:sellect2())

box.pack(side=LEFT)
box1.pack(side=RIGHT)
fr_1.pack(side=LEFT)
b1.pack(fill=X)
b2.pack(fill=X)


root.mainloop()
