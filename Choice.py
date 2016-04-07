import sys, pygame, math, random

class Choice(pygame.sprite.Sprite):
    def __init__(self, text, index, screenSize):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.text = text
        self.index = index
        
        font = pygame.font.Font(None, 36)
        self.image = font.render(text, 1, (200, 0, 0))
        self.rect = self.image.get_rect(center = [screenSize[0]/2, 36/2*index*1.5+20])
        print self.rect
    
    def isClicked(self, pt):
        if pt[0] > self.rect.left and pt[0] < self.rect.right:
            if pt[1] > self.rect.top and pt[1] < self.rect.bottom:
                return True
        return False
