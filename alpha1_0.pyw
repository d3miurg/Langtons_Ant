import pygame
import sys

screen_size = 1000
pixel_size = 10

def projection(pixel_position: tuple[int, int]) -> tuple[int, int]:
    
    pos_x=pixel_position[0]*pixel_size
    pos_y=pixel_position[1]*pixel_size

    real_position=(pos_x,pos_y)

    return real_position

#for arg in sys.argv:

#    arg = arg.replace('--', '')
#    args = arg.split('=')

#    print(args)

#    if args[0] == 'screen-size':
#        screen_size = int(args[1])

#    if args[0] == 'pixel-size':
#        pixel_size = int(args[1])

game_size = int(screen_size / pixel_size)
scale=int(screen_size/game_size)

game_matrix = [[0]]
game_matrix= [[0] * game_size for i in range(game_size)]

pos_ant_x=int(game_size/2)
pos_ant_y=int(game_size/2)


# Направление Langton's ant
# 0 - left
# 1 - up
# 2 - right
# 3 - down

direction=1



color_ant = [255,0,0]

pygame.init()
pygame.display.set_caption('Langtons ant _ Alpha v1.0')

screen_surface = pygame.display.set_mode([screen_size, screen_size])

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    tmp_x=pos_ant_x
    tmp_y=pos_ant_y

    # Смена координаты
    
    if(direction==0):     
        pos_ant_x-=1

    if(direction==1):
        pos_ant_y-=1

    if(direction==2):
        pos_ant_x+=1

    if(direction==3):
        pos_ant_y+=1

    #Проверка координат на выход из массива
        
    if pos_ant_x==game_size:
        pos_ant_x=0
    elif pos_ant_x<0: 
        pos_ant_x=game_size-1
    if pos_ant_y==game_size:
        pos_ant_y=0
    elif pos_ant_y<0:
        pos_ant_y=game_size-1

    # Поворот на основе цвета и измение цвета предыдущей клетки
    # Если клетка черная, то поворот влево
    # Если клетка белая, то поворот вправо

    if game_matrix[pos_ant_y][pos_ant_x]==255:
        direction+=1
        game_matrix[pos_ant_y][pos_ant_x]=0

    elif game_matrix[pos_ant_y][pos_ant_x]==0:
        direction-=1
        game_matrix[pos_ant_y][pos_ant_x]=255

    if direction==4:
        direction=0
    elif direction==-1:
        direction=3

    for i in range(len(game_matrix)):
        for j in range(len(game_matrix[i])):        
            pos = projection((i,j))
            pygame.draw.rect(screen_surface,  (game_matrix[i][j], game_matrix[i][j], game_matrix[i][j]),(pos[0],pos[1],pixel_size,pixel_size))
    
    pos = projection((pos_ant_y,pos_ant_x))

    pygame.draw.rect(screen_surface,  (color_ant),(pos[0],pos[1],pixel_size,pixel_size))        
    pygame.time.wait(170)
    pygame.display.flip()

pygame.quit()
