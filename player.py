# Character class. Movement, drawing, and collision detection.
import pygame
import math


class Player(pygame.sprite.Sprite): 
 

    def __init__(self, screen, max_health):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.original_image = pygame.image.load("images/lil_player.png")
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width() / 2, screen.get_height() / 2)
        wep_images = ["images/weapon1.png", "images/weapon2.png"]
        self.weapon = 0
        self.max_health = max_health
        self.curr_health = max_health
        self.radius = self.rect.width / 2
        self.score = 0
        
    # def damage(self, amount):
    #     self.curr_health -= amount
    #     if self.curr_health < 0:
    #         self.curr_health = 0
    #     self.health_bar.update()
    
    def draw_health_bar(self):
        bar_width = 40
        bar_height = 5
        fill = (self.curr_health / self.max_health) * bar_width

        background_rect = pygame.Rect(self.rect.centerx - bar_width / 2, self.rect.y - self.radius - bar_height, bar_width, bar_height)
        pygame.draw.rect(self.screen, (255, 255, 255), background_rect)

        health_rect = pygame.Rect(self.rect.centerx - bar_width / 2, self.rect.y - self.radius - bar_height, fill, bar_height)
        pygame.draw.rect(self.screen, (255, 0, 0), health_rect)


    def change_weapon(self, index):
        ''' 
        Temp class to change between two weapons.
        Currently we only have one weapon so this is not used.
        
        '''
        if index == 1:
            self.image = pygame.image.load("images/weapon1.png")
        elif index == -1:
            self.image = pygame.image.load("images/weapon2.png")
        
    def update_image(self, image):
        '''
        Update the image of the player.
        '''
        self.image = pygame.image.load(image)

    def damage(self, amount):
        '''
        Damage the player by a certain amount.
        '''
        self.curr_health -= amount
        if self.curr_health < 0:
            self.curr_health = 0
        self.draw_health_bar()


    def return_rect(self):
        '''
        Return the center rectangle of the player.
        '''
        return self.rect.center

    def move(self, keys, dt, angle):
        # Rotate the sprite to the angle
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.rect.center)

        if keys[pygame.K_w]:
            self.rect.y -= 300 * dt
        if keys[pygame.K_s]:
            self.rect.y += 300 * dt
        if keys[pygame.K_a]:
            self.rect.x -= 300 * dt
        if keys[pygame.K_d]:
            self.rect.x += 300 * dt


    