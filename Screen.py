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
                       Choice("D. Hide in closet, call Police", 3, screenSize),
                       Choice("E. Call your friend and videotape an asylum. How fun.", 4, screenSize)]
        if self.name == "Basement":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Basement.png")
            self.choices = [Choice("A. Check te closet", 0, screenSize),
                       Choice("B. Go back upstairs. Probably just a mouse, right?", 1, screenSize),
                       Choice("C. RUN FOREST RUN!", 2, screenSize)]
                       
        elif self.name == "YouFailMiserabally":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/YouFailMiserabally.png")
            self.choices = [Choice("Retry?", 0, screenSize)]

        elif self.name == "911":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/911.png")
            self.choices = [Choice("Retry?", 0, screenSize)]

        elif self.name == "Run Away!":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Run Away!.png")
            self.choices = [Choice("Retry?", 0, screenSize)]

        elif self.name == "Room(2)":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Room (2).png")
            self.choices = [Choice("Retry?", 0, screenSize)]
        
        elif self.name == "Milk Choke":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/MilkChoke.png")
            self.choices = [Choice("Retry?", 0, screenSize)]
            
        elif self.name == "RunUp1":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/RunUp1.png")
            self.choices = [Choice("Fists", 0, screenSize),
                            Choice("Rubber Chicken XD", 1, screenSize),
                            Choice("Old Shotgun", 2, screenSize),
                            Choice("Plasma Cannon", 3, screenSize)]
                            
        elif self.name == "RunUp2":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/RunUp2.png")
            self.choices = [Choice("Retry?", 0, screenSize)]
        
        elif self.name == "RunUp3":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/RunUp3.png")
            self.choices = [Choice("Retry?", 0, screenSize)]
        
        elif self.name == "RunUp4":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/RunUp4.png")
            self.choices = [Choice("Retry?", 0, screenSize)]
            
        elif self.name == "RunUp5":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/RunUp5.png")
            self.choices = [Choice("Retry?", 0, screenSize)]
            
        elif self.name == "Asylum 1":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Asylum 1.png")
            self.choices = [Choice("Go Back", 0, screenSize),
                            Choice("Next", 1, screenSize)]

        elif self.name == "Outside":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/The Outside.png")
            self.choices = [Choice("Next", 0, screenSize)]

        elif self.name == "Stairs":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Stairs.png")
            self.choices = [Choice("Next", 0, screenSize)]

        elif self.name == "Upstairs":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Upstairs.png")
            self.choices = [Choice("2B", 0, screenSize),
                            Choice("2E", 1, screenSize),
                            Choice("2H", 2, screenSize)] 

        elif self.name == "2B":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/2B.png")
            self.choices = [Choice("Next", 0, screenSize)]

        elif self.name == "2E":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/2H.png")
            self.choices = [Choice("Back", 0, screenSize)]

        elif self.name == "2H":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/2H.png")
            self.choices = [Choice("Back", 0, screenSize)]
            
        elif self.name == "ContinueFilm":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Continue Filming.png")
            self.choices = [Choice("Next", 0, screenSize)]
            
        elif self.name == "Check":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/Check It Out.png")
            self.choices = [Choice("Sprint for the front exit!", 0, screenSize),
                            Choice("Escape to the cellar and find an exit there.", 1, screenSize)]

        elif self.name == "SPRINT FOR THE EXIT!":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/SPRINT FOR THE EXIT!.png")
            self.choices = [Choice("Retry?", 0, screenSize)]
            
        elif self.name == "cellar":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/cellar.png")
            self.choices = [Choice("Next", 0, screenSize)]
            
        elif self.name == "News":
            self.bgImage = pygame.image.load("Home Alone - Noises In Basement/Backgrounds/News Report.png")
            self.choices = [Choice("Retry?", 0, screenSize)]

        self.bgImage = pygame.transform.scale(self.bgImage, screenSize)    
        self.image = self.bgImage
        self.rect = self.image.get_rect()

    def unload(self):
        for choice in self.choices:
            choice.kill()
        self.kill()
