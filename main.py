import pygame
import sys

screen_size = 1000
pixel_size = 10

for arg in sys.argv:
    arg = arg.replace('--', '')
    args = arg.split('=')
    print(args)

    if args[0] == 'screen-size':
        screen_size = int(args[1])

    if args[0] == 'pixel-size':
        pixel_size = int(args[1])

step = int(screen_size)
scale = int(screen_size / pixel_size)
screen_matrix = [[0]]

for i in range(0, scale):
    screen_matrix[0].append(0)
    screen_matrix.append(screen_matrix[0])

pos_x = int(scale / 2)
pos_y = pos_x

pygame.init()

screen_surface = pygame.display.set_mode([screen_size, screen_size])


def to_real_position(position):
    return position * scale


screen_surface.fill((255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen_surface,
                     (0, 0, 0),
                     (0, 0, pixel_size, pixel_size))

    pygame.display.flip()

pygame.quit()
