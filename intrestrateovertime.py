from tkinter import *
window = Tk()
window.title('Interest rate calculator!')
showLabel = Label(window, text='')
showLabel.grid(row=0, column=0)
Label(window, text='Time:').grid(row=1, column=0, sticky=W)
timeEntry = Entry(window)
timeEntry.grid(row=1, column=1)
monthoryearvar = StringVar()
monthoryearvar.set('month(s)')
OptionMenu(window, monthoryearvar, *['month(s)', 'year(s)']).grid(row=1, column=2)
Label(window, text='Starting Amount(in dollars):').grid(row=2, column=0, sticky=W)
startEntry = Entry(window)
startEntry.grid(row=2, column=1)
Label(window, text='Rate:').grid(row=3, column=0, sticky=W)
rateEntry = Entry(window)
rateEntry.grid(row=3, column=1)
def calculate():
    start = float(startEntry.get())
    time = float(timeEntry.get())
    unit = monthoryearvar.get()
    rate = float(rateEntry.get())/100
    if unit == 'year(s)':
        total = start * (1 + rate/(12*time)) ** (12*time*time)
    else:
        total = start * (1 + rate) ** time
    show = f'In {time} {unit} the amount  of {start} dollars would have became {total} dollars.'
    showLabel.config(text=show)
    showLabel.update()
Button(window, text='Calculate', command=calculate).grid(row=4, column=0)
Button(window, text='Close', command=window.destroy).grid(row=4, column=1)
window.mainloop()