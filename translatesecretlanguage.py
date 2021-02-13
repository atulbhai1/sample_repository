from helpful_stuff.functions import encoder
from tkinter import *
window = Tk()
lbl = Label(window, text='You Have not translated anything yet!')
lbl.grid(row=0, column=0)
entry = Entry(window)
entry.grid(row=1, column=0)
def ok():
    lbl.config(text=encoder(entry.get()))
    lbl.update()
Button(window, text='Translate', command=ok).grid(row=2, column=0, sticky=W)
Button(window, text='Close', command=window.destroy).grid(row=2, column=0, sticky=E)
window.mainloop()