from tkinter import *
from tkinter import colorchooser
from random import randint
window = Tk()
label = Label(master=window, text='PRESS THE BUTTON TO CHANGE THE COLOR')
label.pack()
def converter(rgb):
    return '%02x%02x%02x' % rgb
def ok():
    label.config(fg=colorchooser.askcolor()[1], bg=colorchooser.askcolor()[1])
    label.update()
    button.config(fg=colorchooser.askcolor()[1])
    button.update()
    button2.config(fg=colorchooser.askcolor()[1])
    button2.update()
    window.config(bg=colorchooser.askcolor()[1])
    window.update()
button = Button(master=window, text='PRESS ME', command=ok)
button.pack()
button2 = Button(master=window, text='CLOSE', command=window.destroy)
button2.pack()
window.geometry('350x300')
window.mainloop()

