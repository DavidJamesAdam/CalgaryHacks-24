# Character class. Movement, drawing, and collision detection.
import pygame
import math



class Player(pygame.sprite.Sprite): 
 

    def __init__(self, screen):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.original_image = pygame.image.load("images/lil_player.png")
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width() / 2, screen.get_height() / 2)
        wep_images = ["images/weapon1.png", "images/weapon2.png"]
        
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