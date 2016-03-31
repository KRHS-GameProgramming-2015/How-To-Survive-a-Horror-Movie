import sys, pygame, math, random
from Choice import Choice


class Screen(pygame.sprite.Sprite):
    def __init__(self, screenName, screenSize):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.name = screenName
        
        if self.name == "Room(1.5)":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement\Backgrounds\Room(1.5).png")
            choices = [Choice("You are home alone when you here noises from the basement.", 0, screenSize),
                       Choice("A. Go check it out", 1, screenSize)]
        
        self.bgImage = pygame.transform.scale(self.bgImage, screenSize)    
        self.image = self.bgImage
        self.rect = self.image.get_rect()
