import matplotlib.pyplot as plt
import helpful_stuff.functions as functions
squares = []
inputValues = []
for i in range(int(functions.get_entry('Number Of Points:'))):
    inputValues.append(functions.get_entry('Value Name:'))
    squares.append(int(functions.get_entry(f'Value Number {i + 1}:')))
plt.plot(inputValues, squares, linewidth=5)
title = functions.get_entry('Title:')
plt.title(title)
XVal = functions.get_entry('X Label:')
YVal = functions.get_entry('Y Label:')
plt.xlabel(XVal, fontsize=24)
plt.ylabel(YVal, fontsize=24)
plt.tick_params(axis='both', labelsize=14)
plt.show()