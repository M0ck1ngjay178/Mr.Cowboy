# Pygame -- Mr. Cowboy
# Caleb Massey, Margo Bonal
# attacks.py
# Stores various attack classes (Bullet, Dynamite, Explosion)

# LIBRARIES
import pygame
import os
import sys

# MODULES
import setUp

# ---------------------- START BULLET CLASS ---------------------- #
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, choice, speed): #choice for whose bullet to shoot
        pygame.sprite.Sprite.__init__(self)
        
        # Speed and direction of every bullet
        self.bulletSpeed = speed
        self.flip = True

        # Determine which way bullet is facing upon being fired
        if direction == 1:
            self.flip = False
        elif direction == -1:
            self.flip = True

        # Bullet Image setup
         #---------------------------------------------#
        if choice == "player":
            self.image = setUp.initGame.playerBullet
        elif choice == "enemy":
             self.image = setUp.initGame.enemyBullet
        elif choice == "cactus":
             self.image = setUp.initGame.cactusBullet
        else: #Default bullet = set to player's bullet img
            self.image = setUp.initGame.playerBullet
        #---------------------------------------------#
       # self.image = setUp.initGame.playerBullet
        self.rect = self.image.get_rect()       
        self.rect.center = (x,y)
        self.direction = direction


        # If looking left, bullet is drawn fired to the left. Otherwise, right.
        if self.direction == 1:
            self.image = pygame.transform.flip(self.image, self.direction, False)
        else:
            self.image = pygame.transform.flip(self.image, False, False)

    def update(self):
        # Move the bullet
        self.rect.x -= (self.direction * self.bulletSpeed)

        # Check if bullet has left screen: Delete if so.
        if self.rect.right < 0 or self.rect.left > setUp.initGame.SCREEN_WIDTH:
            self.kill()

        # Check collision with characters
        if pygame.sprite.spritecollide(setUp.initGame.player, setUp.initGame.bulletGroup, False):
            if setUp.initGame.player.alive:
                self.kill()
                setUp.initGame.player.health -= 10
        for enemy in setUp.initGame.enemyGroup:
            if pygame.sprite.spritecollide(enemy, setUp.initGame.bulletGroup, False):
                if enemy.alive:
                    self.kill()
                    enemy.health -= 30


# ---------------------- CLOSE BULLET CLASS ---------------------- #



# ---------------------- START DYNAMITE CLASS ---------------------- #
class Dynamite(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        
        # Fuse 'Length'/Timer
        self.timer = 100

        # Speed and direction of every throw
        self.velY = -9        
        self.speed = 8
        self.flip = True

        # Dynamite Image setup
        self.image = setUp.initGame.dynamiteImg
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction

    def update(self):
        
        # Create arc of movement for throwable
        self.velY += setUp.initGame.GRAVITY
        dx = self.direction * self.speed
        dy = self.velY

        # Check for floor collision
        if self.rect.bottom + dy > 500:
            dy = 500 - self.rect.bottom
            self.speed = 0

        # Check for wall collision
        if (self.rect.left + dx < 0):
            self.rect.x = setUp.initGame.SCREEN_WIDTH
        
        if (self.rect.right + dx > setUp.initGame.SCREEN_WIDTH):
            self.rect.x = 0

        # Update position
        self.rect.x += dx
        self.rect.y += dy

        # Countdown Timer for Explosion
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            explosion = Explosion(self.rect.centerx, self.rect.y - 25, 5)
            setUp.initGame.explosionGroup.add(explosion)

            # Check for collision to apply damage to anybody
            if abs(self.rect.centerx - setUp.initGame.player.rect.centerx) < setUp.initGame.TILE_SIZE * 2 and abs(self.rect.centery - setUp.initGame.player.rect.centery) < setUp.initGame.TILE_SIZE * 2:
                setUp.initGame.player.health -= 50
            for enemy in setUp.initGame.enemyGroup:
                if abs(self.rect.centerx - enemy.rect.centerx) < setUp.initGame.TILE_SIZE * 2 and abs(self.rect.centery - enemy.rect.centery) < setUp.initGame.TILE_SIZE * 2:
                    enemy.health -= 75
            

# ---------------------- CLOSE DYNAMITE CLASS ---------------------- #


# ---------------------- START EXPLOSION CLASS ---------------------- #
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)

        # Load explosion frames into list
        self.images = []
        for i in range (1, 9):
            explosionImg = pygame.image.load(f'img/icons/EXPLOSION/{i}.png').convert_alpha()
            explosionImg = pygame.transform.scale(explosionImg, (int(explosionImg.get_width() * scale), int(explosionImg.get_height() * scale)))
            self.images.append(explosionImg)
        
        # Set current frame
        self.currentFrame = 0
        self.image = self.images[self.currentFrame]

        # Hitbox Image setup
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0


    def update(self):

        # Controls speed of explosion animation
        EXPLOSION_SPEED = 4

        # Update explosion animation
        self.counter += 1
        if self.counter >= EXPLOSION_SPEED:
            self.counter = 0
            self.currentFrame += 1
            # If animation completed, delete explosion
            if self.currentFrame >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.currentFrame]

# ---------------------- CLOSE EXPLOSION CLASS ---------------------- #