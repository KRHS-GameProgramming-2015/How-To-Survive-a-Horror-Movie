import sys, pygame, math

class Player(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.image = pygame.image.load("Player/cursor.png")
        self.image = pygame.transform.scale(self.image, [25,25])
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(*args):
        self = args[0]
        pos = args[1]
        
        self.rect.topleft = pos
