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
frame.pack()

fr1 = Frame()
fr1.pack()

ent = Entry(fr1,width=50)
b = Button(fr1,text='Открыть',width=5,height=2,command=open_file)
b1 = Button(fr1,text='Сохранить',width=5,height=2, command=save_file)

ent.pack()
b.pack(side=TOP)
b1.pack(side=TOP)

fr2 = Frame()
fr2.pack()

text = Text(width=100,height=50)
text.pack()

#fflf
root.mainloop()