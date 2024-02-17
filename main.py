# Example file showing a circle moving on screen
import pygame
from player import Player
from levelManager import LevelManager



# pygame setup
pygame.init()
bg = pygame.image.load("images\\background.jpg")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# initializing objects
player = Player(screen, dt)
surface = pygame.display.get_surface()
wallColour = pygame.Color(0,0,0)
wallStartThickness = 50
levManager = LevelManager(surface, wallColour, wallStartThickness)
levManager.loadLevel(0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(bg, (0, 0))
    levManager.drawLevel()

    key = pygame.key.get_pressed()
    # Create collisiong checking for the player here
    player.move(key, dt)
    player.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

