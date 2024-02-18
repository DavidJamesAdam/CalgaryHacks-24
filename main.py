# Example file showing a circle moving on screen
import pygame
import math
import pygame_menu

from enemies import Enemy, spawn_enemy_at_edge
from player import Player
from levelManager import LevelManager
from weapons import Weapon

MAX_HEALTH = 100
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


# pygame setup
pygame.init()
bg = pygame.image.load("images/background.jpg")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# running = True
# dt = 0

# sprite setup
all_sprites = pygame.sprite.Group() # create a group for all sprites
player_group = pygame.sprite.Group() # create a group for the player
enemies_group = pygame.sprite.Group() # create a group for the enemies
bullets_group = pygame.sprite.Group() # create a group for the bullets
traps_group = pygame.sprite.Group() # create a group for the traps
obstacles_group = pygame.sprite.Group() # create a group for the obstacles


# create the player
player = Player(screen, MAX_HEALTH)
# weapons = weapon(screen, bullets_group)
player_group.add(player) # add the player to the group
weapon = Weapon(screen, bullets_group)

# create the level manager
surface = pygame.display.get_surface()
wallColour = pygame.Color(0,0,0)
wallStartThickness = 50
wallUpdateRate = 0.1
lvlManager = LevelManager(surface, wallColour, wallStartThickness, wallUpdateRate)
lvlManager.loadLevel(0)

collidedWithWallList = []

# add the player to the all_sprites group
all_sprites.add(player) # add the player to the group
enemies = Enemy(start_x=0, start_y=0)
enemies_list = []  # List to keep track of all enemies
# spawn_timer = 0  # Timer to manage enemy spawns
# spawn_interval = 240


def main():
    running = True
    dt = 0
    spawn_timer = 0  # Timer to manage enemy spawns
    spawn_interval = 240
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        # Calculate the angle between the sprite and the mouse
        dx, dy = pygame.mouse.get_pos() - pygame.Vector2(player.return_rect())
        angle = math.degrees(math.atan2(-dy, dx))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                click_pos = pygame.mouse.get_pos()
                p_x, p_y = player.return_rect()
                # print(angle)
                weapon.fire(angle, p_x, p_y, screen)

                # Check each enemy to see if it was clicked
                for enemy in enemies_list:
                    distance = ((enemy.pos[0] - click_pos[0]) ** 2 + (enemy.pos[1] - click_pos[1]) ** 2) ** 0.5
                    if distance < enemy.radius:  # The click is within the enemy's circle
                        enemy.current_health -= 10  # Decrease health by 10
                # weapon.fire()






            # elif event.type == pygame.K_q:
            #     player.change_weapon(-1)
            #     weapons.change_weapon(-1)
            # elif event.type == pygame.K_e:
            #     player.change_weapon(1)
            #     weapons.change_weapon(1)

        # fill the screen with a color to wipe away anything from last frame
        # screen.fill("purple")
        # screen.blit(bg, (0, 0))
        lvlManager.drawLevel()

        key = pygame.key.get_pressed()
    
        bullet_collision = pygame.sprite.groupcollide(bullets_group, enemies_group, False, False)
        for bullet, enemy in bullet_collision.items():
            enemy[0].current_health -= bullet.damage()
            bullet.kill()
            enemy[0].draw_health_bar(screen)
            if enemy[0].current_health <= 0:

                enemy[0].kill()
    
    
        # Create collisiong checking for the player here
        collidedWithWallList = lvlManager.detectCollisions()
        player.move(key, dt, angle)
    

        # sprite management
        bullets_group.update()
        bullets_group.draw(screen)
        player.draw_health_bar()
        all_sprites.update()
        all_sprites.draw(screen)
        bullets_group.update()

        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            spawn_timer = 0
            new_enemy = spawn_enemy_at_edge(screen.get_width(), screen.get_height(), enemies.radius)
            # new_enemy = lvlManager.spawn_enemy_within_box()
            enemies_list.append(new_enemy)
        for enemy in enemies_list:
            if hasattr(enemy, 'update'):
                enemy.update(player.rect.center, screen.get_width(), screen.get_height())
            else:
                enemy.move_towards(player.rect.center)
            enemy.draw(screen) 
            enemy.draw_health_bar(screen)  # Draw health bar above each enemy
        for enemy in enemies_list[:]:  # Iterate over a slice copy of the list to avoid modification issues
            # Check for defeated enemies
            if enemy.current_health <= 0:
                enemies_list.remove(enemy)
                continue  # Skip the rest of the loop for this enemy

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = clock.tick(60) / 1000

            lvlManager.updateLevel()

    pygame.quit()

def start_the_game():
    main()
    return

menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)
