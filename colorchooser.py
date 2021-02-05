from tkinter.colorchooser import askcolor
from tkinter import *
window = Tk()
color = askcolor()
color_in_hex = color[1]
color_in_RGB = color[0]
def choose_again():
    global color, color_in_RGB, color_in_hex
    color = askcolor()
    color_in_hex = color[1]
    color_in_RGB = color[0]
    rgbLBL.config(text=f'Color In RGB : {color_in_RGB}')
    rgbLBL.update()
    hexLBL.config(text=f'Color In Hex : {color_in_hex}')
    hexLBL.update()
rgbLBL = Label(window, text=f'Color In RGB : {color_in_RGB}')
rgbLBL.pack()
hexLBL = Label(window, text=f'Color In Hex : {color_in_hex}')
hexLBL.pack()
Button(window, text='Choose A Different Color', command=choose_again).pack()
Button(window, text='Close', command=window.destroy).pack()
window.mainloop()
