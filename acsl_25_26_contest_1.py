#!/bin/python3

import math
import os
import random
import re
import sys

from numba.core.cgutils import true_byte


#
# Complete the 'findCreature' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING guess
#  2. STRING distance
#

def digitize(thing):
    if thing.isdigit():
        return int(thing)
    else:
        if thing == "A":
            return 10
        elif thing == "B":
            return 11
        elif thing == "C":
            return 12
        elif thing == "D":
            return 13
        elif thing == "E":
            return 14
        elif thing == "F":
            return 15


def undigitize(thing):
    if thing <= 9:
        return str(thing)
    else:
        if thing == 10:
            return "A"
        elif thing == 11:
            return "B"
        elif thing == 12:
            return "C"
        elif thing == 13:
            return "D"
        elif thing == 14:
            return "E"
        elif thing == 15:
            return "F"


def graph(spots, center):
    for i in range(16):
        for j in range(16):
            tracker = False
            for spot in spots:
                if spot[0] == i and spot[1] == j:
                    print("X", end=" | ")
                    tracker = True
                    break
            if not tracker:
                if center[0] == i and center[1] == j:
                    print("~", end=" | ")
                else:
                    print("O", end=" | ")
        print()


def decode(thing):
    return digitize(thing[0]) * 16 + digitize(thing[1])


def findCreature(guess, distance):
    row = guess[0]
    column = guess[1]
    row = digitize(row)
    distance = digitize(distance)
    column = digitize(column)
    spots = []
    for i in range(distance):
        if (row + distance - i) <= 15 and (column + i) <= 15:
            spots.append((row + distance - i, column + i))
        if (row - distance + i) >= 0 and (column - i) >= 0:
            spots.append((row - distance + i, column - i))
        if (row - i) >= 0 and (column + distance - i) <= 15:
            spots.append((row - i, column + distance - i))
        if (row + i) <= 15 and (column - distance + i) >= 0:
            spots.append((row + i, column - distance + i))
    graph(spots, (row, column))
    max_sum = ["", 0]
    for spot in spots:
        if decode(undigitize(spot[0]) + undigitize(spot[1])) > max_sum[1]:
            max_sum[1] = decode(undigitize(spot[0]) + undigitize(spot[1]))
            max_sum[0] = undigitize(spot[0]) + undigitize(spot[1])
    print(max_sum[0])
    min_sum = ["", 1000]
    for spot in spots:
        if decode(undigitize(spot[0]) + undigitize(spot[1])) < min_sum[1]:
            min_sum[1] = decode(undigitize(spot[0]) + undigitize(spot[1]))
            min_sum[0] = undigitize(spot[0]) + undigitize(spot[1])
    print(min_sum[0])
    return min_sum[0] + " " + max_sum[0]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    guess = input()

    distance = input()

    result = findCreature(guess, distance)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
"""
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findCreature' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING guess
#  2. STRING distance
#

def digitize(thing):
    if thing.isdigit():
        return int(thing)
    else:
        if thing == "A":
            return 10
        elif thing == "B":
            return 11
        elif thing == "C":
            return 12
        elif thing == "D":
            return 13
        elif thing == "E":
            return 14
        elif thing == "F":
            return 15

def undigitize(thing):
    if thing <= 9:
        return str(thing)
    else:
        if thing == 10:
            return "A"
        elif thing == 11:
            return "B"
        elif thing == 12:
            return "C"
        elif thing == 13:
            return "D"
        elif thing == 14:
            return "E"
        elif thing == 15:
            return "F"



def findCreature(guess, distance):
    row = guess[0]
    column = guess[1]
    row = digitize(row)
    d = digitize(distance)
    column = digitize(column)
    print(row, column, d)
    minSpot = ""
    maxSpot = ""
    if (row - d) >= 0:
        nrow = row-d
        minSpot =  undigitize(nrow)+undigitize(column)
    else:
        found = False
        counter = 1
        while not found:
            if row - (d-counter) >= 0:
                nrow = row-(d-counter)
                if column-counter >= 0:
                    ncolumn = column-counter
                    minSpot =  undigitize(nrow)+undigitize(ncolumn)
                    found = True
                    continue
            if counter > d:
                if row - (d-counter) <= 15 and row - (d-counter) >=0:
                    nrow = row - (d-counter)
                    if column-(2*d-counter) <= 15 and column-(2*d-counter) >=0:
                        ncolumn = column-(2*d-counter)
                        minSpot =  undigitize(nrow)+undigitize(ncolumn)
                        found = True
                        continue

            counter += 1


    if (row+d) <= 15:
        #print(row*2, d*2, "ALIVE!!!")
        nrow = row+d
        maxSpot = undigitize(nrow)+undigitize(column)
    else:
        found = False
        counter = 1
        while not found:
            if row + (d-counter) <=15:
                nrow = row+(d-counter)
                if column+counter <=15:
                    ncolumn = column+counter
                    maxSpot =  undigitize(nrow)+undigitize(ncolumn)
                    found = True
                    continue
            if counter > d:
                if row + (d-counter) <= 15 and row + (d-counter) >=0:
                    nrow = row + (d-counter)
                    if column+((2*d)-counter) >= 0 and column+((2*d)-counter) <= 15:
                        ncolumn = column+((2*d)-counter)
                        minSpot =  undigitize(nrow)+undigitize(ncolumn)
                        found = True
                        continue

            counter += 1

    return minSpot+" "+maxSpot



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    guess = input()

    distance = input()

    result = findCreature(guess, distance)

    fptr.write(result + '\n')

    fptr.close()
"""