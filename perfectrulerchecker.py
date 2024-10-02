#Perfect Ruler
#Goal: Check Perfect Ruler
#the blotted-out lines were for a perfect ruler maker that just didn't want to work :(
'''
def c(s={1, 2}, l=3):
    print("Opened Check")
    theSet = s
    length_o_desired_ruler = l
    print("Hello")
    for n in range(length_o_desired_ruler):
        print("Yi")
        #n is integer from 0-> length of set-1
        if n == 0:
            print("Zero is Hero!")
        print("n =! 0")
        for a in theSet:
            if a == n or length_o_desired_ruler - a == n:
                print(f"Length {n} can be measured")
                yield True
                break
            for b in theSet - {a}:
                if abs(a-b) == n:
                    print(f"Length {n} can be measured")
                    yield True
                    break
        else:
            print(f"Sadly, {n} cannot be measured")
            yield False

h = True

while h:
    try:
        length_of_ruler = int(input("Welcome to Perfect Ruler Creator!\nHow long do you want your perfect ruler to be?"))
        assert length_of_ruler > 1
        h = False
    except:
        print("An Integer Value Over 1 Was Expected")

print("Got Here")
m = {1, 2}
print("Hi")
c()
print("Done")
'''
class CannotBeMeasuredError(BaseException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

print("Opened Perfect Ruler Checker")
#Get Length
getLength = True
while getLength:
    try:
        length_o_desired_ruler = int(input("What is the length of the perfect ruler you want to check?"))
        assert length_o_desired_ruler > 1
        getLength = False
    except:
        print("Your perfect ruler has to be an integer over 1")
getNumOfMarks = True
#length_o_desired_ruler = 100 -> Example used for testing

#get the number of marks on the ruler
while getNumOfMarks:
    try:
        numberOfMarks = int(input("What is the number of marks used in your solution to this perfect ruler?"))
        assert numberOfMarks > 0
        getNumOfMarks = False
    except:
        print("Your perfect ruler has to have at least 1 mark on it and must be an integer value long")
#get the marks!!!
theSetOfMarks = []
for i in range(numberOfMarks):
    getSolution = True
    while getSolution:
        try:
            markToAdd = int(input("What is the mark you want to add to your ruler?"))
            assert markToAdd > 0
            getSolution = False
            theSetOfMarks.append(markToAdd)
        except:
            print("The marks on your ruler have to be greater than 0 and have to be integers")

theSetOfMarks = list(set(theSetOfMarks))# Removes redundant values

#theSetOfMarks = list({1, 4, 6, 7, 10, 15, 28, 33, 44, 45, 59, 63, 75, 76, 79, 87, 88, 95, 98}) -> Example used for testing

print(f"This checks if the set of numbers provided is sufficient to make a perfect {length_o_desired_ruler} length ruler")
print("O can be measured by all rulers")
for n in range(1, length_o_desired_ruler):
    print(f"Started New Number: {n}")
    continueCheckForN = True
    locationInSet = 0
    while continueCheckForN:
        mark = theSetOfMarks[locationInSet]
        if mark == n or length_o_desired_ruler - mark == n:
            print(f"{n} can be measured")
            continueCheckForN = False
        else:
            backupChecker = True
            setWithoutMark = theSetOfMarks.copy()
            setWithoutMark.pop(locationInSet)
            otherLocationInSet = 0
            while backupChecker:
                otherMark = setWithoutMark[otherLocationInSet]
                if abs(otherMark - mark) == n:
                    print(f"{n} can be measured")
                    backupChecker = False
                    continueCheckForN = False
                else:
                    if otherLocationInSet == (len(setWithoutMark) - 1):
                        backupChecker = False
                    else:
                        otherLocationInSet += 1
        if continueCheckForN is True:
            if locationInSet == (len(theSetOfMarks) - 1):
                raise CannotBeMeasuredError(f"{n} cannot be measured!")
            else:
                locationInSet += 1
print(f"{length_o_desired_ruler} can be measured by this ruler because it's {length_o_desired_ruler} units long")