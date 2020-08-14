import pygame

pygame.init



myScreen = pygame.display.set_mode((1000, 1000))

class drawable():


        def __init__(self, imagePath):
                self.myImagePath = pygame.image.load(imagePath)

        def draw(self):
                while True:  
                        myScreen.blit (self.myImagePath, (200, 200))
                        pygame.display.update()


