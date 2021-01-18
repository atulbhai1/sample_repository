from tkinter import *
from random import randint
window = Tk()
label = Label(master=window, text='PRESS THE BUTTON TO CHANGE THE COLOR')
label.pack()
def converter(rgb):
    return '%02x%02x%02x' % rgb
def ok(to):
    label.config(fg='#'+converter((randint(0, 255), randint(0, 255), randint(0, 255))), bg='#'+converter((randint(0, 255), randint(0, 255), randint(0, 255))))
    label.update()
    to.config(fg='#'+converter((randint(0, 255), randint(0, 255), randint(0, 255))), bg='#'+converter((randint(0, 255), randint(0, 255), randint(0, 255))))
    to.update()
    window.config(bg='#'+converter((randint(0, 255), randint(0, 255), randint(0, 255))))
    window.update()
button = Button(master=window, text='PRESS ME', command=lambda : ok(button))
button.pack()
window.geometry('350x300')
window.mainloop()

