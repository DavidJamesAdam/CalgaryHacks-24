import pygame
from player import Player
from levelList import LevelList

class Portal:
    def __init__(self,surface,size,location,player,scoremax):
        self.surface = surface
        self.size = size
        self.location = location
        self.player = player
        self.scoremax = scoremax

        self.isActive = False

        left = location[0] - (size/2)
        top = location[1] - size/2
        self.rect = pygame.Rect(left,top,size,size)

        self.sprite = pygame.sprite.Sprite()
        self.portalImage = pygame.image.load("images/PortalTexture.png")
        self.sprite.image = pygame.transform.scale(self.portalImage, (self.rect.width, self.rect.height))

    def drawPortal(self):
        if (self.isActive):
            self.surface.blit(self.sprite.image,self.rect)

    def playerCollidesWithPortal(self):
        if (self.isActive):
            return self.rect.colliderect(self.player.rect)
        
    def updatePortal(self):
        print(self.player.score, " ", self.scoremax, " ", self.player.score > self.scoremax)
        if (self.player.score > self.scoremax):
            self.isActive = True

    def deactivatePortal(self):
        self.isActive = False
