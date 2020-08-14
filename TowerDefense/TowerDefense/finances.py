import game
import pygame

class finance():
    def __init__(self):
        pygame.font.init()
        self.money = 500

        self.font = pygame.font.Font('freesansbold.ttf', 15)

    def draw(self, screen):
        text = self.font.render('money:' + str(self.money), True, (0, 0, 0))
        screen.blit(text, (30, 20))

    def placeTower(self, pos):
        if self.money >= 100:
            game.addPlant(pos[0], pos[1])
            self.money -= 100
        else:
            print("not enough money")

finance = finance()
