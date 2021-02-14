from tkinter import *
from random import randint
from math import sqrt
score = 0
for i in range(20):
    window = Tk()
    a = randint(0, 1000)
    while [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 841, 900, 961].count(a) == 0:
        a = randint(0, 1000)
    Label(window, text=f'√{a} = ?').pack()
    entry = Entry(window)
    entry.pack()
    def check():
        global score
        if int(entry.get()) == sqrt(a):
            score += 1
        window.destroy()
    Button(window, text='Check', command=check).pack()
    window.mainloop()
score = f' You got {score} out of 20'
window = Tk()
Label(window, text=score).pack()
Button(window, text='Close', command=window.destroy).pack()
window.mainloop()
