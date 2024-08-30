import pygame
import numpy as np

import functions
import settings


class Ship:
    def __init__(self):
        self.rotatedImage = settings.ship_image
        self.x = settings.max_width / 2
        self.y = settings.max_height / 2
        self.angle = 90
        self.vector_x = 0
        self.vector_y = 0
        self.direction = 1

    def draw(self):
        settings.screen.blit(self.rotatedImage,
                             (self.x - settings.imageSize["x"] / 2, self.y - settings.imageSize["y"] / 2))
        pygame.draw.circle(settings.screen, (255, 0, 0), (int(self.x), int(self.y)), 5)

    def motion(self):
        self.x += self.vector_x
        self.y -= self.vector_y
        self.draw()

    def rotate(self, cursor_x, cursor_y):
        self.angle = functions.calculate_angle(cursor_x, cursor_y, self.x, self.y)

        self.direction = functions.calculate_direction(cursor_x, cursor_y, self.x, self.y)

        if self.direction == 1:
            self.rotatedImage = pygame.transform.rotate(settings.ship_image, -np.rad2deg(self.angle))
        elif self.direction == 2:
            self.rotatedImage = pygame.transform.rotate(settings.ship_image, np.rad2deg(self.angle))
        elif self.direction == 3:
            self.rotatedImage = pygame.transform.rotate(settings.ship_image, 180 - np.rad2deg(self.angle))
        else:
            self.rotatedImage = pygame.transform.rotate(settings.ship_image, 180 + np.rad2deg(self.angle))

        self.vector_x, self.vector_y = functions.calculate_vectors(self.angle, settings.ship_speed,
                                                                   self.direction)
