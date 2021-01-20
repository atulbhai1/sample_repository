import time, tkinter.messagebox, tkinter
hours = 0
minutes = 0
seconds = 0
window = tkinter.Tk()
tkinter.Label(window, text='Hours:').grid(row=0, column=0)
hours_entry = tkinter.Entry(window, width=30)
hours_entry.insert(0, '0')
hours_entry.grid(row=0, column=1)
tkinter.Label(window, text='Minutes:').grid(row=1, column=0)
minutes_entry = tkinter.Entry(window, width=30)
minutes_entry.insert(0, '0')
minutes_entry.grid(row=1, column=1)
tkinter.Label(window, text='Seconds:').grid(row=2, column=0)
seconds_entry = tkinter.Entry(window, width=30)
seconds_entry.insert(0, '0')
seconds_entry.grid(row=2, column=1)
def get():
    global hours, minutes, seconds
    hours = int(hours_entry.get())
    minutes = int(minutes_entry.get())
    seconds = int(seconds_entry.get())
    seconds += minutes*60 + hours*3600
    window.destroy()
tkinter.Button(window, text='Make The Timer', command=get).grid(row=3, column=1)
window.mainloop()
keep_counting = True
if minutes > 59:
    raise ValueError('Minutes can be a maximum of 59.For anything over 59 minutes use hours.')
if seconds > 59:
    raise ValueError('Seconds can be a maximum of 59.For anything over 59 seconds use minutes.')
try:
    window = tkinter.Tk()
    show = tkinter.Label(window, text='')
    show.pack()
    def delete():
        window.destroy()
    tkinter.Button(window, text='Delete', command=delete).pack()
    start = time.time()
    while keep_counting:
            time.sleep(1)
            current_time = time.time()
            if current_time - start >= seconds:
                keep_counting = False
                tkinter.messagebox.showinfo(title='YOUR TIMER IS OVER!', message='YOUR TIMER IS OVER!')
                window.destroy()
                continue
            show.config(text=str(int(seconds - (current_time-start)))+' seconds left')
            show.update()
    window.mainloop()
except:pass