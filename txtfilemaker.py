from tkinter import *
from tkinter.filedialog import asksaveasfilename
window = Tk()
text_editor = Text(window, width=68, height=20, fg='black', font=(('Times'), 15), wrap=WORD)
text_editor.grid(row=0, column=0)
text_editor.insert(INSERT, 'Enter The Text')
def save():
    result = text_editor.get(1.0, END)
    with open(asksaveasfilename(), 'w') as file:
        file.write(result)
Button(window, text='Save', width=50, height=1, command=save).grid(row=55, column=0)
window.geometry('560x390')
window.mainloop()