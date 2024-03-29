import math
import pygame

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, angle, p_x, p_y, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("images/bullet_dark.png")  # Example bullet size
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, int(angle))
        self.rect = self.image.get_rect(center=self.rect.center)

        
        self.rect.x = p_x
        self.rect.y = p_y
        self.angle = angle
        
        #Update location of bullet based on angle and dy and dx
        self.speed = 8
        self.velocity_x = self.speed * math.cos(math.radians(self.angle))
        self.velocity_y = -(self.speed * math.sin(math.radians(self.angle)))
        self.damage = 25
        
        self.update()


    def update(self):
        
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        #print("I did update")
        width, height = 1280, 720
        if(self.rect.x < 0 or self.rect.x > 1280 or self.rect.y < 0 or self.rect.y > 720):
            self.kill()

    def damage(self):
        return self.damage
    