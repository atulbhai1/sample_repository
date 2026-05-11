def fillPuzzle(n, numbers):
    grid = []
    real_numbers = [int(n) for n in numbers.split(" ")]
    my_numbers = real_numbers.copy()
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(my_numbers.pop(0))
        grid.append(temp)
    print(grid)
    stuff = []
    for a in range(n):
        for b in range(n):
            if grid[a][b] == 0:
                up = None
                down = None
                left = None
                right = None
                if a > 0:
                    up = grid[a-1][b]
                if a < n-1:
                    down = grid[a+1][b]
                if b > 0:
                    left = grid[a][b-1]
                if b < n-1:
                    right = grid[a][b+1]
                if up and down:
                    if ((up - down) == 2) or ((down - up) == 2):
                        z = (up+down)//2
                        if z not in real_numbers:
                            stuff.append(z)
                if right and left:
                    if ((right - left) == 2) or ((left - right) == 2):
                        z = (left+right)//2
                        if z not in real_numbers:
                            stuff.append(z)

                if right and up:
                    if ((right - up) == 2) or ((up - right) == 2):
                        z = (up+right)//2
                        if z not in real_numbers:
                            stuff.append(z)
                if right and down:
                    if ((right - down) == 2) or ((down - right) == 2):
                        z = (down+right)//2
                        if z not in real_numbers:
                            stuff.append(z)
                if left and up:
                    if ((left - up) == 2) or ((up - left) == 2):
                        z = (left+up)//2
                        if z not in real_numbers:
                            stuff.append(z)
                if left and down:
                    if ((left - down) == 2) or ((down - left) == 2):
                        z = (left+down)//2
                        if z not in real_numbers:
                            stuff.append(z)
    message = ""
    for q in stuff:
        message += str(q)
        if stuff[-1] != q:
            message += " "
    return message