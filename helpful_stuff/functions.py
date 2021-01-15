import os
def sum2(*numbers):
    total = 0
    for i in numbers:
        if isinstance(i, int):
            return 'you should only put numbers in this function'
        total += i
    return total
def num_input(prompt=''):
    value = input(prompt)
    try:
        show = int(value)
    except ValueError:
        try:
            show = float(value)
        except ValueError:
            raise TypeError('You must enter a number')
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
