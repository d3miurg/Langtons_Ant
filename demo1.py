import pygame

pygame.init()

screen_surface = pygame.display.set_mode([1000, 1000])

red = 0
green = 0
blue = 0

x = 0
y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen_surface, (red, green, blue), (x, y, 10, 10))

    x += 10
    if x == 1000:
        x = 0
        y += 10
    if y == 1000:
        y = 0

    red += 64
    if red == 256:
        red = 0
        green += 64
    if green == 256:
        green = 0
        blue += 64
    if blue == 256:
        blue = 0

    pygame.display.flip()
