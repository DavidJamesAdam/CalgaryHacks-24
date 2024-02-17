# Example file showing a circle moving on screen
import pygame
from enemies import Enemy, spawn_enemy_at_edge

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

enemies = Enemy(start_x=0, start_y=0)

enemies_list = []  # List to keep track of all enemies
spawn_timer = 0  # Timer to manage enemy spawns
spawn_interval = 120

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            click_pos = pygame.mouse.get_pos()

            # Check each enemy to see if it was clicked
            for enemy in enemies_list:
                distance = ((enemy.pos[0] - click_pos[0]) ** 2 + (enemy.pos[1] - click_pos[1]) ** 2) ** 0.5
                if distance < enemy.radius:  # The click is within the enemy's circle
                    enemy.current_health -= 10  # Decrease health by 10

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    spawn_timer += 1
    if spawn_timer >= spawn_interval:
        spawn_timer = 0
        new_enemy = spawn_enemy_at_edge(screen.get_width(), screen.get_height(), enemies.radius)
        enemies_list.append(new_enemy)
    for enemy in enemies_list:
        enemy.move_towards(player_pos)
        enemy.draw  # Draw enemy as a circle
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

pygame.quit()

