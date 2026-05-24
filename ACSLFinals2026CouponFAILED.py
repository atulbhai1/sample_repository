"""def findMaxValue(coupons):
    old_coupons = list(coupons.split(" "))
    coupons = []
    for coupon in old_coupons:
        coupons.append(int(coupon))
    #best_to_worst = sorted(coupons, reverse=True)
    #print(best_to_worst)
    max = 0
    for i in range(len(coupons)):
        temp_coupons = coupons.copy()

        if i == 0:
            left = []
            right = temp_coupons[2:]
            mine = temp_coupons.pop(i)
            temp_coupons.pop(0)
        elif i == (len(coupons)-1):
            left = temp_coupons[:i-1]
            right = []
            mine = temp_coupons.pop(i)
            temp_coupons.pop(len(temp_coupons)-1)
        else:
            left = temp_coupons[:i-1]
            right = temp_coupons[i+2:]
            mine = temp_coupons.pop(i)
            temp_coupons.pop(i-1)
            temp_coupons.pop(i-1)

        comb = newSort(left, right) + mine
        if comb > max:
            max = comb
    return max

def newSort(left, right):
    direction = False
    if left == []:
        direction = "right"
    elif right == []:
        direction = "left"
    if direction:
        if direction == "left":
            really = left
        else:
            really = right
        max = 0
        for i in range(len(really)):
            temp_coupons = really.copy()

            if i == 0:
                left = []
                right = temp_coupons[2:]
                mine = temp_coupons.pop(i)
                if temp_coupons != []:
                    temp_coupons.pop(0)
            elif i == (len(really) - 1):
                left = temp_coupons[:i - 1]
                right = []
                mine = temp_coupons.pop(i)
                temp_coupons.pop(len(temp_coupons) - 1)
            else:
                left = temp_coupons[:i - 1]
                right = temp_coupons[i + 2:]
                mine = temp_coupons.pop(i)
                temp_coupons.pop(i - 1)
                temp_coupons.pop(i - 1)

            if temp_coupons != []:
                comb = sorted(temp_coupons)[-1] + mine
            else:
                comb = mine
            if comb > max:
                max = comb
        return max
    else:
        #have to consider both!!!
        max = sorted(left)[-1] + sorted(right)[-1]
        really = right
        for i in range(len(really)):
            temp_coupons = really.copy()

            if i == 0:
                left = []
                right = temp_coupons[2:]
                mine = temp_coupons.pop(i)
                if temp_coupons != []:
                    temp_coupons.pop(0)
            elif i == (len(really) - 1):
                left = temp_coupons[:i - 1]
                right = []
                mine = temp_coupons.pop(i)
                temp_coupons.pop(len(temp_coupons) - 1)
            else:
                left = temp_coupons[:i - 1]
                right = temp_coupons[i + 2:]
                mine = temp_coupons.pop(i)
                temp_coupons.pop(i - 1)
                temp_coupons.pop(i - 1)

            if temp_coupons != []:
                comb = sorted(temp_coupons)[-1] + mine
            else:
                comb = mine
            if comb > max:
                max = comb
        really = left
        for i in range(len(really)):
            temp_coupons = really.copy()

            if i == 0:
                left = []
                right = temp_coupons[2:]
                mine = temp_coupons.pop(i)
                if temp_coupons != []:
                    temp_coupons.pop(0)
            elif i == (len(really) - 1):
                left = temp_coupons[:i - 1]
                right = []
                mine = temp_coupons.pop(i)
                temp_coupons.pop(len(temp_coupons) - 1)
            else:
                left = temp_coupons[:i - 1]
                right = temp_coupons[i + 2:]
                mine = temp_coupons.pop(i)
                temp_coupons.pop(i - 1)
                temp_coupons.pop(i - 1)

            if temp_coupons != []:
                comb = sorted(temp_coupons)[-1] + mine
            else:
                comb = mine
            if comb > max:
                max = comb
        return max



print(findMaxValue("5 7 3 1 4"))"""
def findMaxValue(coupons):
    old_coupons = list(coupons.split(" "))
    coupons = []
    for coupon in old_coupons:
        coupons.append(int(coupon))
    #best_to_worst = sorted(coupons, reverse=True)
    #print(best_to_worst)
    max = 0
    for i in range(len(coupons)):
        temp_coupons = coupons.copy()

        if i == 0:
            left = []
            right = temp_coupons[2:]
            mine = temp_coupons.pop(i)
            temp_coupons.pop(0)
        elif i == (len(coupons)-1):
            left = temp_coupons[:i-1]
            right = []
            mine = temp_coupons.pop(i)
            temp_coupons.pop(len(temp_coupons)-1)
        else:
            left = temp_coupons[:i-1]
            right = temp_coupons[i+2:]
            mine = temp_coupons.pop(i)
            temp_coupons.pop(i-1)
            temp_coupons.pop(i-1)
        print(left, right, mine)

        if (not left) and right:#max on right
            MINImax = sorted(right)[-1]
            if len(right) > 3:
                for j in range(len(right)):
                    temp_right = right.copy()
                    if j == 0:
                        rine = temp_right.pop(j)
                        temp_right.pop(0)
                    elif j == (len(right) - 1):
                        rine = temp_right.pop(j)
                        temp_right.pop(len(temp_right) - 1)
                    else:
                        rine = temp_right.pop(j)
                        temp_right.pop(j - 1)
                        temp_right.pop(j - 1)
                    t = sorted(temp_right)[-1] + rine
                    print(temp_right, t, rine)
                    if t > MINImax:
                        MINImax = t
        elif (not right) and left:#max on left
            MINImax = sorted(left)[-1]
            if len(left) > 3:
                for j in range(len(left)):
                    temp_left = left.copy()
                    if j == 0:
                        rine = temp_left.pop(j)
                        temp_left.pop(0)
                    elif j == (len(left) - 1):
                        rine = temp_left.pop(j)
                        temp_left.pop(len(temp_left) - 1)
                    else:
                        rine = temp_left.pop(j)
                        temp_left.pop(j - 1)
                        temp_left.pop(j - 1)
                    t = sorted(temp_left)[-1] + rine
                    if t > MINImax:
                        MINImax = t
        else: #Sadly, both sides have stuff :(
            MiniMax = sorted(left)[-1] + sorted(right)[-1]#max on both sides
            #Now check left for better minimaxes
            if len(left) > 3:
                for j in range(len(left)):
                    temp_left = left.copy()
                    if j == 0:
                        rine = temp_left.pop(j)
                        temp_left.pop(0)
                    elif j == (len(left) - 1):
                        rine = temp_left.pop(j)
                        temp_left.pop(len(temp_left) - 1)
                    else:
                        rine = temp_left.pop(j)
                        temp_left.pop(j - 1)
                        temp_left.pop(j - 1)
                    t = sorted(temp_left)[-1] + rine
                    if t > MINImax:
                        MINImax = t
            #Now check right for better minimaxes
            if len(right) > 3:
                for j in range(len(right)):
                    temp_right = right.copy()
                    if j == 0:
                        rine = temp_right.pop(j)
                        temp_right.pop(0)
                    elif j == (len(right) - 1):
                        rine = temp_right.pop(j)
                        temp_right.pop(len(temp_right) - 1)
                    else:
                        rine = temp_right.pop(j)
                        temp_right.pop(j - 1)
                        temp_right.pop(j - 1)
                    t = sorted(temp_right)[-1] + rine
                    if t > MINImax:
                        MINImax = t
        comb = MINImax + mine
        if comb > max:
            max = comb

    return max



print(findMaxValue("27 8 24 22 17 15 25 10 19"))