import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        #Generate a display screen
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect
        self.image = pygame.image.load('ai_images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom middle of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        #Movement flag; start the game with the flag = False
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Re-centers ship after an alien collision"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    
    def update(self):
        """Updates the ships position based on the movement flags"""
        #Update the ship's x value, not the rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #Update the rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)