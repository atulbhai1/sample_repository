from time import *
from tkinter import *
from googlesearch import search
import random
import gc
import os
to_do = 0
user_score = 0
comp_score = 0
def browser():
        query = input('Enter a URL or a keyword')
        for j in search(query, tld="com", num=10, stop=10, pause=2):
            print(j)
def screen_saver_mode():
        time2763 = time()
        time2764 = time()
        while (time2764 - time2763) < 300:
            time2764 = time()
            print(
                '---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            sleep(0.25)
def quiz():
        print('Ready to quiz yourself!')
        c = input("Wish to Continue (Y/N)")
        correct = 0
        wrong = 0
        while c.upper() == "Y":
            type1 = input('what type of quiz do you want?(addition-A/subtraction-S/multiplication-M')
            for x in range(5):
                if type1.upper() == "A":
                    a, b = random.randint(0, 1000), random.randint(0, 1000)  # generating a random number
                    ans1 = int(input("what is the answer of the equation: " + str(a) + "+" + str(b) + "=? "))
                    if ans1 == eval(str(a) + "+" + str(b)):
                        print("Correct")
                        correct = correct + 1
                    else:
                        print("Incorrect")
                        wrong = wrong + 1
                elif type1.upper() == "S":
                    ret, ret1 = True, True
                    while ret:
                        f77 = random.randint(0, 1000)  # generating a random number
                        if ret1:
                            t = random.randint(0, 1000)
                        if f77 > t:
                            ret, ret1 = False, False
                    ans1 = int(input("what is the answer of the equation: " + str(a) + "-" + str(b) + "=? "))
                    if ans1 == eval(str(a) + "-" + str(b)):
                        print("Correct")
                        correct = correct + 1
                    else:
                        print("Incorrect")
                        wrong = wrong + 1
                else:
                    a, b = random.randint(0, 10), random.randint(0, 10)  # generating a random number
                    ans1 = int(input("what is the answer of the equation: " + str(a) + "*" + str(b) + "=? "))
                    if ans1 == eval(str(a) + "*" + str(b)):
                        print("Correct")
                        correct = correct + 1
                    else:
                        print("Incorrect")
                        wrong = wrong + 1
            c = input("Wish to Continue (Y/N)")
        print("you had " + str(correct) + " correct answers and " + str(wrong) + " wrong answers")
        print("Your score is " + str((correct / (correct + wrong)) * 100) + "%")
        print('You are done with this quiz!')
def word_game1():
        random_stuff = (
        'apple', 'airplane', 'ball', 'beach', 'cat', 'call', 'degree', 'destroy', 'elephant', 'elevate', 'fat', 'faint',
        'grow', 'gigabyte', 'hat', 'hot', 'in', 'is', 'java', 'javascript', 'kangaroo', 'long', 'love', 'move', 'mop',
        'no', 'not', 'of', 'octopus', 'pot', 'plant', 'quiz', 'question', 'rat', 'raven', 'safe', 'save', 'tech', 'top',
        'umbrella', 'under', 'vent', 'was', 'x-mas', 'year', 'zylaphone')
        rand_num = random.randint(0, 45)
        secret = random_stuff[rand_num]
        print('                WORD GUESSING GAME')
        print()
        input('               PRESS ENTER TO START')
        for i in range(100):
            print()
        level = input('WHAT LEVEL WILL YOU PLAY? EASY/MEDIUM/HARD/IMPOSSIBLE?')
        if level.lower() == 'easy':
            num_of_tries = 23
        elif level.lower() == 'medium':
            num_of_tries = 15
        elif level.lower() == 'hard':
            num_of_tries = 9
        elif level.lower() == 'impossible':
            num_of_tries = 1
        else:
            print('INVALID LEVEL REQUESTED! SETTING LEVEL TO MEDIUM!')
            num_of_tries = 15
        hmm = False
        xyz = 0
        while hmm == False and num_of_tries > 0:
            if xyz == 0:
                guess = input('WHAT IS YOUR FIRST GUESS?')
                if guess == secret:
                    hmm == True
                else:
                    num_of_tries = num_of_tries - 1
                    xyz = 999999
            else:
                guess = input('WHAT IS YOUR NEXT GUESS?')
                if guess == secret:
                    hmm == True
                else:
                    num_of_tries -= 1
        if num_of_tries == 0:
            print('YOU LOST!!!')
        else:
            print('YOU WON!!!')
def rebase_from10():
        def encode(digits, other_digit_map):
            if max(digits) >= len(other_digit_map):
                raise ValueError('digit_map is not long enough to encode the digits')
            other_encoding = ''
            for d in digits:
                other_encoding += digit_map[d]
            return other_encoding

        def from_base10(n, b):
            if b < 2:
                raise ValueError('Base b must be >= 2')
            if n < 0:
                raise ValueError('Number n must be >= 0')
            if n == 0:
                return [0]
            digits = []
            while n > 0:
                n, m = divmod(n, b)
                digits.insert(0, m)
            return digits

        number, base = int(input('What number do you want to change')), int(input('What is the base of number you want to change'))
        digit_map = '''0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()-_=+[{]}\\|;:'",<.>/?'''
        if base < 2 or base > len(digit_map):
            raise ValueError(f'Base must be equal to or below {len(digit_map)} and more than or equal to 2')
        sign = -1 if number < 0 else 1
        number *= sign
        encoding = encode(from_base10(number, base), digit_map)
        if sign == -1:
            encoding = '-' + encoding
        print('Your new number is:', encoding)
def titanic_game():
        print('You are sleeping peacefully when a sudden bang wakes you up.You realize that something crashed into the')
        to_do = input('ship. What do you do? stay here or look outside?')
        if to_do == 'stay here':
            def stay_here():
                print(
                    'You stay inside the cabin, covering yourself with bed sheets.Nothing happens for a while, but then someone')
                print(
                    'knocks the door. You hop up and open it.A crew member then tells you that the Titanic has hit an iceberg')
                print(
                    'and is sinking, so all passengers are requested to come up on deck and wait for further instructions.')
                to_do1 = input('Will you leave the room or stay?')
                if to_do1 == 'stay':
                    def stay():
                        print(
                            'You cover yourself up with sheets hoping it will all get over soon.But soon you feel a mighty crash as if')
                        print(
                            'the ship is colliding with something again,in a few more minutes another hit follows and you see water')
                        print('water coming into your cabin.')
                        print(' Game Over! You Lost!')

                    stay()
                elif to_do1 == 'leave the room':
                    def leave():
                        print(
                            'You get on deck where a crowd of scared people has already gathered.The ship\'s band is playing music.')
                        print(
                            'The crew are trying to calm everybody down but they look like they are at a loss themselves.')
                        print('Then, someone gives a signal and the lifeboats start getting untied.')
                        to_do2 = input(
                            'The order is clear though women and children first. What do you do? help passengers or help the crew?')
                        if to_do2 == 'help passengers':
                            def help_passengers():
                                print(
                                    'You go inside the ship knocking on all the cabins doors,checking if anybody is inside.Then suddenly another')
                                print(
                                    'boom shake the ship.The ship has collided with something again.You run on deck but then another crash knocks')
                                print(
                                    'off your feet and the floor under you lurches.You try to hurry but it\'s no use the ship is filling up with water.')
                                print('Game Over! You Lose!')

                            help_passengers()
                        elif to_do2 == 'help the crew':
                            def help_crew():
                                print(
                                    'You help the crew seat women and children into the lifeboats and calm down other passengers.')
                                print(
                                    'Then another boom crashes through the ship.You keep calm and continue to help loading up passengers.')
                                print(
                                    'When the last child is put in the last lifeboat,you see there is space for one more person.')
                                to_do3 = input(
                                    'What will you do with it? run across the stern/hop in the boat/run through the ship? ')
                                if to_do3 == 'run across the stern':
                                    def run_stern():
                                        print(
                                            'You run to the other side of the Titanic, taking the longer but safer route through the stern.')
                                        print(
                                            'But then another shudder knocks you off your feet and makes the Titanic split in half.You try on grab on')
                                        print('but the part you are on suddenly falls into the water.')
                                        print('Game Over! You Lose!')

                                    run_stern()
                                elif to_do3 == 'run through the ship':
                                    def run_ship():
                                        print(
                                            'You run to the other side of the Titanic.You choose the shortest route through the ship.')
                                        print(
                                            'But then another crash hits the Titanic and the floor lurches,you get back up and hurry.')
                                        print(
                                            'You reach the other side but it broke of and the last lifeboat just left.You try to reach it')
                                        print(
                                            'but miss,so you jump off the Titanic and swim to the boat and someone pulls you to safety.')
                                        print('Game Over! You Won!')

                                    run_ship()
                                elif to_do3 == 'hop in the boat':
                                    def hop():
                                        print('You hop into the boat.The boat goes into the water and floats.')
                                        print('Game Over! You Win!')

                                    hop()

                            help_crew()
                        else:
                            print('Invalid action! quiting game')

                    leave()
                else:
                    print('Invalid action! quiting game')

            stay_here()
        elif to_do == 'look outside':
            def look_out():
                print('You get up from the bed and try to open the door.The door is locked,so you break the door open.')
                print(
                    'You see crew members running everywhere.You manage to grab one and ask him what is happening.He tells you to stay in the cabin.')
                to_do4 = input('Will you stay in your cabin or leave?')
                if to_do4 == 'leave':
                    print(
                        'You go outside and look over the guardrail.You see that there is a huge gash at the front of the Titanic')
                    to_do4 = input(
                        'You go back inside and see the crew who tell you o get on deck. Will you get on deck or help others?')
                    if to_do4 == 'get on deck':
                        print(
                            'You get on deck where a crowd of scared people has already gathered.The ship\'s band is playing music.')
                        print(
                            'The crew are trying to calm everybody down but they look like they are at a loss themselves.')
                        print('Then, someone gives a signal and the lifeboats start getting untied.')
                        to_do4 = input(
                            'The order is clear though women and children first. What do you do? help passengers or help the crew?')
                        if to_do4 == 'help passengers':
                            def help_passengers():
                                print(
                                    'You go inside the ship knocking on all the cabins doors,checking if anybody is inside.Then suddenly another')
                                print(
                                    'boom shake the ship.The ship has collided with something again.You run on deck but then another crash knocks')
                                print(
                                    'off your feet and the floor under you lurches.You try to hurry but it\'s no use the ship is filling up with water.')
                                print('Game Over! You Lose!')

                            help_passengers()
                        elif to_do4 == 'help the crew':
                            def help_crew():
                                print(
                                    'You help the crew seat women and children into the lifeboats and calm down other passengers.')
                                print(
                                    'Then another boom crashes through the ship.You keep calm and continue to help loading up passengers.')
                                print(
                                    'When the last child is put in the last lifeboat,you see there is space for one more person.')
                                to_do5 = input(
                                    'What will you do with it? run across the stern/hop in the boat/run through the ship? ')
                                if to_do5 == 'run across the stern':
                                    def run_stern():
                                        print(
                                            'You run to the other side of the Titanic, taking the longer but safer route through the stern.')
                                        print(
                                            'But then another shudder knocks you off your feet and makes the Titanic split in half.You try on grab on')
                                        print('but the part you are on suddenly falls into the water.')
                                        print('Game Over! You Lose!')

                                    run_stern()
                                elif to_do5 == 'run through the ship':
                                    def run_ship():
                                        print(
                                            'You run to the other side of the Titanic.You choose the shortest route through the ship.')
                                        print(
                                            'But then another crash hits the Titanic and the floor lurches,you get back up and hurry.')
                                        print(
                                            'You reach the other side but it broke of and the last lifeboat just left.You try to reach it')
                                        print(
                                            'but miss,so you jump off the Titanic and swim to the boat and someone pulls you to safety.')
                                        print('Game Over! You Won!')

                                    run_ship()
                                elif to_do5 == 'hop in the boat':
                                    def hop():
                                        print('You hop into the boat.The boat goes into the water and floats.')
                                        print('Game Over! You Win!')

                                    hop()

                            help_crew()
                        else:
                            print('Invalid action! quiting game')
                    elif to_do4 == 'help others':
                        print(
                            'You go inside the ship knocking on all the cabins doors,checking if anybody is inside.Then suddenly another')
                        print(
                            'boom shake the ship.The ship has collided with something again.You run on deck but then another crash knocks')
                        print(
                            'off your feet and the floor under you lurches.You try to hurry but it\'s no use the ship is filling up with water.')
                        print('Game Over! You Lose!')
                    else:
                        print('Invalid action! quiting game')
                elif to_do4 == 'stay in your cabin':
                    print(
                        'You cover yourself up with sheets hoping it will all get over soon.But soon you feel a mighty crash as if')
                    print(
                        'the ship is colliding with something again,in a few more minutes another hit follows and you see water')
                    print('water coming into your cabin.')
                    print(' Game Over! You Lost!')
                else:
                    print('Invalid action! quiting game')

            look_out()
        else:
            print('Invalid action! quiting game')
def num_game1():
        print('                NUMBER GUESSING GAME')
        print()
        print()
        input('                press enter to start')
        for i in range(99):
            print()
        secret_number, h = random.randint(1, 20), input('What level do you want to play at? easy/medium/hard')
        if h == 'hard':
            guess_limit = 5
        elif h == 'medium':
            guess_limit = 10
        elif h == 'easy':
            guess_limit = 15
        else:
            print('Invalid Input setting level to medium.')
            guess_limit = 10
        out_of_guesses, guess, guess_count = False, input('WHAT IS YOUR FIRST GUESS FOR A NUMBER BETWEEN 1 AND 20?'), 1
        while int(guess) != secret_number and not out_of_guesses:
            if guess_count < guess_limit:
                guess, guess_count = input('ENTER YOUR NEXT GUESS'), guess_count + 1
            else:
                out_of_guesses = True
        if out_of_guesses:
            print('YOU LOST!')
            print('THE CORRECT NUMBER WAS', secret_number)
        else:
            print('YOU WON!')
def calculator():

            x = eval(input('enter a equation you want to solve!'))
            print(x)
def tictactoe():
        board = [i for i in range(0, 9)]
        player, computer = '', ''

        # Corners, Center and Others, respectively
        moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))
        # Winner combinations
        winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        # Table
        tab = range(1, 10)

        def print_board():
            x = 1
            for i in board:
                end = ' | '
                if x % 3 == 0:
                    end = ' \n'
                    if i != 1: end += '---------\n';
                char = ' '
                if i in ('X', 'O'): char = i;
                x += 1
                print(char, end=end)

        def select_char():
            chars = ('X', 'O')
            if random.randint(0, 1) == 0:
                return chars[::-1]
            return chars

        def can_move(brd, player, move):
            if move in tab and brd[move - 1] == move - 1:
                return True
            return False

        def can_win(brd, player, move):
            places = []
            x = 0
            for i in brd:
                if i == player: places.append(x);
                x += 1
            win = True
            for tup in winners:
                win = True
                for ix in tup:
                    if brd[ix] != player:
                        win = False
                        break
                if win == True:
                    break
            return win

        def make_move(brd, player, move, undo=False):
            if can_move(brd, player, move):
                brd[move - 1] = player
                win = can_win(brd, player, move)
                if undo:
                    brd[move - 1] = move - 1
                return (True, win)
            return (False, False)

        # AI goes here
        def computer_move():
            move = -1
            # If I can win, others don't matter.
            for i in range(1, 10):
                if make_move(board, computer, i, True)[1]:
                    move = i
                    break
            if move == -1:
                # If player can win, block him.
                for i in range(1, 10):
                    if make_move(board, player, i, True)[1]:
                        move = i
                        break
            if move == -1:
                # Otherwise, try to take one of desired places.
                for tup in moves:
                    for mv in tup:
                        if move == -1 and can_move(board, computer, mv):
                            move = mv
                            break
            return make_move(board, computer, move)

        def space_exist():
            return board.count('X') + board.count('O') != 9

        player, computer = select_char()
        print('Player is [%s] and computer is [%s]' % (player, computer))
        result = '   Tie! Nobody wins!'
        while space_exist():
            print_board()
            print('# Make your move ! [1-9] : ', end='')
            move = int(input())
            moved, won = make_move(board, player, move)
            if not moved:
                print(' >> Invalid number ! Try again !')
                continue
            #
            if won:
                result = ' Congratulations ! You won ! '
                break
            elif computer_move()[1]:
                result = ' You lose ! '
                break;

        print_board()
        print(result)
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
        OPTIONS = ['pick a option', 'screen saver mode', 'browser', 'number guessing game', 'calculator', 'quit harsha os', 'word guessing game',
                   'tic-tac-toe', 'rock-paper-scissors', 'base converter', 'titanic game']
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
        if to_do == 'screen saver mode':
            print('\n' * 80), screen_saver_mode()
            stop = False
        elif to_do == 'browser':
            print('\n'*80), browser()
            stop = False
        elif to_do == 'number guessing game':
            print('\n'*80), num_game1()
            stop = False
        elif to_do == 'calculator':
            print('\n'*80), calculator()
            stop = False
        elif to_do == 'quit harsha os':
            print('\n'*80)
            stop = True
        elif to_do == 'quiz':
            print('\n'*80), quiz()
            stop = False
        elif to_do == 'word guessing game':
            print('\n'*80), word_game1()
            stop = False
        elif to_do == 'tic-tac-toe':
            print('\n'*80), tictactoe()
            stop = False
        elif to_do == 'rock-paper-scissors':
            print('\n'*80), rock_paper_scissors()
            stop = False
        elif to_do == 'base converter':
            print('\n'*80), rebase_from10()
            stop = False
        elif to_do == 'titanic game':
            print('\n'*80), titanic_game()
            stop = False
        else:
            stop = False
        if not stop:
            print('\n'*80), os_command()



key = 'atulharsha123$$'
def a():
    password_input = input('Password:')
    if key == password_input:
        print('\n'*80)
        os_command()
    else:
        print('Access Denied!')


try:
    a()
except:
    print('                                                                          UNKNOWN ERROR OCCURRED')
gc.collect()
