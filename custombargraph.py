import pygal, csv
import helpful_stuff.functions as functions
from tkinter.filedialog import asksaveasfilename, askopenfilename
hist = pygal.Bar()
hist.title = functions.get_entry('Title:')
if functions.get_dropdown('PORT FROM .csv FILE ?', ['YES', 'NO']) == 'NO':
    hist.x_title = functions.get_entry('X Axis Label:')
    hist.y_title = functions.get_entry('Y Axis Label:')
    data = []
    labels = []
    for i in range(int(functions.get_entry('Num Of Bars:'))):
        labels.append(functions.get_entry(f'Label of Bar #{i + 1}'))
        data.append(float(functions.get_entry(f'Value of Bar #{i + 1}')))
    hist.x_labels = labels
else:
    filename = askopenfilename()
    point = 0
    for i in range(len(filename)):
        if filename[i] == '.':
            point = i
    filetype = filename[point:]
    l = []
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            l.append(line)
    labels = []
    for i, d in l[1].items():
        labels.append(i)
    hist.x_title = labels[0]
    hist.y_title = labels[1]
    x_values = []
    data = []
    for i in l:
        x_values.append(i[hist.x_title.__str__()])
        data.append(float(i[hist.y_title.__str__()]))
    hist.x_labels = x_values
hist.add(hist.title.__str__(), data)
if functions.get_dropdown('DOWNLOAD ?:', ['YES', 'NO']) == 'YES':
    hist.render_to_file(asksaveasfilename())
hist.render_in_browser()