import pygame
import os

scriptDir = os.path.dirname(os.path.abspath(__file__))
# pygame setup  
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
value1 = 0
value2 = 0
run = True
moving1 = False
moving2 = False
velocity = 12

testFont = pygame.font.Font(os.path.join(scriptDir, "Fonts", "Unbounded-VariableFont_wght.ttf"), 60)


#Loading in all the images
background_image =  pygame.image.load(os.path.join(scriptDir, "Background", 'background final.png'))
instructions_image = pygame.image.load(os.path.join(scriptDir, "Background", 'Ins.png'))
startButton =  testFont.render("Start", True, "Black")
startButton = pygame.transform.rotozoom(startButton,5,1.5)
howToPlayButton = testFont.render("Instructions", True, "Black")
howToPlayButton = pygame.transform.rotozoom(howToPlayButton,3,1)
menuButton = pygame.image.load(os.path.join(scriptDir,"Buttons", "Menu.png"))
menuButton = pygame.transform.rotozoom(menuButton,0,0.25)



#Loading in the sprites
playerOne = pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Idle","PlayerOne_0.png")).convert_alpha()
playerOne = pygame.transform.rotozoom(playerOne,0,5)
playerOneRun = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_0.png")).convert_alpha(), pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_1.png")).convert_alpha(), 
                pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_2.png")).convert_alpha(), pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_3.png")).convert_alpha(), 
                pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_4.png")).convert_alpha(), pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_5.png")).convert_alpha(), 
                pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_6.png")).convert_alpha(), pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_7.png")).convert_alpha()]
playerOneIdle = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Idle","PlayerOne_0.png")).convert_alpha()]

playerTwo = pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Player 2/Idle","PlayerTwo_0.png")).convert_alpha()
playerTwo = pygame.transform.rotozoom(playerTwo,0,5)


gameActive = False
instructions = False

# startScreen = testFont.render("Hong Kong Food Market", True, "Black")

#Rectangles
# startScreenRect = startScreen.get_rect(center = (1050,150))
startButtonRect = startButton.get_rect(topleft = (1180,630))

howToPlayButtonRect = howToPlayButton.get_rect(center = ( 620,700))
menuButtonRect = menuButton.get_rect(topleft = (740,500))

#Sprite Rectangles
playerOneRect = playerOne.get_rect(bottomleft = (200,800))
playerTwoRect = playerTwo.get_rect(bottomleft = (1300,800))

#This loads the images

while running:
    keys = pygame.key.get_pressed()

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if startButtonRect.collidepoint(event.pos):
                    gameActive = True
    if gameActive:
        if keys[pygame.K_a]:
            if playerOneRect.x >= 0:
                playerOneRect.x -= 20
                value1 += 1
                moving1 = True
                if value1 >= len(playerOneRun):
                    value1 = 0
        elif keys[pygame.K_d]:
            if playerOneRect.x <= 1700:
                playerOneRect.x +=20
                value1 += 1
                moving1 = True
                if value1 >= len(playerOneRun):
                    value1 = 0

        elif keys[pygame.K_l]:
            if playerTwoRect.x <= 1700:
                playerTwoRect.x += 20
                value2 += 1
                moving2 = True
                if value2 >= len(playerTwoRun):
                    value2 = 0
        elif keys[pygame.K_j]:
            if playerTwoRect.x >= 0:
                playerTwoRect.x -=20
                moving2 = True
                if value2 >= len(playerTwoRun):
                    value2 = 0
        else:
            value2 = 0
            moving2 = False
            playerTwo = playerTwoIdle[value2]
            value1 = 0
            moving1 = False
            playerOne = playerOneIdle[value1]
        
        if event.type == pygame.MOUSEBUTTONDOWN:
                if howToPlayButtonRect.collidepoint(event.pos):
                    instructions = True
                if menuButtonRect.collidepoint(event.pos):
                    instructions = False
        
        
    
    
    # fill the screen with a color to wipe away anything from last frame
    
    if gameActive == False:
        screen.blit(background_image,(0,0))
        # screen.blit(startScreen,startScreenRect)
        screen.blit(startButton,startButtonRect)
        screen.blit(howToPlayButton,howToPlayButtonRect)
        if instructions == True:
            screen.blit(instructions_image,(0,0))
            screen.blit(menuButton,menuButtonRect)
    else:
        screen.fill('black')
        screen.blit(playerOne, (playerOneRect))
        screen.blit(playerTwo, (playerTwoRect))
        screen.blit(playerOne, (playerOneRect.x,playerOneRect.y))
        screen.blit(playerTwo, (playerTwoRect.x,playerTwoRect.y))
        #movement for player One
        

    # flip() the display to put your work on screen
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60
    
    if moving1:
        playerOne = playerOneRun[value1]
    elif moving2:
        playerTwo = playerTwoRun[value2]
    else:
        playerOne = playerOne
        playerTwo = playerTwo
    playerOne = pygame.transform.rotozoom(playerOne,0,5)

pygame.quit()
