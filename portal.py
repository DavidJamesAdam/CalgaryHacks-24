import pygame
from player import Player
from levelList import LevelList

class Portal(pygame.sprite.Sprite):
    def __init__(self, surface, size, location, player, scoremax):
        super().__init__()

        self.surface = surface
        self.size = size
        self.location = location
        self.player = player
        self.scoremax = scoremax

        self.isActive = False

        left = location[0] - (size/2)
        top = location[1] - size/2
        self.rect = pygame.Rect(left, top, size, size)

        self.image = pygame.image.load("images/PortalTexture.png")
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

    def update(self):
        if (self.player.score > self.scoremax):
            self.isActive = True
            
        if self.isActive:
            self.image = pygame.transform.scale(self.portalImage, (self.rect.width, self.rect.height))
        else:
            self.image = pygame.Surface((0, 0))  # Invisible image

    def deactivatePortal(self):
        self.isActive = False

    # def drawPortal(self):
    #     if (self.isActive):
    #         self.surface.blit(self.sprite.image,self.rect)

    def playerCollidesWithPortal(self):
        collision = pygame.sprite.spritecollideany(self.player, self, pygame.sprite.collide_mask)
        if collision is not None:
            # # Determine the direction of the collision
            # dx = self.player.rect.centerx - collision.rect.centerx
            # dy = self.player.rect.centery - collision.rect.centery
            # # Normalize the direction vector
            # dist = math.hypot(dx, dy)
            # dx, dy = dx / dist, dy / dist

            # # Move the player away from the wall
            # self.player.rect.x += dx * 10
            # self.player.rect.y += dy * 10
            return True
        return False
        
    def updatePortal(self):
        # print(self.player.score, " ", self.scoremax, " ", self.player.score > self.scoremax)
        if (self.player.score > self.scoremax):
            self.isActive = True

    def deactivatePortal(self):
        self.isActive = False
