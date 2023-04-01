from tkinter import *

root = Tk()

fr = Frame(root)
fr_but = Frame(root)
fr1 = Frame(root)

def click(item):
    global number
    number = number + str(item)
    text.set(number)

def delete(): 
    global number
    number = "" 
    text.set("")
 
def ravno():
    global number
    result = str(eval(number)) 
    text.set(result)
    number = ""
 
number = ""

text = StringVar()

#def pr_nt(set):
   # ent.insert(END,set)

#def stir():
    #ent.delete(0,END)

fr.pack()
ent = Entry(fr, text = '0', width=20, textvariable=text, justify=CENTER).pack()
fr_but.pack()
b = Button(fr_but,width=3,height=1,text = '1', command = lambda: click(1)).grid(row=2,column=0)
b1 = Button(fr_but,width=3,height=1,text = '2', command = lambda: click(2)).grid(row=2,column=1)
b2 = Button(fr_but,width=3,height=1,text = '3', command = lambda: click(3)).grid(row=2,column=2)
b3 = Button(fr_but,width=3,height=1,text = '4', command = lambda: click(4)).grid(row=1,column=0)
b4 = Button(fr_but,width=3,height=1,text = '5', command = lambda: click(5)).grid(row=1,column=1)
b5 = Button(fr_but,width=3,height=1,text = '6', command = lambda: click(6)).grid(row=1,column=2)
b6 = Button(fr_but,width=3,height=1,text = '7', command = lambda: click(7)).grid(row=0,column=0)
b7 = Button(fr_but,width=3,height=1,text = '8', command = lambda: click(8)).grid(row=0,column=1)
b8 = Button(fr_but,width=3,height=1,text = '9', command = lambda: click(9)).grid(row=0,column=2)
b9 = Button(fr_but,width=3,height=1,text = '0', command = lambda: click(0)).grid(row=3,column=1)
b10 = Button(fr_but,width=3,height=1,text = "/", command = lambda: click("/")).grid(row=0,column=3)
b11 = Button(fr_but,width=3,height=1,text = "*", command = lambda: click("*")).grid(row=1,column=3)
b12 = Button(fr_but,width=3,height=1,text = "-", command = lambda: click("-")).grid(row=2,column=3)
b13 = Button(fr_but,width=3,height=1,text = "+", command = lambda: click("+")).grid(row=3,column=3)
b14 = Button(fr_but,width=3,height=1,text = "=", command = lambda: ravno()).grid(row=3,column=2)
b15 = Button(fr_but,width=3,height=1,text="C", command = lambda: delete()).grid(row=3,column=0)
fr1.pack()

root.mainloop()
