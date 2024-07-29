# Pygame -- Mr. Cowboy
# Caleb Massey, Margo Bonal
# items.py
# Stores various collectibles information pieces

# LIBRARIES
import pygame
import os
import sys

# MODULES
import setUp

# ---------------------- START COLLECTIBLE CLASS ---------------------- #
class ItemBox(pygame.sprite.Sprite):
    
    def __init__(self, itemType, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        # Whenever an item type is passed, we choose the sprite (and effect) with this.
        self.itemType = itemType

        self.image = setUp.initGame.itemBoxes[self.itemType]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + (setUp.initGame.TILE_SIZE // 2), y + (setUp.initGame.TILE_SIZE - self.image.get_height()))


    def update(self):
        # Check for player collision using player's rectangle
        if pygame.sprite.collide_rect(self, setUp.initGame.player):
            # Check itemBox type
            if self.itemType == 'HEALTH' and setUp.initGame.player.health < 100:
                setUp.initGame.player.health += 25
                if setUp.initGame.player.health > setUp.initGame.player.maxHealth:
                    setUp.initGame.player.health = setUp.initGame.player.maxHealth
            elif self.itemType == 'AMMO' and setUp.initGame.player.ammoLeft < 24:
                setUp.initGame.player.ammoLeft += 12
                if setUp.initGame.player.ammoLeft > setUp.initGame.player.maxAmmo:
                    setUp.initGame.player.ammoLeft = setUp.initGame.player.maxAmmo
            elif self.itemType == 'DYNAMITE':
                setUp.initGame.player.dynaSticks += 2
            elif self.itemType == 'SPEED' and setUp.initGame.player.speed <= 5:
                setUp.initGame.player.speed += 1
            elif self.itemType == 'RESTORE':
                setUp.initGame.player.health = setUp.initGame.player.maxHealth
                setUp.initGame.player.ammoLeft = setUp.initGame.player.maxAmmo
                setUp.initGame.player.dynaSticks += 5

            self.kill()

# ---------------------- CLOSE COLLECTIBLE CLASS ---------------------- #