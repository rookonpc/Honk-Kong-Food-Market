import pygame
import os
import time

scriptDir = os.path.dirname(os.path.abspath(__file__))
# pygame setup
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
value1left = 0
value1right = 0
value2left = 0
value2right = 0
run = True
movingROne = False
movingLOne = False
movingRTwo = False
movingLTwo = False
velocity = 6
roundOne = False
punchOne = False
punchTwo = False
punchValue1 = 0
punchValue2 = 0
rightRunOne = False
leftRunOne = False
rightRunTwo = False
leftRunTwo = False

class HealthBar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = 100
        self.max_hp = max_hp

    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

health_bar_player1 = HealthBar(250, 200, 500, 60, 100)
health_bar_player2 = HealthBar(1370, 200, 500, 60, 100)

testFont = pygame.font.Font(os.path.join(scriptDir, "Fonts", "Unbounded-VariableFont_wght.ttf"), 60)

# Loading in all the images
background_image = pygame.image.load(os.path.join(scriptDir, "Background", 'background final.png'))
instructions_image = pygame.image.load(os.path.join(scriptDir, "Background", 'Ins.png'))
startButton = testFont.render("Start", True, "Black")
startButton = pygame.transform.rotozoom(startButton, 5, 1.5)
howToPlayButton = testFont.render("Instructions", True, "Black")
howToPlayButton = pygame.transform.rotozoom(howToPlayButton, 3, 1)
menuButton = pygame.image.load(os.path.join(scriptDir, "Buttons", "Menu.png"))
menuButton = pygame.transform.rotozoom(menuButton, 0, 0.25)
backgroundMusic = os.path.join(scriptDir, "Sounds", "Background.wav")
roundOneImg = pygame.image.load(os.path.join(scriptDir, "Background", 'bck.png')).convert_alpha()

# Loading in the sprites
playerOne = pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Idle", "PlayerOne_0.png")).convert_alpha()
playerOneRun = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Run", f"PlayerOneRun_{i}.png")).convert_alpha() for i in range(8)]
playerOneRunInverted = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player One Inverted/Run", f"PlayerOneRun_{i}INV.png")).convert_alpha() for i in range(8)]
playerOneIdle = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Idle", "PlayerOne_0.png")).convert_alpha()]
playerOnePunch = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Attack", f"PlayerPunch_{i}.png")).convert_alpha() for i in range(4)]

playerTwo = pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Idle", "PlayerTwo_0.png")).convert_alpha()
playerTwoRun = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Run", f"PlayerTwoRun_{i}.png")).convert_alpha() for i in range(8)]
playerTwoIdle = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Idle", "PlayerTwo_0.png")).convert_alpha()]
playerTwoPunch = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Attack", f"PlayerTwoPunch_{i}.png")).convert_alpha() for i in range(4)]
playerTwoRunInverted = [pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two Inverted/PlayerTwoRunINV", f"PlayerTwoRun_{i}INV.png")).convert_alpha() for i in range(8)]

gameActive = False
instructions = False
roundOver = False

# Rectangles
startButtonRect = startButton.get_rect(topleft=(1180, 630))
howToPlayButtonRect = howToPlayButton.get_rect(center=(620, 700))
menuButtonRect = menuButton.get_rect(topleft=(740, 500))

# Sprite Rectangles
playerOneRect = playerOne.get_rect(bottomleft=(200, 1000))
playerTwoRect = playerTwo.get_rect(bottomleft=(1300, 1000))

# Punch cooldown variables
last_punch_time_player1 = 0
last_punch_time_player2 = 0
punch_cooldown = 0.5  # Cooldown duration in seconds

# Animation clock
animation_clock = pygame.time.Clock()

# This loads the images
pygame.mixer.music.load(backgroundMusic)
pygame.mixer.music.play()

while running:
    keys = pygame.key.get_pressed()

    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if startButtonRect.collidepoint(event.pos):
                gameActive = True

    if gameActive and not roundOver:
        pygame.mixer.music.stop()

        # Player 1 Movement
        if keys[pygame.K_a] and playerOneRect.x >= 0:
            leftRunOne = True
            movingLOne = True
            playerOneRect.x -= 15
            value1left += 1
            if value1left >= len(playerOneRunInverted):
                value1left = 0
        elif keys[pygame.K_d] and playerOneRect.x <= 1700:
            rightRunOne = True
            movingROne = True
            playerOneRect.x += 15
            value1right += 1
            if value1right >= len(playerOneRun):
                value1right = 0
        else:
            movingROne = False
            movingLOne = False

        # Player 2 Movement
        if keys[pygame.K_j] and playerTwoRect.x >= 0:
            leftRunTwo = True
            movingLTwo = True
            playerTwoRect.x -= 15
            value2left += 1
            if value2left >= len(playerTwoRunInverted):
                value2left = 0
        elif keys[pygame.K_l] and playerTwoRect.x <= 1700:
            rightRunTwo = True
            movingRTwo = True
            playerTwoRect.x += 15
            value2right += 1
            if value2right >= len(playerTwoRun):
                value2right = 0
        else:
            movingRTwo = False
            movingLTwo = False

        # Player 1 Punch
        current_time = time.time()
        if keys[pygame.K_f] and current_time - last_punch_time_player1 >= punch_cooldown:
            punchOne = True
            punchValue1 += 1
            if punchValue1 >= len(playerOnePunch):
                punchValue1 = 0
            if playerOneRect.colliderect(playerTwoRect):
                health_bar_player2.hp -= 10  # Decrease player 2's health on punch
            last_punch_time_player1 = current_time  # Update last punch time
        else:
            punchOne = False

        # Player 2 Punch
        if keys[pygame.K_h] and current_time - last_punch_time_player2 >= punch_cooldown:
            punchTwo = True
            punchValue2 += 1
            if punchValue2 >= len(playerTwoPunch):
                punchValue2 = 0
            if playerTwoRect.colliderect(playerOneRect):
                health_bar_player1.hp -= 10  # Decrease player 1's health on punch
            last_punch_time_player2 = current_time  # Update last punch time
        else:
            punchTwo = False

        # Check for game end conditions
        if health_bar_player1.hp <= 0 or health_bar_player2.hp <= 0:
            roundOver = True

    if keys[pygame.K_t]:
        running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        if howToPlayButtonRect.collidepoint(event.pos):
            instructions = True
        if menuButtonRect.collidepoint(event.pos):
            instructions = False

    # Fill the screen with a color to wipe away anything from last frame
    if gameActive == False:
        screen.blit(background_image, (0, 0))
        screen.blit(startButton, startButtonRect)
        screen.blit(howToPlayButton, howToPlayButtonRect)

        if instructions == True:
            screen.blit(instructions_image, (0, 0))
            screen.blit(menuButton, menuButtonRect)
    elif not roundOver:
        screen.blit(roundOneImg, (0, 0))
        screen.blit(playerOne, (playerOneRect))
        screen.blit(playerTwo, (playerTwoRect))
        screen.blit(playerOne, (playerOneRect.x, playerOneRect.y))
        screen.blit(playerTwo, (playerTwoRect.x, playerTwoRect.y))
        health_bar_player1.draw(screen)
        health_bar_player2.draw(screen)
    else:
        screen.fill((0, 0, 0))
        winner_font = pygame.font.Font(None, 100)
        winner_text = "Player 2 Wins!" if health_bar_player1.hp <= 0 else "Player 1 Wins!"
        winner_text_surface = winner_font.render(winner_text, True, (255, 255, 255))
        winner_text_rect = winner_text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(winner_text_surface, winner_text_rect)
        round_over_font = pygame.font.Font(None, 40)
        round_over_text_surface = round_over_font.render("Press Space to go to Round 2", True, (255, 255, 255))
        round_over_text_rect = round_over_text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
        screen.blit(round_over_text_surface, round_over_text_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            roundOver = False
            # Reset player positions and health for round 2
            playerOneRect.x = 200
            playerTwoRect.x = 1300
            health_bar_player1.hp = 100
            health_bar_player2.hp = 100

    # Flip() the display to put your work on screen
    pygame.display.update()

    clock.tick(60)  # Limits FPS to 24
    animation_clock.tick(24)  # Limits punch animation FPS to 12

    if rightRunOne and movingROne:
        playerOne = playerOneRun[value1right]
    elif leftRunOne and movingLOne:
        playerOne = playerOneRunInverted[value1left]
    else:
        playerOne = pygame.image.load(os.path.join(scriptDir, "Sprite/Player One/Idle", "PlayerOne_0.png")).convert_alpha()

    if rightRunTwo and movingRTwo:
        playerTwo = playerTwoRun[value2right]
    elif leftRunTwo and movingLTwo:
        playerTwo = playerTwoRunInverted[value2left]
    else:
        playerTwo = pygame.image.load(os.path.join(scriptDir, "Sprite/Player Two/Idle", "PlayerTwo_0.png")).convert_alpha()

    if punchOne:
        playerOne = playerOnePunch[punchValue1]
    if punchTwo:
        playerTwo = playerTwoPunch[punchValue2]

pygame.quit()
