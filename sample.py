print('hello')
from tkinter.filedialog import *
import mysql.connector
import random
class num_programs:
    def quiz(self):
        print('Ready to quiz yourself!')
        c = input("Wish to Continue (Y/N)")
        correct = 0
        wrong = 0
        while (c.upper() == "Y"):
            type1 = input('what type of quiz do you want?(addition-A/subtraction-S/multiplication-M')
            for x in range(5):
                if (type1.upper() == "A"):
                    a = random.randint(0, 1000)  # generating a rndom number
                    b = random.randint(0, 1000)
                    ans1 = int(input("what is the answer of the equation: " + str(a) + "+" + str(b) + "=? "))
                    if (ans1 == eval(str(a) + "+" + str(b))):
                        print("Correct")
                        correct = correct + 1
                    else:
                        print("Incorrect")
                        wrong = wrong + 1
                elif (type1.upper() == "S"):
                    ret = True
                    ret1 = True
                    while (ret):
                        a = random.randint(0, 1000)  # generating a rndom number
                        if (ret1):
                            b = random.randint(0, 1000)
                        if (a > b):
                            ret = False
                            ret1 = False
                    ans1 = int(input("what is the answer of the equation: " + str(a) + "-" + str(b) + "=? "))
                    if (ans1 == eval(str(a) + "-" + str(b))):
                        print("Correct")
                        correct = correct + 1
                    else:
                        print("Incorrect")
                        wrong = wrong + 1
                else:
                    a = random.randint(0, 10)  # generating a rndom number
                    b = random.randint(0, 10)
                    ans1 = int(input("what is the answer of the equation: " + str(a) + "*" + str(b) + "=? "))
                    if (ans1 == eval(str(a) + "*" + str(b))):
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

    def square_num_sequence(self):
        x = int(input('What is the largest possible square number that you want to see?'))
        i = 1
        c = i * i
        while c <= x:
            print(c)
            i = i + 1
            c = i * i

    def fib(self):
        x = int(input('How many numbers do you want to see in the fibonacci sequence? '))
        a = 0
        b = 1
        if x == 1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2, x):
                c = a + b
                a = b
                b = c
                print(c)

    def fact(self):
        f = 1
        x = int(input('What number do you want to find the factorial of?'))
        for i in range(1, x + 1):
            f = f * i
        return f

    def random_num_generator(self):
        rand1 = int(input(' Type the smallest possible random number you want '))
        rand2 = int(input(' Type the largest possible random number you want '))
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
        x = input('type down what you want to say')
        y = int(input('type down the number of times you want to print it'))
        for i in range(y):
            print(x)
class file_related_programs:
    def file_maker(self):
        x = input('Enter the text you want to save in the file')
        path_to_save = asksaveasfilename(title='enter file name')
        try:
            f = open(path_to_save, 'w')
            print(f)
        except:
            print('Unknown error occurred')
    def user_viewer(self):
        mydb = mysql.connector.connect(host='localhost', user='root', passwd='atulbhai2', database='Atul_test')
        mycursor = mydb.cursor()
        mycursor.execute('select * from people')
        for i in mycursor:
            print(i)
a1 = num_programs
b1 = word_programs()
c1 = file_related_programs()
x = input('Hello how are you doing? good/bad')
if x == 'good':
    print(' That is good!')
elif x == 'bad':
    print('I hope you will feel better soon!')
y = input('Do you want to start? Y/N')
while y.upper() == "Y":
    x = input(
        'What do you want to do quiz/calculate/print/skip count/random number generator/years to seconds/fibonacci sequence/factorial finder/create a file/square number sequence/see users')
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
    else:
        print('Invalid input!Next time type in something else.')
    y = input('Wish to continue? Y/N')