import sys
import pygame
from time import sleep

from ai_settings import Settings
from ai_game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        #initialize pygame
        pygame.init()
        #Set the clock
        self.clock = pygame.time.Clock()
        #call the game settings
        self.settings = Settings()
        #build the game display surface
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height
        ))
        pygame.display.set_caption("Alien Invasion")
        #create an instance of our in-game statistics class
        self.stats = GameStats(self)
        #Call instances of object classes
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        #create the alien fleet
        self._create_fleet()
        #Set the background color
        self.screen.fill(self.settings.bg_color)
        #set the game-active flag
        self.game_active = True

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #check for events, update accordingly, display result, 60fps
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_f:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False    

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """"Update the position of bullets and delete old bullets"""
        #update bullet positions
        self.bullets.update()
        #delete old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Detects alien hits. Removes the bullet and alien"""
        collisions = pygame.sprite.groupcollide(self.aliens, self.bullets,
        True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Creates the fleet"""
        alien = Alien(self)
        #get the width  and height measurement
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        #builds the number of rows in the fleet
        while current_y < (self.settings.screen_height - 3 * alien_height):
            #builds one row of aliens
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            #first row is finished so we reset the x and increment the y
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row"""
        new_alien = Alien(self)
        #place the image and rect at the current_x and current_y
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        #add it to the group list
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """updates the positions of all aliens in the group"""
        #check for aliens at the screen edge
        self._check_fleet_edges()
        #update every alien's position
        self.aliens.update()
        #check for a ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        #check if aliens have reached the bottom of the screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Handles ship hit events"""
        #decrease the remaining ships
        if self.settings.ship_limit > 0:
            self.settings.ship_limit -= 1
            #clear the aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            #create a new alien fleet
            self._create_fleet()
            #re-center the ship
            self.ship.center_ship()
            #half-second pause
            sleep(0.5)
        else:
            self.game_active = False

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the fleet down and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #Treat it the same as a ship collision
                self._ship_hit()
                break

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        #background
        self.screen.fill(self.settings.bg_color)
        #bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 
        #ship
        self.ship.blitme()
        #draw the alien fleet
        self.aliens.draw(self.screen)
        #show it all
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()