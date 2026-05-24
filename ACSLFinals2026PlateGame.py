from itertools import chain, zip_longest, permutations

symbols = ["*", "+", "-", "^", "/"]
def mather(expression):
    expression = list(expression)
    for index, val in enumerate(expression):
        if type(val) == str:
            if val.isdigit():
                expression[index] = int(val)
    temp = None
    for index, val in enumerate(expression):
        if val in symbols:
            before = expression[index - 1]
            after = expression[index + 1]
            if val == "*":
                temp = before * after
            elif val == "+":
                temp = before + after
            elif val == "-":
                temp = before - after
            elif val == "^":
                if before == 0 and after == 0:
                    temp = "Rotten"
                else:
                    temp = before ** after
            elif val == "/":
                if after == 0:
                    temp = "Rotten"
                else:
                    temp = before // after
            expression.pop(0)
            expression.pop(0)
            expression.pop(0)
            break
    c = True
    for s in symbols:
        if s in expression:
            c = False
            break
    if c or temp == "Rotten":
        return temp
    else:
        expression.insert(0, temp)
        return mather(expression)
#print(mather("2*3/4+6"))
def countSolutions(target, plate):
    done_so_far = []
    numbers = []
    counter = 0
    for p in plate:
        if p.isdigit():
            numbers.append(int(p))
    sym_perms = list(permutations(symbols))
    num_perms = []
    for n in range(len(numbers)+1):
        if n >= 2:
            perm = list(permutations(numbers, n))
            num_perms += perm
    for i in range(len(num_perms)):
        numbers_temp = num_perms[i]
        for i in range(len(sym_perms)):
            symbol_temp = sym_perms[i]
            expr = [x for x in chain.from_iterable(zip_longest(numbers_temp, symbol_temp)) if x is not None]

            for i in range(len(symbol_temp)-len(numbers_temp)+1):
                expr.pop()
            result = mather(expr)

            if result == target and expr not in done_so_far:
                print(expr, "->", result)
                done_so_far.append(expr)
                counter += 1


    return counter
print(countSolutions(144, "F11235"))

