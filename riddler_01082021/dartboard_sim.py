import random

center = (0.5, 0.5)
board_radius = 0.5

def dist_to_center(point):
    return ((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2 ) ** 0.5

def get_random_point():
    return (random.random(), random.random())

shots = []
for i in range(1000000):
    last_radius = board_radius
    shot_num = 0
    while(True):
        dist = dist_to_center(get_random_point())
        if dist > board_radius:
            # point is off board, throw out
            continue
        shot_num += 1
        if dist > last_radius:
            # hit the board but further away than the last shot
            shots.append(shot_num)
            break
        # hit the board close to the last shot
        last_radius = dist


print(shots)
print(sum(shots) / len(shots))
