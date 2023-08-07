"""
This driver does not do any action.
"""
from rose.common import obstacles, actions  # NOQA

driver_name = "EpicAwesome" #do recommend better names in the whatasapp group chat :D


def drive(world):
    pos = world.car


"""
none - 0
penguin - 10/0
water - 4/-10
crack - 5/-10
trash, bike, barrier - -10
"""
def count_best_score(world, pos: tuple, by_turn: bool):
    try:
        obstacle = world.get(pos)
    except:
        return 0
    score = get_points_by_obstacle(obstacle, by_turn)  # This square score
    score_forward = count_best_score(world, (pos[0], pos[1] - 1), False)
    score_left = count_best_score(world, (pos[0] - 1, pos[1] - 1), True)
    score_right = count_best_score(world, (pos[0] + 1, pos[1] - 1), True)
    
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
## this function decides what action to do based on the obstacle thats directly infront of it
def do_action(obstacle):
    if obstacle == obstacles.WATER:
        return actions.BRAKE
    elif obstacle == obstacles.PENGUIN:
        return actions.PICKUP
    elif obstacle == obstacles.CRACK:
        return actions.JUMP
    elif obstacle == obstacles.BIKE or obstacle == obstacles.TRASH or obstacle == obstacles.BARRIER:
        pass
        #TODO: write logic for which direction to choose

