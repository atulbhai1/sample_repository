from tkinter import *
window = Tk()
lbl = Label(window, text='You have 0.00 dollars!')
lbl.grid(row=0, column=0)
Label(window, text='NUM OF DOLLARS:').grid(row=1, column=0, sticky=W)
dollarEntry = Entry(window)
dollarEntry.insert(0, '0')
dollarEntry.grid(row=1, column=1)
Label(window, text='NUM OF HALF DOLLARS:').grid(row=2, column=0, sticky=W)
halfDollarEntry = Entry(window)
halfDollarEntry.insert(0, '0')
halfDollarEntry.grid(row=2, column=1)
Label(window, text='NUM OF QUARTERS:').grid(row=3, column=0, sticky=W)
quarterEntry = Entry(window)
quarterEntry.insert(0, '0')
quarterEntry.grid(row=3, column=1)
Label(window, text='NUM OF DIMES:').grid(row=4, column=0, sticky=W)
dimeEntry = Entry(window)
dimeEntry.insert(0, '0')
dimeEntry.grid(row=4, column=1)
Label(window, text='NUM OF NICKELS:').grid(row=5, column=0, sticky=W)
nickelEntry = Entry(window)
nickelEntry.insert(0, '0')
nickelEntry.grid(row=5, column=1)
Label(window, text='NUM OF PENNIES:').grid(row=6, column=0, sticky=W)
pennyEntry = Entry(window)
pennyEntry.insert(0, '0')
pennyEntry.grid(row=6, column=1)
def ok():
    try:
        dollar = int(dollarEntry.get())
        halfDollar = int(halfDollarEntry.get())
        halfDollar *= 0.5
        quarter = int(quarterEntry.get())
        quarter *= 0.25
        dime = int(dimeEntry.get())
        dime *= 0.10
        nickel = int(nickelEntry.get())
        nickel *= 0.05
        penny = int(pennyEntry.get())
        penny /= 100
        total = dollar + halfDollar + quarter + dime + nickel + penny
        lbl.config(text=f'You have {total} dollars!')
    except:
        lbl.config(text='ERROR OCCURRED')
    lbl.update()
Button(window, text='RELOAD', command=ok).grid(row=7, column=0, columnspan=2)
Button(window, text='CLOSE', command=window.destroy).grid(row=8, column=0, columnspan=2)
window.mainloop()