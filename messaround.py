from tkinter import *
from tkinter import ttk
window = Tk()
pw = ttk.Panedwindow(window, orient=HORIZONTAL)
pw.pack(fill=BOTH, expand=True)
for i in range(100):
    pw.add(ttk.Frame(pw, width=1, height=500, relief=SUNKEN), weight=100)
ttk.Button(window, text='Close', command=window.destroy).pack()
window.title('Mess Around')
window.geometry(str(f'{window.winfo_screenwidth()}x{window.winfo_screenheight()}'))
window.mainloop()