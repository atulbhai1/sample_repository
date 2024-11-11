#Carolina Commons App: Core function: Basic notebook app

from tkinter import *
from config import *
import journal
while True:
    window = Tk()
    window.maxsize(size[0], size[1])
    window.minsize(size[0], size[1])
    window.title(name)
    window.config(bg=bg_color)

    choice = None

    #Make the heading label

    Label(window, text="Welcome to Touchstone.ai\nPlease choose what you want to do", font=font, bg=label_bg).place(x=20, y=0)

    #Make 1st Button
    def journal_prompt_button():
        global choice
        choice = "j"
        window.destroy()
    b = Button(window, text="Answer a \nJournal Prompt", command=journal_prompt_button, height=10, width=10)
    b.place(x=10, y=50)
    b.config(bg=button_bg)

    #Make 2nd Button
    def leave_button():
        global choice
        choice = "l"
        window.destroy()
    b = Button(window, text="Leave Touchstone.ai", command=leave_button, height=10, width=27)
    b.place(x=10, y=300)
    b.config(bg=button_bg)

    window.mainloop()

    if choice == "j":
        journal.run()
    else:
        break

