import sys, pygame, math, random
from Choice import Choice


class Screen(pygame.sprite.Sprite):
    def __init__(self, screenName, screenSize):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.name = screenName
        
        if self.name == "Room(1.5)":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Room(1.5).png")
            choices = [Choice("A. Go check te basement", 0, screenSize),
                       Choice("B. DO ABSOLUTELY NOTHING", 1, screenSize),
                       Choice("C. RUN OUTSIDE for whatever reason", 2, screenSize),
                       Choice("D. Hide in closet, call Police", 3, screenSize)]
        
        self.bgImage = pygame.transform.scale(self.bgImage, screenSize)    
        self.image = self.bgImage
        self.rect = self.image.get_rect()
