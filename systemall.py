from os import system
from tkinter import *
say = ''
app = 'Safari'
close_command = f"""osascript -e 'quit app "{app}"'"""
volume = 100
empty_trash = """osascript -e 'tell application "Finder" to empty trash'"""
window = Tk()
Label(window, text='Action: ').grid(row=0, column=0, sticky=W)
action = StringVar()
action.set('Say')
actions = ['Say', 'Open App', 'Close App', 'Change Volume', 'Empty Trash']
OptionMenu(window, action, *actions).grid(row=0, column=1)
Button(window, text='OK', command=window.destroy).grid(row=1, column=0, columnspan=2, sticky=W+E)
window.mainloop()
if action.get() == 'Empty Trash':
    system(empty_trash)
    #
elif action.get() == 'Say':
    window = Tk()
    Label(window, text='To Say: ').grid(row=0, column=0, sticky=W)
    say_entry = Entry(window)
    say_entry.grid(row=0, column=1)
    def ok():
        global say
        say = say_entry.get()
        system(f"say '{say}'")
        window.destroy()
    Button(window, text='OK', command=ok).grid(row=1, column=0, columnspan=2, sticky=W+E)
    window.mainloop()
elif action.get() == 'Change Volume':
    window = Tk()
    Label(window, text='Volume: ').grid(row=0, column=0, sticky=W)
    volume_entry = Entry(window)
    volume_entry.grid(row=0, column=1)
    def ok():
        global volume
        volume = volume_entry.get()
        system(f"osascript -e 'set volume output volume {volume}'")
        window.destroy()
    Button(window, text='OK', command=ok).grid(row=1, column=0, columnspan=2, sticky=W+E)
    window.mainloop()
elif action.get() == 'Open App':
    window = Tk()
    Label(window, text='App: ').grid(row=0, column=0, sticky=W)
    app_entry = Entry(window)
    app_entry.grid(row=0, column=1)
    def ok():
        global app
        app = app_entry.get()
        system(f"""osascript -e' tell application "{app}" to activate'""")
        window.destroy()
    Button(window, text='OK', command=ok).grid(row=1, column=0, sticky=W+E, columnspan=2)
    window.mainloop()
elif action.get() == 'Close App':
    window = Tk()
    Label(window, text='App: ').grid(row=0, column=0, sticky=W)
    app_entry = Entry(window)
    app_entry.grid(row=0, column=1)
    def ok():
        global app
        app = app_entry.get()
        system(f"""osascript -e 'quit app "{app}"'""")
        window.destroy()
    Button(window, text='OK', command=ok).grid(row=1, column=0, sticky=W+E, columnspan=2)
    window.mainloop()