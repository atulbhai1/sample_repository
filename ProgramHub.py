import os
from tkinter import *
options = []
for root, dirs, files in os.walk('/Users/srinivasansrinivasan/PycharmProjects/sample_repository'):
    for file in files:
        if file.endswith('.py'):
            options.append(file)
options.pop(), options.pop(), options.pop(), options.remove('Server.py'), options.remove('Client.py'), options.remove('ProgramHub.py'), options.remove('__init__.py'), options.remove('functions.py'), options.remove('classes.py')
option = ''
options.append('close')
def get_dropdown(prompt, possibleOptions=[''], name='tk', button='OK'):
    window = Tk()
    window.title(name)
    Label(window, text=prompt).grid(row=0, column=0, sticky=W)
    answer = StringVar()
    answer.set(possibleOptions[0])
    answers = list(possibleOptions)
    OptionMenu(window, answer, *answers).grid(row=0, column=1)
    Button(window, text=button, command=window.destroy).grid(row=1, column=0, columnspan=2)
    window.mainloop()
    return answer.get()
while option != 'close':
    option = get_dropdown('What do you want to do? :', options, 'Program Hub')
    if option == 'close':continue
    os.system(f'python3 /Users/srinivasansrinivasan/PycharmProjects/sample_repository/{option}')