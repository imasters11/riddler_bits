from random import randint


num_disks = 5

def make_move(towers):
    start_tower = randint(0, 2)
    if not any(towers[start_tower]):
        # start tower has no disks, invalid. try again
        return make_move(towers)

    # attempt to shift the top disk by 1 or 2 towers
    dest_tower = (start_tower + randint(1, 2)) % 3
    
    # get smallest disk on the start tower
    disk_size = 0
    for i, disk_position in enumerate(towers[start_tower]):
        if disk_position:
            disk_size = i
            break

    # check if theres a smaller disk on the dest tower
    if any(towers[dest_tower][:disk_size + 1]):
            return make_move(towers)

    # move is valid, make the move
    towers[start_tower][disk_size] = False
    towers[dest_tower][disk_size] = True

    return dest_tower


def play_game():
    towers = [[False] * num_disks if i != 0 else [True] * num_disks for i in range(3)]
    num_moves = 0
    while True:
        dest_tower = make_move(towers)
        num_moves += 1

        # only have to check the tower we moved a disk to since
        # the game always ends with moving the smallest disk there
        if dest_tower != 0 and all(towers[dest_tower]):
            break

    return num_moves


iterations = 10000
total_moves = 0
for i in range(iterations):
    total_moves += play_game()

print(total_moves / iterations) 
