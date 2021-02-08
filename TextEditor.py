from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askquestion
from tkinter import ttk
from tkinter.filedialog import askopenfilename
window = Tk()
window.title('My Text Editor')
Label(window, text='Enter the text below').grid(column=0, row=0)
text_editor = Text(window, width=68, height=20, fg='black', font=(('Times'), 15), wrap=WORD)
text_editor.grid(row=1, column=0)
text_editor.insert(INSERT, 'Enter The Text')
scroll = ttk.Scrollbar(window, orient=VERTICAL, command=text_editor.yview)
scroll.grid(row=1, column=1, sticky=N+S)
text_editor.config(yscrollcommand=scroll.set)
def save():
    reply = askquestion('Are You Sure?', 'Are You Sure This Will Create A New File')
    if reply == 'yes':
        result = text_editor.get(1.0, END)
        with open(asksaveasfilename(), 'w') as file:
            file.write(result)
def delete():
    reply = askquestion('Are You Sure?', 'Are You Sure This Will Erase The Text Editor')
    if reply == 'yes':
        text_editor.delete(0.0, END)
def close():
    reply = askquestion('Are You Sure?', 'Are You Sure This Will Close The Window ?')
    if reply == 'yes':
        reply2 = askquestion('Do You Want To Save The File', 'Do You Want To Save?')
        if reply2 == 'yes':
            save()
        window.destroy()
def port():
    cont = askquestion('Are You Sure?', 'Are You Sure This Will Erase The Text Editor')
    if cont == 'yes':
        text_editor.delete(0.0, END)
        with open(askopenfilename(), 'r') as txtFile:
            text_editor.insert(INSERT, txtFile.read())
Button(window, text='Save', command=save).grid(row=55, column=0, sticky=W)
Button(window, text='Clear Text', command=delete).grid(row=55, column=0, sticky=E)
Button(window, text='Close', command=close).grid(row=56, column=0, sticky=W)
Button(window, text='Port from other file', command=port).grid(row=56, column=0, sticky=E)
window.geometry('570x415')
window.mainloop()
