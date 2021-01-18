import time, tkinter
hours = int(input('How many Hours?'))
minutes = int(input('How many Minutes?'))
seconds = int(input('How many Seconds?'))
seconds += minutes*60 + hours*3600
start = time.time()
keep_counting = True
while keep_counting:
    time.sleep(1)
    current_time = time.time()
    if current_time - start >= seconds:
        keep_counting = False
    print(current_time-start)
window = tkinter.Tk()
tkinter.Label(window, text='YOUR TIMER IS OVER!').pack()
tkinter.Button(window, text='OK', command=lambda : window.destroy()).pack()
window.mainloop()