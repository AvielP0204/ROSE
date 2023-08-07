"""
This driver does not do any action.
"""
from rose.common import obstacles, actions  # NOQA

driver_name = "EpicAwesome" #do recommend better names in the whatasapp group chat :D


def drive(world):
    try:
        obstacle = world.get((x, y - 1))
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
    elif obstacle != obstacles.NONE:
        choose_direction(world.car.x, world.car.y)

## this function returns the expected point gain (or loss) if the correct (or incorrect) action is used
def get_value(obstacle):
    if obstacle == obstacles.PENGUIN:
        return 10
    if obstacle == obstacles.CRACK:
        return 5
    if obstacle == obstacles.WATER:
        return 4
    if obstacle == obstacles.NONE:
        return 0
    return -10

## this function makes the car choose which direction to turn to
def choose_direction(xpos, ypos, expectedLeftScore=0, expectedRightScore=0, count=0):
    counter = count
    if counter < 6:
        try:
            leftObstacle = world.get((x - 1, y - (count + 1)))
        except IndexError:
            pass
        else:
            expectedLeftScore += get_value(leftObstacle)
        try:
            rightObstacle = world.get((x + 1, y - (count + 1)))
        except IndexError:
            pass
        else:
            expectedRightScore += expget_value(rightObstacle)
        return math.max(choose_direction(xpos - 1, ypos - 1,expectedLeftScore, expectedRightScore,counter + 1), choose_direction(xpos + 1, ypos - 1,expectedLeftScore, expectedRightScore,counter + 1))
    else:
        return 0




