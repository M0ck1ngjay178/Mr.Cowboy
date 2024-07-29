
# Pygame -- Mr. Cowboy
# Caleb Massey, Margo Bonal
# environment.py
# Contains environment features; tumbleweeds, platforms, etc.

# LIBRARIES
import pygame
import os
import sys

# MODULES
import setUp


# ------------- TUMBLEWEED CLASS ------------- #
class Tumbleweed():
    def __init__(self, screen, image, x, y, speed, rotation, scale):
        self.screen = screen
        self.tumbleImg = pygame.image.load(image)
        self.tumbleImg = pygame.transform.scale(self.tumbleImg, (int(self.tumbleImg.get_width() * scale), int(self.tumbleImg.get_height() * scale)))
        self.rect = self.tumbleImg.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.rotationSpeed = rotation
        self.angle = 0

        self.image = self.tumbleImg.copy()


    def update(self):
        # Move along X axis; No movement on Y
        self.rect.x += self.speed

        # Tumble the weed
        self.angle -= self.rotationSpeed
        if self.angle <= 0:
            self.angle += 360

        self.image = pygame.transform.rotate(self.tumbleImg, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Stop tumbleweed at edge;
        if self.rect.x > setUp.initGame.SCREEN_WIDTH + self.rect.width:
            self.rect.x = -self.rect.width
        elif self.rect.left > setUp.initGame.SCREEN_WIDTH:
            self.rect.right = 0
        
        #Collision

        if pygame.sprite.collide_rect(self, setUp.initGame.player):
            setUp.initGame.player.health -= 0.5
        

    def draw(self):
        self.screen.blit(self.image, self.rect)



# ------------- PLATFORM CLASS ------------- #
class platform(pygame.sprite.Sprite):

    def __init__(self, screen, image, x, y, speed, scale):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.platformImg = pygame.image.load(image)
        self.platformImg = pygame.transform.scale(self.platformImg, (int(self.platformImg.get_width() * scale), int(self.platformImg.get_height() * scale)))
        self.rect = self.platformImg.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def getSpeed(self):
        return int(self.speed)

    def update(self):         
        # Move platform to left of screen upon creation
        self.rect.x -= self.speed

        # Move back to other side of screen if gone
        if self.rect.left < -100:            
            self.rect.x = setUp.initGame.SCREEN_WIDTH + 100

    def draw(self):
        self.screen.blit(self.platformImg, self.rect)
