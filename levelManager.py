import pygame
from levelList import LevelList
import random
from enemies import Enemy, FastEnemy, StrongEnemy, TeleportingEnemy, RegularEnemy
# Level design class.
# Level drawing, updating, and collision detection done in this class.

class LevelManager:
    def __init__(self,surface, wallShade, wallThicc, wallUpdateRate):
        self.surface = surface
        self.screenSize = surface.get_size()
        self.wallColour = wallShade
        self.wallThickness = wallThicc
        self.wallUpdateRate = wallUpdateRate
        self.wallUpdateTick = 0
        
        # level is made of a series of boxes, each of which can increase/decrease in size, and also a background colour
        self.levelRectangles = []

        #levelList
        self.lvls = LevelList(self.screenSize,self.wallThickness)

    # loads a level from a set of rectangles
    def loadLevel(self, rectList):
        self.levelRectangles = rectList
    # loads a level based on the preset level list
    def loadLevel(self, levelNum):
        self.levelRectangles = self.lvls.getLevel(levelNum)

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
        for box in self.levelRectangles: #for all boxes in the level
            pygame.draw.rect(self.surface, self.wallColour, box) #draw the box

    # check collisions with level
    def detectCollisions(self):
        return []
    # takes in object (e.g. enemy, player) location & size as argument
    # spits out if collision happens as result
    # check the object vs all the rectangles, quick return if true on any of them
    # if (obj Right => box Left || obj Leftt <= box Right) && (obj Top => box Bottom || obj Bottom <= box Top)
    # collision, return true
    # else next box

    def updateLevel(self):
        # updatePx = number of pixels each box will be changed by each frame
        updatePx = self.wallUpdateRate / 2
        
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

    # later feature to add move the door, maybe other objects if it collides with any of the rectangles, if it does

#uniformly changes the size of a wall (a rectangle) such that it maintains its centrepoint
def resizeWall(wall, sizeChange):
    wall.left -= sizeChange
    wall.width += sizeChange * 2
    wall.top -= sizeChange
    wall.height += sizeChange * 2


