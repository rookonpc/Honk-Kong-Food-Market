import pygame
import os
from pygame import mixer 

scriptDir = os.path.dirname(os.path.abspath(__file__))
# pygame setup  
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
value1 = 0
value2 = 0
run = True
moving = False
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
backgroundMusic = os.path.join(scriptDir,"Sounds","Background.wav")


#Loading in the sprites
playerOne = pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Idle","PlayerOne_0.png")).convert_alpha()
playerOneRun = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_0.png")).convert_alpha(), pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_1.png")).convert_alpha(), 
                pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_2.png")).convert_alpha(), pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_3.png")).convert_alpha(), 
                pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_4.png")).convert_alpha(), pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_5.png")).convert_alpha(), 
                pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_6.png")).convert_alpha(), pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run","PlayerOneRun_7.png")).convert_alpha()]
playerOneIdle = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Idle","PlayerOne_0.png")).convert_alpha()]

playerTwo = pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Player 2/Idle","PlayerTwo_0.png")).convert_alpha()
playerTwoRun = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Player 2/Run","PlayerTwoRun_0.png")).convert_alpha(), pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Player 2/Run","PlayerTwoRun_1.png")).convert_alpha(), 
                pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Player 2/Run","PlayerTwoRun_2.png")).convert_alpha(), pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Player 2/Run","PlayerTwoRun_3.png")).convert_alpha(), 
                pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Player 2/Run","PlayerTwoRun_4.png")).convert_alpha(), pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Player 2/Run","PlayerTwoRun_5.png")).convert_alpha(), 
                pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Player 2/Run","PlayerTwoRun_6.png")).convert_alpha(), pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Player 2/Run","PlayerTwoRun_7.png")).convert_alpha()]
playerTwoIdle = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Player 2/Idle","PlayerTwo_0.png")).convert_alpha()]

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

pygame.mixer.music.load(backgroundMusic)
pygame.mixer.music.play()
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
        pygame.mixer.music.stop()
        if keys[pygame.K_a] and playerOneRect.x >= 0:
            playerOneRect.x -= 20
            value1 += 1
            moving = True
            if value1 >= len(playerOneRun):
                value1 = 0
        elif keys[pygame.K_d] and playerOneRect.x <= 1700:
            playerOneRect.x +=20
            value1 += 1
            moving = True
            if value1 >= len(playerOneRun):
                value1 = 0
        else:
            moving = False 
            playerOne = pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Idle","PlayerOne_0.png")).convert_alpha()

        if keys[pygame.K_j] and playerTwoRect.x >= 0:
            playerTwoRect.x -=20
            value2 += 1
            moving2 = True
            if value2 >= len(playerTwoRun):
                value2 = 0        
        elif keys[pygame.K_l] and playerTwoRect.x <= 1700:
            playerTwoRect.x += 20
            value2 += 1
            moving2 = True
            if value2 >= len(playerTwoRun):
                value2 = 0        
        else:
            moving2 = False
            playerTwo = pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Player 2/Idle","PlayerTwo_0.png")).convert_alpha()
            
    if keys[pygame.K_t]:    
        running = False        
        
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
    
    if moving:
        playerOne = playerOneRun[value1]
    else:
        value1 = 0
        playerOne = pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Idle","PlayerOne_0.png")).convert_alpha()
    
    if moving2:
        playerTwo = playerTwoRun[value2]
    else:
        playerTwo = pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Player 2/Idle","PlayerTwo_0.png")).convert_alpha()


pygame.quit()
