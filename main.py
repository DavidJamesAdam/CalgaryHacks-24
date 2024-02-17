# Example file showing a circle moving on screen
import pygame
from player import Player
from levelManager import LevelManager



# pygame setup
pygame.init()
bg = pygame.image.load("images/background.jpg")
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0


# sprite setup
all_sprites = pygame.sprite.Group() # create a group for all sprites
player_group = pygame.sprite.Group() # create a group for the player
enemies_group = pygame.sprite.Group() # create a group for the enemies
#bullets_group = pygame.sprite.Group() # create a group for the bullets
traps_group = pygame.sprite.Group() # create a group for the traps
obstacles_group = pygame.sprite.Group() # create a group for the obstacles


# create the player
player = Player(screen)
player_group.add(player) # add the player to the group

# create the level manager
surface = pygame.display.get_surface()
wallColour = pygame.Color(0,0,0)
wallStartThickness = 50
levManager = LevelManager(surface, wallColour, wallStartThickness)
levManager.loadLevel(0)

# add the player to the all_sprites group
all_sprites.add(player) # add the player to the group


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
    screen.fill("purple")

    # sprite management
    all_sprites.update()
    all_sprites.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

