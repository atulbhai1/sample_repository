from tkinter import *
import random

def get_dropdown(prompt, options=[''], name='tk', button='OK'):
    window = Tk()
    window.configure(bg='lightblue')
    window.title(name)
    Label(window, text=prompt, bg='lightblue').grid(row=0, column=0, sticky=W)
    answer = StringVar()
    answer.set(options[0])
    answers = list(options)
    OptionMenu(window, answer, *answers).grid(row=0, column=1)
    Button(window, text=button, command=window.destroy, bg='yellow').grid(row=1, column=0, columnspan=2)
    window.mainloop()
    return answer.get()

def get_entry(prompt, name='tk', button='OK'):
    global show
    window = Tk()
    window.configure(bg='lightblue')
    window.title(name)
    show = ''
    Label(window, text=prompt, bg='lightblue').grid(row=0, column=0, sticky=W)
    entry = Entry(window)
    entry.grid(row=0, column=1)
    def ok():
        global show
        show = entry.get()
        window.destroy()
    Button(window, text=button, command=ok, bg='yellow').grid(row=2, column=0, columnspan=2)
    window.mainloop()
    return show

def display_data(data, name="tk", button="OK"):
    window = Tk()
    window.configure(bg='lightblue')
    window.title(name)
    Label(window, text=data, bg='lightblue').grid(row=0, column=0, sticky=W)
    def ok():
        window.destroy()
    Button(window, text=button, command=ok, bg='yellow').grid(row=2, column=0, columnspan=1)
    window.mainloop()

#Games!!!
def game_menu():
    while True:
        game_choice = get_dropdown("What do you want to do?", ["Simple Addition", "Number to Words", "Go to Main Menu"], "ApSeed - Game Menu", "I want to do this!")
        if game_choice == "Simple Addition":
            simple_addition()
        elif game_choice == "Number to Words":
            number_words()
        else:
            break
def simple_addition():
    number_of_times = get_dropdown("How many times do you want to play?",['1', '2', '3', '4', '5'], "ApSeed - Simple Addition Game", "Enter")
    number_correct = 0
    for i in range(int(number_of_times)):
        person = random.choice(["Bob", "Tim", "Rob", "Sally", "Cathy"])
        objects = random.choice(["apples", "oranges", "grapes", "tomatoes", "carrots"])
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        total = num1+num2

        reply = get_entry(f"{person} has {num1} {objects} and gets {num2} more {objects}. How many {objects} does {person} have now?", f"ApSeed - Simple Addition Game - Question {i+1}", "Enter")

        try:
            if int(reply) == total:
                display_data("Great! That was amazing!", f"ApSeed - Simple Addition Game - Question {i+1}", "Next")
                number_correct += 1
            else:
                display_data("That was incorrect, you'll do better next time!", f"ApSeed - Simple Addition Game - Question {i + 1}","Next")
        except:
            display_data("That was incorrect. Remember to only enter numbers!",f"ApSeed - Simple Addition Game - Question {i + 1}", "Next")

    display_data(f"You did great! You got {number_correct} out of {number_of_times} correct!", "ApSeed - Simple Addition Game", "Back to Games")

def number_words():
    number_of_times = get_dropdown("How many times do you want to play?", ['1', '2', '3', '4', '5'],
                                   "ApSeed - Number to Words", "Enter")
    number_correct = 0
    for i in range(int(number_of_times)):
        num1 = random.randint(1, 11)

        reply = get_dropdown(
            f"What is {num1} as a word?", ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"],
            f"ApSeed - Number to Words - Question {i + 1}", "Enter")

        if reply == "one":
            if num1 == 1:
                display_data("That was correct, AMAZING!!!", f"ApSeed - Number to Words - Question {i + 1}", "Next")
                number_correct += 1
            else:
                display_data("That was incorrect, I know you'll do better next time!", f"ApSeed - Number to Words - Question {i + 1}", "Next")
        elif reply == "two":
            if num1 == 2:
                display_data("That was correct, AMAZING!!!", f"ApSeed - Number to Words - Question {i + 1}", "Next")
                number_correct += 1
            else:
                display_data("That was incorrect, I know you'll do better next time!",
                             f"ApSeed - Number to Words - Question {i + 1}", "Next")
        elif reply == "three":
            if num1 == 3:
                display_data("That was correct, AMAZING!!!", f"ApSeed - Number to Words - Question {i + 1}", "Next")
                number_correct += 1
            else:
                display_data("That was incorrect, I know you'll do better next time!",
                             f"ApSeed - Number to Words - Question {i + 1}", "Next")
        elif reply == "four":
            if num1 == 4:
                display_data("That was correct, AMAZING!!!", f"ApSeed - Number to Words - Question {i + 1}", "Next")
                number_correct += 1
            else:
                display_data("That was incorrect, I know you'll do better next time!",
                             f"ApSeed - Number to Words - Question {i + 1}", "Next")
        elif reply == "five":
            if num1 == 5:
                display_data("That was correct, AMAZING!!!", f"ApSeed - Number to Words - Question {i + 1}", "Next")
                number_correct += 1
            else:
                display_data("That was incorrect, I know you'll do better next time!",
                             f"ApSeed - Number to Words - Question {i + 1}", "Next")
        elif reply == "six":
            if num1 == 6:
                display_data("That was correct, AMAZING!!!", f"ApSeed - Number to Words - Question {i + 1}", "Next")
                number_correct += 1
            else:
                display_data("That was incorrect, I know you'll do better next time!",
                             f"ApSeed - Number to Words - Question {i + 1}", "Next")
        elif reply == "seven":
            if num1 == 7:
                display_data("That was correct, AMAZING!!!", f"ApSeed - Number to Words - Question {i + 1}", "Next")
                number_correct += 1
            else:
                display_data("That was incorrect, I know you'll do better next time!",
                             f"ApSeed - Number to Words - Question {i + 1}", "Next")
        elif reply == "eight":
            if num1 == 8:
                display_data("That was correct, AMAZING!!!", f"ApSeed - Number to Words - Question {i + 1}", "Next")
                number_correct += 1
            else:
                display_data("That was incorrect, I know you'll do better next time!",
                             f"ApSeed - Number to Words - Question {i + 1}", "Next")
        elif reply == "nine":
            if num1 == 9:
                display_data("That was correct, AMAZING!!!", f"ApSeed - Number to Words - Question {i + 1}", "Next")
                number_correct += 1
            else:
                display_data("That was incorrect, I know you'll do better next time!",
                             f"ApSeed - Number to Words - Question {i + 1}", "Next")
        else:
            if num1 == 10:
                display_data("That was correct, AMAZING!!!", f"ApSeed - Number to Words - Question {i + 1}", "Next")
                number_correct += 1
            else:
                display_data("That was incorrect, I know you'll do better next time!", f"ApSeed - Number to Words - Question {i + 1}", "Next")


    display_data(f"You did great! You got {number_correct} out of {number_of_times} correct!",
                 "ApSeed - Number to Words", "Back to Games")


#Game ideas
ideas = ["Make children count the number of green objects in the house.", "Count things and write the number as a word.", "Use shaving cream to trace letters.", "Use chalk to write words on the sidewalk."]
def game_ideas():
    window = Tk()
    window.configure(bg='lightblue')
    window.title("ApSeed - Game Ideas")
    for i in range(len(ideas)):
        Label(window, text=ideas[i], bd=3, bg="yellow", relief=RAISED).grid(row=i%2, column=i//2, sticky=W)

    def ok():
        window.destroy()

    Button(window, text="Go Back To The Main Screen", command=ok, bg='yellow').grid(row=2, column=0, columnspan=1)
    window.mainloop()


print("Launching 'ApSeed'")

while True:
    main_choice = get_dropdown("Welcome to ApSeed! What do you want to do?", ['Play A Game', "Get Game Ideas", "Leave ApSeed"], "ApSeed", "I want to do this!")

    if main_choice == "Play A Game":
        game_menu()
    elif main_choice == "Get Game Ideas":
        game_ideas()
    else:
        display_data("You are leaving ApSeed. Goodbye!", "ApSeed", "OK")
        break

print("Exited 'ApSeed'")
