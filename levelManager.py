import pygame
import math
from player import Player
from levelList import LevelList
from portal import Portal

# Level design class.
# Level drawing, updating, and collision detection done in this class.

class LevelManager:
    def __init__(self,surface, wallShade, wallThicc, wallUpdateRate, wallSpriteGroup, player):
        self.surface = surface
        self.screenSize = surface.get_size()
        self.wallColour = wallShade
        self.wallThickness = wallThicc
        self.wallUpdateRate = wallUpdateRate
        self.wallUpdateTick = 0
        self.player = player
        
        # level is made of a series of boxes, each of which can increase/decrease in size, and also a background colour
        self.levelRectangles = []
        self.wallSprites = []
        self.wallSpriteGroup = wallSpriteGroup
        self.levelNumber = -1

        # levelList
        self.lvls = LevelList(self.screenSize,self.wallThickness)

        self.portal = 0
        self.levelMax = 0

        # wall image
        self.wallImage = pygame.image.load("images/WallTexture.png")

    # loads a level from a set of rectangles
    def loadLevelList(self, rectList):
        self.levelRectangles = rectList.copy()

        for wall in rectList:
            newSprite = pygame.sprite.Sprite(self.wallSpriteGroup)
            newSprite.rect = wall
            self.refitSprite(newSprite)
            self.wallSprites.append(newSprite)
    # loads a level based on the preset level list
    def loadLevel(self, levelNum):
        rects = self.lvls.getLevel(levelNum)
        self.loadLevelList(rects)
        portalLocation = self.lvls.getPortalLocation(levelNum)
        self.levelMax = self.lvls.getLevelMax(levelNum)
        print(self.levelMax)
        self.portal = Portal(self.surface,self.wallThickness,portalLocation,self.player,self.levelMax)

    # adds a rectangle as a wall to the current level
    def addWall(self, wallRect):
        if isinstance(wallRect,pygame.Rect):
            self.levelRectangles.append(wallRect)
        else :
            print(wallRect," is not a pygame.Rect! Consider defining it with createWall(left,top,width,height)")

    # creates a new wall for the current level by integer parameters, defined by the top-left corner
    def createWall(self, left, top, width, height):
        newWall = pygame.Rect(left, top, width, height)
        self.addWall(newWall)
    # creates a new wall for the current level by integer parameters, defined by the centrepoint
    def createCentredWall(self, x, y, width, height):
        left = x - (width/2)
        top = y - (height/2)
        newWall = pygame.Rect(left, top, width, height)
        self.addWall(newWall)

    # draw the level (its walls)
    def drawLevel(self):
        for i in range(len(self.levelRectangles)): #for all boxes in the level
            #pygame.draw.rect(self.surface, self.wallColour, self.levelRectangles[i]) #draw the box
            self.surface.blit(self.wallSprites[i].image,self.levelRectangles[i])

        # self.portal.update()
            
    

  
        
        
    def updateLevel(self):
        # updatePx = number of pixels each box will be changed by each frame
        updatePx = self.wallUpdateRate / 1
        
        # if updatePx is too small, then don't update it this frame.
        # Instead, increment a counter that triggers adding one pixel at a future frame
        # This makes the average pixel increase/frame be the set wallUpdateRate
        if ((updatePx < 1) & (updatePx > -1)):
            self.wallUpdateTick += updatePx
            updatePx = 0

        # If the counter gets high enough, trigger adding one pixel to the walls in this frame, and then reset the counter
        if (self.wallUpdateTick > 2):
            updatePx = 1
            self.wallUpdateTick = 0
        elif (self.wallUpdateTick < -2):
            updatePx = -1
            self.wallUpdateTick = 0

        # for all boxes in the level
        for box in self.levelRectangles:
            resizeWall(box, updatePx)

        for sprite in self.wallSprites:
            self.refitSprite(sprite)

        # self.portal.updatePortal()

    # check collisions with walls and character.
    # if there is a collision with a wall, move character away from wall
    def detectWallCollisions(self):
        # dict = pygame.sprite.groupcollide(self.wallSpriteGroup,spriteGroup,False,False)
        collision = pygame.sprite.spritecollideany(self.player, self.wallSpriteGroup, pygame.sprite.collide_mask)
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
            self.player.go_to_old()

    # later feature to add move the door, maybe other objects if it collides with any of the rectangles, if it does

    def refitSprite(self, sprite):
        rect = sprite.rect
        sprite.image = pygame.transform.scale(self.wallImage, (rect.width, rect.height))

#uniformly changes the size of a wall (a rectangle) such that it maintains its centrepoint
def resizeWall(wall, sizeChange):
    wall.left -= sizeChange
    wall.width += sizeChange * 2
    wall.top -= sizeChange
    wall.height += sizeChange * 2