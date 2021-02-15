import pygal
import helpful_stuff.functions as functions
from tkinter.filedialog import asksaveasfilename
hist = pygal.Bar()
hist.title = functions.get_entry('Title:')
hist.x_title = functions.get_entry('X Axis Label:')
hist.y_title = functions.get_entry('Y Axis Label:')
data = []
labels = []
for i in range(int(functions.get_entry('Num Of Bars:'))):
    labels.append(functions.get_entry(f'Label of Bar #{i + 1}'))
    data.append(float(functions.get_entry(f'Value of Bar #{i + 1}')))
hist.x_labels = labels
hist.add(hist.title.__str__(), data)
if functions.get_dropdown('Download ?:', ['yes', 'no']) == 'yes':
    hist.render_to_file(asksaveasfilename())
hist.render_in_browser()