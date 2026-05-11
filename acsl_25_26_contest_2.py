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
#G6B & G7B
def verifyPlate(plate):
    NumberCount = sum(c.isdigit() for c in plate)
    letterCount = sum(c.isalpha() for c in plate)
    length = len(plate.replace("-", ""))
    code = ""
    if length == 6:
        if NumberCount == 6:
            code = "G6A"
        elif NumberCount == 2 and letterCount == 4:
            if sum(c.isalpha() for c in plate[:3]) == 3:
                if plate[3] == "-":
                    if sum(c.isdigit() for c in plate[4:7]) == 2:
                        if sum(c.isalpha() for c in plate[4:7]) == 1:
                            code = "G6B"
        elif NumberCount == 3 and letterCount == 3:
            if sum(c.isalpha() for c in plate[:3]) == 3:
                if sum(c.isdigit() for c in plate[4:7]) == 3:
                    if plate[3] == "-":
                        code="G6C"
            elif sum(c.isdigit() for c in plate[:3]) == 3:
                if sum(c.isalpha() for c in plate[4:7]) == 3:
                    if plate[3] == "-":
                        code="G6D"
    elif length == 7:
        if NumberCount == 7:
            code = "G7A"
        elif NumberCount == 3 and letterCount == 4:
            if sum(c.isalpha() for c in plate[:3]) == 3:
                if plate[3] == "-":
                    if sum(c.isdigit() for c in plate[4:8]) == 3:
                        if sum(c.isalpha() for c in plate[4:8]) == 1:
                            code = "G7B"
        elif NumberCount == 4 and letterCount == 3:
            if sum(c.isdigit() for c in plate[:4]) == 4:
                if sum(c.isalpha() for c in plate[4:7]) == 3:
                    code="G7C"
            elif sum(c.isalpha() for c in plate[:3]) == 3:
                if sum(c.isdigit() for c in plate[3:7]) == 4:
                    code="G7D"
            elif plate.isalnum():
                code = "G7F"
        elif NumberCount == 5 and letterCount == 2:
            if sum(c.isdigit() for c in plate[3:7]) == 5:
                if sum(c.isalpha() for c in plate[:2]) == 2:
                    if plate[2] == "-":
                        code="G7E"

    if code == "":
        if length <= 7 and sum(c.isalpha() for c in plate[:2]) == 2:
            if len(plate.replace(' ', '')) == 7 or len(plate.replace('-', '')) == 7:
                 code = "V"
    if code == "":
        code = "IV"
    return code


verifyPlate(input())
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