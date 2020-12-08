from tkinter import *

def os_command_mainframe():
    OPTIONS = ['help', 'browser', 'number guessing game', 'calculator', 'quit harsha os', 'word guessing game', 'tic-tac-toe', 'rock-paper-scissors', 'base converter', 'titanic game']
    master = Tk()

    variable = StringVar(master)
    variable.set(OPTIONS[0]) # default value

    w = OptionMenu(master, variable, *OPTIONS)
    w.pack()


    def ok():
        to_do = variable.get()


    button = Button(master, text="OK", command=ok)
    button.pack()


    mainloop()



#os_command_mainframe()
