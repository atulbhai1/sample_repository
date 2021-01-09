from random import randint
replies = {1 : 'magic-8 ball is busy', 2 : 'yes', 3 : 'no', 4 : 'maybe', 5 : 'it is unclear', 6 : 'almost definitely', 7 : 'probably not', 8 : 'probably', 9 : 'it shall not happen', 10 : 'it is undecided'}
while True:
    f = input()
    num = randint(1, 10)
    print(replies[num])