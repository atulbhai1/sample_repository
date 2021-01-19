import time, tkinter.messagebox
hours = float(input('How many Hours?'))
minutes = float(input('How many Minutes?'))
seconds = float(input('How many Seconds?'))
seconds += minutes*60 + hours*3600
start = time.time()
keep_counting = True
while keep_counting:
    time.sleep(1)
    current_time = time.time()
    if current_time - start >= seconds:
        keep_counting = False
    print(current_time-start)
tkinter.messagebox.showinfo(title='YOUR TIMER IS OVER!', message='YOUR TIMER IS OVER!')

