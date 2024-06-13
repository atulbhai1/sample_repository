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

print("Opened Check")
theSet = {1, 4, 6, 7, 10, 15, 28, 33, 44, 45, 59, 63, 75, 76, 79, 87, 88, 95, 98}
length_o_desired_ruler = 100
print("Hello")
for n in range(length_o_desired_ruler):
        print("Yi")
        #n is integer from 0-> length of set-1
        if n == 0:
            print("Zero is Hero!")
            continue
        print("n =! 0")
        for a in theSet:
            global purple
            purple = 1
            if a == n or length_o_desired_ruler - a == n:
                print(f"Length {n} can be measured")
                purple = 2
                break
            for b in theSet - {a}:

                if abs(a-b) == n:
                    print(f"Length {n} can be measured")
                    purple = 2
                    break
            if purple == 2:
                break
        else:
            print(f"Sadly, {n} cannot be measured")
print("Yi\nn =! 0")
print(f"Length {length_o_desired_ruler} can be measured")