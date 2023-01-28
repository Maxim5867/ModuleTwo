from tkinter import *
from tkinter import ttk

click = 0

def x():
    print(" ")
def click_button():
    global click
    click +=1
    btn["text"] = f"Нажатие {click}"
    if click==1:
        btn["text"] = f"1"
    elif click==2:
        btn["text"] = f"2"
    elif click==3:
        btn["text"] = f"3"
    elif click==4:
        btn["text"] = f"4"
    else:
        btn["text"] = f"Всё"
        btn["state"] = [DISABLED]

window = Tk()
window.title('Кнопка')
window.geometry('800x600')

btn = ttk.Button(text="Нажми меня", command=click_button)
btn.pack(expand=True)

window.mainloop()

