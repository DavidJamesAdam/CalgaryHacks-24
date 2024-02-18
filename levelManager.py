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

    def loadLevel(self, levelNum):
        self.levelRectangles = self.lvls.getLevel(levelNum)

    def addWall(self, wallRect):
        if isinstance(wallRect,pygame.Rect):
            self.levelRectangles.append(wallRect)
        else :
            print(wallRect," is not a pygame.Rect! Consider defining it with createWall(left,top,width,height)")

    def createWall(self, left, top, width, height):
        newWall = pygame.Rect(left, top, width, height)
        self.levelRectangles.append(newWall)

    # draw level
    def drawLevel(self):
        for box in self.levelRectangles:
            pygame.draw.rect(self.surface, self.wallColour, box)

    # for all boxes in level
    # draw the box

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
        updatePx = self.wallUpdateRate / 2
        if (updatePx):
            self.wallUpdateTick += updatePx
            updatePx = 0

        if (self.wallUpdateTick > 2):
            updatePx += 1
            self.wallUpdateTick = 0

        for box in self.levelRectangles:
            box.left -= updatePx
            box.width += updatePx * 2
            box.top -= updatePx
            box.height += updatePx * 2

    # update level
    # takes in size change
    # for all boxes in level
    # change size of boxes by indicated factor (with at least one pixel of width)
    # later feature to add move the door if it collides with any of the rectangles, if it does
            
    # def get_playable_area(self):
    #     if self.levelRectangles:
    #         return self.levelRectangles[0]  # Assuming the first rectangle is the playable area
    #     else:
    #         return pygame.Rect(0, 0, *self.screenSize)  # Fallback to full screen size
        
    # def spawn_enemy_within_box(self, enemy_width, enemy_height):
    #     playable_area = self.get_playable_area()  # Ensure this method returns the current level box as a pygame.Rect
    #     x = random.randint(playable_area.left, playable_area.right - enemy_width)
    #     y = random.randint(playable_area.top, playable_area.bottom - enemy_height)

    #     enemy_type = random.choice([FastEnemy, StrongEnemy, RegularEnemy, TeleportingEnemy])
    #     return enemy_type(x, y)  # Adjust parameters as needed



