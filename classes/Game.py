from random import randint

import pygame

from classes.Blackhole import Blackhole
from classes.Ship import Ship
from classes.Alien import Alien
from classes.Bullet import Bullet
import numpy as np
import settings
import functions
import math


class Game:
    def __init__(self):
        self.ship = Ship()
        self.bullets = []
        self.aliens = []
        self.blackholes = []

    def begin(self):
        pygame.init()
        settings.screen.fill(settings.bg_color)
        for i in range(settings.count_aliens):
            self.aliens.append(Alien(self.ship.x, self.ship.y))

        self.create_blackholes()

    def check_collision(self):
        for bullet in self.bullets:
            if bullet.check_borders():
                self.bullets.remove(bullet)

        for bullet in self.bullets:
            for alien in self.aliens:
                if alien.check_collision(bullet.x, bullet.y):
                    self.aliens.remove(alien)
                    self.bullets.remove(bullet)
                    self.aliens.append(Alien(self.ship.x, self.ship.y))
                    break

        for alien in self.aliens:
            result = math.sqrt(math.pow(self.ship.x-alien.x,2)+math.pow(self.ship.y-alien.y,2))
            if result < settings.ship_radius+ alien.radius:
                return True

    def draw(self):
        settings.screen.fill(settings.bg_color)

        self.ship.motion()

        for bullet in self.bullets:
            if bullet.check_borders():
                self.bullets.remove(bullet)

            bullet.move()

        for alien in self.aliens:
            alien.move(self.ship.x,self.ship.y)

        for blackhole in self.blackholes:
            blackhole.draw()

        pygame.display.flip()

    def shoot(self):

        bullet_x = self.ship.x + settings.imageSize["x"]/2
        bullet_y = self.ship.y - settings.imageSize["y"]/4

        if self.ship.direction == 2:
            bullet_x = self.ship.x - settings.imageSize["x"] / 4
            bullet_y = self.ship.y - settings.imageSize["y"] / 4
        elif self.ship.direction == 3:
            bullet_x = self.ship.x - settings.imageSize["x"] / 4
            bullet_y = self.ship.y + settings.imageSize["y"]/2
        elif self.ship.direction == 4:
            bullet_x = self.ship.x + settings.imageSize["x"]/2
            bullet_y = self.ship.y + settings.imageSize["y"]/2

        self.bullets.append(
            Bullet(bullet_x, bullet_y, self.ship.angle, self.ship.direction))

    def mouse_motion(self):
        cursor_x, cursor_y = pygame.mouse.get_pos()

        self.ship.rotate(cursor_x, cursor_y)

    def create_blackholes(self):
        for i in range(settings.count_blackholes):
            x = randint(30, settings.max_width - 30)
            y = randint(30, settings.max_height - 30)
            self.blackholes.append(Blackhole(x,y))

    def gravity_force(self):
        for blackhole in self.blackholes:
            for alien in self.aliens:
                if not blackhole.move_object_by_force(alien,settings.blackhole_radius):
                    self.aliens.remove(alien)
                    self.aliens.append(Alien(self.ship.x, self.ship.y))

            for bullet in self.bullets:
                if not blackhole.move_object_by_force(bullet,settings.blackhole_radius/2):
                    self.bullets.remove(bullet)

            if not blackhole.move_object_by_force(self.ship,settings.blackhole_radius):
                return True

