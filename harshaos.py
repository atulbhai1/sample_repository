from time import *
from tkinter import *
import tkinter.messagebox
import random
import gc
from math import *
to_do = 0
user_score = 0
comp_score = 0
equation = ''
txt = ''
counter = 0
num = 0
def sqrt_calculator():
    global num
    frame = Tk()
    frame.title('Square Root Calculator')
    frame.geometry('400x200')
    frame.iconify()
    frame.update()
    frame.deiconify()
    frame.eval('tk::PlaceWindow . center')

    def get_num():
        global num
        num = input_txt.get(1.0, 'end-1c')
        frame.destroy()

    lbl = Label(frame, text="Enter the number you want to get the square root of")
    lbl.pack()
    input_txt = Text(frame, height=1, width=20)
    input_txt.pack()
    Buttoncool = Button(frame, text="Ok", command=get_num)
    Buttoncool.pack()
    frame.mainloop()
    frame2 = Tk()
    show = Label(frame2, text=f'The square root of {num} is {sqrt(int(num))}.')
    show.pack()
    so = Button(frame2, text='ok', command=frame2.destroy)
    so.pack()
    frame2.mainloop()


def titanic_game():
    def stay_in_bed1():
        show = 'You go back to sleep hoping it all goes over soon.But later someone knocks your door and tells you to come on deck immediately. What do you do?'
        stay1_window = Tk()
        stay1_story = Label(stay1_window, text=show)
        stay1_story.pack()

        def ok1():
            stay1_window.destroy()
            stay_in_bed2()

        def ok2():
            stay1_window.destroy()
            get_out2()

        stay1_button1 = Button(stay1_window, text='stay', command=ok1)
        stay1_button1.pack()
        stay1_button2 = Button(stay1_window, text='leave', command=ok2)
        stay1_button2.pack()
        stay1_window.mainloop()

    def stay_in_bed2():
        stay2_window = Tk()

        def ok():
            stay2_window.destroy()

        stay2_says = Label(stay2_window,
                           text='You go back to sleep.But after a while you notice that the ship is filling with water.You try to escape but drown.YOU LOST!😞')
        stay2_says.pack()
        stay2_button = Button(stay2_window, text='ok', command=ok)
        stay2_button.pack()
        stay2_window.mainloop()

    def get_out2():
        show = 'You get out on deck and see a large commotion.Everyone was panicking and the crew was trying to calm everyone down, but they seemed at a loss themselves.What do you do?'
        get_out2_window = Tk()
        get_out2_story = Label(get_out2_window, text=show)
        get_out2_story.pack()

        def ok():
            get_out2_window.destroy()
            help_crew()

        def ok2():
            get_out2_window.destroy()
            help_others()

        get_out2_button1 = Button(get_out2_window, text='help people out of the ship', command=ok2)
        get_out2_button1.pack()
        get_out2_button2 = Button(get_out2_window, text='help the crew', command=ok)
        get_out2_button2.pack()
        get_out2_window.mainloop()

    def help_others():
        show = 'You go back in the ship to check if anyone is left behind.\nSuddenly the floor shudders and you fall down,you get back up but later the floor lurches and you drown.You Lose!😞'
        help_others_window = Tk()
        lose_message = Label(help_others_window, text=show)
        lose_message.pack()

        def ok():
            help_others_window.destroy()

        fine = Button(help_others_window, text='ok', command=ok)
        fine.pack()
        help_others_window.mainloop()

    def help_crew():
        help_crew_window = Tk()
        show = 'You help the crew put everyone into the lifeboats with only one shudder occuring.Once you are done you see that their is room left for one person.What do you do?'
        help_crew_story = Label(help_crew_window, text=show)
        help_crew_story.pack()

        def ok1():
            help_crew_window.destroy()
            run_across_the_stern()

        def ok2():
            help_crew_window.destroy()
            run_through_the_ship()

        def ok3():
            help_crew_window.destroy()
            hop_in_the_boat()

        help_crew_button1 = Button(help_crew_window, text='hop in the boat', command=ok3)
        help_crew_button1.pack()
        help_crew_button2 = Button(help_crew_window, text='run through the ship', command=ok2)
        help_crew_button2.pack()
        help_crew_button3 = Button(help_crew_window, text='run across the stern', command=ok1)
        help_crew_button3.pack()
        help_crew_window.mainloop()

    def run_across_the_stern():
        run_across_the_stern_window = Tk()
        show = Label(run_across_the_stern_window,
                     text='You run across the stern,the longer but safer route.After a bit of running the floor suddenly lurches.You try to escape but fail.YOU LOSE!😞')
        show.pack()

        def ok():
            run_across_the_stern_window.destroy()

        run_across_the_stern_button = Button(run_across_the_stern_window, text='ok', command=ok)
        run_across_the_stern_button.pack()
        run_across_the_stern_window.mainloop()

    def run_through_the_ship():
        run_through_the_ship_window = Tk()
        show = Label(run_through_the_ship_window,
                     text='You run through the ship.After some running you reach the other side and see the last lifeboat leaving you manage to hop on it.YOU WIN!😎😀')
        show.pack()

        def ok():
            run_through_the_ship_window.destroy()

        close = Button(run_through_the_ship_window, text='ok', command=ok)
        close.pack()

    def hop_in_the_boat():
        hop_in_the_boat_window = Tk()
        show = Label(hop_in_the_boat_window, text='You hop in the boat.YOU WIN!😀😎')
        show.pack()

        def ok():
            hop_in_the_boat_window.destroy()

        close = Button(hop_in_the_boat_window, text='ok', command=ok)
        close.pack()
        hop_in_the_boat_window.mainloop()

    def get_out1():
        get_out1_window = Tk()
        show = 'You go outside and see a that the ship is badly damaged.Then you run back inside and see a crew member who tells you to get on deck.What do you do?'
        get_out1_label = Label(get_out1_window, text=show)
        get_out1_label.pack()

        def ok1():
            get_out1_window.destroy()
            stay_in_bed2()

        def ok2():
            get_out1_window.destroy()
            get_out2()

        get_out1_button1 = Button(get_out1_window, text='go back to the room and sleep', command=ok1)
        get_out1_button1.pack()
        get_out1_button2 = Button(get_out1_window, text='get on deck', command=ok2)
        get_out1_button2.pack()
        get_out1_window.mainloop()

    show = 'You wake up to a sudden bang to the ship.What do you do?'
    start_window = Tk()
    start_story = Label(start_window, text=show)
    start_story.pack()

    def ok1():
        start_window.destroy()
        stay_in_bed1()

    def ok2():
        start_window.destroy()
        get_out1()

    start_button1 = Button(start_window, text='Stay in bed', command=ok1)
    start_button1.pack()
    start_button2 = Button(start_window, text='Get out!', command=ok2)
    start_button2.pack()
    start_window.mainloop()



def pointless_button():
    global counter
    pointless = Tk()
    message = StringVar()
    message.set('Warning Pointless')

    def ok():
        global counter
        if counter == 0:
            message.set('I told you the button does nothing.')
        elif counter == 1:
            message.set('Stop pressing it!')
        elif counter == 2:
            message.set('I said stop pressing it!')
        elif counter == 3:
            message.set("Really the button doesn't like it!")
        elif counter == 4:
            message.set('Please?🥺')
        elif counter == 5:
            message.set('You want it to do something right?')
        elif counter == 6:
            message.set("It won't.")
        elif counter == 7:
            message.set('Stop and I can make it do something.')
        elif counter == 8:
            message.set('I said STOP!')
        elif counter == 9:
            message.set('What is making you to give him so much agony?')
        elif counter == 10:
            message.set('You are evil.')
        elif counter == 11:
            message.set('Fine, I will ignore you!')
        elif 12 == counter:
            message.set('I said I am ignoring you!')
        elif counter == 13:
            message.set('I am exhausted!')
        else:
            message.set('STOP!')
        counter += 1

    they_see = Entry(pointless, textvariable=message)
    they_see.grid(columnspan=10, ipadx=70)
    ok = Radiobutton(pointless, command=ok)
    ok.grid(row=2, column=4)
    pointless.mainloop()
    message = Tk()
    show = Label(message, text=f'You pressed the button {counter + 1} times.')
    show.pack()

    def kay():
        message.destroy()

    stop = Button(message, text='ok', command=kay)
    stop.pack()
    message.mainloop()
def about_os():
    about_window = Tk()
    show = Label(about_window, text='OS: Harsha os 2.4.1')
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
        txt = txt + '✖️'
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
    button_dot = Button(calculator_window, text='    ．    ', command=decimal, height=1, width=7)
    button_dot.grid(row=6, column=3)
    button__open_parentheses = Button(calculator_window, text='   ⦅   ', command=open_parentheses, height=1, width=7)
    button__open_parentheses.grid(row=6, column=4)
    button_close_parentheses = Button(calculator_window, text='   ⦆   ', command=close_parentheses, height=1, width=7)
    button_close_parentheses.grid(row=6, column=5)
    button_equal = Button(calculator_window, text='   ₌   ', command=equals, height=1, width=7)
    button_equal.grid(row=6, column=6)
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
        OPTIONS = ['pick a option', 'sqrt calculator', 'password generator', 'titanic game', 'about os', 'mess around with the pointless button', 'calculator', 'quit harsha os', 'rock-paper-scissors']
        master = Tk()
        master.title('Harsha OS')
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
            password_generator()
            stop = False
        elif to_do == 'sqrt calculator':
            sqrt_calculator()
            stop = False
        elif to_do == 'titanic game':
            titanic_game()
            stop = False
        elif to_do == 'mess around with the pointless button':
            pointless_button()
            stop = False
        elif to_do == 'about os':
            about_os()
            stop = False
        elif to_do == 'calculator':
            calculator()
            stop = False
        elif to_do == 'quit harsha os':
            stop = True
        elif to_do == 'rock-paper-scissors':
            rock_paper_scissors()
            stop = False
        else:
            stop = False
        if not stop:
            os_command()



key = 'harshaisevil'
password_input = ''
def a():
    frame = Tk()
    frame.title('Password')
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
    if password_input == key:
        os_command()
    else:
        access_denied_window = Tk()
        Message = Label(access_denied_window, text='ACCESS DENIED!')
        Message.pack()

        def ok():
            access_denied_window.destroy()

        close = Button(access_denied_window, text='ok', command=ok)
        close.pack()
        access_denied_window.mainloop()


try:
    a()
except:
    Error_Window = Tk()
    Error_label = Label(Error_Window, text='ERROR OCCURRED')
    Error_label.pack()


    def ok():
        Error_Window.destroy()


    Close = Button(Error_Window, text='ok', command=ok)
    Close.pack()
    Error_Window.mainloop()
gc.collect()
