# Character class. Movement, drawing, and collision detection.
import pygame



class Player: 
 

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images\lil_player.png")
        self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)



    def update_pos(self, coord_x, coord_y):
        self.player_pos = pygame.Vector2(coord_x, coord_y)
   

    def draw(self):
        self.screen.blit(self.image , self.player_pos)
                         
    

    

    def move(self, keys, dt):
        if keys[pygame.K_w]:
            self.player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            self.player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            self.player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            self.player_pos.x += 300 * dt