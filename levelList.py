import pygame
# The list of levels available to load
screen = pygame.get_window_size()
wallStartSize = 50

# level 1
topWall = pygame.Rect(0,0,screen[0],wallStartSize)
leftWall = pygame.Rect(0,0,wallStartSize,screen[1])
bottomWall = pygame.Rect(0,screen[1],screen[0],wallStartSize)
rightWall = pygame.Rect(screen[0],0,wallStartSize,screen[1])
level1 = [topWall, rightWall, leftWall, bottomWall]

#all levels
levels = [level1]