from time import *
from tkinter import *


def timer():
    hours = 3600 * int(input('How many hours?'))
    minutes = 60 * int(input('How many minutes?'))
    seconds = int(input('How many seconds?'))
    length = hours + minutes + seconds
    then = time()
    now = time()
    while now - then < length:
        now = time()
    box = Tk()

    def ok():
        box.destroy()
    box.geometry('400x400+0+0')
    box.iconify()
    box.update()
    box.deiconify()
    box.eval('tk::PlaceWindow . center')
    box.config(bg='white')
    message = Label(box, text='Your Timer Is Over!')
    message.pack()
    button = Button(box, text='ok', command=ok, bg='blue')
    button.pack()
    mainloop()


timer()
