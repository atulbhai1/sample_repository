import os
from random import randint
from tkinter import *
import translators
import scipy.stats as stats
show = ''
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
def last_num_in_sequence(first_num, increment, operation, length):
    num = first_num
    for i in range(length - 1):
        if operation == 'addition':
            num += increment
        elif operation == 'subtraction':
            num -= increment
        elif operation == 'multiplication':
            num *= increment
        else:
            num /= increment
    return num
def play_sound(location):
    os.system(f'afplay {location}&')
def say(to_say=''):
    os.system(f"say '{to_say}'")
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
    answer.set(options[0])
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
    rex = ''
    for i in word:
        rex = rex + i
    return rex
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
def mean(numbers=[0]):
    return sum(numbers)/len(numbers)
def median(sequence=[0]):
    if len(sequence) % 2 == 0:
        ty = 'noGap'
    else:
        ty = 'Gap'
    c = len(sequence) // 2 - 1
    if ty == 'noGap':
        an = (sequence[c] + sequence[c+1]) / 2
    else:
        an = sequence[c + 1]
    return an
def mode(sequence=[0]):
    myDict = {}
    counted = []
    for i in range(len(sequence)):
        if i == 0:
            item = sequence[0]
            item_count = 0
            for t in sequence:
                if t == item:
                    item_count += 1
            counted.append(item)
            myDict.update({item : item_count})
        else:
            item = sequence[i]
            if item in counted:
                continue
            item_count = 0
            for t in sequence:
                if t == item:
                    item_count += 1
            counted.append(item)
            myDict.update({item : item_count})
    ma = {'0' : 0}
    for i, t in myDict.items():
        if t == ma[list(ma.keys())[0]]:
            ma.update({str(i) : t})
        elif t > ma[list(ma.keys())[0]]:
            ma = {str(i) : t}
    ans = list(ma.keys())
    for i in range(len(ans)):
        ans[i] = int(ans[i])
    if len(ans) == 1:
        ans = ans[0]
    return ans
def coinFlip():
    chose = randint(0, 1)
    if chose == 1:
        return 'heads'
    else:
        return 'tails'
def translate(text='hello', to_lang='english'):
    lang_key = {'english': 'en', 'tamil': 'ta', 'french': 'fr', 'spanish': 'es'}
    return translators.google(text, if_use_cn_host=True, to_language=lang_key[to_lang])
def rgbToHex(rgb):
    return '%02x%02x%02x' % rgb
def tokenizeWordsInSentence(string=''):
    wordList = []
    start = 0
    for pos, letter in enumerate(string):
        if letter == ' ':
            word = string[start : pos]
            wordList.append(word)
            start = pos + 1
        if pos == len(string) - 1:
            word = string[start: ]
            wordList.append(word)
    return wordList
def tokenizeSentence(string=''):
    sentenceList = []
    start = 0
    for pos, letter in enumerate(string):
        if letter == '.' or letter == '!' or letter == '?':
            sentence = string[start : pos + 1]
            sentenceList.append(sentence)
            start = pos + 1
        if pos == len(string) - 1:
            sentence = string[start: ]
            sentenceList.append(sentence)
    return sentenceList
def splitStringIntoList(string='', sep=' '):
    wordList = []
    start = 0
    for pos, letter in enumerate(string):
        if letter == sep:
            word = string[start : pos]
            wordList.append(word)
            start = pos + 1
        if pos == len(string) - 1:
            word = string[start: ]
            wordList.append(word)
    return wordList
def factorial(num=1):
    bigNum = 1
    if num > 1:
        bigNum *= factorial(num - 1) * num
        return bigNum
    elif num == 1:
        return 1
    if num == 0:
        return 0
def sumtorial(num=1):
    bigNum = 1
    if num > 1:
        bigNum += sumtorial(num - 1) + num
        return bigNum
    elif num == 1:
        return 1
    if num == 0:
        return 0
def oneVarianceTestForIsItMoreScenarios(n, s, sigma, p):
    Chi_sq_cal = (n - 1) * (s ** 2) / (sigma ** 2)
    criticalValue = stats.chi2.isf(1-p, n-1)
    if criticalValue < Chi_sq_cal:
        return 'The Null Hypothesis has been rejected'
    else:
        return 'The Null Hypothesis has not been rejected'
def multiplication_if_ten_is_same_and_ones_add_to_ten(x, y):
    a = x
    b = y
    def get_last_digit_and_rest(n):
        n = str(n)
        n = list(n)
        n1 = ''
        n2 = n.pop(-1)
        for i in n:
            n1 = n1+i
        n = [n1, n2]
        return n
    a = get_last_digit_and_rest(a)
    b = get_last_digit_and_rest(b)
    ans = str(int(a[0])*(int(b[0])+1)) + str(int(a[1])*int(b[1]))
    return ans