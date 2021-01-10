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
