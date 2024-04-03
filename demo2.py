import pygame
import sys

screen_size = 1000
pixel_size = 10


def projection(pixel_position: tuple[int, int]) -> tuple[int, int]:

    pos_x = pixel_position[0] * pixel_size
    pos_y = pixel_position[1] * pixel_size
    real_position = (pos_x, pos_y)
    return real_position


for arg in sys.argv:
    arg = arg.replace('--', '')
    args = arg.split('=')
    print(args)

    if args[0] == 'screen-size':
        screen_size = int(args[1])

    if args[0] == 'pixel-size':
        pixel_size = int(args[1])

game_size = int(screen_size / pixel_size)
scale = int(screen_size / game_size)

game_matrix = [[0] * game_size for i in range(game_size)]


pygame.init()

screen_surface = pygame.display.set_mode([screen_size, screen_size])

screen_surface.fill((255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(len(game_matrix)):
        for j in range(len(game_matrix[i])):
            pos = projection((i, j))
            pygame.draw.rect(screen_surface,
                             (game_matrix[i][j],
                              game_matrix[i][j],
                              game_matrix[i][j]),
                             (pos[0], pos[1], pixel_size, pixel_size))

    for i in range(len(game_matrix)):
        for j in range(len(game_matrix[i])):

            game_matrix[i][j] += 1

            if game_matrix[i][j] == 255:
                game_matrix[i][j] = 0

    pygame.display.flip()

pygame.quit()
