from random import randint
import pygame
import numpy as np

import functions
import settings


class Alien:
    def __init__(self,ship_x,ship_y):
        x = randint(30, settings.max_width - 30)
        y = randint(30, settings.max_height - 30)
        while x+settings.alien_space_between_ship > ship_x > x-settings.alien_space_between_ship and y+settings.alien_space_between_ship > ship_y > y-settings.alien_space_between_ship:
            x = randint(30, settings.max_width - 30)
            y = randint(30, settings.max_height - 30)
        self.x = x
        self.y = y
        self.image_index = randint(0, 1)
        self.radius = settings.alien_images[self.image_index-1].get_width() / 2

        self.mass = settings.alien_mass

    def move(self, ship_x, ship_y):
        direction = functions.calculate_direction(ship_x,ship_y,self.x,self.y)

        radians = functions.calculate_angle(self.x,self.y,ship_x,ship_y)

        vector_x, vector_y = functions.calculate_vectors(radians, settings.alien_speed, direction)

        self.x += vector_x
        self.y -= vector_y

        self.draw()

    def draw(self):
        settings.screen.blit(settings.alien_images[self.image_index], (self.x - settings.alien_images[self.image_index].get_width() / 2, self.y - settings.alien_images[self.image_index].get_height() / 2))
        # pygame.draw.circle(settings.screen, settings.alien_color, (self.x, self.y), self.radius)

    def check_collision(self, bullet_x, bullet_y):
        if self.x - self.radius < bullet_x < self.x + self.radius and self.y - self.radius < bullet_y < self.y + self.radius:
            return True
        return False
