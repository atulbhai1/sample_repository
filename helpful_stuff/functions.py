import os
show = ''
from tkinter import *
def sum2(*numbers):
    total = 0
    for i in numbers:
        if isinstance(i, int):
            return 'you should only put numbers in this function'
        total += i
    return total
def num_input(prompt='', accept_float='yes'):
    value = input(prompt)
    try:
        awns = int(value)
    except ValueError:
        try:
            if accept_float == 'yes':
                awns = float(value)
            else:
                raise ValueError
        except ValueError:
            if accept_float != 'yes':
                raise TypeError('You must enter a whole number!')
            else:
                raise TypeError('You must enter a number!')
    return awns
def make_copy(origin_file_location, copyfile_location):
    file = open(origin_file_location, 'r')
    info = file.read()
    file.close()
    file = open(copyfile_location, 'w')
    file.write(info)
    file.close()
    return copyfile_location
def len_of_a_sequence(first_num, last_num, increment_by, operation):
    num = first_num
    keep = True
    counter = 1
    if first_num == last_num:
        return counter
    while keep:
        if operation == '+':
            num += increment_by
        elif operation == '-':
            num -= increment_by
        counter += 1
        if num == last_num:
            keep = False
        elif num > last_num:
            raise ValueError('last_num needs to be a value in this sequence!')
    return counter
def sum_of_sequence(first_num, last_num, len_of_sequence):
    return (len_of_sequence*(first_num + last_num))/2
def play_sound(location):
    os.system(f'afplay {location}&')
def say(to_say=''):
    os.system(f"say '{to_say}'")
def word_splitter(words=''):
    if not isinstance(words, str):
        raise TypeError('The value of words must be a string!')
    words = words + ' '
    separated_words = []
    b = 0
    for i in range(len(words)):
        if i != 0:
            if words[i] == ' ':
                separated_words.append(words[b:i])
                b = i + 1
    return separated_words
def get_entry(prompt, name='tk', button='OK'):
    global show
    window = Tk()
    window.title(name)
    show = ''
    Label(window, text=prompt).grid(row=0, column=0, sticky=W)
    entry = Entry(window)
    entry.grid(row=0, column=1)
    def ok():
        global show
        show = entry.get()
        window.destroy()
    Button(window, text=button, command=ok).grid(row=2, column=0, columnspan=2)
    window.mainloop()
    return show
def get_dropdown(prompt, options=[''], name='tk', button='OK'):
    window = Tk()
    window.title(name)
    Label(window, text=prompt).grid(row=0, column=0, sticky=W)
    answer = StringVar()
    answer.set(options[1])
    answers = list(options)
    OptionMenu(window, answer, *answers).grid(row=0, column=1)
    Button(window, text=button, command=window.destroy).grid(row=1, column=0, columnspan=2)
    window.mainloop()
    return answer.get()
def dictionary_flipper(dictionary={'' : ''}):
    ret = {}
    for key, value in dictionary.items():
        ret.update({value : key})
    return ret
def list_or_tuple_to_str(ob=['']):
    rex = ''
    for i in ob:
        rex = rex + i
    return rex
def encoder(words=''):
    key = {'': '', ' ': ' ', 'a': '~', 'b': '!', 'c': '@', 'd': '#', 'e': '$', 'f': '%', 'g': '^', 'h': '&', 'i': '*',
           'j': '(', 'k': ')', 'l': '-', 'm': '_', 'n': '=', 'o': '+', 'p': '[', 'q': '{', 'r': ']', 's': '}',
           't': '\\', 'u': '|', 'v': ';', 'w': ':', 'x': '\'', 'y': '"', 'z': ',', '~': 'a', '!': 'b', '@': 'c',
           '#': 'd', '$': 'e', '%': 'f', '^': 'g', '&': 'h', '*': 'i', '(': 'j', ')': 'k', '-': 'l', '_': 'm', '=': 'n',
           '+': 'o', '[': 'p', '{': 'q', ']': 'r', '}': 's', '\\': 't', '|': 'u', ';': 'v', ':': 'w', '\'': 'x',
           '"': 'y', ',': 'z', 'A': '~', 'B': '!', 'C': '@', 'D': '#', 'E': '$', 'F': '%', 'G': '^', 'H': '&', 'I': '*',
           'J': '(', 'K': ')', 'L': '-', 'M': '_', 'N': '=', 'O': '+', 'P': '[', 'Q': '{', 'R': ']', 'S': '}',
           'T': '\\', 'U': '|', 'V': ';', 'W': ':', 'X': '\'', 'Y': '"', 'Z': ','}
    word = list(words)
    for i in range(len(word)):
        try:
            word[i] = key[word[i]]
        except:pass
    re = ''
    for i in word:
        re = re + i
    return re
def capitalize_dict(dictionary={'' : ''}):
    ret = {}
    for key, value in dictionary.items():
        ret.update({key.capitalize() : value.capitalize()})
    return ret
def uppercase_dict(dictionary={'' : ''}):
    ret = {}
    for key, value in dictionary.items():
        ret.update({key.upper() : value.upper()})
    return ret
