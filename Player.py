import sys, pygame, math

class Player(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.baseImage = pygame.image.load("Player/cursor.png")
        self.baseImage = pygame.transform.scale(self.baseImage, [30,40])
        self.clickImage = pygame.image.load("Player/cursor2.png")
        self.clickImage = pygame.transform.scale(self.clickImage, [30,40])
        self.image = self.baseImage
        self.rect = self.image.get_rect(topleft = pos)
        
        self.clicking = False
        
    def update(*args):
        self = args[0]

    def click(self):
        self.clicking = True
        self.image = self.clickImage
        
    def unclick(self):
        self.clicking = False
        self.image = self.baseImage
        
    def move(self, pos):
        self.rect.topleft = pos

