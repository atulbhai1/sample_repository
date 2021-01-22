from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askquestion
from tkinter import ttk
window = Tk()
window.title('My Text Editor')
text_editor = Text(window, width=68, height=20, fg='black', font=(('Times'), 15), wrap=WORD)
text_editor.grid(row=0, column=0)
text_editor.insert(INSERT, 'Enter The Text')
scroll = ttk.Scrollbar(window, orient=VERTICAL, command=text_editor.yview)
scroll.grid(row=0, column=1, sticky=N+S)
text_editor.config(yscrollcommand=scroll.set)
def save():
    result = text_editor.get(1.0, END)
    with open(asksaveasfilename(), 'w') as file:
        file.write(result)
def delete():
    reply = askquestion('Are You Sure?', 'Are You Sure')
    if reply == 'yes':
        text_editor.delete(0.0, END)
def close():
    reply = askquestion('Are You Sure?', 'Are You Sure?')
    if reply == 'yes':
        window.destroy()
Button(window, text='Save', command=save).grid(row=55, column=0, sticky=W)
Button(window, text='Clear Text', command=delete).grid(row=55, column=0, sticky=E)
Button(window, text='Close', command=close).grid(row=55, column=0, sticky=N)
window.geometry('570x390')
window.mainloop()