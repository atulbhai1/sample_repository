from time import time
from time import sleep
from googlesearch import search
import random
import gc



def help101():
    print('''To activate harsha os type in : activate.activate(Harsha_os,_'activate ')''')
    print('To turn of type in: turn.off.type(full)')
    print('To turn on screen saver mode type in: mode.screen.saver(screensaver)')
    command()


def screen_saver_mode():
    time2763 = time()
    time2764 = time()
    while (time2764-time2763) < 300:
        time2764 = time()
        print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        sleep(0.25)
    command()


def command():
    to_do = input('>>')
    if to_do == 'help':
        help101()
    elif to_do == "activate.activate(Harsha_os,_'activate ')":
        harsha_os()
    elif to_do == 'mode.screen.saver(screensaver)':
        screen_saver_mode()
    elif to_do == 'turn.off.type(full)':
        pass
    else:
        print(f'{to_do} is not a internal nor external command')
        command()


def harsha_os():
    def browser():
        query = input('Enter a URL or a keyword')
        for j in search(query, tld="com", num=10, stop=10, pause=2):
            print(j)
        os_command()
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
        os_command()

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
        os_command()
    def calculator():

            x = eval(input('enter a equation you want to solve!'))
            print(x)
            os_command()
    def help11():
        print('To access the browser type in: browser')
        print('To access the quiz type in: quiz')
        print('To access the number guessing game type in: number guessing game')
        print('To access the calculator type in: calculator')
        print('To access tic-tac-toe type in: tic-tac-toe')
        print('To access rock-paper-scissors ype in: rock-paper-scissors')
        print('To quit harsha os type in: quit harsha os')
        os_command()
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
        os_command()

    def rock_paper_scissors():
        score = 0
        computer_score = 0
        rounds = int(input('How many rounds do you want to play?'))
        extra_rounds = 0
        for i in range(rounds):
            move = input('What will you you play?')
            rand_num = random.randint(1, 3)
            if rand_num == 1:
                computer_move = 'rock'
            elif rand_num == 2:
                computer_move = 'paper'
            else:
                computer_move = 'scissors'
            print(f'Computer played {computer_move}')
            if move == 'rock':
                if computer_move == 'paper':
                    computer_score += 1
                elif computer_move == 'scissors':
                    score += 1
            elif move == 'paper':
                if computer_move == 'rock':
                    score += 1
                elif computer_move == 'scissors':
                    computer_score += 1
            elif move == 'scissors':
                if computer_move == 'paper':
                    score += 1
                elif computer_move == 'rock':
                    computer_score += 1
        if computer_score == score:
            print('Tie!')
        elif computer_score < score:
            print('You win!')
        else:
            print('Computer wins!')
        os_command()
    def os_command():
        to_do = input('What do you want to do?')
        if to_do == 'help':
            help11()
        elif to_do == 'browser':
            browser()
        elif to_do == 'number guessing game':
            num_game1()
        elif to_do == 'calculator':
            calculator()
        elif to_do == 'quit harsha os':
            command()
        elif to_do == 'quiz':
            quiz()
        elif to_do == 'tic-tac-toe':
            tictactoe()
        elif to_do == 'rock-paper-scissors':
            rock_paper_scissors()
        else:
            print(f'{to_do} is not a program')
            os_command()
    os_command()


key = 'atulharsha123$$'
master_key = 'atul$$'
def a():
    password_input = input('Password:')
    if key == password_input:
        for i in range(50):
            print()
        command()
    elif master_key == password_input:
        print('Password:atulharsha123$$')
        a()
    else:
        print('Access Denied!')


try:
    a()
except:
    print('                                                                          UNKNOWN ERROR OCCURRED')
gc.collect()
