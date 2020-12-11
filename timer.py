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
        time_left = now - then - length
        if int(time_left) % 3600 == 0:
            print(time_left/3600, 'hours left')
        elif int(time_left) % 60 == 0:
            print(time_left/60, 'minutes left')
        else:
            print(time_left, 'seconds left')
        sleep(.9937)
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
