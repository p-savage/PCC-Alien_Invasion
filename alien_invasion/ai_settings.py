class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #Ship speed setting
        self.ship_speed = 10.5
        #Initialize settings for the bullets
        self.bullet_speed = 15.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4
        #set the lateral speed of the alien fleet
        self.fleet_speed = 1.0
        #how far the fleet drops down
        self.fleet_drop_speed = 10
        #fleet direction; 1 = right,  -1 = left
        self.fleet_direction = 1