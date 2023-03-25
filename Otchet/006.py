from tkinter import *
from decimal import *

root = Tk()

fr = Frame(root)
fr_but = Frame(root)
fr1 = Frame(root)

activeStr = ''
stack = []

def calculate():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop(0))
    operation = stack.pop(0)
    operand1 = Decimal(stack.pop(0))

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    label.configure(text=str(result))

def click(text):
    global activeStr
    global stack
    if text == 'C':
        stack.clear()
        activeStr = ''
        label.configure(text=' ')
    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text=' ') 

#def pr_nt(set):
  #ent.insert(END,set)
#def stir():
    #ent.delete(0,END)
#def ravno():
    #value = ent.get()
    #ent.insert(0,eval(value))
 
label = Label(fr,text = ' ',width=15,justify=CENTER)
b = Button(fr_but,width=1,height=1,text='1',command=lambda text='1':click(text))
b1 = Button(fr_but,width=1,height=1,text='2',command=lambda text='2':click(text))
b2 = Button(fr_but,width=1,height=1,text='3',command=lambda text='3':click(text))
b3 = Button(fr_but,width=1,height=1,text='4',command=lambda text='4':click(text))
b4 = Button(fr_but,width=1,height=1,text='5',command=lambda text='5':click(text))
b5 = Button(fr_but,width=1,height=1,text='6',command=lambda text='6':click(text))
b6 = Button(fr_but,width=1,height=1,text='7',command=lambda text='7':click(text))
b7 = Button(fr_but,width=1,height=1,text='8',command=lambda text='8':click(text))
b8 = Button(fr_but,width=1,height=1,text='9',command=lambda text='9':click(text))
b9 = Button(fr_but,width=1,height=1,text='0',command=lambda text='0':click(text))
b10 = Button(fr_but,width=1,height=1,text='/',command=calculate)
b11 = Button(fr_but,width=1,height=1,text='*',command=calculate)
b12 = Button(fr_but,width=1,height=1,text='-',command=calculate)
b13 = Button(fr_but,width=1,height=1,text='+',command=calculate)
b14 = Button(fr_but,width=1,height=1,text='=',command=calculate)
b15 = Button(fr_but,width=1,height=1,text='C',command=calculate)

fr.pack()
label.pack()
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


root.mainloop()