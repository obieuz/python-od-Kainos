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
        self.radius = randint(10, 20)

    def move(self, ship_x, ship_y):
        direction = functions.calculate_direction(ship_x,ship_y,self.x,self.y)

        radians = functions.calculate_angle(self.x,self.y,ship_x,ship_y)

        if direction == 1:
            self.x += settings.alien_speed * np.sin(radians)
            self.y -= settings.alien_speed * np.cos(radians)
        elif direction == 2:
            self.x -= settings.alien_speed * np.sin(radians)
            self.y -= settings.alien_speed * np.cos(radians)
        elif direction == 3:
            self.x -= settings.alien_speed * np.sin(radians)
            self.y += settings.alien_speed * np.cos(radians)
        else:
            self.x += settings.alien_speed * np.sin(radians)
            self.y += settings.alien_speed * np.cos(radians)

        self.draw()

    def draw(self):
        pygame.draw.circle(settings.screen, settings.alien_color, (self.x, self.y), self.radius)

    def check_collision(self, bullet_x, bullet_y):
        if self.x - self.radius < bullet_x < self.x + self.radius and self.y - self.radius < bullet_y < self.y + self.radius:
            return True
        return False
