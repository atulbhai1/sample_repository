def main():
    print("\nRunning part loopDetection()...")
    print(loopDetection([0, 2, 7, 0]))  # 5
    print(loopDetection([4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3,
                         5]))  # 12841
    [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]
    [0, 13, 12, 10, 9, 8, 7, 5, 3, 2, 1, 1, 1, 10, 6, 5]

    print("\nRunning part loopDuration()...")
    print(loopDuration([0, 2, 7, 0]))  # 4
    print(loopDuration([4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3,
                        5]))  # 8038


# part 1
def loopDetection(blocks):
    blocks_history = [blocks]
    loop_length = len(blocks)
    cycles = 0
    repeated = False
    while not repeated:
        temp_blocks = blocks_history[-1].copy()
        cycles += 1
        highest_value_block_index = None
        highest_block_value = -1
        for index, block in enumerate(temp_blocks):
            if block > highest_block_value:
                highest_block_value = block
                highest_value_block_index = index
        temp_blocks[highest_value_block_index] = 0
        for i in range(1, highest_block_value+1):
            temp_blocks[(highest_value_block_index+i)%loop_length] += 1
        for block in blocks_history:
            if block == temp_blocks:
                repeated = True
                break
        else:
            blocks_history.append(temp_blocks)

    return cycles


# part 2
def loopDuration(blocks):
    #First need 2 get same list of blocks as last time, so reuse code but w/ out cycle count bcz uneeded!!!
    blocks_history = [blocks]
    loop_length = len(blocks)
    repeated = False
    repeated_index = None
    while not repeated:
        temp_blocks = blocks_history[-1].copy()
        highest_value_block_index = None
        highest_block_value = -1
        for index, block in enumerate(temp_blocks):
            if block > highest_block_value:
                highest_block_value = block
                highest_value_block_index = index
        temp_blocks[highest_value_block_index] = 0
        for i in range(1, highest_block_value + 1):
            temp_blocks[(highest_value_block_index + i) % loop_length] += 1
        for index, block in enumerate(blocks_history):
            if block == temp_blocks:
                repeated = True
                repeated_index = index
                break
        else:
            blocks_history.append(temp_blocks)
    #Now have index of repeated and index of last!!!
    mega_loop_length = len(blocks_history) - repeated_index
    return mega_loop_length


main()
