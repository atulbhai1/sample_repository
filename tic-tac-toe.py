from tkinter import *
from tkinter.messagebox import showinfo
window = Tk()
grid = [["-", '-', '-'],
        ["-", '-', '-'],
        ["-", '-', '-']]
turn = "O"
def find_lines_of_3():
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2]:
            winner = grid[i][0]
            return [True, winner]
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i]:
            winner = grid[1][i]
            return [True, winner]
    if grid[1][1] == grid[0][0] == grid[2][2]:
        winner = grid[0][0]
        return [True, winner]
    if grid[1][1] == grid[0][2] == grid[2][0]:
        winner = grid[0][2]
        return [True, winner]
def clicked(pos=[0, 0]):
    global turn
    global grid
    button = buttons[pos[0]][pos[1]]
    if button.cget('text') == "-":
        buttons[pos[0]][pos[1]].config(text=turn)
        grid[pos[0]][pos[1]] = turn
        if turn == "O":
            turn = "X"
        else:
            turn = "O"
        s = find_lines_of_3()
        if s[0] and s[1] != "-":
            showinfo("We Have A Winner", f'{s[1]} Won!')
    else:
        showinfo('There Was A Mistake', "You Selected A Box That Was Already Chosen!")
buttons = []
button1 = Button(window, command=lambda: clicked([0, 0]), height=10, width=20, text=grid[0][0])
button1.grid(row=0, column=0)
button2 = Button(window, command=lambda: clicked([0, 1]), height=10, width=20, text=grid[0][1])
button2.grid(row=0, column=1)
button3 = Button(window, command=lambda: clicked([0, 2]), height=10, width=20, text=grid[0][2])
button3.grid(row=0, column=2)
buttons.append([button1, button2, button3])
button4 = Button(window, command=lambda: clicked([1, 0]), height=10, width=20, text=grid[1][0])
button4.grid(row=1, column=0)
button5 = Button(window, command=lambda: clicked([1, 1]), height=10, width=20, text=grid[1][1])
button5.grid(row=1, column=1)
button6 = Button(window, command=lambda: clicked([1, 2]), height=10, width=20, text=grid[1][2])
button6.grid(row=1, column=2)
buttons.append([button4, button5, button6])
button7 = Button(window, command=lambda: clicked([2, 0]), height=10, width=20, text=grid[2][0])
button7.grid(row=2, column=0)
button8 = Button(window, command=lambda: clicked([2, 1]), height=10, width=20, text=grid[2][1])
button8.grid(row=2, column=1)
button9 = Button(window, command=lambda: clicked([2, 2]), height=10, width=20, text=grid[2][2])
button9.grid(row=2, column=2)
buttons.append([button7, button8, button9])
window.mainloop()
