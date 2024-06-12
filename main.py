#Perfect Ruler
#Goal: Make ruler with the least number of dashes
def c(s, l):
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
'''
while h:
    try:
        length_of_ruler = int(input("Welcome to Perfect Ruler Creator!\nHow long do you want your perfect ruler to be?"))
        assert length_of_ruler > 1
        h = False
    except:
        print("An Integer Value Over 1 Was Expected")
'''
print("Got Here")
m = {1, 2}
print("Hi")
c(s=m, l=10)
print("Done")