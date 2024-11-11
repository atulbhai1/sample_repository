#Let the user make a journal entry based off a random prompt

from tkinter import *
from config import *
from random import choice
import time

prompts = ["Write about your pet", "Write about your week", "Write a short story", "Write a haiku about your day", "Write about your happiest moment"]


data = ""
def run():
    global prompts, data
    window = Tk()
    window.maxsize(size[0], size[1])
    window.minsize(size[0], size[1])
    window.title(name)
    window.config(bg=bg_color)
    #First label
    c = choice(prompts)
    prompt = f"{c}\n(This is saved in your files)"
    Label(window, text=prompt, font=font, bg=label_bg).place(relx=0.5, rely=0.034, anchor=CENTER)

    #Text Box
    t = Text(window, height=30, width=40)
    t.place(x=5, y=50)

    #Close Button

    def save():
        global data
        data = str(t.get("1.0", "end"))
        window.destroy()

    Button(window, text="Save and Exit", command=save, font=font, height=6, width=28).place(x=5, y=460)
    window.mainloop()

    file_path = f"/Users/srinivasansrinivasan/PycharmProjects/sample_repository/CarolinaCommonsApp/JournalEntries/{c}{time.strftime('%m-%d-%Y-%H:%M:%S-%Z')}.txt"

    print(data)
    file = open(file_path, "w")
    print(file)
    file.write(data)
    #print(file.read())
    file.close()

if __name__ == '__main__':
    run()

