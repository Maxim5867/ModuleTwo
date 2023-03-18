from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def insert_text():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0,s)
    f.close()

def extract_text():
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*html;*.htm"),
                   ("All files", "*_*")))
    try:
        f = open(file_name, 'w')
    except FileNotFoundError:TypeError
    s = text.get(1.0,END)
    f.write(s)
    f.close()

root = Tk()

text = Text(width=50,height=25)
text.grid(columnspan=2)

b1 = Button(text='Открыть', command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text='Сохранить', command=extract_text)
b2.grid(row=1, columnspan=4, sticky=SE)

root.mainloop()