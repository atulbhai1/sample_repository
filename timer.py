import sys
from tkinter import *
from tkinter.messagebox import showinfo
t = 0
timer_on = True
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)
def set_timer():
    global t
    t = int(e1.get()) * 3600 + int(e2.get()) * 60 + int(e3.get())
    return t
def countdown():
    global t
    if t > 0:
        l1.config(text=convert(t))
        if timer_on:
            t = t-1
        l1.after(1000, countdown)
    elif t == 0:
        l1.config(text='Set Timer')
        showinfo(message='Your Timer Is Over')
def clear():
    global t
    t = 0
def pauseUnpause():
    global timer_on
    timer_on = not timer_on
    if timer_on:
        button4.config(text='Pause')
    else:
        button4.config(text='Unpause')
window = Tk()
window.title("Timer")
l1 = Label(window, font='times 20', text= 'Set Timer')
l1.grid(row=1, column=2)
Label(window, text='Hours:').grid(row=3, column=1)
e1 = Entry(window)
e1.insert(0, '0')
e1.grid(row=3, column=2)
Label(window, text='Minutes:').grid(row=4, column=1)
e2 = Entry(window)
e2.insert(0, '0')
e2.grid(row=4, column=2)
Label(window, text='Seconds:').grid(row=5, column=1)
e3 = Entry(window)
e3.insert(0, '0')
e3.grid(row=5, column=2)
button1 = Button(window, text='Set', width=21, command=set_timer, bd=2)
button1.grid(row=6, column=2, padx = 21, pady=5)
button2 = Button(window, text='Start', width=21, command=countdown, bd=2)
button2.grid(row=7, column=2, padx=21)
button3 = Button(window, text='Clear', width=21, command=clear, bd=2)
button3.grid(row=8, column=2, padx=21)
button4 = Button(window, text='Pause', width=21, command=pauseUnpause, bd=2)
button4.grid(row=9, column=2, padx=21)
window.mainloop()