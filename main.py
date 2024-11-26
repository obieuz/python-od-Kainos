import pygame
import time
import settings
from classes.Game import Game

max_width = 800
max_height = 600

clock = pygame.time.Clock()

game = Game()
game.begin()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            game.mouse_motion()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_SPACE]:
        game.shoot()

    if game.gravity_force():
        running = False

    game.draw()

    if game.check_collision():
        running = False
    clock.tick(settings.fps)

settings.screen.fill(settings.bg_color)
settings.screen.blit(settings.game_over, (settings.max_width / 2 - settings.game_over_x / 2,
                                          settings.max_height / 2 - settings.game_over_y / 2))
pygame.display.flip()
time.sleep(1)

pygame.quit()
