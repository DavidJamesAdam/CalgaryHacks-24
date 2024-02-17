import pygame
# The list of levels available to load

class LevelList:
    def __init__(self,screenSize,wallStartSize):
        wallStartSize

        # level 1
        topWall = pygame.Rect(0,0,screenSize[0],wallStartSize)
        leftWall = pygame.Rect(0,0,wallStartSize,screenSize[1])
        bottomWall = pygame.Rect(0,screenSize[1]-wallStartSize,screenSize[0],wallStartSize)
        rightWall = pygame.Rect(screenSize[0]-wallStartSize,0,wallStartSize,screenSize[1])
        level1 = [topWall, rightWall, leftWall, bottomWall]

        # level 2


        # all levels
        self.levels = [level1]

    def numLevels(self) :
        return len(self.levels)
        
    def getLevel(self, levelNumber):
        if levelNumber >= self.numLevels() :
            print("%d is not a valid level! Returning level[0] from getLevel() instead.")
            return self.levels[0]
        else :
            return self.levels[levelNumber]