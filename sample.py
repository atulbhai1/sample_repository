from tkinter.filedialog import *
import mysql.connector
import random
from numpy import *
import datetime


class num_programs:
    def quiz(self):
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
                        f77 = random.randint(0, 1000)  # generating a rndom number
                        if ret1:
                            u = random.randint(0, 1000)
                        if f77 > u:
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

    def calculate(self):
        x = eval(input('enter a equation you want to solve!'))
        print(x)

    def guess_game(self):
        import random
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

    def skip_count(self):
        print('follow the instructions below to make a sequence that will skip count by the number you enter')
        a, b, c = int(input('starting number?')), int(input('ending number?')), int(input('What number should you skip count by? '))
        arr = arange(a, b, c)
        if b - a > c:
            print(arr)
        else:
            print('Please enter a smaller number to skip count by next time.')

    def square_num_sequence(self):
        x, i, c = int(input('What is the largest possible square number that you want to see?')), 1, 1
        while c <= x:
            print(c)
            i = i + 1
            c = i * i

    def fib(self):
        x, a, b = int(input('How many numbers do you want to see in the fibonacci sequence? ')), 0, 1
        if x == 1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2, x):
                c, a, b= a + b, b, a + b
                print(c)

    def fact(self):
        f, x = 1, int(input('What number do you want to find the factorial of?'))
        for i in range(1, x + 1):
            f = f * i
        return f

    def random_num_generator(self):
        rand1, rand2 = int(input(' Type the smallest possible random number you want ')), int(input(' Type the largest possible random number you want '))
        print(random.randint(rand1, rand2))

    def years_to_seconds(self):
        print("Follow the instructions to find your age in seconds!")
        print('Your answer will be within 31,556,952 seconds of accuracy to your real age!')
        x = float(input("Enter age in years: "))
        g = x * 365 * 24 * 3600
        print("Your age in seconds is: ", g)


class word_programs():
    def print1(self):
        print('follow the instructions below to print words or numbers and how many times you want to see it!')
        x, y = input('type down what you want to say'), int(input('type down the number of times you want to print it'))
        for i in range(y):
            print(x)


class file_related_programs:
    def file_maker(self):
        what_to_print, path_to_save = input('Enter the text you want to save in the file'), asksaveasfilename(title='enter file name')
        f = open(path_to_save, 'w')
        f.write(what_to_print)

    def user_viewer(self):
        mydb = mysql.connector.connect(host='localhost', user='root', passwd='atulbhai2', database='Atul_test')
        mycursor = mydb.cursor()
        mycursor.execute('select * from people')
        for i in mycursor:
            print(i)

    def create_python_file(self):
        print('Follow the instructions below to create or re-write a one line python file and code in it.')
        name, what_to_do = input('What is the name of your python file?'), input('Type the code now!')
        name = name + '.py'
        file = open(name, 'w')
        file.write(what_to_do)
        print('Done!')


class product_creation_programs():
    def create_a_product_basic(self):
        print('Follow the instructions bellow to create products.')
        x = input('Do you want to start? yes/no')
        while x == 'yes':
            num_of_prods = int(input('How many products to you want to create today?(please enter a numerical value)'))
            for i in range(num_of_prods):
                prod_name, prod_price = input('What is the name of your product you want to create?'), float(input('What is the price of you product you are creating?'))
                print('You created a product called', prod_name, 'which costs', prod_price, 'dollars.')
            x = input('Do you want to continue? yes/no')


class chatbots():
    def talk_to_santa(self):
        import time

        print('Calling Santa\'s workshop...')
        time.sleep(5)

        def santa1():
            print('Hello,I am doing something now please go away now bye!')
            x = input(
                'Oh wait a second can you help me come up with special gifts for very good people? are you in? yes or no?')
            if x == 'yes':
                print('Great!')
                gift = input('So first there is this boy in Sweden,what should I get him?')
                print('Ok,I will get him a' + gift)
                gift = input('Next,there is this girl in Israel,what should I get her?')
                print('Ok,I will get her a' + gift)
                gift = input(
                    'Last of all,there is this boy in Canada who happens to love tamales,what should I get him?')
                print('Ok,I will get him a' + gift)
            else:
                print('Ok then,bye!')
            North_pole_operator()

        def Mrs_Santa():
            print('Oh,Hello there!')
            print('I hope you are doing well.')
            gift = input('What do you want for Christmas?')
            print('Ok I will make sure you get a' + gift + 'this Christmas!')
            print('It was nice meeting you but now I have to go.Bye!')
            North_pole_operator()

        def Elf():
            print('Sorry we are to busy to talk now!Bye!')
            North_pole_operator()

        def North_pole_operator():
            yes_no = input('Do you want to continue your call to the North Pole? yes or no?')
            if yes_no == 'yes':
                to_call = input('Hello who do you want to talk to? Santa,Mrs.Santa or the Elves')
                time.sleep(2)
                if to_call == 'Santa':
                    santa1()
                elif to_call == 'Mrs.Santa':
                    Mrs_Santa()
                elif to_call == 'Elves' or to_call == 'the Elves':
                    Elf()
                else:
                    print('Unknown Error Call Failed')
            else:
                pass

        North_pole_operator()


a1 = num_programs()
b1 = word_programs()
c1 = file_related_programs()
d1 = product_creation_programs()
e1 = chatbots()
try:
    x = input('Hello how are you doing? good/bad')
    if x == 'good':
        print(' That is good!')
    elif x == 'bad':
        print('I hope you will feel better soon!')
    y = input('Do you want to start? Y/N')
    if y.upper() == 'Y':
        time = input('Do you want to activate time reminders? yes/no')
        if time == 'yes':
            while y.upper() == "Y":
                x = input(
                    'What do you want to do quiz/calculate/print/skip count/random number generator/years to seconds/fibonacci sequence/factorial finder/create a file/square number sequence/see users/create products simple/call santa\'s workshop/skip count/guessing game/create a python file')
                if x == 'quiz':
                    a1.quiz()
                elif x == 'calculate':
                    a1.calculate()
                elif x == "print":
                    b1.print1()
                elif x == "skip count":
                    a1.skip_count()
                elif x == "factorial finder":
                    a1.fact()
                elif x == "fibonacci sequence":
                    a1.fib()
                elif x == 'create a python file':
                    c1.create_python_file()
                elif x == 'random number generator':
                    a1.random_num_generator()
                elif x == 'years to seconds':
                    a1.years_to_seconds()
                elif x == 'create a file':
                    c1.file_maker()
                elif x == 'square number sequence':
                    a1.square_num_sequence()
                elif x == 'see users':
                    c1.user_viewer()
                elif x == 'create products simple':
                    d1.create_a_product_basic()
                elif x == 'guessing game':
                    a1.guess_game()
                elif x == 'call santa\'s workshop':
                    e1.talk_to_santa()
                elif x == 'skip count':
                    a1.skip_count()
                else:
                    print('Invalid input!Next time type in something else.')
                time = datetime.datetime.now()
                print("The  exact time is", time.strftime('%I') + ':' + time.strftime('%M') + ':' + time.strftime('%S'))
                print()
                y = input('Wish to continue? Y/N')
        elif time == 'no':
            while y.upper() == "Y":
                x = input(
                    'What do you want to do quiz/calculate/print/skip count/random number generator/years to seconds/fibonacci sequence/factorial finder/create a file/square number sequence/see users/create products simple/call santa\'s workshop/skip count/guessing game/create a python file')
                if x == 'quiz':
                    a1.quiz()
                elif x == 'calculate':
                    a1.calculate()
                elif x == "print":
                    b1.print1()
                elif x == "skip count":
                    a1.skip_count()
                elif x == "factorial finder":
                    a1.fact()
                elif x == "fibonacci sequence":
                    a1.fib()
                elif x == 'create a python file':
                    c1.create_python_file()
                elif x == 'random number generator':
                    a1.random_num_generator()
                elif x == 'years to seconds':
                    a1.years_to_seconds()
                elif x == 'create a file':
                    c1.file_maker()
                elif x == 'square number sequence':
                    a1.square_num_sequence()
                elif x == 'see users':
                    c1.user_viewer()
                elif x == 'create products simple':
                    d1.create_a_product_basic()
                elif x == 'guessing game':
                    a1.guess_game()
                elif x == 'call santa\'s workshop':
                    e1.talk_to_santa()
                elif x == 'skip count':
                    a1.skip_count()
                else:
                    print('Invalid input!Next time type in something else.')
                print()
                y = input('Wish to continue? Y/N')
        else:
            print('Invalid Input!')

except:
    for i in range(99):
        print()
    print('                    UNKNOWN ERROR OCCURRED')
