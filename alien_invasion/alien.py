import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        #link to the main game screen and settings
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #load the image of the alien ship and get its rect
        self.image = pygame.image.load('ai_images/alien.bmp')
        self.rect = self.image.get_rect()
        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #store the aliens exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if an alien hits the screen edge"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien fleet left or right"""
        self.x += self.settings.fleet_speed * self.settings.fleet_direction
        self.rect.x = self.x