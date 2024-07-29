
# Pygame -- Mr. Cowboy
# Caleb Massey, Margo Bonal
# setUp.py
# Stores Constants and Variables used throughout the program

#module-> class-> class var/function


# LIBRARIES
import pygame
from pygame.locals import *
import os
import sys
import math
import time
import random

# MODULES
import characters
import environment
import guiFeatures

pygame.init()

# ----------------------- START initGame CLASS ----------------------- #
class initGame:

    # ------------ GAME CONSTANTS/VARIABLES ------------ #
    
    # Screen sizes
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    
    # Set screen
    gameScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("MR. COWBOY")
    
    # Set framerate to 60
    clock = pygame.time.Clock()
    frameRate = 60
    start = time.time()
    timer = 30 # 30sec
    
    # Difficulty Flags
    survivedTime = 0
    worldTime = 0
    moreSpeed = True
    newEnemy1 = True
    newEnemy2 = True

    # Game Traits
    GRAVITY = 0.50
    TILE_SIZE = 40
    GAME_RUNNING = True
    ITEM_LOCK = False

    # HIGH SCORES INFO
    currentScore = 0
    scoreInp = open("highScore.txt", "r")
    for x in scoreInp:
        highScore = int(x)
    scoreInp.close()

    # GAME STATE CONSTANTS
    PAUSED = 0
    UNPAUSED = 1
    TRAVEL = 2
    DESERT = 3
    scroll = 0
    CHANGE_BACKGROUND = False

    #Bullet Types
    TypeC = "cactus"
    TypeP = "player"
    TypeE = "enemy"
    
    # Player Action Flags
    movingLeft  = False
    movingRight = False
    shooting    = False
    throwing    = False
    dynaThrown  = False
    invincible  = True

    # Color Contants - Uses RGB scale
    BG = (144, 201, 120)
    RED = (255, 0, 0)
    GREEN = (57, 255, 20)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TAN = (210, 180, 140)
    
    # Font Loading
    infoFont = pygame.font.SysFont('Courier New', 30)


    # ------------ IMAGE LOADING ------------ #
    
    # Background Loading
    backgroundImg = pygame.image.load("img/background/townedit.png").convert_alpha()
    backgroundImg = pygame.transform.scale(backgroundImg, (SCREEN_WIDTH, SCREEN_HEIGHT - 220))

    nightImg = pygame.image.load("img/background/night.png").convert_alpha()
    nightImg = pygame.transform.scale(nightImg, (SCREEN_WIDTH, SCREEN_HEIGHT - 220))
    # Bullet Loading
    playerBullet = pygame.image.load('img\icons\playerBullet.png').convert_alpha()
    playerBullet = pygame.transform.scale(playerBullet, (int(playerBullet.get_width() * 4), int(playerBullet.get_height() * 4)))
    enemyBullet  = pygame.image.load("img\icons\enemyBullet.png").convert_alpha()
    enemyBullet  = pygame.transform.scale(enemyBullet, (int(enemyBullet.get_width() * 4), int(enemyBullet.get_height() * 4)))
    cactusBullet = pygame.image.load("img\icons\cactusBullet.png").convert_alpha()
    cactusBullet  = pygame.transform.scale(cactusBullet, (int(cactusBullet.get_width() * 4), int(cactusBullet.get_height() * 4)))

    # Dynamite Loading
    dynamiteImg = pygame.image.load('img\icons\dynamite.png').convert_alpha()
    dynamiteImg = pygame.transform.scale(dynamiteImg, (int(dynamiteImg.get_width() * 4), int(dynamiteImg.get_height() * 4)))

    # Pickup Images -- Stored in dictionary
    healthHat = pygame.image.load('img\icons/restoreHealth.png').convert_alpha()
    healthHat = pygame.transform.scale(healthHat, (int(healthHat.get_width() * 5), int(healthHat.get_height() * 5)))
    speedBoot = pygame.image.load('img\icons\speedUp.png').convert_alpha()
    speedBoot = pygame.transform.scale(speedBoot, (int(speedBoot.get_width() * 5), int(speedBoot.get_height() * 5)))
    shinyCoin = pygame.image.load('img\icons/restoreCoin.png').convert_alpha()
    shinyCoin = pygame.transform.scale(shinyCoin, (int(shinyCoin.get_width() * 5), int(shinyCoin.get_height() * 5)))
    bulletBox = pygame.image.load('img\icons/ammoPickup.png').convert_alpha()
    bulletBox = pygame.transform.scale(bulletBox, (int(bulletBox.get_width() * 5), int(bulletBox.get_height() * 5)))
    dynaCrate = pygame.image.load('img\icons\dynamitePickup.png').convert_alpha()
    dynaCrate = pygame.transform.scale(dynaCrate, (int(dynaCrate.get_width() * 5), int(dynaCrate.get_height() * 5)))
    
    # StartUp Screen Loading
    startScreen = pygame.image.load("img/banner/mrCowboy.png").convert_alpha()
    hatAbove    = pygame.image.load("img/enemy/DEATH/0.png").convert_alpha()
    scaledHat   = pygame.transform.scale(hatAbove, (250, 250))
    enterToPlay = pygame.image.load("img/banner/enter.png").convert_alpha()

    #Game Over Banner
    over   = pygame.image.load("img/banner/gameOver.png").convert_alpha()
    scaledOver   = pygame.transform.scale(over, (550, 250))

    #load Credits Screen Imgs
    credits = pygame.image.load("img/banner/credits2.png").convert_alpha()
    scrollingImg = pygame.image.load("img/background/sunset2.png").convert_alpha()
    scrolling_width = scrollingImg.get_width()
    scaledcredits   = pygame.transform.scale(credits, (400, 300))
    #----------------------------PAUSE/UNPAUSE------------------------------------------------#

    #----------------PAUSE----------------------------------------#
    # Pause Screen loading
    pause_img = pygame.image.load("img/banner/pause.png").convert_alpha()
    #Pause Button Creation
    pause_button = guiFeatures.GUI_Button(1100, 5, pause_img, 6)

    #Pause Screen Loading
    pausebanner = pygame.image.load("img/banner/gamePausedBanner.png").convert_alpha()
    scaledPause   = pygame.transform.scale(pausebanner, (750, 500))
    #---------------- END PAUSE--------------------------------------#
    
    #----------------UNPAUSE----------------------------------------#

    # Resume game buttons
    resume_img = pygame.image.load("img/banner/resume.png").convert_alpha()
    resume_button = guiFeatures.GUI_Button(300,300, resume_img, 4)

    #exit button
    quit_img = pygame.image.load("img/banner/quit.png").convert_alpha()
    quit_button = guiFeatures.GUI_Button(600,300, quit_img, 12)

    #----------------END UNPAUSE-------------------------------------#

    sign_img = pygame.image.load("img/banner/sign.png").convert_alpha()
    sign_button = guiFeatures.GUI_Button(1050, 600, sign_img, 6)
    desertImg = pygame.image.load("img/background/desert.png").convert_alpha()
    desert_width = desertImg.get_width()
    #---------------------------END PAUSE/UNPAUSE-------------------------------------------#


    # ------------ POWERUP LOADING ------------ #
    itemBoxes = {
    'HEALTH'     : healthHat,
    'AMMO'       : bulletBox,
    'DYNAMITE'   : dynaCrate,
    'SPEED'      : speedBoot,
    'RESTORE'    : shinyCoin   
    }
    # ----------------------------------------- #


    # ------------ SPRITE GROUPS ------------ #
    enemyGroup      = pygame.sprite.Group()
    bulletGroup     = pygame.sprite.Group()
    dynamiteGroup   = pygame.sprite.Group()
    explosionGroup  = pygame.sprite.Group()
    itemBoxGroup    = pygame.sprite.Group()
    platformGroup   = pygame.sprite.Group()
    # --------------------------------------- #


    # ------------- PLAYER CREATION ------------- #
    player = characters.character('player', SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 5, 4, 24, 5, not invincible)
    horse = characters.character('horse', SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 5, 4, 24, 5, not invincible)
    healthBar = characters.HealthBar(150, 515, player.health, player.maxHealth)
    # ------------------------------------------- #


    # ----------- ENVIRONMENT CREATIONS ----------- #
    tumbler  = environment.Tumbleweed(gameScreen, 'img/icons/ENVIRONMENTAL/STATIC/tumbleweed.png', 50, 460, 2, 1, 3)
    tumbler2 = environment.Tumbleweed(gameScreen, 'img/icons/ENVIRONMENTAL/STATIC/tumbleweed.png', 50, 460, 4, 1, 3)
    tumbler3 = environment.Tumbleweed(gameScreen, 'img/icons/ENVIRONMENTAL/STATIC/tumbleweed.png', 50, 460, 5, 1, 3)
    tumbler4 = environment.Tumbleweed(gameScreen, 'img/icons/ENVIRONMENTAL/STATIC/tumbleweed.png', 50, 460, 3, 1, 3)
    platform  = environment.platform(gameScreen, 'img/icons/ENVIRONMENTAL/PLATFORMS/platform2.png', SCREEN_WIDTH + 100, 125, random.randint(1, 5), 5)
    platform2 = environment.platform(gameScreen, 'img/icons/ENVIRONMENTAL/PLATFORMS/platform2.png', SCREEN_WIDTH + 50, 250, random.randint(1, 5), 5)
    platform3 = environment.platform(gameScreen, 'img/icons/ENVIRONMENTAL/PLATFORMS/platform2.png', SCREEN_WIDTH, 375, random.randint(1, 5), 5)
    platformGroup.add(platform)
    platformGroup.add(platform2)
    platformGroup.add(platform3)

    # --------------------------------------------- #

    # Initial creation of enemies
    enemy = characters.character('enemy', 900, 450, 5, 3, 20, 0, not invincible, collidable=False)
    enemy2 = characters.character('enemy', 200, 450, 5, 3, 20, 0, not invincible, collidable=False)
    enemy3 = characters.character('enemy', SCREEN_WIDTH + 100, 450, 5, 4, 20, 0, not invincible, collidable=False)
    enemy4 = characters.character('enemy', -100, 450, 5, 4, 20, 0, not invincible, collidable=False)
    cactus = characters.character('cactus', 1180, 420, 5, 3, 20, 0, invincible, collidable=True)
    cactus2 = characters.character('cactus', 100, 420, 5, 3, 20, 0, invincible, collidable=True)
    enemyGroup.add(enemy)
    enemyGroup.add(enemy2)
    enemyGroup.add(enemy3)
    enemyGroup.add(enemy4)
    enemyGroup.add(cactus)
    enemyGroup.add(cactus2)

    # ------------ CLOSE CONSTANTS/VARIABLES ------------ #


    # ------- BACKGROUND DRAWING FUNCTION ------- #
    def drawBackground(GAME):
        pygame.draw.line(GAME.gameScreen, GAME.RED, (0, 500), (GAME.SCREEN_WIDTH, 500))
        belowLine = pygame.Surface((GAME.SCREEN_WIDTH, GAME.SCREEN_HEIGHT - 500))
        belowLine.fill(GAME.TAN)
        GAME.gameScreen.blit(belowLine, (0, 500))
        GAME.gameScreen.blit(GAME.backgroundImg, (0, 0))
    
    def night(GAME):
        pygame.draw.line(GAME.gameScreen, GAME.RED, (0, 500), (GAME.SCREEN_WIDTH, 500))
        belowLine = pygame.Surface((GAME.SCREEN_WIDTH, GAME.SCREEN_HEIGHT - 500))
        belowLine.fill(GAME.TAN)
        GAME.gameScreen.blit(belowLine, (0, 500))
        GAME.gameScreen.blit(GAME.nightImg, (0, 0))
    # ------------------------------------------- #


    # ---------- INFO TEXT FUNCTION ---------- #
    def drawText(text, font, textColor, x, y, GAME):
        img = font.render(text, True, textColor)
        GAME.gameScreen.blit(img, (x, y))
    # ---------------------------------------- #


    # ----- START-UP SCREEN FUNCTION ----- #
    def showStartScreen(GAME):
       
        # Screen Coords
        GAME.gameScreen.fill(GAME.TAN)
        centerScreenX = (GAME.SCREEN_WIDTH - GAME.startScreen.get_width()) // 2
        centerScreenY = (GAME.SCREEN_HEIGHT - GAME.startScreen.get_height()) * (0.2)

        startScreenHatX = (GAME.SCREEN_WIDTH - GAME.scaledHat.get_width()) // 2
        startScreenHatY = (GAME.SCREEN_HEIGHT - GAME.scaledHat.get_width()) // 2

        enterPromptX = (GAME.SCREEN_WIDTH - GAME.enterToPlay.get_width()) // 2
        enterPromptY = (GAME.SCREEN_HEIGHT - GAME.enterToPlay.get_height()) * (0.75) 

        GAME.gameScreen.blit(GAME.startScreen, (centerScreenX, centerScreenY))
        GAME.gameScreen.blit(GAME.scaledHat, (startScreenHatX, startScreenHatY))
        GAME.gameScreen.blit(GAME.enterToPlay, (enterPromptX, enterPromptY))

        pygame.display.update()
        waitingToStart = True

        while waitingToStart:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waitingToStart = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    # ------------------------------------ #
                    


    def pausedScreen(GAME):
        GAME.gameScreen.fill(GAME.TAN)

        # Ensure player is paused; Will add enemy and platform pause as needed.
        # May result in its own function...
        initGame.movingLeft  = False
        initGame.movingRight = False
        initGame.shooting    = False

        # Screen Coords
        ScreenX = (GAME.SCREEN_WIDTH - GAME.scaledPause.get_width()) // 2
        ScreenY = (GAME.SCREEN_HEIGHT - GAME.scaledPause.get_height()) * (0.2)

        #display pause banner
        GAME.gameScreen.blit(GAME.scaledPause, (ScreenX, ScreenY))
        initGame.resume_button.draw(GAME.gameScreen)
        initGame.quit_button.draw(GAME.gameScreen)
        


    def scrollingScreen(GAME, scroll, t1, t2, t3):
        initGame.movingLeft  = t1
        initGame.movingRight = t2
        initGame.shooting    = t3
        
        tiles = math.ceil(GAME.SCREEN_WIDTH / GAME.scrolling_width) + 1
        #draw scrolling background
        for i in range(0,tiles):
            GAME.gameScreen.blit(GAME.scrollingImg, (i* GAME.scrolling_width + scroll, 0))
        
        GAME.gameScreen.blit(GAME.scaledcredits, (530,0))


    def desert(GAME, scroll, t1, t2, t3):
        tiles = math.ceil(GAME.SCREEN_WIDTH / GAME.desert_width) + 1
        #draw scrolling background
        for i in range(0,tiles):
            GAME.gameScreen.blit(GAME.desertImg, (i* GAME.desert_width + scroll, 0))


    def gameOver(GAME):
        ScreenX = (GAME.SCREEN_WIDTH - GAME.scaledOver.get_width()) // 2
        ScreenY = (GAME.SCREEN_HEIGHT - GAME.scaledOver.get_height()) * (0.2)

        #display pause banner
        GAME.gameScreen.blit(GAME.scaledOver, (ScreenX, ScreenY))


    def tumblerStorm(GAME):

        GAME.tumbler2.update()
        GAME.tumbler2.draw()

        GAME.tumbler3.update()
        GAME.tumbler3.draw()

        GAME.tumbler4.update()
        GAME.tumbler4.draw()
    

    # Check if enemies are dead; If dead, respawn off screen
    def respawnEnemies():
        if initGame.enemy.alive == False and initGame.enemy.deathTimer <= 0:
            initGame.enemyGroup.remove(initGame.enemy)
            del initGame.enemy
            initGame.enemy = characters.character('enemy', initGame.SCREEN_WIDTH + 100, 450, 5, 2, 20, 0, not initGame.invincible, collidable=False)
            initGame.enemyGroup.add(initGame.enemy)
            
        if initGame.enemy2.alive == False and initGame.enemy2.deathTimer <= 0:
            initGame.enemyGroup.remove(initGame.enemy2)
            del initGame.enemy2
            initGame.enemy2 = characters.character('enemy', -100, 450, 5, 2, 20, 0, not initGame.invincible, collidable=False)
            initGame.enemyGroup.add(initGame.enemy2)

        if initGame.enemy3.alive == False and initGame.enemy3.deathTimer <= 0:
            initGame.enemyGroup.remove(initGame.enemy3)
            del initGame.enemy3
            initGame.enemy3 = characters.character('enemy', -initGame.SCREEN_WIDTH + 100, 450, 5, 2, 20, 0, not initGame.invincible, collidable=False)
            initGame.enemyGroup.add(initGame.enemy3)

        if initGame.enemy4.alive == False and initGame.enemy4.deathTimer <= 0:
            initGame.enemyGroup.remove(initGame.enemy4)
            del initGame.enemy4
            initGame.enemy4 = characters.character('enemy', -100, 450, 5, 2, 20, 0, not initGame.invincible, collidable=False)
            initGame.enemyGroup.add(initGame.enemy4)
    
    # Add some more difficulty after some time
    def moreDifficulty():
        # After X amount of time, adjust enemy speeds
        if initGame.survivedTime > 900 and initGame.moreSpeed == True:
            initGame.enemy.speed += 0.5
            initGame.enemy2.speed += 0.5
            initGame.moreSpeed = False

        # After X amount of time, add another enemy
        if initGame.survivedTime > 1800 and initGame.newEnemy1 == True:
            initGame.moreSpeed = True
            initGame.newEnemy1 = False

        # After X amount of time, add another enemy
        if initGame.survivedTime > 3600 and initGame.newEnemy2 == True:
            initGame.newEnemy2 = False

        # After new enemies are in, simply increase speed until practically impossible to play lol
        if (initGame.newEnemy1 == False and initGame.newEnemy2 == False) and initGame.survivedTime > 1800:
            initGame.enemy.speed += 0.5
            initGame.enemy2.speed += 0.5
            initGame.enemy3.speed += 0.5
            initGame.enemy4.speed += 0.5

            # Randomly adjust platform speeds
            initGame.platform.speed = random.randint(1, 5)
            initGame.platform2.speed = random.randint(1, 5)
            initGame.platform3.speed = random.randint(1, 5)

            # Continually add more enemy speed, lock out health items (aside from the 1% chance full restore)
            initGame.survivedTime = 0   # Reset Timer
            initGame.ITEM_LOCK = True
            

# ----------------------- CLOSE initGame CLASS ----------------------- #