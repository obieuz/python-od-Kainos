import pygame

bg_color = (0, 18, 51)
bullet_speed = 5
count_aliens = 1
max_width = 800
max_height = 600
screen = pygame.display.set_mode((max_width, max_height))
ship_image = pygame.image.load("./assets/ship.png")
imageSize = {"x": ship_image.get_width(), "y": ship_image.get_height()}
ship_speed = 2
bullet_length = 10
bullet_color = (0, 255, 0)

alien_color = (0, 0, 255)
alien_speed = 1.5
alien_space_between_ship = 50
alien_collision_bonus = 5

ship_radius = (imageSize["x"]/2 + imageSize["y"]/2)/2

game_over = pygame.image.load("./assets/explosion.png")
game_over_x = game_over.get_width()
game_over_y = game_over.get_height()
