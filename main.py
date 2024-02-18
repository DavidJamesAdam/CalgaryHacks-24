# Example file showing a circle moving on screen
import pygame
import math
import pygame_menu

from enemies import Enemy, spawn_enemy_at_edge
from player import Player
from levelManager import LevelManager
from weapons import Weapon
from portal import Portal

MAX_HEALTH = 100
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Global data
bg = None
screen = None
clock = None
all_sprites = None
player_group = None
enemies_group = None
bullets_group = None
traps_group = None
obstacles_group = None
wall_group = None
player = None
weapon = None
font = None
surface = None
wallColour = None
wallStartThickness = None
wallUpdateRate = None
lvlManager = None
collidedWithWallList = None
enemies = None
enemies_list = None
currentLevel = None
currentLevel = None
gun_sound = None


def reset_game():
    global bg, screen, clock, all_sprites, player_group, enemies_group, bullets_group, traps_group, obstacles_group, wall_group
    global player, weapon, font, surface, wallColour, wallStartThickness, wallUpdateRate, lvlManager, collidedWithWallList, enemies, enemies_list, currentLevel, gun_sound

    # pygame setup
    pygame.init()
    bg = pygame.image.load("images/background.jpg")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # running = True
    # dt = 0

    # sprite setup
    all_sprites = pygame.sprite.Group() # create a group for all sprites (except walls)
    player_group = pygame.sprite.Group() # create a group for the player
    enemies_group = pygame.sprite.Group() # create a group for the enemies
    bullets_group = pygame.sprite.Group() # create a group for the bullets
    traps_group = pygame.sprite.Group() # create a group for the traps
    obstacles_group = pygame.sprite.Group() # create a group for the obstacles
    wall_group = pygame.sprite.Group() # create a group for walls


    # create the player
    player = Player(screen, MAX_HEALTH)

    # weapons = weapon(screen, bullets_group)
    player_group.add(player) # add the player to the group
    weapon = Weapon(screen, bullets_group)

    # Managing the scoreboard
    font = pygame.font.Font(None, 36)

    # create the level manager
    surface = pygame.display.get_surface()
    wallColour = pygame.Color(0,0,0)
    wallStartThickness = 50
    wallUpdateRate = 0.1

    currentLevel = 0
    lvlManager = LevelManager(surface, wallColour, wallStartThickness, wallUpdateRate, wall_group, player)
    lvlManager.loadLevel(currentLevel)

    collidedWithWallList = []

    # add the player to the all_sprites group
    all_sprites.add(player) # add the player to the group
    enemies = Enemy(start_x=0, start_y=0)
    enemies_list = []  # List to keep track of all enemies

    gun_sound = pygame.mixer.Sound("audio/gunshot.mp3")
    gun_sound.set_volume(0.25)


def main():
    running = True
    dt = 0
    spawn_timer = 0  # Timer to manage enemy spawns
    spawn_interval = 120
    killcount = 50
    currentLevel = 0

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        # Calculate the angle between the sprite and the mouse
        dx, dy = pygame.mouse.get_pos() - pygame.Vector2(player.return_rect())
        angle = math.degrees(math.atan2(-dy, dx))

        for event in pygame.event.get():

            if (event.type == pygame.QUIT) or (event.type == pygame.K_ESCAPE):
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                click_pos = pygame.mouse.get_pos()
                p_x, p_y = player.return_rect()
                # print(angle)
                weapon.fire(angle, p_x, p_y, screen)
                gun_sound.play()


        # fill the screen with a color to wipe away anything from last frame
        screen.blit(bg, (0, 0))
        lvlManager.drawLevel()
        key = pygame.key.get_pressed()
        player.move(key, dt, angle)
        bullet_collision = pygame.sprite.groupcollide(bullets_group, enemies_group, False, False, pygame.sprite.collide_mask)

        for bullet, enemy in bullet_collision.items():
            enemy[0].current_health -= bullet.damage
            bullet.kill()
            enemy[0].draw_health_bar(screen)
            if enemy[0].current_health <= 0:
                enemies_list.remove(enemy[0])
                enemies_group.remove(enemy[0])
                enemy[0].kill()
                player.score += 1
                killcount -= 1
                
        if killcount == 0:
            reset_game()
            return
                 
        # enemy collision detection
        enemy_collision = pygame.sprite.spritecollide(player, enemies_group, False, pygame.sprite.collide_mask)
        for enemy in enemy_collision:
            player.curr_health -= enemy.damage
            
            
            if player.curr_health <= 0:
                running = False
                print("You died")
                reset_game()
                return
                
        # Wall collision
        lvlManager.detectWallCollisions()

        # sprite management
        bullets_group.update()
        bullets_group.draw(screen)
        player.draw_health_bar()
        all_sprites.update()
        all_sprites.draw(screen)

        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            spawn_timer = 0
            # new_enemy = spawn_enemy_at_edge(screen.get_width(), screen.get_height(), enemies.radius)
            new_enemy = spawn_enemy_at_edge(screen.get_width(), screen.get_height(), enemies.radius)
            enemies_group.add(new_enemy)
            enemies_list.append(new_enemy)
        for enemy in enemies_list:
            if hasattr(enemy, 'update_teleport'):
                enemy.update_teleport(player.rect.center, screen.get_width(), screen.get_height())
            else:
                enemy.move_towards(player.rect.center)
            enemy.draw_health_bar(screen)  # Draw health bar above each enemy
        
        enemies_group.update(player.rect.center, screen.get_width(), screen.get_height())
        enemies_group.draw(screen)

        # draw the rest of the level overtop of the enemies & sprites
        lvlManager.drawLevel()
        
        score_surface = font.render(f"Score: {player.score} | Kills left: {killcount}", True, (255, 255, 255))
        screen.blit(score_surface, (10, 10)) 

        if running:
            pygame.display.flip()
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
        lvlManager.updateLevel()   
        
    pygame.quit()

def start_the_game():
    pygame.mixer.music.load("audio/red_star.mp3")
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(0)
    main()
    pygame.mixer.music.unload()
    pygame.mixer.music.stop()
    return

def display_menu():
    menu = pygame_menu.Menu('CLAUSTROPHOBIA: Escape the Martian Ship before time runs out', 1280, 720, theme=pygame_menu.themes.THEME_GREEN)
    menu.add.label('Lil\' Wayne the Martian has been kidnapped by evil aliens.', font_color='black')
    menu.add.label('Dropped off on an alien landscape he must survive the onslaught', font_color='black')
    menu.add.label('of hostile aliens and the encroaching sentient landscape.', font_color='black')
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)

reset_game()
display_menu()
