"""
This driver does not do any action.
"""
from rose.common import obstacles, actions  # NOQA

driver_name = "EpicAwesome1" #do recommend better names in the whatasapp group chat :D


def drive(world):
    max_iterations = 4
    car_pos = (world.car.x, world.car.y)

    pos_forward = get_forward_pos(car_pos)
    pos_left = get_left_pos(car_pos)
    pos_right = get_right_pos(car_pos)

    try:
        obs_forward = world.get(pos_forward)
    except IndexError:
        obs_forward = obstacles.TRASH
    try:
        obs_left = world.get(pos_left)
    except IndexError:
        obs_left = obstacles.TRASH
    try:
        obs_right = world.get(pos_right)
    except IndexError:
        obs_right = obstacles.TRASH

    score_forward = count_best_score(world, pos_forward, False, max_iterations)
    score_left = count_best_score(world, pos_left, True, max_iterations)
    score_right = count_best_score(world, pos_right, True, max_iterations)
    if get_points_by_obstacle(obs_forward, False) >= 0 and score_right < score_forward > score_left:  # Forward score is the best
        return do_action(world.get(pos_forward))
    if get_points_by_obstacle(obs_left, True) >= 0 and score_forward < score_left > score_right:  # Left score is the best
        return actions.LEFT
    if get_points_by_obstacle(obs_right, True) >= 0 and score_forward < score_right > score_left:  # Right score is the best
        return actions.RIGHT
    return actions.NONE


"""
none - 0
penguin - 10/0
water - 4/-10
crack - 5/-10
trash, bike, barrier - -10
"""


def count_best_score(world, pos, by_turn: bool, iterations):
    if iterations == 0:
        return 0
    try:
        obstacle = world.get(pos)
    except IndexError:
        return -30

    pos_forward = get_forward_pos(pos)
    pos_left = get_left_pos(pos)
    pos_right = get_right_pos(pos)

    score = get_points_by_obstacle(obstacle, by_turn)  # This square score
    score_forward = count_best_score(world, pos_forward, False, iterations - 1)
    score_left = count_best_score(world, pos_left, True, iterations - 1)
    score_right = count_best_score(world, pos_right, True, iterations - 1)

    return score + max([score_forward, score_left, score_right])


def get_points_by_obstacle(obstacle, by_turn: bool):
    if obstacle == obstacles.NONE:
        return 0
    if not by_turn:
        if obstacle == obstacles.PENGUIN:
            return 10
        if obstacle == obstacles.WATER:
            return 4
        if obstacle == obstacles.CRACK:
            return 5
    else:
        if obstacle == obstacles.PENGUIN:
            return 0
    return -10


# this function decides what action to do based on the obstacle thats directly infront of it
def do_action(obstacle):
    if obstacle == obstacles.WATER:
        return actions.BRAKE
    elif obstacle == obstacles.PENGUIN:
        return actions.PICKUP
    elif obstacle == obstacles.CRACK:
        return actions.JUMP
    return actions.NONE


def get_forward_pos(pos):
    return [pos[0], pos[1] - 1]


def get_left_pos(pos):
    return [pos[0] - 1, pos[1] - 1]


def get_right_pos(pos):
    return [pos[0] + 1, pos[1] - 1]
