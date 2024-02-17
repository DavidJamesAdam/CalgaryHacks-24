# Character class. Movement, drawing, and collision detection.
import pygame
import math



class Player(pygame.sprite.Sprite): 
 

    def __init__(self, screen):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.original_image = pygame.image.load("images/player.png")
        self.curr_image = pygame.image.load("images/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width() / 2, screen.get_height() / 2)
        
        
        # self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)



    # def update_pos(self, coord_x, coord_y):
    #     self.player_pos = pygame.Vector2(coord_x, coord_y)
   

    # def draw(self):
    #     self.screen.blit(self.image , self.player_pos)
                        
    

    # def move(self, keys, dt):
    #     if keys[pygame.K_w]:
    #         self.player_pos.y -= 300 * dt
    #     if keys[pygame.K_s]:
    #         self.player_pos.y += 300 * dt
    #     if keys[pygame.K_a]:
    #         self.player_pos.x -= 300 * dt
    #     if keys[pygame.K_d]:
    #         self.player_pos.x += 300 * dt
        
    def move(self, keys, dt):
        # Calculate the angle between the sprite and the mouse
        dx, dy = pygame.mouse.get_pos() - pygame.Vector2(self.rect.center)
        angle = math.degrees(math.atan2(-dy, dx))

        # Rotate the sprite to the angle
        self.curr_image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.rect.center)

        if keys[pygame.K_w]:
            self.rect.y -= 300 * dt
        if keys[pygame.K_s]:
            self.rect.y += 300 * dt
        if keys[pygame.K_a]:
            self.rect.x -= 300 * dt
        if keys[pygame.K_d]:
            self.rect.x += 300 * dt