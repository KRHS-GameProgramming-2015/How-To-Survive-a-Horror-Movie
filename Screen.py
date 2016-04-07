import sys, pygame, math, random
from Choice import Choice


class Screen(pygame.sprite.Sprite):
    def __init__(self, screenName, screenSize):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.name = screenName
        
        if self.name == "Room(1.5)":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Room(1.5).png")
            self.choices = [Choice("A. Go check te basement", 0, screenSize),
                       Choice("B. DO ABSOLUTELY NOTHING", 1, screenSize),
                       Choice("C. RUN OUTSIDE for whatever reason", 2, screenSize),
                       Choice("D. Hide in closet, call Police", 3, screenSize)]
        if self.name == "Basement":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Basement.png")
            self.choices = [Choice("A. Check te closet", 0, screenSize),
                       Choice("B. Go back upstairs. Probably just a mouse, right?", 1, screenSize),
                       Choice("C. RUN FOREST RUN!", 2, screenSize)]
        if self.name == "YouFailMiserabally":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/YouFailMiserabally.png")
        
        self.bgImage = pygame.transform.scale(self.bgImage, screenSize)    
        self.image = self.bgImage
        self.rect = self.image.get_rect()
        
    def unload(self):
        for choice in self.choices:
            choice.kill()
        self.kill()
