from tkinter import *

root = Tk()

def open_file():
    if ent.get()!='':
        with open(ent.get(),'r') as f1:
            r_text = f1.read()
            text.delete(1.0,END)
            text.insert(1.0,r_text)

def save_file():
    if ent.get()!='':
        r_text = text.get('1.0', END)
        with open(ent.get(),'w') as f1:
            f1.write(r_text)


frame = Frame()
fr1 = Frame()
fr2 = Frame()
fr3 = Frame()

ent = Entry(fr1,width=75)
b = Button(fr1,text='Открыть',width=23,height=1,command=open_file)
b1 = Button(fr1,text='Сохранить',width=23,height=1, command=save_file)

fr1.pack(side=TOP)
ent.pack(side=LEFT)
b.pack(side=RIGHT)
b1.pack(side=RIGHT)


fr2.pack(side=BOTTOM)
text = Text(fr2,width=100,height=30)
text.pack(side=BOTTOM)

root.mainloop()
