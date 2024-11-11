#Let the user make a journal entry based off a random prompt

from tkinter import *
from config import *
def run():
    window = Tk()
    window.maxsize(size[0], size[1])
    window.minsize(size[0], size[1])
    window.title(name)
    window.config(bg=bg_color)

if __name__ == '__main__':
    run()

