import numpy as np

import settings


def calculate_angle(character_x, character_y, object_x, object_y):
    try:
        if character_x > object_x:
            deltaX = character_x - object_x
        else:
            deltaX = object_x - character_x

        if character_y > object_y:
            deltaY = character_y - object_y
        else:
            deltaY = object_y - character_y

        radians = np.atan(deltaX / deltaY)

        return radians
    except:
        return False


def calculate_direction(character_x, character_y, object_x, object_y):
    if character_x > object_x:
        if character_y < object_y:
            return 1
        return 4
    elif character_x < object_x:
        if character_y < object_y:
            return 2
        return 3


def calculate_vectors(angle, speed, direction):
    vector_x = np.sin(angle) * speed
    vector_y = np.cos(angle) * speed

    if direction == 2 or direction == 3:
        vector_x *= -1
    if direction == 3 or direction == 4:
        vector_y *= -1
    return vector_x, vector_y
