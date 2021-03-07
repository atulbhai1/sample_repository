from datetime import datetime
from tkinter import *
window = Tk()
window.title('Clock')
now = datetime.now()
lbl = Label(window, text=f'{now.strftime("%I")}:{now.strftime("%M")}:{now.strftime("%S")} {now.strftime("%p")}', font=('Arial', 200))
lbl.pack()
count = True
def ok():
    global count
    count = False
    window.destroy()
Button(window, text='Close', command=ok).pack()
while count:
    now = datetime.now()
    if count:
        lbl.config(text=f'{now.strftime("%I")}:{now.strftime("%M")}:{now.strftime("%S")} {now.strftime("%p")}')
    if count:
        lbl.update()
    if count:
        window.update()
window.mainloop()
