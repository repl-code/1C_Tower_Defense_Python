#this code is going to be programmed by you later in this session

import pygame
import game
from finances import *
from plant import *

pygame.init() 

last_tick = pygame.time.get_ticks()
screen = pygame.display.set_mode((500, 500))
game.screen = screen

clock = pygame.time.Clock()
myPlant = plant("C:\\Users\\ragin\\Downloads\\TowerDefense\\TowerDefense\\assets\\plant.png", 45, 100)

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    myPlant.draw()
    screen.fill((255,230,230))

    #milliseconds
    frame_duration = pygame.time.get_ticks() - last_tick
    last_tick = pygame.time.get_ticks()


    game.loop(screen, frame_duration)

    pygame.display.update()
    clock.tick(60)

