import pygame

bg_color = (0, 18, 51)
bullet_speed = 5

count_aliens = 10
count_blackholes = 5

fps = 60

max_width = 800
max_height = 600
screen = pygame.display.set_mode((max_width, max_height))
ship_image = pygame.image.load("./assets/ship.png")
imageSize = {"x": ship_image.get_width(), "y": ship_image.get_height()}
ship_speed = 2
bullet_length = 10
bullet_color = (0, 255, 0)

alien_color = (0, 0, 255)
alien_speed = 1
alien_space_between_ship = 250
alien_collision_bonus = 5

blackhole_space_between_ship = 200

ship_radius = (imageSize["x"]/2 + imageSize["y"]/2)/2

game_over = pygame.image.load("./assets/explosion.png")
game_over_x = game_over.get_width()
game_over_y = game_over.get_height()

blackhole_image = pygame.image.load("./assets/blackhole.png")

blackhole_mass =3 * 1.989e30

bullet_mass = 10

blackhole_radius = 20

radius_multiplayer = 6


gravity_const = 6.67430e-11

ship_mass = 1000
alien_mass = 2000

alien_images = [pygame.image.load("./assets/alien1.png"), pygame.image.load("./assets/alien2.png")]
