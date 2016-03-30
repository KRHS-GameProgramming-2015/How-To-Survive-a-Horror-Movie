import sys, pygame, math, random

class Screen(pygame.sprite.Sprite):
    def __init__(self, screenName, screenSize):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        if screenName == "Room(1.5)":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement\Backgrounds\Room(1.5).png")
            self.bgImage = pygame.transform.scale(self.bgImage, screenSize)
            
        self.image = self.bgImage
        self.rect = self.image.get_rect()
