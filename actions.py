from directions import *

UP = NORTH
DOWN = SOUTH
LEFT = WEST
RIGHT = EAST

def RotateDirVec45Deg(dirVec,rotation):
    if rotation == CW:
        if dirVec == NORTH:
            return NORTHEAST
        elif dirVec == NORTHEAST:
            return EAST
        elif dirVec == EAST:
            return SOUTHEAST
        elif dirVec == SOUTHEAST:
            return SOUTH
        elif dirVec == SOUTH:
            return SOUTHWEST
        elif dirVec == SOUTHWEST:
            return WEST
        elif dirVec == WEST:
            return NORTHWEST
        elif dirVec == NORTHWEST:
            return NORTH

    elif rotation == CCW:
        if dirVec == NORTH:
            return NORTHWEST
        elif dirVec == NORTHWEST:
            return WEST
        elif dirVec == WEST:
            return SOUTHWEST
        elif dirVec == SOUTHWEST:
            return SOUTH
        elif dirVec == SOUTH:
            return SOUTHEAST
        elif dirVec == SOUTHEAST:
            return EAST
        elif dirVec == EAST:
            return NORTHEAST
        elif dirVec == NORTHEAST:
            return NORTH

def RotateDirVec90Deg(dirVec,rotation):
    return RotateDirVec45Deg(RotateDirVec45Deg(dirVec,rotation),rotation)

def RotateDirVec180Deg(dirVec,rotation):
    return RotateDirVec90Deg(RotateDirVec90Deg(dirVec,rotation),rotation)
