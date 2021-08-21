#!/usr/bin/env python3
import random
from tkinter.messagebox import showinfo
special = '!@#$%^&*()_+-={[]}|\\:"\',<.>?/'
alpha = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
num = '123456789'
num_special = random.randint(2, 5)
num_alpha = random.randint(3, 9)
num_num = random.randint(3, 9)
password = ''
for i in range(num_num):
    num_choice = random.randint(0, len(num) - 1)
    password = password + num[num_choice]
for i in range(num_alpha):
    alpha_special = random.randint(0, len(alpha) - 1)
    password = password + alpha[alpha_special]
for i in range(num_special):
    special_special = random.randint(0, len(special) - 1)
    password = password + special[special_special]
showinfo(f'Your password is : {password}', f'Your password is : {password}')

