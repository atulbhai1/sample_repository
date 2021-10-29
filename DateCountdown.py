from datetime import datetime, timedelta
from tkinter import *
from tkcalendar import Calendar
from helpful_stuff.functions import get_dropdown
current_date = None
wanted_date = None
def get_wanted_date():
    global cal
    mydate = get_current_date_for_asking()
    root = Tk()
    root.geometry("400x400")
    root.title('Picking A Day')
    cal = Calendar(root, selectmode='day', year=mydate['year'], month=mydate['month'], day=mydate['day'])
    cal.pack(pady=20)
    def grad_date():
        root.destroy()
        return cal.get_date()
    Button(root, text="I Choose This Date",command=grad_date).pack(pady=20)
    root.mainloop()
def get_current_date_for_asking():
    now = datetime.now()
    return {'year': int(now.strftime('%Y')), 'month':int(now.strftime('%m')), 'day':int(now.strftime('%d'))}
def get_current_date():
    now = datetime.now()
    return now
def get_wanted_date_master():
    get_wanted_date()
    return cal.get_date()
def convert_cal_to_datetime(c, t):
    cal2 = str(c)
    cal3 = cal2.replace('/', '-')
    cal4 = cal3 + f' {t[0]}:{t[1]}:{t[2]}'
    frmt = "%m-%d-%y %H:%M:%S"
    return datetime.strptime(cal4, frmt)
wanted_date = get_wanted_date_master()
wanted_time = [int(get_dropdown('Hour', range(24), 'Choosing The Wanted Hour', 'OK')),int(get_dropdown('Minute', range(60), 'Choosing The Wanted Hour', 'OK')), int(get_dropdown('Second', range(60), 'Choosing The Wanted Hour', 'OK'))]
window = Tk()
timeLeftLabel = Label(window, text='', font=('Arial', 100))
timeLeftLabel.pack()
def KillWindow():
    global goOn
    goOn = False
QuitButton = Button(window, text='Quit', command=KillWindow)
goOn = True
QuitButton.pack()
while goOn:
    window.title(f"Countdown To {wanted_date}")
    wanted_date_datetime = convert_cal_to_datetime(wanted_date, wanted_time)
    current_date = get_current_date()
    distance = wanted_date_datetime - current_date
    timeLeftLabel.config(text=distance)
    timeLeftLabel.update()
    window.update()
else:
    window.destroy()