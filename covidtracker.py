#!/usr/bin/env python3
import COVID19Py
from os import system
from time import sleep
covid19sample1 = COVID19Py.COVID19(data_source='jhu')#jhu global, csbs US
covid19sample2 = COVID19Py.COVID19(data_source='csbs')
while True:
    data = covid19sample1.getLatest()
    # noinspection PyTypeChecker
    message = f'''
    Total Confirmed Cases : {data["confirmed"]}
Total Active Cases : {int(data['confirmed']) - int(data['deaths']) - int(data['recovered'])}
Total Number of Cases That Ended : {int(data['deaths']) + int(data['recovered'])}'''
    command = f'osascript -e \'display notification "{message}" with title "Covid Report Global"\''
    system(command)
    sleep(5)
    data = covid19sample2.getLatest()
    # noinspection PyTypeChecker
    message = f'''
Total Confirmed Cases : {data["confirmed"]}
Total Active Cases : {int(data['confirmed']) - int(data['deaths']) - int(data['recovered'])}
Total Number of Cases That Ended : {int(data['deaths']) + int(data['recovered'])}'''
    command = f'osascript -e \'display notification "{message}" with title "Covid Report US"\''
    system(command)
    sleep(600)
