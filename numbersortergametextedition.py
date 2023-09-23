import random


def space():
    for b in range(20):print("\n")
print("Welcome to \"NUMBER SORTER: TEXT EDITION\". In this game, you have to sort the Origin list from greatest to least by moving all items to the End list and keeping some stored in the Middle List to help you organize. You can move things to the Middle and Origin lists and can move things from both lists to the other or the End list. Numbers in the End list cannot be moved.")
input("Press enter to begin")
space()
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(n)
print(n)
origin = n
middle = []
end = []
while len(end) != 9 :
    print("Origin:")
    for i in origin: print(i, end=" ")
    print("", end="\n")
    print("Middle:")
    for i in middle: print(i, end=" ")
    print("", end="\n")
    print("End:")
    for i in end: print(i, end=" ")
    print("", end="\n")
    movable = []
    if len(origin) > 0:
        movable.append(1)
    if len(middle) > 0:
        movable.append(2)
    if 1 in movable and 2 in movable:
        tobemoved = int(input("Do you want to move from Origin(1) or Middle(2)?"))
    elif 1 in movable:
        tobemoved = 1
    else:
        tobemoved = 2
    if tobemoved == 1:
        dest = int(input(f"Do you want to move number {origin[-1]} from Origin to Middle(2) or End(3)?"))
    else:
        dest = int(input(f"Do you want to move number {middle[-1]} from Middle to Origin(1) or End(3)"))
    if dest == 1:
        if tobemoved == 1:
            moved = origin.pop()
        else:
            moved = middle.pop()
        origin.append(moved)
    elif dest == 2:
        if tobemoved == 1:
            moved = origin.pop()
        else:
            moved = middle.pop()
        middle.append(moved)
    else:
        if tobemoved == 1:
            moved = origin.pop()
        else:
            moved = middle.pop()
        end.append(moved)
    space()
print("Origin:")
for i in origin: print(i, end=" ")
print("", end="\n")
print("Middle:")
for i in middle: print(i, end=" ")
print("", end="\n")
print("End:")
for i in end: print(i, end=" ")
print("", end="\n")
if list(reversed(sorted(end))) == end:
    print("🎉 YOU WIN 🎉")
else:
    print("😭 YOU LOSE 😭")