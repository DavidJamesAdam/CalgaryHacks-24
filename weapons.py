from player import Player
import pygame

class weapon(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("images/weapon1.png")
        self.rect = self.image.get_rect()

    def change_weapon(self, weapon):
        self.image = pygame.image.load(weapon)