import pygame
import os

scriptDir = os.path.dirname(os.path.abspath(__file__))
# pygame setup  
pygame.init()
screen = pygame.display.set_mode((2000, 1000))
clock = pygame.time.Clock()
running = True

#Loading in all the images
background_image =  pygame.image.load(os.path.join(scriptDir, "Background", 'bg.png'))
instructions_image = pygame.image.load(os.path.join(scriptDir, "Background", 'Ins.png'))
startButton =  pygame.image.load(os.path.join(scriptDir,"Buttons", "Start.png"))
startButton = pygame.transform.scale2x(startButton)
howToPlayButton = pygame.image.load(os.path.join(scriptDir,"Buttons", "Tutorial.png"))
howToPlayButton = pygame.transform.scale2x(howToPlayButton)
menuButton = pygame.image.load(os.path.join(scriptDir,"Buttons", "Menu.png"))
menuButton = pygame.transform.rotozoom(menuButton,0,0.25)

testFont = pygame.font.Font(os.path.join(scriptDir, "Fonts", "Unbounded-VariableFont_wght.ttf"), 70)

gameActive = False
instructions = False

startScreen = testFont.render("Hong Kong Food Market", True, "Black")

#Rectangles
startScreenRect = startScreen.get_rect(center = (1050,150))
startButtonRect = startButton.get_rect(topleft = (1000,570))

howToPlayButtonRect = howToPlayButton.get_rect(center = ( 300,400))
menuButtonRect = menuButton.get_rect(topleft = (700,500))

#This loads the images

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if startButtonRect.collidepoint(event.pos):
                    gameActive = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
                if howToPlayButtonRect.collidepoint(event.pos):
                    instructions = True
                if menuButtonRect.collidepoint(event.pos):
                    instructions = False
        

    # fill the screen with a color to wipe away anything from last frame
    
    screen.fill("black")
    if gameActive == False:
        screen.blit(background_image,(0,0))
        screen.blit(startScreen,startScreenRect)
        screen.blit(startButton,startButtonRect)
        screen.blit(howToPlayButton,howToPlayButtonRect)
        if instructions == True:
            screen.blit(instructions_image,(0,0))
            screen.blit(menuButton,menuButtonRect)
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()