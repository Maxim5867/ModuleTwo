from tkinter import *
window = Tk()
window.title('Первое окно')
window.geometry('800x600')
canvas = Canvas(window,width=800,height=600,background='#c78591')
canvas.create_line(100,100,700,100,width=60,fill='white')
canvas.create_line(100,160,700,160,width=60,fill='blue')
canvas.create_line(100,220,700,220,width=60,fill='red')
canvas.create_rectangle(100,270,700,370,fill = 'red',outline = 'green', width=5)
canvas.create_text(400,320,font='Arial 20', fill='yellow',text = 'Привет,мир')
canvas.create_polygon(100, 450, 150, 505, 125, 560, 75, 560, 50, 505, fill = 'blue')
canvas.pack(expand=True,fill=BOTH)
window.mainloop()

#dash = пунктирные линии#