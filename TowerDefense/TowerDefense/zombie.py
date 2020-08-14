import pygame
import game
import math

class zombie():
    def __init__(self, screen, health=1):
        self.screen = screen
        self.image = None
        self.x = 0
        self.y = 0
        self.direction = 0

        self.screen = screen

        self.image = pygame.image.load("C:\\Users\\ragin\\Downloads\\TowerDefense\\TowerDefense\\assets\\zombie.png")
        self.delete = False
        self.health = health

        self.xvel = 0
        self.yvel = 0

        self.xacc = 0
        self.yacc = 0

        self.landmark = 0

    def draw(self):
        self.screen.blit(pygame.transform.rotate(
            self.image, -self.direction), (self.x, self.y))

    def distanceBetween(one, two):
        return math.hypot(one.x - two.x, one.y - two.y)

    def loop(self, elapsed):
        pos = game.map[self.landmark]
        self.xacc = (pos[0] - self.x)/1000
        self.yacc = (pos[1] - self.y)/1000

        self.xvel += self.xacc
        self.yvel += self.yacc

        # constant vel
        vel = math.hypot(self.xvel, self.yvel)
        self.xvel *= 3 / vel
        self.yvel *= 3 / vel

        self.x += self.xvel
        self.y += self.yvel

        #move along path
        if math.hypot(pos[0] - self.x, pos[1] - self.y) < 40:
            self.landmark += 1
        
        #end of path
        if self.landmark == len(game.map):
            self.delete = True

        #killed
        if self.health <= 0:
            self.delete = True
