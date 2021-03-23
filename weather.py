import requests
from tkinter import *
key = 'c973e051a52d4f1122c7a0f9eff64fe4'
city = None
window = Tk()
Label(window, text='City:').grid(row=0, column=0, sticky=W)
cityInput = Entry(window)
cityInput.grid(row=0, column=1)
def ok():
    global city
    city = cityInput.get()
    window.destroy()
Button(window, text='OK', command=ok).grid(row=1, column=1, sticky=W+E)
window.mainloop()
url = f'http://api.openweathermap.org/data/2.5/weather?appid={key}&q={city}'
response = requests.get(url)
x = response.json()
window = Tk()
if x['cod'] != '404':
        y = x['main']
        temp = y['temp']
        temp = int((1.8 * (temp - 273)) + 32)
        feelslike = y['feels_like']
        feelslike = int((1.8 * (feelslike - 273)) + 32)
        maximum = y['temp_max']
        maximum = int((1.8 * (maximum - 273)) + 32)
        minimum = y['temp_min']
        minimum = int((1.8 * (minimum - 273)) + 32)
        humidity = y['humidity']
        z = x['weather']
        description = z[0]['description']
else:
    temp = 'Unavailable'
    feelslike = 'Unavailable'
    maximum = 'Unavailable'
    minimum = 'Unavailable'
    humidity = 'Unavailable'
    description = 'Unavailable'
def reload():
    response = requests.get(url)
    x = response.json()
    if x['cod'] != '404':
        y = x['main']
        temp = y['temp']
        temp = int((1.8 * (temp - 273)) + 32)
        feelslike = y['feels_like']
        feelslike = int((1.8 * (feelslike - 273)) + 32)
        maximum = y['temp_max']
        maximum = int((1.8 * (maximum - 273)) + 32)
        minimum = y['temp_min']
        minimum = int((1.8 * (minimum - 273)) + 32)
        humidity = y['humidity']
        z = x['weather']
        description = z[0]['description']
    else:
        temp = 'Unavailable'
        feelslike = 'Unavailable'
        maximum = 'Unavailable'
        minimum = 'Unavailable'
        humidity = 'Unavailable'
        description = 'Unavailable'
    des.config(text=f'Description: {description}')
    des.update()
    tem.config(text=f'Temperature: {temp}℉')
    tem.update()
    f.config(text=f'Feels Like: {feelslike}℉')
    f.update()
    h.config(text=f'High Today: {maximum}℉')
    h.update()
    l.config(text=f'Low Today: {minimum}℉')
    l.update()
    hu.config(text=f'Humidity: {humidity}%')
    hu.update()
def close():
    window.destroy()
des = Label(window, text=f'Description: {description}')
des.grid(row=0, column=0)
tem = Label(window, text=f'Temperature: {temp}℉')
tem.grid(row=1, column=0)
f = Label(window, text=f'Feels Like: {feelslike}℉')
f.grid(row=2, column=0)
h = Label(window, text=f'High Today: {maximum}℉')
h.grid(row=3, column=0)
l = Label(window, text=f'Low Today: {minimum}℉')
l.grid(row=4, column=0)
hu = Label(window, text=f'Humidity: {humidity}%')
hu.grid(row=5, column=0)
Button(window, text='Refresh', command=reload).grid(row=6, column=0, sticky=W)
Button(window, text='Close', command=close).grid(row=6, column=0, sticky=E)
window.mainloop()
