from tkinter import *
window = Tk()
lbl = Label(window, text='THE PRICE OF THE ITEM INCLUDING TAX IS 0 DOLLARS!')
lbl.grid(row=0, column=0)
Label(window, text='YOUR STATE\'S TAX RATE IN PERCENT:').grid(row=1, column=0, sticky=W)
taxEntry = Entry(window)
taxEntry.insert(0, '0')
taxEntry.grid(row=1, column=1)
Label(window, text='THE COST OF THE ITEM YOU WANT TO GET(BEFORE TAX):').grid(row=2, column=0, sticky=W)
priceEntry = Entry(window)
priceEntry.insert(0, '0')
priceEntry.grid(row=2, column=1)
def ok():
    rate = float(taxEntry.get())
    rate += 100
    price = float(priceEntry.get())
    rate = rate/100
    total = price * rate
    lbl.config(text=f'THE PRICE OF THE ITEM INCLUDING TAX IS {total} DOLLARS!')
    lbl.update()
Button(window, text='REFRESH', command=ok).grid(row=3, column=0, columnspan=2)
Button(window, text='CLOSE', command=window.destroy).grid(row=4, column=0, columnspan=2)
window.mainloop()