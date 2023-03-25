from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

root = Tk()

def delete_text():
    text.delete(1.0,END)

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

main = Menu()


root.config(menu=main)

filemenu = Menu(main, tearoff=0)
filemenu.add_command(label='Открыть файл...', command=insert_text)

dopmenu = Menu(main,tearoff=0)
dopmenu.add_command(label='Сохранить файл...',command=extract_text)

chistmenu = Menu(main, tearoff=0)
chistmenu.add_command(label='Очистить файл',command=delete_text)

main.add_cascade(label='Открыть', menu=filemenu)
main.add_cascade(label='Сохранить', menu=dopmenu)
main.add_cascade(label='Очистить', menu=chistmenu)

text = Text(width=50,height=25)
text.grid(columnspan=2)

root.mainloop()