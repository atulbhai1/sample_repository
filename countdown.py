from datetime import datetime
from time import sleep


countdown_year = input('what year are you counting down to?')
while True:
        current_time = datetime.now()
        if current_time.strftime('%Y') == countdown_year: break
        month = current_time.strftime('%B')
        day = current_time.strftime('%d')
        other_time = current_time.strftime('%X')
        print(f'The year is still {int(countdown_year) - 1}, the month is {month}, the day number is {day}, and the time is {other_time}')
        sleep(1)
print('Happy New Year!🥳')