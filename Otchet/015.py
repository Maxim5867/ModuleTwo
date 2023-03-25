from tkinter import *
from decimal import *

root = Tk()

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

activeStr = ''
stack = []

def calculate():
    global stack
    global label
    result = ' '
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

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

label = Label(root, text=' ', width=35)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")

button = Button(root, text='C', command=lambda text='C': click(text))
button.grid(row=1, column=3, sticky="nsew")
for row in range(4):
    for column in range(4):
        button = Button(root, text=buttons[row][column],
                command=lambda row=row, col=column: click(buttons[row][col]))
        button.grid(row=row + 2, column=column, sticky="nsew")

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()                