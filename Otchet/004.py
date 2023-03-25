from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def insert_text():
    file_name = fd.askopenfilename()
    try:
        f = open(file_name)
    except:
        mb.showerror("TypeError", "FileNotFoundError")
    else:
        s = f.read()
        text.insert(1.0,s)
        f.close()

def delete_text():
    text.delete(1.0,END)    

def extract_text():
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*html;*.htm"),
                   ("All files", "*_*")))
    try:
        f = open(file_name, 'w')
    except (FileNotFoundError):
        mb.showerror("TypeError","FileNotFoundError")
    else:    
        s = text.get(1.0,END)
        f.write(s)
        f.close()

root = Tk()

text = Text(width=50,height=25)
text.grid(columnspan=2)

b1 = Button(text='Открыть', command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text='Сохранить', command=extract_text)
b2.grid(row=1, columnspan=2, sticky=E)
b3 = Button(text='Очистить', command=delete_text)
b3.grid(row=1, sticky=W)

root.mainloop()
