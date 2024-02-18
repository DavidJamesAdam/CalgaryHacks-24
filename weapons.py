from player import Player
from bullets import Bullet
import pygame

class Weapon(pygame.sprite.Group):
    def __init__(self, screen, bullet_group):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("images/lil_player_armed.png")
        self.rect = self.image.get_rect()
        self.bullet_group = bullet_group
        self.bullets = []


    def change_weapon(self, weapon):
        self.image = pygame.image.load(weapon)
        
    def update(self):
        self.bullet_group.update()

    def fire(self, angle, p_x, p_y, screen):
        bullet = Bullet(angle, p_x, p_y, screen)
        self.bullets.append(bullet)
        self.bullet_group.add(bullet)
        # print("I fired")
