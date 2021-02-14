from tkinter import *
from random import randint
score = 0
for i in range(20):
    window = Tk()
    a = randint(0, 1000000)
    b = randint(0, 1000000)
    Label(window, text=f'{a} + {b} = ?').pack()
    entry = Entry(window)
    entry.pack()
    def check():
        global score
        if int(entry.get()) == a + b:
            score += 1
        window.destroy()
    Button(window, text='Check', command=check).pack()
    window.mainloop()
score = f' You got {score/20}%'
window = Tk()
Label(window, text=score).pack()
Button(window, text='Close', command=window.destroy).pack()
window.mainloop()