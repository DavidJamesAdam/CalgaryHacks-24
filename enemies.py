# enemies class. 
# This class is used to create the enemies in the game. Drawing, 
# drawing, and updating the enemies is done in this class.

# Enemy ai goes towards the player and "attacks" the player
# by colliding with the player.

from pygame.locals import *
import pygame
import random

class Enemy:
    def __init__(self, start_x, start_y, radius = 10, max_health = 100, speed = 2, colour = (255, 0, 0)):
        self.pos = [start_x, start_y]
        self.speed = speed
        self.radius = radius
        self.max_health = max_health
        self.current_health = max_health
        self.colour = colour


    def move_towards(self, target_pos):
        # Calculate direction vector towards player
        direction = [target_pos[0] - self.pos[0], target_pos[1] - self.pos[1]]
        
        # Normalize direction
        distance = (direction[0]**2 + direction[1]**2)**0.5
        if distance > 0:
            direction = [direction[0] / distance, direction[1] / distance]

        # Move enemy
        self.pos[0] += direction[0] * self.speed
        self.pos[1] += direction[1] * self.speed

    def draw_health_bar(self, screen):
        # Health bar settings
        bar_width = 40
        bar_height = 5
        fill = (self.current_health / self.max_health) * bar_width

        # Health bar background (optional, could be skipped for a simpler version)
        background_rect = pygame.Rect(self.pos[0] - bar_width / 2, self.pos[1] - self.radius - bar_height - 5, bar_width, bar_height)
        pygame.draw.rect(screen, (255, 255, 255), background_rect)

        # Health bar fill
        health_rect = pygame.Rect(self.pos[0] - bar_width / 2, self.pos[1] - self.radius - bar_height - 5, fill, bar_height)
        pygame.draw.rect(screen, (255, 0, 0), health_rect)

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.pos, self.radius)
        self.draw_health_bar(screen)

class FastEnemy(Enemy):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y, radius=8, max_health=50, speed=4, colour=(0, 255, 0))


class StrongEnemy(Enemy):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y, radius=15, max_health=200, speed=1, colour=(0, 0, 255))

class RegularEnemy(Enemy):
     def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y, radius=15, max_health=100, speed=2, colour=(255, 0, 0))


def spawn_enemy_at_edge(screen_width, screen_height, enemy_radius):
    edge = random.choice(['top', 'bottom', 'left', 'right'])
    
    if edge in ['top', 'bottom']:
        x = random.randint(0, screen_width)
        y = 0 if edge == 'top' else screen_height
    else:  # 'left' or 'right'
        x = 0 if edge == 'left' else screen_width
        y = random.randint(0, screen_height)
    
    # Adjust position if spawning on the right or bottom edge to ensure the enemy is fully visible
    if edge == 'right':
        x -= enemy_radius * 2
    if edge == 'bottom':
        y -= enemy_radius * 2
    
    enemy_type = random.choice([FastEnemy, StrongEnemy, RegularEnemy])
    return enemy_type(x, y)