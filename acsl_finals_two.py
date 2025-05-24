#ACSL Finals - Spiral

#Get inputs:
direction = input("Direction:")
horiz = int(input("Horizontal:"))
vert = int(input("Vertical:"))
M = int(input("M:"))
N = int(input("N"))

for i in range(1):
    #First, let's filter by the type of spiral
    grid = []
    if direction == "inward":

        for i in range(vert):
            grid.append([None for j in range(horiz)])

        current_pos = [0, -1]
        counter = 1
        direction = "right"
        while counter <= horiz*vert:
            if counter == horiz*vert:
                grid[current_pos[0]][current_pos[1]] = counter
                break
            try:#The one error that is expected is that the program will hit the walls and run above the range of the iterable.
                if direction == "right":
                    next_spot = current_pos
                    next_spot[1] += 1
                    if grid[next_spot[0]][next_spot[1]] is None:#If next_spot is empty
                        current_pos = next_spot
                        grid[current_pos[0]][current_pos[1]] = counter
                        counter +=1
                    else:#if the next spot is occupied
                        direction = "down"
                elif direction == "down":
                    next_spot = current_pos
                    next_spot[0] += 1
                    next_spot[1] -= 1
                    if grid[next_spot[0]][next_spot[1]] is None:#If next_spot is empty
                        current_pos = next_spot
                        grid[current_pos[0]][current_pos[1]] = counter
                        counter +=1
                        current_pos[1] += 1

                    else:#if the next spot is occupied
                        direction = "left"
                elif direction == "left":
                    next_spot = current_pos
                    next_spot[1] -= 1
                    next_spot[0] -= 1
                    if grid[next_spot[0]][next_spot[1]] is None:#If next_spot is empty
                        current_pos = next_spot
                        grid[current_pos[0]][current_pos[1]] = counter
                        counter +=1
                        current_pos[0] += 1

                    else:#if the next spot is occupied
                        direction = "up"
                elif direction == "up":
                    next_spot = current_pos
                    next_spot[0] -= 1

                    if grid[next_spot[0]][next_spot[1]] is None:  # If next_spot is empty
                        current_pos = next_spot
                        grid[current_pos[0]][current_pos[1]] = counter
                        counter += 1


                    else:  # if the next spot is occupied
                        direction = "right"


            except IndexError as  err:#If we hit the walls

                if direction == "right":
                    direction = "down"
                elif direction == "down":
                    direction = "left"
                elif direction == "left":
                    direction = "up"
                elif direction == "up":
                    direction = "right"

            print(counter)


    print(grid)