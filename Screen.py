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
        elif self.name == "YouFailMiserabally":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/YouFailMiserabally.png")
        elif self.name == "911":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/911.png")
        elif self.name == "Run Away!":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Run Away!.png")
        elif self.name == "Room(2)":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Room (2).png")
        elif self.name == "Milk Choke":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/MilkChoke.png")
        elif self.name == "RunUp1":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/RunUp1.png")
        elif self.name == "RunUp2":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/RunUp2.png")
        elif self.name == "RunUp3":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/RunUp3.png")
        elif self.name == "RunUp4":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/RunUp4.png")
        
        if self.name == "YouFailMiserabally":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/YouFailMiserabally.png")
            self.choices = [Choice("Retry?", 0, screenSize)]

        if self.name == "911":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/911.png")
            self.choices = [Choice("Retry?", 0, screenSize)]

        if self.name == "Run Away!":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Run Away!.png")
            self.choices = [Choice("Retry?", 0, screenSize)]

        if self.name == "Room(2)":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Room (2).png")
            self.choices = [Choice("Retry?", 0, screenSize)]
        
        if self.name == "Milk Choke":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/MilkChoke.png")
            self.choices = [Choice("Retry?", 0, screenSize)]
            
        if self.name == "RunUp1":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/RunUp1.png")
            self.choices = [Choice("Fists", 0, screenSize),
                            Choice("Rubber Chicken XD", 1, screenSize),
                            Choice("Old Shotgun", 2, screenSize),
                            Choice("Plasma Cannon", 3, screenSize)]
                            
        if self.name == "RunUp2":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/RunUp2.png")
            self.choices = [Choice("Retry?", 0, screenSize)]
        
        if self.name == "RunUp3":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/RunUp3.png")
            self.choices = [Choice("Retry?", 0, screenSize)]
        
        if self.name == "RunUp4":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/RunUp4.png")
            self.choices = [Choice("Retry?", 0, screenSize)]

        self.bgImage = pygame.transform.scale(self.bgImage, screenSize)    
        self.image = self.bgImage
        self.rect = self.image.get_rect()
        
    def unload(self):
        for choice in self.choices:
            choice.kill()
        self.kill()
