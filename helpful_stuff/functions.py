import os
def sum2(*numbers):
    total = 0
    for i in numbers:
        if isinstance(i, int):
            return 'you should only put numbers in this function'
        total += i
    return total
def num_input(prompt='', accept_float='yes'):
    value = input(prompt)
    show = ''
    try:
        show = int(value)
    except ValueError:
        try:
            if accept_float == 'yes':
                show = float(value)
            else:
                raise ValueError
        except ValueError:
            if accept_float != 'yes':
                raise TypeError('You must enter a whole number!')
            else:
                raise TypeError('You must enter a number!')
    return show
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
