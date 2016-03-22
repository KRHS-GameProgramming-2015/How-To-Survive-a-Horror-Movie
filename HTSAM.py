import sys, pygame, math, random
from Player import Player

pygame.init()

clock = pygame.time.Clock()

width = 1000 
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)

#balls = pygame.sprite.Group()
players = pygame.sprite.Group()
#boundries = pygame.sprite.Group()

all = pygame.sprite.OrderedUpdates()

#Ball.containers = (balls, all)
#Wall.containers = (boundries, all)
Player.containers = (players, all)
#Not sure if I needed these

player = Player(pygame.mouse.get_pos())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        
    all.update(pygame.mouse.get_pos())
    
            
    bgColor = r,g,b
    screen.fill(bgColor)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)
