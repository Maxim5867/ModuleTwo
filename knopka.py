from tkinter import *
from tkinter import ttk

click = 0
window = Tk()
window.title('Кнопка')
window.geometry('800x600')
canvas = Canvas(window,width=800,height=600,background='green')
def click_button():
    global click
    click +=1
    canvas["background"] = 'black'
    window.update_idletasks()
    btn["text"] = f"Нажатие {click}"
    if click==1:
        btn["text"] = f"1"
        canvas["background"] = 'red'
    elif click==2:
        btn["text"] = f"2"
        canvas["background"] = 'yellow'
    elif click==3:
        btn["text"] = f"3"
        canvas["background"] = 'blue'
    elif click==4:
        btn["text"] = f"4"
        canvas["background"] = 'purple'
    else:
        btn["text"] = f"Всё"
        canvas["background"] = 'white'
        btn["state"] = [DISABLED]
    




btn = ttk.Button(window,text="Нажми меня", command=click_button)
btn.pack()
canvas.pack()


window.mainloop()

