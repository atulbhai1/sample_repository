from tkinter import *
from tkinter.messagebox import *
from helpful_stuff.functions import get_dropdown, get_entry
from random import shuffle
lists = []
lenLists = int(get_entry('How many sets of people/things are there?', 'People/Thing Pairing', 'Continue'))
for i in range(lenLists):
        lis = []
        lenLis = int(get_entry(f'How many people/things are there in group {i + 1} ?', 'People/Thing Pairing', 'Continue'))
        for v in range(lenLis):
            lis.append(get_entry(f'Enter value number {v + 1} in list number {i + 1}:', 'People/Thing Pairing', 'Continue'))
        lists.append(lis)
biggestLen = 0
for myList in lists:
    if len(myList) > biggestLen:
        biggestLen = len(myList)
for myList in lists:
    while len(myList) < biggestLen:
        myList.append('Nobody & Nothing')
sortBy = get_dropdown('How do you want to sort them?', ['Alphabetize', 'Randomize'], 'People/Thing Pairing', 'Continue')
if sortBy == 'Randomize':
    for myList in lists:
        shuffle(myList)
else:
    for myList in lists:
        myList.sort()
newList = []
for x in range(len(lists[0])):
    value = ''
    for y in range(len(lists)):
        value += lists[y][x] + ', '
    newList.append(value)
newStr = ''
for val in newList:
    newStr += val + '&'
showinfo(message=newStr)
