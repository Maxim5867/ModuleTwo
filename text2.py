from tkinter import *

root = Tk()

text = Text(width=20,height=7,fg='white',background='black',wrap=WORD)
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT,fill=Y)

text.config(yscrollcommand=scroll.set)

root.mainloop()