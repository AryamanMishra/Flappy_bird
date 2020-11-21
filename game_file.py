
# Necessary header files
import pygame
import math

# Initialising pygame
pygame.init()

# Setting screen resolution
screen = pygame.display.set_mode((570,730))

# Handling FPS
clock = pygame.time.Clock()

# Game Title
pygame.display.set_caption("FLAPPY_BIRD")

# Background image
bg_image = pygame.image.load("background-day.png")

# Increasing bg-image size to fit in
bg_image = pygame.transform.scale2x(bg_image)

pipe_green = pygame.image.load("pipe-green.png")
pipe_red = pygame.image.load("pipe-red.png")



# Floor image fields
floor_image_1 = pygame.image.load("base.png")
floor_image_1 = pygame.transform.scale2x(floor_image_1)
floor_image_1_xpos = 0
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(bg_image,(0,-300))

    screen.blit(pipe_green,(400,370))
    screen.blit(pipe_red,(400,-30))
    floor_image_1_xpos -= 1.5

    screen.blit(floor_image_1,(floor_image_1_xpos,600))
    screen.blit(floor_image_1,(floor_image_1_xpos + 600,600))

    if floor_image_1_xpos <= -570:
        floor_image_1_xpos = 0
    pygame.display.update() 
    clock.tick(100)     