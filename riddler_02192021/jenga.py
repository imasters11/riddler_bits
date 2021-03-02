import random


def get_rand_midpoint(prev_midpoint):
    return random.uniform(prev_midpoint - 0.5, prev_midpoint + 0.5)

total = 0
iterations = 100000

for i in range(iterations):
    # represent blocks by their midpoint (all len 1)
    # c_gravs list to represent the center of gravity from the ith block up to the top
    # WLOG we can place the first block where we like. I place it at 0
    blocks = [0]
    c_gravs = [0]
    while(True):
        new_block = get_rand_midpoint(blocks[-1])
    
        # calculate the new centers of gravity
        for i, center in enumerate(c_gravs):
            # number of blocks to the top, including this one
            # this is the number of blocks we have considered in the cgrav calc so far
            num_blocks = len(c_gravs) - i
    
            # new center of gravity is the weighted average of the existing cgrav
            # with that of the new block
            c_gravs[i] = (num_blocks * center + new_block) / (num_blocks + 1)
    
            # check if the new center of gravity falls outside the block below
            # dont check for block 0 since its on the ground
            if i == 0:
                continue
    
            if abs(c_gravs[i] - blocks[i - 1]) > 0.5:
                break
        else:
            blocks.append(new_block)
            c_gravs.append(new_block)
            # this is kinda jank
            # continue if we make it through the stack without breaking
            continue
    
        # if we get here, we have found a breaking point, break the outer loop
        break
    
    total += (len(blocks) + 1)

print(total / iterations)
