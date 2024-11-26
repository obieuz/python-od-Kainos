from random import randint

import numpy as np
import pygame

import settings
from functions import calculate_angle, calculate_vectors, calculate_direction, check_borders


class Blackhole:
    def __init__(self, ship_x, ship_y):
        x = randint(30, settings.max_width - 30)
        y = randint(30, settings.max_height - 30)
        while x + settings.blackhole_space_between_ship > ship_x > x - settings.blackhole_space_between_ship and y + settings.blackhole_space_between_ship > ship_y > y - settings.blackhole_space_between_ship:
            x = randint(30, settings.max_width - 30)
            y = randint(30, settings.max_height - 30)
        self.x = x
        self.y = y
        self.x = x
        self.y = y
        self.mass = settings.blackhole_mass

    def draw(self):
        settings.screen.blit(settings.blackhole_image, (self.x - settings.blackhole_image.get_width() / 2,
                                                        self.y - settings.blackhole_image.get_height() / 2))

    def move_object_by_force(self, object,radius):
        r = ((self.x - object.x) ** 2 + (self.y - object.y) ** 2) ** 0.5

        if r < radius:
            return False

        fixed_r = r**settings.radius_multiplayer

        force = (settings.gravity_const * (self.mass * object.mass)) / fixed_r ** 2

        angle = calculate_angle(self.x, self.y, object.x, object.y)

        direction = calculate_direction(self.x,self.y,object.x,object.y)

        vector_x, vector_y = calculate_vectors(angle, force, direction)

        object.x += vector_x
        object.y -= vector_y

        if check_borders(object):
            return False

        return True
