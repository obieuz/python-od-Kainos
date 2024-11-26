import pygame
import numpy as np

import functions
import settings


class Bullet:
    def __init__(self, x, y, angle, direction):
        self.x = x
        self.y = y
        self.angle = angle
        self.direction = direction
        self.mass = settings.bullet_mass

        self.vector_x, self.vector_y = functions.calculate_vectors(self.angle, settings.bullet_speed, self.direction)

    def draw(self):
        vector_x, vector_y = functions.calculate_vectors(self.angle, settings.bullet_speed, self.direction)

        pygame.draw.line(settings.screen, settings.bullet_color, (self.x, self.y), (self.x + vector_x, self.y - vector_y))

    def move(self):
        self.x += self.vector_x
        self.y -= self.vector_y

        self.draw()

    def check_borders(self):
        if self.x > settings.max_width or self.x < 0 or self.y > settings.max_height or self.y < 0:
            return True
        return False
