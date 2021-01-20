from tkinter import *
window = Tk()
window.title('Frames')
frame = Frame(window, height=300, width=300, bg='red').pack()
window.geometry('650x650+450+200')
Button(window, text='Ok', command= lambda :window.destroy()).pack()
resume = True
while resume:
    window.update()
window.mainloop()