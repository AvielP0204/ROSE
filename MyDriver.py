"""
This driver does not do any action.
"""
from rose.common import obstacles, actions  # NOQA

driver_name = "EpicAwesome" #do recommend better names in the whatasapp group chat :D


def drive(world):
    try:
        obstacles = world.get ((x, y - 1))
    except IndexError:
        pass
    else:
        do_action(obstacle)

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

