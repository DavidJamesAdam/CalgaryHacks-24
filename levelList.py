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
        portal1 = (screenSize[0]/2,screenSize[1]/2)
        level1max = 20
        level1 = [topWall, rightWall, leftWall, bottomWall]

        # level 2
        barheight = 3*wallStartSize
        rightbar = pygame.Rect((screenSize[0]/4)-(wallStartSize/2),(screenSize[1]/2)-(barheight/2),wallStartSize/2,barheight)
        leftbar = pygame.Rect((3*screenSize[0]/4)-(wallStartSize/2),(screenSize[1]/2)-(barheight/2),wallStartSize/2,barheight)
        level2 = [topWall,leftWall,bottomWall,rightWall,rightbar,leftbar]
        portal2 = (screenSize[0]/2,screenSize[1]/2)
        level2max = 50

        # all levels
        self.levels = [level1,level2]
        self.levelPortalLocations = [portal1, portal2]
        self.levelMax = [level1max,level2max]

    def numLevels(self) :
        return len(self.levels)
        
    def getLevel(self, levelNumber):
        lvlToLoad = levelNumber
        if levelNumber >= self.numLevels() :
            lvlToLoad = 0
        
        print( "Starting Level ",str(lvlToLoad))
        return self.levels[lvlToLoad]
    
    def getPortalLocation(self, levelNumber):
        lvlToLoad = levelNumber
        if levelNumber >= self.numLevels() :
            lvlToLoad = 0
        
        return self.levelPortalLocations[lvlToLoad]
    
    def getLevelMax(self, levelNumber):
        lvlToLoad = levelNumber
        if levelNumber >= self.numLevels() :
            lvlToLoad = 0
        
        return self.levelMax[lvlToLoad]