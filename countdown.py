#!/usr/bin/env python3
from datetime import datetime
from time import sleep


countdown_year = input('what year are you counting down to?')
cheat = False
cheat2 = False
while True:
        current_time = datetime.now()
        if int(current_time.strftime('%Y')) > int(countdown_year):
            cheat = True
            break
        if int(current_time.strftime('%Y')) == int(countdown_year):
            cheat2 = True
            break
        if current_time.strftime('%Y') == countdown_year: break
        month = current_time.strftime('%B')
        day = current_time.strftime('%d')
        other_time = current_time.strftime('%X')
        print('\n'*10)
        print(f'The year is still {current_time.strftime("%Y")}, the month is {month}, the day number is {day}, and the time is {other_time}')
        sleep(1)
if cheat2:print('Why are you counting down to a year that you already live in?')
elif cheat:print('That year has already passed!')
else:print('Happy New Year!🥳')