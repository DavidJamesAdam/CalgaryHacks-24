import pygame
import levelList
# Level design class.
# Level drawing, updating, and collision detection done in this class.

screen = pygame.get_window_size()

# level is made of a series of boxes, each of which can increase/decrease in size, and also a background colour
levelRectangles = []


# loads a level from a set of rectangles
def loadLevel(rectList):
    levelRectangles = rectList

def loadLevel(levelNum):
    if (len(levelList.levels) < levelNum) :
        levelRectangles = levelList.levels[levelNum]
    else :
        levelRectangles = levelList.levels[0]

# draw level
# for all boxes in level
# draw the box

# check collisions with level
# takes in object (e.g. enemy, player) location & size as argument
# spits out if collision happens as result
# check the object vs all the rectangles, quick return if true on any of them
# if (obj Right => box Left || obj Leftt <= box Right) && (obj Top => box Bottom || obj Bottom <= box Top)
# collision, return true
# else next box

# update level
# takes in size change
# for all boxes in level
# change size of boxes by indicated factor (with at least one pixel of width)
# later feature to add move the door if it collides with any of the rectangles, if it does


