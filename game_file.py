
# Necessary header files
import pygame
import math

from pygame.constants import K_DOWN, K_UP

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
pipe_green_2xpos = 550
pipe_red_2xpos = 550
pipe_green_1xpos = 260
pipe_red_1xpos = 260

bird_initial_mid = pygame.image.load("bluebird-midflap.png")
bird_initial_mid_ypos = 300
bird_initial_mid_ypos_change = 0
change = 0

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
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                bird_initial_mid_ypos_change -= 1.2
            if event.key == K_DOWN:
                bird_initial_mid_ypos_change += 1.2
        clock.tick(120 + change)
        change += 20  

    bird_initial_mid_ypos += bird_initial_mid_ypos_change

    screen.blit(bg_image,(0,-300))

    screen.blit(pipe_green,(pipe_green_1xpos,390))
    screen.blit(pipe_red,(pipe_red_1xpos,-50))
    screen.blit(pipe_green,(pipe_green_2xpos,300))
    screen.blit(pipe_red,(pipe_red_2xpos,-100))

    floor_image_1_xpos -= 1.5

    pipe_green_1xpos -= 1
    pipe_red_1xpos -= 1
    pipe_green_2xpos -= 1
    pipe_red_2xpos -= 1

    if pipe_green_1xpos <= -50:
        pipe_green_1xpos = 560
        pipe_red_1xpos = 560
    if pipe_green_2xpos <= -50:
        pipe_green_2xpos = 560
        pipe_red_2xpos = 560

    screen.blit(bird_initial_mid,(100,bird_initial_mid_ypos))

    screen.blit(floor_image_1,(floor_image_1_xpos,600))
    screen.blit(floor_image_1,(floor_image_1_xpos + 600,600))

    if floor_image_1_xpos <= -570:
        floor_image_1_xpos = 0
    pygame.display.update()    