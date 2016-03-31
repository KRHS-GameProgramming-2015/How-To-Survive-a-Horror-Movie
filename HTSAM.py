import sys, pygame, math, random
from Player import Player
from Screen import Screen
from Choice import Choice

pygame.init()

clock = pygame.time.Clock()

width = 1000 
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 0

window = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)

players = pygame.sprite.Group()
screens = pygame.sprite.Group()
choices = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Player.containers = (players, all)
Screen.containers = (screens, all)
Choice.containers = (choices, all)

screen = Screen("Room(1.5)", size)
player = Player(pygame.mouse.get_pos())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            player.move(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            player.unclick()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.click()

    all.update()

    bgColor = r,g,b
    window.fill(bgColor)
    dirty = all.draw(window)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)
