from time import *
from tkinter import *
from webbrowser import open
import tkinter.messagebox
import random
import gc
to_do = 0
user_score = 0
comp_score = 0
equation = ''
txt = ''
def simple_web_browser():
    url = ''
    frame = Tk()
    frame.geometry('400x200')
    frame.iconify()
    frame.update()
    frame.deiconify()
    frame.eval('tk::PlaceWindow . center')
    def get_password():
        global url
        url = input_txt.get(1.0, 'end-1c')
        frame.destroy()
    lbl = Label(frame, text="Enter the URL of the site you want to visit")
    lbl.pack()
    input_txt = Text(frame, height=1, width=20)
    input_txt.pack()
    Buttoncool4 = Button(frame, text="Ok", command=get_password)
    Buttoncool4.pack()
    frame.mainloop()
    open('http://' + url)


def tic_tac_toe():
    def create_button(relx, rely):
        button = Button(width=10, height=2, command=lambda: callback(button))
        button.place(relx=relx, rely=rely)
        return button

    def check_win():
        if (buttons[0]['text'] == buttons[1]['text'] == buttons[2]['text'] != '') or \
                (buttons[3]['text'] == buttons[4]['text'] == buttons[5]['text'] != '') or \
                (buttons[6]['text'] == buttons[7]['text'] == buttons[8]['text'] != '') or \
                (buttons[0]['text'] == buttons[3]['text'] == buttons[6]['text'] != '') or \
                (buttons[1]['text'] == buttons[4]['text'] == buttons[7]['text'] != '') or \
                (buttons[2]['text'] == buttons[5]['text'] == buttons[8]['text'] != '') or \
                (buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] != '') or \
                (buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] != ''):
            return True
        else:
            return False

    def callback(button):
        global turn, x
        if x == 1:
            sleep(1)
            game.quit()
        invalid['text'] = ''
        if button['text'] != '':
            invalid['text'] = 'Invalid space try again'
            return
        button['text'] = turn
        if check_win():
            invalid['text'] = 'Player ' + turn + ' WINS!!!!!'
            x = 1
        turn = ('0' if turn == 'X' else 'X')
        label_button['text'] = 'PLAYER ' + turn + '\'S TURN.'

    x = 0
    turn = 'X'
    game = Tk()
    game.title('TicTacToe')
    game.geometry('700x500')
    buttons = []
    for i in range(1, 10):
        button_created = create_button(0.25 if i / 3 <= 1 else 0.45 if i / 3 <= 2 else 0.65, 0.2 if i in [1, 4, 7] else
        0.4 if i in [2, 5, 8] else 0.6)
        buttons.append(button_created)
    label_button = Button(game, text='PLAYER ' + turn + '\'S TURN.', style='Fun.TButton', width=20, state='disabled')
    label_button.pack(pady=30)
    invalid = Label(text='')
    invalid.place(relx=0.4, rely=0.12)
    game.mainloop()
def about_os():
    about_window = Tk()
    show = Label(about_window, text='OS: Harsha os 2.3.1')
    show.pack()
    def ok_do_kay():
        about_window.destroy()
    button_close = Button(about_window, text='ok', command=ok_do_kay)
    button_close.pack()
    about_window.mainloop()
def password_generator():
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
    password_window = Tk()
    password_window.iconify()
    password_window.update()
    password_window.deiconify()
    password_window.eval('tk::PlaceWindow . center')
    password_label = Label(password_window, text=f'Your password is: {password}')
    password_label.pack()
    def password_ok():
        password_window.destroy()
    password_button = Button(password_window, text='ok', command=password_ok)
    password_button.pack()
    password_window.mainloop()
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


def rock_paper_scissors():
    window = Tk()
    window.geometry('400x400+0+0')
    window.iconify()
    window.update()
    window.deiconify()
    window.eval('tk::PlaceWindow . center')
    window.title('Rock-Paper-Scissors')
    global comp_score
    global user_score
    user_score = 0
    comp_score = 0  # this is the computer's score
    user_choice = ''
    comp_choice = ''

    def choice_to_number(choice):
        rps = {'rock': 0, 'paper': 1, 'scissors': 2}
        return rps[choice]

    def number_to_choice(number):
        rps = {0: 'rock', 1: 'paper', }
        return rps[number]

    def random_choice():
        return random.choice(['rock', 'paper', 'scissors'])

    def result(human_choice, comp_choice):
        global user_score
        global comp_score
        user = choice_to_number(human_choice)
        comp = choice_to_number(comp_choice)
        if (user == comp):
            print("Tie")
        elif ((user - comp) % 3 == 1):
            print("You win")
            user_score += 1
        else:
            print("Comp wins")
            comp_score += 1
        text_area = Text(master=window, height=12, width=30, bg="#FFFF99")
        text_area.grid(column=0, row=4)
        answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(
            uc=human_choice, cc=comp_choice, u=user_score, c=comp_score)
        text_area.insert(END, answer)

    def rock():
        global user_choice
        global comp_choice
        user_choice = 'rock'
        comp_choice = random_choice()
        result(user_choice, comp_choice)

    def paper():
        global user_choice
        global comp_choice
        user_choice = 'paper'
        comp_choice = random_choice()
        result(user_choice, comp_choice)

    def scissor():
        global user_choice
        global comp_choice
        user_choice = 'scissors'
        comp_choice = random_choice()
        result(user_choice, comp_choice)

    button1 = Button(text="       Rock       ", bg="skyblue", command=rock)
    button1.grid(column=0, row=1)
    button2 = Button(text="       Paper      ", bg="pink", command=paper)
    button2.grid(column=0, row=2)
    button3 = Button(text="      Scissor     ", bg="lightgreen", command=scissor)
    button3.grid(column=0, row=3)
    mainloop()


def os_command():
        OPTIONS = ['pick a option', 'password generator', 'tic-tac-toe', 'about os', 'number guessing game', 'calculator', 'quit harsha os', 'rock-paper-scissors', 'web browser']
        master = Tk()
        master.geometry("400x400+0+0")
        master.config(bg='yellow')
        master.iconify()
        master.update()
        master.deiconify()
        master.eval('tk::PlaceWindow . center')
        variable = StringVar(master)
        variable.set(OPTIONS[0])  # default value
        w = OptionMenu(master, variable, *OPTIONS)
        w.pack()
        def ok():
            global to_do
            to_do = variable.get()
            master.destroy()
        button = Button(master, text="OK", command=ok, bg='blue')
        button.pack()
        mainloop()
        global to_do
        if to_do == 'password generator':
            print('\n'*80), password_generator()
            stop = False
        elif to_do == 'about os':
            print('\n'*80), about_os()
            stop = False
        elif to_do == 'calculator':
            print('\n'*80), calculator()
            stop = False
        elif to_do == 'quit harsha os':
            print('\n'*80)
            stop = True
        elif to_do == 'rock-paper-scissors':
            print('\n'*80), rock_paper_scissors()
            stop = False
        elif to_do == 'web browser':
            print('\n'*80), simple_web_browser()
            stop = False
        elif to_do == 'tic-tac-toe':
            print('\n'*80), tic_tac_toe()
            stop = False
        else:
            stop = False
        if not stop:
            print('\n'*80), sleep(10), os_command()



key = 'atulharsha123$$'
password_input = ''
def a():
    frame = Tk()
    frame.geometry('400x200')
    frame.iconify()
    frame.update()
    frame.deiconify()
    frame.eval('tk::PlaceWindow . center')
    def get_password():
        global password_input
        password_input = input_txt.get(1.0, 'end-1c')
        frame.destroy()
    lbl = Label(frame, text="Enter the password")
    lbl.pack()
    input_txt = Text(frame, height=1, width=20)
    input_txt.pack()
    Buttoncool = Button(frame, text="Ok", command=get_password)
    Buttoncool.pack()
    frame.mainloop()
    if key == password_input:
        print('\n' * 80)
        os_command()
    else:
        print('Access Denied')


try:
    a()
except:
    print('                                                                          UNKNOWN ERROR OCCURRED')
gc.collect()
