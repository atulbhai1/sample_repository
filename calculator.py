from tkinter import *

equation = ''
txt = ''


def calculator():
    calculator_window = Tk()
    user_sees_txt = StringVar()
    calculator_window.title('Calculator')

    def subtract():
        global equation
        global txt
        equation = equation + '-'
        txt = txt + '-'
        user_sees_txt.set(txt)

    def add():
        global equation
        global txt
        equation = equation + '+'
        txt = txt + '+'
        user_sees_txt.set(txt)

    def multiply():
        global equation
        global txt
        equation = equation + '*'
        txt = txt + '*'
        user_sees_txt.set(txt)

    def divide():
        global equation
        global txt
        equation = equation + '/'
        txt = txt + chr(247)
        user_sees_txt.set(txt)

    def equals():
        global equation
        global txt
        txt = eval(equation)
        user_sees_txt.set(txt)
        txt = ''
        equation = ''

    def backspace():
        global equation
        global txt
        length = len(equation) - 2
        equation = equation[:length]
        txt = txt[:len(txt) - 2]
        user_sees_txt.set(txt)

    def clear():
        global equation
        global txt
        equation = ''
        txt = ''
        user_sees_txt.set(txt)

    def decimal():
        global equation
        global txt
        equation = equation + '.'
        txt = txt + '.'
        user_sees_txt.set(txt)

    def open_parentheses():
        global equation
        global txt
        equation = equation + '('
        txt = txt + '('
        user_sees_txt.set(txt)

    def close_parentheses():
        global equation
        global txt
        equation = equation + ')'
        txt = txt + ')'
        user_sees_txt.set(txt)

    def zero():
        global equation
        global txt
        equation = equation + '0'
        txt = txt + '0'
        user_sees_txt.set(txt)

    def one():
        global equation
        global txt
        equation = equation + '1'
        txt = txt + '1'
        user_sees_txt.set(txt)

    def two():
        global equation
        global txt
        equation = equation + '2'
        txt = txt + '2'
        user_sees_txt.set(txt)

    def three():
        global equation
        global txt
        equation = equation + '3'
        txt = txt + '3'
        user_sees_txt.set(txt)

    def four():
        global equation
        global txt
        equation = equation + '4'
        txt = txt + '4'
        user_sees_txt.set(txt)

    def five():
        global equation
        global txt
        equation = equation + '5'
        txt = txt + '5'
        user_sees_txt.set(txt)

    def six():
        global equation
        global txt
        equation = equation + '6'
        txt = txt + '6'
        user_sees_txt.set(txt)

    def seven():
        global equation
        global txt
        equation = equation + '7'
        txt = txt + '7'
        user_sees_txt.set(txt)

    def eight():
        global equation
        global txt
        equation = equation + '8'
        txt = txt + '8'
        user_sees_txt.set(txt)

    def nine():
        global equation
        global txt
        equation = equation + '9'
        txt = txt + '9'
        user_sees_txt.set(txt)

    user_sees_txt.set('enter the expression')
    expression_field = Entry(calculator_window, textvariable=user_sees_txt)
    expression_field.grid(columnspan=10, ipadx=70)
    button_one = Button(calculator_window, text='   𝟙   ', command=one, height=1, width=7)
    button_one.grid(row=2, column=3)
    button_two = Button(calculator_window, text='   𝟚   ', command=two, height=1, width=7)
    button_two.grid(row=2, column=4)
    button_three = Button(calculator_window, text='   𝟛   ', command=three, height=1, width=7)
    button_three.grid(row=2, column=5)
    button_plus = Button(calculator_window, text='   ₊   ', command=add, height=1, width=7)
    button_plus.grid(row=2, column=6)
    button_four = Button(calculator_window, text='   𝟜   ', command=four, height=1, width=7)
    button_four.grid(row=3, column=3)
    button_five = Button(calculator_window, text='   𝟝   ', command=five, height=1, width=7)
    button_five.grid(row=3, column=4)
    button_six = Button(calculator_window, text='   𝟞   ', command=six, height=1, width=7)
    button_six.grid(row=3, column=5)
    button_minus = Button(calculator_window, text='   ˗   ', command=subtract, height=1, width=7)
    button_minus.grid(row=3, column=6)
    button_seven = Button(calculator_window, text='   𝟟   ', command=seven, height=1, width=7)
    button_seven.grid(row=4, column=3)
    button_eight = Button(calculator_window, text='   𝟠   ', command=eight, height=1, width=7)
    button_eight.grid(row=4, column=4)
    button_nine = Button(calculator_window, text='   𝟡   ', command=nine, height=1, width=7)
    button_nine.grid(row=4, column=5)
    button_multiply = Button(calculator_window, text='   ✖️️️   ', command=multiply, height=1, width=7)
    button_multiply.grid(row=4, column=6)
    button_zero = Button(calculator_window, text='   𝟘   ', command=zero, height=1, width=7)
    button_zero.grid(row=5, column=3)
    button_clear = Button(calculator_window, text='   🆑   ', command=clear, height=1, width=7)
    button_clear.grid(row=5, column=4)
    button_undo = Button(calculator_window, text='   🔙   ', command=backspace, height=1, width=7)
    button_undo.grid(row=5, column=5)
    button_divide = Button(calculator_window, text='   ÷   ', command=divide, height=1, width=7)
    button_divide.grid(row=5, column=6)
    button_dot = Button(calculator_window, text='    ．    ', command=decimal, height=1, width=9)
    button_dot.grid(row=6, column=3)
    button__open_parentheses = Button(calculator_window, text='   ⦅   ', command=open_parentheses, height=1, width=9)
    button__open_parentheses.grid(row=6, column=4)
    button_close_parentheses = Button(calculator_window, text='   ⦆   ', command=close_parentheses, height=1, width=9)
    button_close_parentheses.grid(row=6, column=5)
    button_equal = Button(calculator_window, text='              ₌             ', command=equals, height=1, width=28)
    button_equal.grid(row=7, column=5)
    calculator_window.mainloop()

try:
    calculator()
except TypeError:
    print('ERROR')
