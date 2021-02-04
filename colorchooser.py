from tkinter.colorchooser import askcolor
from tkinter import *
window = Tk()
color = askcolor()
color_in_hex = color[1]
color_in_RGB = color[0]
Label(window, text=f'Color In RGB : {color_in_RGB}').pack()
Label(window, text=f'Color In Hex : {color_in_hex}').pack()
Button(window, text='Close', command=window.destroy).pack()
window.mainloop()
