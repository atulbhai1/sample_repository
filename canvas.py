from tkinter import *
currentX, currentY = 0, 0
mode1 = False
cl = 'black'
def locateXY(event):
    global currentX, currentY
    currentX, currentY = event.x, event.y
def addLine(event):
    global currentX, currentY
    canvas.create_line((currentX, currentY, event.x, event.y), fill=cl)
    if not mode1:
        currentX, currentY = event.x, event.y
def show_color(color):
    global cl
    cl = color
def swap(event):
    global mode1
    mode1 = not mode1
window = Tk()
window.geometry('500x500')
window.attributes('-fullscreen', True)
window.title("Paint")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
canvas = Canvas(window)
canvas.grid(row=0, column=0, sticky='nsew')
canvas.bind('<Button-1>', locateXY)
canvas.bind('<B1-Motion>', addLine)
canvas.tag_bind(canvas.create_rectangle((10, 10, 30, 30), fill='black'), "<Button-1>", lambda x: show_color("black"))
canvas.tag_bind(canvas.create_rectangle((10, 40, 30, 60), fill='grey'), '<Button-1>', lambda x : show_color('grey'))
canvas.tag_bind(canvas.create_rectangle((10, 70, 30, 90), fill='brown4'), '<Button-1>', lambda x : show_color('brown4'))
canvas.tag_bind(canvas.create_rectangle((10, 100, 30, 120), fill='red'), '<Button-1>', lambda x : show_color('red'))
canvas.tag_bind(canvas.create_rectangle((10, 130, 30, 150), fill='orange'), '<Button-1>', lambda x : show_color('orange'))
canvas.tag_bind(canvas.create_rectangle((10, 160, 30, 180), fill='yellow'), '<Button-1>', lambda x : show_color('yellow'))
canvas.tag_bind(canvas.create_rectangle((10, 190, 30, 210), fill='green'), '<Button-1>', lambda x : show_color('green'))
canvas.tag_bind(canvas.create_rectangle((10, 220, 30, 240), fill='blue'), '<Button-1>', lambda x : show_color('blue'))
canvas.tag_bind(canvas.create_rectangle((10, 250, 30, 270), fill='purple'), '<Button-1>', lambda x : show_color('purple'))
canvas.tag_bind(canvas.create_text(1300,10,fill="black",font="Times 20 italic bold",
                        text="Swap Modes"), '<Button-1>', swap)
window.mainloop()