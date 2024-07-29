
# Pygame -- Mr. Cowboy
# Caleb Massey, Margo Bonal
# guiFeatures.py
# Stores Constants and Variables used throughout the program

# LIBRARIES
import pygame
import os
import sys

#-----------------------GUI BUTTON CLASS---------------------------------#

class GUI_Button():
    
    def __init__(self, x, y, image, scale):
         self.width = image.get_width()
         self.height = image.get_height()

         self.image = pygame.transform.scale(image,(int(self.width * scale), int(self.height * scale)))
         self.rect = self.image.get_rect()
         self.rect.topleft =(x, y)
         self.clicked = False

   
    def draw(self, surface):
        action = False

        #get mouse pos
        pos = pygame.mouse.get_pos()

        #check mouseover and clickes conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action   
#-----------------------END GUI BUTTON CLASS-----------------------------#
