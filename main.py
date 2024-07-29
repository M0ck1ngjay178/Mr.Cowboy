
# Pygame -- Mr. Cowboy
# Caleb Massey, Margo Bonal
# main.py

# LIBRARIES
import pygame
import os
import sys
import time

# MODULES
import setUp
import attacks
import items
import environment

# --------------- UPDATE FUNCTION --------------- #
def updateGroups():

    # Check for dead enemies; Respawn if dead
    setUp.initGame.respawnEnemies()

    # Update Survived Time/Update difficulty
    setUp.initGame.survivedTime += 1
    setUp.initGame.moreDifficulty()
    
    # Update Day/Night Time
    setUp.initGame.worldTime += 1

    # Update Player
    setUp.initGame.player.update()
    setUp.initGame.player.draw()

    # Update Tumbleweed
    setUp.initGame.tumbler.update()
    setUp.initGame.tumbler.draw()

    # Update Platforms
    setUp.initGame.platform.update()
    setUp.initGame.platform.draw()
    setUp.initGame.platform2.update()
    setUp.initGame.platform2.draw() 
    setUp.initGame.platform3.update()
    setUp.initGame.platform3.draw()
    
    # Updates and draws enemies to screen
    setUp.initGame.enemy.update()
    setUp.initGame.enemy.draw()
    setUp.initGame.enemy2.update()
    setUp.initGame.enemy2.draw()
    # Draw and update new enemies
    if setUp.initGame.newEnemy1 == False:
        setUp.initGame.enemy3.update()
        setUp.initGame.enemy3.draw()
    elif setUp.initGame.newEnemy2 == False:
        setUp.initGame.enemy3.update()
        setUp.initGame.enemy3.draw()
        setUp.initGame.enemy4.update()
        setUp.initGame.enemy4.draw()
    setUp.initGame.cactus.update()
    setUp.initGame.cactus.draw()
    setUp.initGame.cactus2.update()
    setUp.initGame.cactus2.draw()
    
    # Update and Draw Groups
    setUp.initGame.bulletGroup.update()
    setUp.initGame.dynamiteGroup.update()
    setUp.initGame.explosionGroup.update()
    setUp.initGame.itemBoxGroup.update()

    setUp.initGame.bulletGroup.draw(setUp.initGame.gameScreen)
    setUp.initGame.dynamiteGroup.draw(setUp.initGame.gameScreen)
    setUp.initGame.explosionGroup.draw(setUp.initGame.gameScreen)
    setUp.initGame.itemBoxGroup.draw(setUp.initGame.gameScreen)
    setUp.initGame.pause_button.draw(setUp.initGame.gameScreen)
    setUp.initGame.sign_button.draw(setUp.initGame.gameScreen)
# ----------------------------------------------- #

def movUpdate():
    # Movement for player / enemies.
    setUp.initGame.player.move(setUp.initGame.movingLeft, setUp.initGame.movingRight, setUp.initGame.platform3, setUp.initGame.platform2, setUp.initGame.platform)
    setUp.initGame.cactus.move(False, False, setUp.initGame.platform3, setUp.initGame.platform2, setUp.initGame.platform)
    setUp.initGame.cactus.enemy_collisions(setUp.initGame.player, setUp.initGame.TypeC)
    setUp.initGame.cactus2.move(False, False, setUp.initGame.platform3, setUp.initGame.platform2, setUp.initGame.platform)
    setUp.initGame.cactus2.enemy_collisions(setUp.initGame.player, setUp.initGame.TypeC)
    setUp.initGame.horse.move(False, False, setUp.initGame.platform3, setUp.initGame.platform2, setUp.initGame.platform) #no (x,y) movement for horse 
    #------Call AI Movement for enemies--------#       
    setUp.initGame.enemy.ai(setUp.initGame.TypeE)
    setUp.initGame.enemy2.ai(setUp.initGame.TypeE)
    # Give new enemies AI Movements
    if setUp.initGame.newEnemy1 == False:
            setUp.initGame.enemy3.ai(setUp.initGame.TypeE)
    elif setUp.initGame.newEnemy2 == False:
            setUp.initGame.enemy3.ai(setUp.initGame.TypeE)
            setUp.initGame.enemy4.ai(setUp.initGame.TypeE)

def actionUpdate():
    # Update player actions
    if setUp.initGame.player.alive:
        # Shoot bullets
        if setUp.initGame.shooting:
            setUp.initGame.player.playerShoot(setUp.initGame.movingLeft, setUp.initGame.movingRight)
        # Throw grenades
        elif setUp.initGame.throwing and setUp.initGame.dynaThrown == False and setUp.initGame.player.dynaSticks > 0:
            dynamite = attacks.Dynamite(setUp.initGame.player.rect.centerx + (0.5 * setUp.initGame.player.rect.size[0] * setUp.initGame.player.direction), setUp.initGame.player.rect.top, setUp.initGame.player.direction)
            setUp.initGame.dynamiteGroup.add(dynamite)
            setUp.initGame.dynaThrown = True
            setUp.initGame.player.dynaSticks -= 1
        elif setUp.initGame.player.inAir and not(setUp.initGame.movingRight or setUp.initGame.movingLeft):
            setUp.initGame.player.updateAction(2) # 2 = Jumping
        elif (setUp.initGame.movingRight or setUp.initGame.movingLeft) and not setUp.initGame.player.inAir:
            setUp.initGame.player.updateAction(1) # 1 = East/West Walk
        elif setUp.initGame.player.inAir and (setUp.initGame.movingRight or setUp.initGame.movingLeft):
            setUp.initGame.player.updateAction(1) # 1 = Moving Jump
        elif setUp.initGame.shooting and (setUp.initGame.movingLeft or setUp.initGame.movingRight):
            setUp.initGame.player.updateAction(5) # 5 = Moving and Shooting
        else:
            setUp.initGame.player.updateAction(0) # 0 = Idle


# --------------- MAIN FUNCTION --------------- #
def main():

    # Initialize pygame
    pygame.init()

    # Creates constant object of class, GAME
    GAME = setUp.initGame()
    
    # Show start screen
    setUp.initGame.showStartScreen(GAME)

    #start game: unpaused
    gameState = setUp.initGame.UNPAUSED 
    
    while setUp.initGame.GAME_RUNNING == True:

        # Set framerate in place
        setUp.initGame.clock.tick(setUp.initGame.frameRate)

        # Continually Clear/Refresh BG
        #--------Toggle between Day/Night-----------------------------------#
        if setUp.initGame.worldTime <= 750:
            setUp.initGame.drawBackground(GAME)
        elif setUp.initGame.worldTime > 750 and setUp.initGame.worldTime <= 1500:
            setUp.initGame.night(GAME)
        else:
            setUp.initGame.worldTime = 0
        #-------------------------------------------------------------------#

        #CONDITION TO CHANGE BACKGROUND 
        if setUp.initGame.CHANGE_BACKGROUND:
            setUp.initGame.desert(GAME, setUp.initGame.scroll, False, False, False)
            #scroll HAS to be in main to update with while loop
            setUp.initGame.scroll -= 5
            #reset scroll 
            if abs(setUp.initGame.scroll) > setUp.initGame.scrolling_width:
                setUp.initGame.scroll = 0

        # Show Player Health Left
        setUp.initGame.drawText("HEALTH: ", setUp.initGame.infoFont, setUp.initGame.WHITE, 10, 510, GAME)
        setUp.initGame.healthBar.draw(setUp.initGame.player.health)

        # Show Bullets Left
        for x in range(setUp.initGame.player.ammoLeft):
            setUp.initGame.gameScreen.blit(setUp.initGame.playerBullet, (100 + (x * 20), 555))
        setUp.initGame.drawText('AMMO: ', setUp.initGame.infoFont, setUp.initGame.WHITE, 10, 550, GAME)

        # Show Dynamite Left
        for x in range(setUp.initGame.player.dynaSticks):
            setUp.initGame.gameScreen.blit(setUp.initGame.dynamiteImg, (175 + (x * 25), 585))
        setUp.initGame.drawText("DYNAMITE: ", setUp.initGame.infoFont, setUp.initGame.WHITE, 10, 590, GAME)

        # Show High Score
        setUp.initGame.drawText("HIGH SCORE: ", setUp.initGame.infoFont, setUp.initGame.WHITE, 10, 635, GAME)
        setUp.initGame.drawText(format(setUp.initGame.highScore, '0,'), setUp.initGame.infoFont, setUp.initGame.WHITE, 210, 635, GAME)

        # Show Current Score
        setUp.initGame.drawText("CURRENT SCORE:", setUp.initGame.infoFont, setUp.initGame.WHITE, 10, 675, GAME)
        setUp.initGame.drawText(format(setUp.initGame.currentScore, '0,'), setUp.initGame.infoFont, setUp.initGame.WHITE, 260, 675, GAME)

        # Updates all characters and groups
        updateGroups()
        actionUpdate()
        movUpdate()

        #---------------TUMBLEWEED STORM--------------#
        currentTime = time.time()

        if currentTime - setUp.initGame.start >= setUp.initGame.timer:
            setUp.initGame.tumblerStorm(GAME)
        #------------------------------------------------#
        
        #------------GAME OVER BANNER---------------#
        game_over_time = None
        if not setUp.initGame.player.alive:
            if game_over_time is None:
                game_over_time = time.time()
                setUp.initGame.gameOver(GAME) 
        #-------------------------------------------#

        # ---------- START OF EVENT HANDLING ---------- #
        # 'event' is our variable to use for everything in the loop.
        for event in pygame.event.get():

            # ---------- QUIT GAME ---------- #
            if event.type == pygame.QUIT:
                setUp.initGame.GAME_RUNNING = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    setUp.initGame.GAME_RUNNING = False
            
            #------END QUIT GAME---------------#

            #-------------PAUSED SCREEN/DESERT---------#
            #Click Pause button with Mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == True: 
                    if gameState == setUp.initGame.PAUSED:
                        # Check if the click is in the area of resume
                        if setUp.initGame.resume_button.draw(setUp.initGame.gameScreen):
                            gameState = setUp.initGame.UNPAUSED
                        elif setUp.initGame.quit_button.draw(setUp.initGame.gameScreen):
                            pygame.time.delay(1000) # 1 millisecond = 1 second, added delay because exit was too abrupt 
                            setUp.initGame.GAME_RUNNING = False
                    elif gameState == setUp.initGame.UNPAUSED:
                        # Check if the click is in the area of the pause 
                        if setUp.initGame.pause_button.draw(setUp.initGame.gameScreen):
                            gameState = setUp.initGame.PAUSED
                        # Check if the click is within the area of sign
                        elif setUp.initGame.sign_button.draw(setUp.initGame.gameScreen):
                            #gameState = setUp.initGame.DESERT
                            setUp.initGame.CHANGE_BACKGROUND = True

            elif event.type == pygame.KEYDOWN:
                #-------------------TRAVEL---------------------------#
                if event.key == pygame.K_t:
                    setUp.initGame.TRAVEL #= True
                    gameState = setUp.initGame.TRAVEL
                elif event.key == pygame.K_b:
                    if gameState == setUp.initGame.TRAVEL:
                        gameState = setUp.initGame.UNPAUSED
                #-------------------END TRAVEL-----------------------#
            

            #ALL MAIN GAME LOGIG: goes in unpaused
            if gameState == setUp.initGame.UNPAUSED:
            # ---------- MOVEMENTS ---------- #
            # KEYBOARD INPUT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a and setUp.initGame.player.alive:
                        setUp.initGame.movingLeft = True

                    if event.key == pygame.K_d and setUp.initGame.player.alive:
                        setUp.initGame.movingRight = True

                    if event.key == pygame.K_w and setUp.initGame.player.alive:
                        setUp.initGame.player.jump = True

                    if event.key == pygame.K_SPACE and setUp.initGame.player.alive:
                        setUp.initGame.shooting = True

                    if event.key == pygame.K_q and setUp.initGame.player.alive:
                        setUp.initGame.throwing = True

                    # DEBUGGING KEY
                    if event.key == pygame.K_p:  
                        print("DEBUGGING MODE ENABLED -- RESTART GAME TO EXIT")
                        print("SURVIVED TIME: ", setUp.initGame.survivedTime) 
                        setUp.initGame.player.maxHealth = 999999
                        setUp.initGame.player.health = 999999

                    # Extra way to quit game
                    if event.key == pygame.K_ESCAPE:
                        setUp.initGame.GAME_RUNNING = False            

                # KEYBOARD BUTTON RELEASE
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        setUp.initGame.movingLeft = False

                    if event.key == pygame.K_d:
                        setUp.initGame.movingRight = False

                    if event.key == pygame.K_SPACE:
                        setUp.initGame.shooting = False

                    if event.key == pygame.K_q:
                        setUp.initGame.throwing = False
                        setUp.initGame.dynaThrown = False
        
        # ---------- CLOSE EVENT HANDLING ---------- #

        #---------------GAME STATES---------------------------------------#

        #------------PAUSED------------------#
        #ALL PAUSE SCREEN LOGIC goes in paused
        if gameState == setUp.initGame.PAUSED:
            setUp.initGame.pausedScreen(GAME)
        #------------PAUSED------------------#

        #------------TRAVEL------------------#
        if gameState == setUp.initGame.TRAVEL:
            setUp.initGame.scrollingScreen(GAME, setUp.initGame.scroll, False, False, False)
            #scroll HAS to be in main to update with while loop
            setUp.initGame.scroll -= 5
            #reset scroll 
            if abs(setUp.initGame.scroll) > setUp.initGame.scrolling_width:
                setUp.initGame.scroll = 0

           #ONLY DISPLAY HERE:
            setUp.initGame.horse.update()
            setUp.initGame.horse.draw()
        #-----------END TRAVEL--------------#
        #--------------------------------------------------------------#
        #---------------END GAME STATES---------------------------------------#
            
        # DO NOT MOVE. EVER. PLEASE. UPDATES EVERYTHING SO IT WORKS PROPERLY. :)
        pygame.display.update()

        # Update HighScore (if needed)
        if setUp.initGame.currentScore > setUp.initGame.highScore:
            scoreInp = open("highScore.txt", "w")
            scoreInp.write(str(setUp.initGame.currentScore))
            scoreInp.close()

    pygame.quit()

# --------------------------------------------- #


# Call main; start program
#*********#
main()
#*********#
