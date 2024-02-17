# Example file showing a circle moving on screen
import pygame
from player import Player



# pygame setup
pygame.init()
bg = pygame.image.load("images/background.jpg")
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0

# initializing objects
all_sprites = pygame.sprite.Group() # create a group for all sprites

player = Player(screen)
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

