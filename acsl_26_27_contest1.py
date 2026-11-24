def findSequences(numbers):
    # Parse numbers
    numbers = numbers.split(" ")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    hot_list = numbers.copy()
    print(hot_list)
    discovered_stuff = []
    # Numbers is now the ordered list of numbers
    keep_going = True
    while keep_going:
        # Check for all the 4 types, need to handle
        first_3 = hot_list[:3]
        print(first_3)
        diffs = [first_3[1] - first_3[0], first_3[2] - first_3[1]]
        pat_typ = ""
        if diffs[0] == diffs[1]:
            pat_typ = f"A{diffs[0]}"
        elif ((diffs[0] + 1 == diffs[1]) and diffs[0] > 0) or ((diffs[0] - 1 == diffs[1]) and diffs[0] < 0):
            pat_typ = f"T{diffs[0]}"
        elif (first_3[0] + first_3[1]) == first_3[2]:
            pat_typ = f"F{diffs[0]}"
        else:
            if int(diffs[1] / diffs[0]) > 1:
                pat_typ = f"G{int(diffs[1] / diffs[0])}"
            else:
                pat_typ = f"G-{int(diffs[0] / diffs[1])}"
        discovered_stuff.append(pat_typ)
        # Now, pattern has been identified. Only thing left is to find how long it goes!!!
        for i in range(3, len(hot_list)):
            if pat_typ[0] == "A":
                if (hot_list[i - 1] + diffs[0]) == hot_list[i]:
                    # Then it keeps going on!!!
                    continue  # so i += 1!!!
                else:
                    break  # so i stops here!!!
            elif pat_typ[0] == "T":
                diffs_diff = (hot_list[i] - hot_list[i - 1]) - (hot_list[i - 1] - hot_list[i - 2])
                if ((diffs_diff == 1) and diffs[0] > 0) or ((diffs_diff == -1) and diffs[0] < 0):
                    # Then it keeps going on!!!
                    continue  # so i += 1!!!
                else:
                    break  # so i stops here!!!
            elif pat_typ[0] == "F":
                if (hot_list[i - 2] + hot_list[i - 1]) == hot_list[i]:
                    # Then it keeps going on!!!
                    continue  # so i += 1!!!
                else:
                    break  # so i stops here!!!
            else:  # pat_typ[0] == "G"
                if (hot_list[i] / hot_list[i - 1]) == (diffs[1] / diffs[0]):
                    # Then it keeps going on!!!
                    continue  # so i += 1!!!
                else:
                    break  # so i stops here!!!
        if i < len(hot_list) - 1:
            hot_list = hot_list[i:]  # EVerything up to but not including i goes away
        else:
            keep_going = False

    return " ".join(discovered_stuff)
numbers = "243 81 27 9 3 1 5 8 11 14 17 20 -2 4 2 6 8 14 9 7 4 0 -5"
print(findSequences(numbers))