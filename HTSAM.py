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

playersHitChoices = {}

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
    
    playersHitChoices = {}
    theChoice = "bob";  
    if player.clicking:
        playersHitChoices = pygame.sprite.groupcollide(players, choices, False, False)
    
      
    for p in playersHitChoices:
        for choice in playersHitChoices[p]:
            if choice.isClicked(player.rect.topleft):
                theChoice = choice.index
                print theChoice
    
    if screen.name == "Room(1.5)":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Basement", size)
            player = Player(pygame.mouse.get_pos())
        elif theChoice == 1:
            screen.unload()
            screen = Screen("Room(2)", size)
            player = Player(pygame.mouse.get_pos())
        elif theChoice == 2:
            screen.unload()
            screen = Screen("Run Away!", size)
            player = Player(pygame.mouse.get_pos())
        elif theChoice == 3:
            screen.unload()
            screen = Screen("911", size)
            player = Player(pygame.mouse.get_pos())
        elif theChoice == 4:
            screen.unload()
            screen = Screen("Asylum 1", size)
            player = Player(pygame.mouse.get_pos())
    
    elif screen.name == "YouFailMiserabally":
       if theChoice == 0:
            screen.unload()
            screen = Screen("Room(1.5)", size)
            player = Player(pygame.mouse.get_pos())
    
    elif screen.name == "Room(2)":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Room(1.5)", size)
            player = Player(pygame.mouse.get_pos())
    
    elif screen.name == "911":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Room(1.5)", size)
            player = Player(pygame.mouse.get_pos())
    
    elif screen.name == "Run Away!":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Room(1.5)", size)
            player = Player(pygame.mouse.get_pos())
            
    elif screen.name == "Milk Choke":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Room(1.5)", size)
            player = Player(pygame.mouse.get_pos())
        
    elif screen.name == "RunUp2":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Room(1.5)", size)
            player = Player(pygame.mouse.get_pos())
    
    elif screen.name == "RunUp3":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Room(1.5)", size)
            player = Player(pygame.mouse.get_pos())
            
    elif screen.name == "RunUp4":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Room(1.5)", size)
            player = Player(pygame.mouse.get_pos())
            
    elif screen.name == "RunUp5":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Room(1.5)", size)
            player = Player(pygame.mouse.get_pos())
    
    elif screen.name == "Basement":
        if theChoice == 0:
            screen.unload()
            screen = Screen("YouFailMiserabally", size)
            player = Player(pygame.mouse.get_pos())
        elif theChoice == 1:
            screen.unload()
            screen = Screen("Milk Choke", size)
            player = Player(pygame.mouse.get_pos())
        elif theChoice == 2:
            screen.unload()
            screen = Screen("RunUp1", size)
            player = Player(pygame.mouse.get_pos())
    
    elif screen.name == "RunUp1":
        if theChoice == 0:
            screen.unload()
            screen = Screen("RunUp2", size)
            player = Player(pygame.mouse.get_pos())
        elif theChoice == 1:
                screen.unload()
                screen = Screen("RunUp3", size)
                player = Player(pygame.mouse.get_pos())
        elif theChoice == 2:
                screen.unload()
                screen = Screen("RunUp4", size)
                player = Player(pygame.mouse.get_pos())
        elif theChoice == 3:
                screen.unload()
                screen = Screen("RunUp5", size)
                player = Player(pygame.mouse.get_pos())

    elif screen.name == "Asylum 1":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Room(1.5)", size)
            player = Player(pygame.mouse.get_pos())
        elif theChoice == 1:
            screen.unload()
            screen = Screen("Stairs", size)
            player = Player(pygame.mouse.get_pos())

    elif screen.name == "Stairs":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Upstairs", size)
            player = Player(pygame.mouse.get_pos())
            
    elif screen.name == "Upstairs":
        if theChoice == 0:
            screen.unload()
            screen = Screen("2B", size)
            player = Player(pygame.mouse.get_pos())
        elif theChoice == 1:
            screen.unload()
            screen = Screen("2E", size)
            player = Player(pygame.mouse.get_pos())
        elif theChoice == 2:
            screen.unload()
            screen = Screen("2H", size)
            player = Player(pygame.mouse.get_pos())
            
    elif screen.name == "2B":
        if theChoice == 0:
            screen.unload()
            screen = Screen("ContinueFilm", size)
            player = Player(pygame.mouse.get_pos())
            
    elif screen.name == "2E":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Upstairs", size)
            player = Player(pygame.mouse.get_pos())
            
    elif screen.name == "2H":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Upstairs", size)
            player = Player(pygame.mouse.get_pos())
            
    elif screen.name == "ContinueFilm":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Check", size)
            player = Player(pygame.mouse.get_pos())
            
    elif screen.name == "Check":
        if theChoice == 0:
            screen.unload()
            screen = Screen("SPRINT FOR THE EXIT!", size)
            player = Player(pygame.mouse.get_pos())
        elif theChoice == 1:
            screen.unload()
            screen = Screen("cellar", size)
            player = Player(pygame.mouse.get_pos())
            
    elif screen.name == "cellar":
        if theChoice == 0:
            screen.unload()
            screen = Screen("News", size)
            player = Player(pygame.mouse.get_pos())
            
    elif screen.name == "News":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Room(1.5)", size)
            player = Player(pygame.mouse.get_pos())
            
    elif screen.name == "SPRINT FOR THE EXIT!":
        if theChoice == 0:
            screen.unload()
            screen = Screen("Room(1.5)", size)
            player = Player(pygame.mouse.get_pos())

    bgColor = r,g,b
    window.fill(bgColor)
    dirty = all.draw(window)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)
