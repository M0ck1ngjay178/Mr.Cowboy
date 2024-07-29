# Pygame -- Mr. Cowboy
# Caleb Massey, Margo Bonal
# characters.py
# Stores character class and player's healthbar class

# LIBRARIES
import pygame
import os
import sys
import random

# MODULES
import setUp
import attacks
import items

# ------------ CHARACTER SET-UP ------------ #
# Used as a blueprint for ALL characters
class character(pygame.sprite.Sprite):

    # INITIALIZATION OF ALL CHARACTER INSTANCES
    def __init__(self, charType, spawnX, spawnY, scale, speed, ammo, dynaSticks, isInvincible, collidable=True):
        pygame.sprite.Sprite.__init__(self)

        # Determines if character is alive
        self.alive = True
        invincible = isInvincible
        if invincible:
            self.health = 999999  # Simulate invincibility
        else:
            self.health = 100     # "Mortal Peasant"
        self.maxHealth = self.health
        self.deathTimer = 120     # Time until remains disappear

        # Determines type of character; player, enemy, npc, etc.
        self.charType = charType

        # Creates character's movement speed
        self.speed = speed

        # Handles direction character faces
        self.direction = 1  # -1 is West : 1 is East
        self.jump = False
        self.inAir = True
        self.velocityY = 0
        self.onPlatform1 = False
        self.onPlatform2 = False
        self.onPlatform3 = False
        self.onGround = True
        self.fallingOffPlatform = False
        self.canLand = False
        self.flip = False

        #AI specific variables
        self.move_counter = 0
        self.ai_idling = False
        self.ai_idling_counter = 0
        self.ai_vision = pygame.Rect(0,0, 150, 20) #(x, y,how far can see, height )
        self.moreVision = False  # Flag for new enemies to get more vision when needed
        
        # Added Points Flag -- AI Specific
        self.addedPoints = False

        # Animation List; Stores a characters animation frames based on actions
        self.animationList = []
        self.currentFrame = 0
        tempList = []

        # Used as flags for animation; 0 = IDLE, 1 = MOVING EAST/WEST
        self.action = 0
        
        # Shooting variables
        self.shootCooldown = 0
        self.reloadCount = 6
        self.ammoLeft = ammo
        self.maxAmmo = ammo

        # Dynamite Variables
        self.dynaSticks = dynaSticks

        # Baseline for updating sprite frames
        self.updateTime = pygame.time.get_ticks()

        # Load all animation types for player
        animationTypes = ['IDLE', 'WALKING', 'JUMPING', 'SHOOTING', 'DEATH', 'WALKING_SHOOT']
        for animation in animationTypes:
            # Reset list of temp images
            tempList = []
            # See how many items are in a folder
            numOfFrames = len(os.listdir(f'img/{self.charType}/{animation}'))
            # Load all frames into array
            for i in range(numOfFrames):
                spriteImg = pygame.image.load(f'img/{self.charType}/{animation}/{i}.png').convert_alpha()
                spriteImg = pygame.transform.scale(spriteImg, (int(spriteImg.get_width() * scale), int(spriteImg.get_height() * scale)))
                tempList.append(spriteImg)
            self.animationList.append(tempList)     

        # Puts our image in the spriteImage var... Now a 2D List
        self.spriteImage = self.animationList[self.action][self.currentFrame]
        
        # Creates a boundary box using size of our image; Used for movements and collisions; "Hitbox"
        self.rect = self.spriteImage.get_rect()
        self.rect.center = (spawnX,spawnY) #Positions rectangle based on x,y coords.

        #set collidable
        self.collidable = collidable
        
    # HANDLES IDLE COUNTERS
    def update(self):
        self.updateAnimation()
        self.checkIfAlive()
        # Update cooldown
        if self.shootCooldown > 0:
            self.shootCooldown -= 1
        
    def gravity(self, dy):
        self.velocityY += setUp.initGame.GRAVITY
        if self.velocityY > 7:
            self.velocityY = 7
        dy += self.velocityY
        return dy

    # MOVEMENT FOR ALL INSTANCES
    def move(self, movingLeft, movingRight, platform1, platform2, platform3):

        # Reset movement vars (d = delta... change in x, change in y)
        dx = 0
        dy = 0

        # Assign movement vars if moving in any given direction
        if movingRight:
            dx = self.speed
            self.flip = False
            self.direction = 1
            # Ensure player cannot wander off screen
            if self.rect.right >= setUp.initGame.SCREEN_WIDTH + 50:
                self.rect.x = -50
                #dx = 0
            else:
                movingRight = movingRight

        if movingLeft:
            dx = -self.speed
            self.flip = True
            self.direction = -1
            # Ensure player cannot wander off screen
            if self.rect.left <= -50:
                self.rect.x = setUp.initGame.SCREEN_WIDTH + 50
                #dx = 0
            else:
                movingLeft = movingLeft

        # Apply jump and gravity
        dy = (self.gravity(dy))

        # Jumping action
        if ((self.jump == True) and (self.inAir == False)):
            self.velocityY = -13
            self.jump = False
            self.inAir = True
            self.fallingOffPlatform = False
            self.onPlatform1 = False
            self.onPlatform2 = False
            self.onPlatform3 = False
            self.canLand = True
            self.onGround = False

        # ------------ PLATFORM COLLISION ------------ #
        # Falling off platforms
        if ((self.onPlatform1 == False) and (self.onPlatform2 == False) and (self.onPlatform3 == False)) and (self.fallingOffPlatform == True):
            self.jump = False
            self.inAir = True
            self.canLand = True
            self.onGround = False
        

        # PLATFORM 1
        if (self.rect.bottom + dy <= platform1.rect.top) and (self.canLand == True) and (self.fallingOffPlatform == False) and (self.onPlatform2 == False) and (self.onPlatform3 == False):
            self.onPlatform1 = True
            self.onPlatform2 = False
            self.onPlatform3 = False
        elif (self.onPlatform1 == True):
            dy = platform1.rect.top - self.rect.bottom
            self.jump = False
            self.inAir = False

        # PLATFORM 2
        if (self.rect.bottom + dy <= platform2.rect.top) and (self.canLand == True) and (self.fallingOffPlatform == False) and (self.onPlatform3 == False):
            self.onPlatform1 = False
            self.onPlatform2 = True
            self.onPlatform3 = False
        elif (self.onPlatform2 == True):
            dy = platform2.rect.top - self.rect.bottom
            self.jump = False
            self.inAir = False

        # PLATFORM 3
        if (self.rect.bottom + dy <= platform3.rect.top) and (self.canLand == True) and (self.fallingOffPlatform == False) and (self.onPlatform1 == False):
            self.onPlatform1 = False
            self.onPlatform2 = False
            self.onPlatform3 = True
        elif (self.onPlatform3 == True):
            dy = platform3.rect.top - self.rect.bottom
            self.jump = False
            self.inAir = False

        # IS PLAYER OFF/ON PLATFORM?
        # PLATFORM 1
        if ((self.rect.left) > platform1.rect.right - 25) or ((self.rect.right) < platform1.rect.left + 25):
            if (self.onPlatform1 == True and self.rect.bottom + dy == platform1.rect.top):
                self.onPlatform1 = False
                self.canLand = False
                self.inAir = True
                self.jump = False
                self.fallingOffPlatform = True
        # PLATFORM 2
        if ((self.rect.left) > platform2.rect.right - 25) or ((self.rect.right) < platform2.rect.left + 25):
            if (self.onPlatform2 == True and self.rect.bottom + dy == platform2.rect.top):
                self.onPlatform2 = False
                self.canLand = False
                self.inAir = True
                self.jump = False
                self.fallingOffPlatform = True
        # PLATFORM 3
        if ((self.rect.left) > platform3.rect.right - 25) or ((self.rect.right) < platform3.rect.left + 25):
            if (self.onPlatform3 == True and self.rect.bottom + dy == platform3.rect.top):
                self.onPlatform3 = False
                self.canLand = False
                self.inAir = True
                self.jump = False
                self.fallingOffPlatform = True

        # ------------ END PLATFORM COLLISION ------------ #

        # Ground Collision
        if self.rect.bottom + dy > 500:
            dy = 500 - self.rect.bottom
            self.onGround = True
            self.fallingOffPlatform = False
            self.inAir = False

        # Update rectangle position
        self.rect.x += dx
        self.rect.y += dy


    # SHOOTING METHOD FOR ALL CLASSES
    def shoot(self, choice):
        if self.shootCooldown == 0 and self.ammoLeft > 0:
            self.shootCooldown = 20
            bullet = attacks.Bullet(self.rect.centerx + ((0.95)*self.rect.size[0] * (self.direction)), 12 + self.rect.centery, -self.direction, choice, 5) #add parameter for who here
            setUp.initGame.bulletGroup.add(bullet)
            self.updateAction(3) # 3 = Shooting
            # Reduces ammo
            # self.ammoLeft -= 1 ---- Enemies have INFINITE ammo.
            self.reloadCount -= 1

        if self.reloadCount == 0:
            self.reloadCount = 6
            self.shootCooldown = 60


    # SHOOTING METHOD FOR PLAYER INSTANCE ONLY!!!
    def playerShoot(self, movingLeft, movingRight):
        if self.shootCooldown == 0 and self.ammoLeft > 0:
            self.shootCooldown = 20
            choice = "player"
            bullet = attacks.Bullet(self.rect.centerx + ((0.95)*self.rect.size[0] * (self.direction)), 12 + self.rect.centery, -self.direction, choice, 8)#add parameter for who here
            setUp.initGame.bulletGroup.add(bullet)

            if movingLeft or movingRight:
                self.updateAction(5) # 5 = Moving Shooting
            else:
                self.updateAction(3) # 3 = Idle Shooting
            
            # Reduces ammo
            self.ammoLeft -= 1
            self.reloadCount -= 1

        if self.reloadCount == 0:
            self.reloadCount = 6
            self.shootCooldown = 60


    # UPDATE OUR SPRITE TO MAKE IT ANIMATED
    def updateAnimation(self):
        # Timer for animation update; Controls speed of animation
        ANIMATION_SPEED = 125

        # Update image depending on current frame
        self.spriteImage = self.animationList[self.action][self.currentFrame]

        # Check how much time has passed since prev update
        if (pygame.time.get_ticks() - self.updateTime > ANIMATION_SPEED):
            self.updateTime = pygame.time.get_ticks()
            self.currentFrame += 1

        # If animation ends, reset to start
        if self.currentFrame >= len(self.animationList[self.action]):
            if self.action == 4:
                self.currentFrame = len(self.animationList[self.action]) - 1
            else:
                self.currentFrame = 0

    # Update action based on key inputs
    def updateAction(self, newAction):
        # Check if new is different than previous
        if newAction != self.action:
            self.action = newAction
            # Update animation settings
            self.currentIndex = 0
            self.currentFrame = 0
            self.updateTime = pygame.time.get_ticks()

    # Determine item drop on enemy death
    def getItem():  
        randValue = random.randint(0, 100)
        if setUp.initGame.ITEM_LOCK == False:    
            if randValue < 15 and randValue >= 0:
                itemID = 'HEALTH'
            elif randValue < 20 and randValue >= 15:
                itemID = 'SPEED'
            elif randValue < 60 and randValue >= 20:
                itemID = 'DYNAMITE'
            elif randValue < 99 and randValue >= 60:
                itemID = 'AMMO'
            elif randValue == 100:
                itemID = 'RESTORE'
            else:   # Exists to prevent error
                itemID = 'AMMO'
            
            return itemID
        elif setUp.initGame.ITEM_LOCK == True:
            if randValue < 50 and randValue >= 0:
                itemID = 'AMMO'
            elif randValue < 75 and randValue >= 50:
                itemID = 'DYNAMITE'
            elif randValue < 90 and randValue >= 75:
                itemID = 'SPEED'
            elif randValue == 100:
                itemID = 'RESTORE'
            else:
                itemID = 'AMMO'
            
            return itemID

    # Check and update health based on hits
    def checkIfAlive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.updateAction(4) # 4 = Dead
            self.deathTimer -= 1

    def collide(self, other):
        return self.rect.colliderect(other.rect)

    # Function for enemy collisions with player
    def enemy_collisions(self, player, BulletType): 
        if player.collide(self) and self.collidable:
            # Make the enemy turn towards the player
            if self.rect.x < player.rect.x:
                # if player to right of enemy, enemy turn right
                self.direction = 1
                self.flip = False
            else:
                # if player left of the enemy, make the enemy face left
                self.direction = -1
                self.flip = True
                
            # Make the enemy shoot
            self.shoot(BulletType)
        else:
            self.updateAction(0)

    #AI for enemies
    def ai(self, BulletType):

        if self.alive and setUp.initGame.player.alive:
            if self.ai_idling == False and random.randint(1,200) == 1:
                self.ai_idling = True
                self.updateAction(0) #set animation back to idle
                self.ai_idling_counter = 50

            #Increase vision after X amount of time
            if setUp.initGame.survivedTime > 1000 and self.moreVision == False:     
                self.ai_vision = pygame.Rect(0,0, 400, 20)   #(x, y,how far he can see, height )
                self.moreVision = True

            #Check if enemy sees player
            if self.ai_vision.colliderect(setUp.initGame.player.rect):
                #stop and face
                self.updateAction(0) #idle
                self.shoot(BulletType)
            else: # if he doesnt see, then patrol
                if self.ai_idling == False:
                    if self.direction == 1:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False

                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right,setUp.initGame.platform3, setUp.initGame.platform2, setUp.initGame.platform) 
                    self.updateAction(1) #walking
                    self.move_counter += 1
                    #----update vision----
                    self.ai_vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)
                    #DEBUGGING CHECK, TO VISUALIZE WHERE HE LOOKING
                    #pygame.draw.rect(setUp.initGame.gameScreen, setUp.initGame.RED, self.ai_vision)

                    if self.move_counter > 70:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.ai_idling_counter -= 1
                    if self.ai_idling_counter <= 0:
                     self.ai_idling = False

        

        # Award player 100 points for each enemy kill
        if self.alive == False and self.addedPoints == False:
            setUp.initGame.currentScore += 100
            self.addedPoints = True
            itemDrop = character.getItem()
            itemBox = items.ItemBox(itemDrop, self.rect.centerx, self.rect.centery)
            setUp.initGame.itemBoxGroup.add(itemBox)

        # Forced left/right movement so they don't go/remain off screen.
        if self.rect.left <= 175:
            ai_moving_right = True
            ai_moving_left = False
            self.move(ai_moving_left, ai_moving_right,setUp.initGame.platform3, setUp.initGame.platform2, setUp.initGame.platform) 
        else:
            ai_moving_left = False
            ai_moving_right = False
        
        if self.rect.right >= setUp.initGame.SCREEN_WIDTH - 175:
            ai_moving_right = False
            ai_moving_left = True
            self.move(ai_moving_left, ai_moving_right,setUp.initGame.platform3, setUp.initGame.platform2, setUp.initGame.platform) 
        else:
            ai_moving_left = False


    # DISPLAYING METHOD OF ALL INSTANCES
    def draw(self):
        setUp.initGame.gameScreen.blit(pygame.transform.flip(self.spriteImage, self.flip, False), self.rect)


# ---------------------- CLOSE CHARACTER CLASS ---------------------- #
        


# ---------------------- START HEALTHBAR CLASS ---------------------- #
class HealthBar():
    def __init__(self, x, y, health, maxHealth):
        self.x = x
        self.y = y
        self.health = health
        self.maxHealth = maxHealth

    def draw(self, health):
        # Update Health Bar w/ new Health Value
        self.health = health
        
        # Calc health ratio
        ratio = self.health / self.maxHealth

        # Draw healthbar
        pygame.draw.rect(setUp.initGame.gameScreen, setUp.initGame.BLACK, (self.x - 2, self.y - 2, 154, 24))
        pygame.draw.rect(setUp.initGame.gameScreen, setUp.initGame.RED, (self.x, self.y, 150, 20))
        pygame.draw.rect(setUp.initGame.gameScreen, setUp.initGame.GREEN, (self.x, self.y, 150 * ratio, 20))


# ---------------------- CLOSE HEALTHBAR CLASS ---------------------- #
