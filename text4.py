from tkinter import *

def change_text():
    text.tag_add('title',SEL_FIRST,SEL_LAST)

root = Tk()

text = Text(width=50,height=10)
text.pack()
text.insert(1.0,'Привет мир!\nвторая строка')
text.tag_config('title',justify=CENTER,font=('Arial',24,'bold'))

Button(text='Изменить текст',command=change_text).pack()




root.mainloop()