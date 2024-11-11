from tkinter import *
from config import *

def run():
    window = Tk()
    window.maxsize(size[0], size[1])
    window.minsize(size[0], size[1])
    window.title(name)
    window.config(bg=bg_color)
    #First label
    Label(window, text="NOT AVAILABLE", font=font, bg=label_bg).place(relx=0.5, rely=0.034, anchor=CENTER)

    #Exit Button
    Button(window, text="Exit", command=window.destroy, font=font, height=6, width=28).place(relx=0.5, rely=0.5, anchor=CENTER)

    window.mainloop()

if __name__ == "__main__":
    run()