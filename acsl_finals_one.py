#ACSL Finals - Marble Game

#First, get inputs

num = int(input("Enter Number N:"))
original = input("Enter original stacks:")
moves = input("Enter moves separated by spaces")

for i in range(1):
    stacks = original.split()
    prepared_stacks = []
    for stack in stacks:
        prepared_stack = list(stack)
        prepared_stacks.append(prepared_stack[::-1])
    prepared_stacks.append(list())
    prepared_stacks.append(list())
    #Now we have stacks prepared, these are based off the provided stacks. 2 extra empty stacks exist

    half_cooked_moves = moves.split()
    prepared_moves = []
    for move in half_cooked_moves:
        prepared_moves.append([int(move[0]), int(move[1])])
    #Moves are also broken up and turned into integers now

    try:
        for move in prepared_moves:

            perfect_stack = True
            last_color = None
            for color in prepared_stacks[move[0]-1]:
                if last_color is None:
                    last_color = color
                else:
                    if color != last_color:
                        perfect_stack = False
            if len(prepared_stacks[move[0]-1]) != num:#If the length of the stack is not the desired number
                perfect_stack = False#It's not perfect
            if perfect_stack:#If the stack they want to remove from is perfect
                raise BaseException#ILLEGAL MOVE!!!


            #Shift marbles to imaginary temp stack
            temp = [prepared_stacks[move[0]-1].pop(),]#Note: If stack is empty, an exception is thrown by Python, so go to failure under except
            try:  # There might not be more marbles. In that case, the exception can lead to a break
                while True:
                    last_marble = prepared_stacks[move[0]-1][-1]#Get the next marble
                    if last_marble == temp[0]:#Check if it matches with the one previously collected
                        temp.append(prepared_stacks[move[0]-1].pop())#If it does, pop it and add it to temp
                    else:#If it doesn't match
                        break#Stop checking

            except:
                pass

            # Temp has been made now
            if len(prepared_stacks[move[1] - 1]) > 0:

                if temp[0] == prepared_stacks[move[1] - 1][-1]:#If the color of the temp is the same as that at the top of the stack
                    pass#Continue onwards
                else:#It's illegal
                    raise BaseException#Illegal move! Stop execution

            #If the len was not above 0, it will come here without the color check
            prepared_stacks[move[1] - 1].extend(temp)  # Add temp to the end of the desired stack

            if len(prepared_stacks[move[1] - 1]) > num:  # If the length of the new stack was too long, the move was illegal
                raise BaseException  # Illegal move! Stop execution


        #ALL MOVES HAVE BEEN EXECUTED
        for stack in prepared_stacks:
            perfect_stack = True
            last_color = None
            for color in stack:
                if last_color is None:
                    last_color = color
                else:
                    if color != last_color:
                        perfect_stack = False
            if len(stack) != num and len(stack) != 0:
                perfect_stack = False
            if not perfect_stack:
                raise BaseException#It needs to be perfect

        result = ""
        #They made it! They got all perfect stacks
        for stack in prepared_stacks:
            if len(stack) == 0:
                result += "E"
            else:
                result += stack[-1]

    except:
        result = ""
        for id, stack in enumerate(prepared_stacks, start=1):
            if len(stack) != 0:
                perfect_stack = True
                last_color = None
                for color in stack:
                    if last_color is None:
                        last_color = color
                    else:
                        if color != last_color:
                            perfect_stack = False
                if len(stack) != num:
                    perfect_stack = False
                if not perfect_stack:
                    result += str(id)
print("")