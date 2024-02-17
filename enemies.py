# enemies class. 
# This class is used to create the enemies in the game. Drawing, 
# drawing, and updating the enemies is done in this class.

# Enemy ai goes towards the player and "attacks" the player
# by colliding with the player.

from pygame.locals import *

class Enemy:
    def __init__(self, start_x, start_y, radius = 10):
        self.pos = [start_x, start_y]
        self.speed = 2
        self.radius = radius


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