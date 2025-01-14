class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #maxmimum number of ship collisions allowed
        self.ship_limit = 3
        #Initialize settings for the bullets
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4
        #how far the fleet drops down (10)
        self.fleet_drop_speed = 10
        #how quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game progress"""
        #Ship speed setting
        self.ship_speed = 3.5
        #bullet speed setting      
        self.bullet_speed = 5.5
        #set the lateral speed of the alien fleet (1)
        self.fleet_speed = 1.0
        #fleet direction; 1 = right,  -1 = left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase dynamic speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.fleet_speed *= self.speedup_scale       
       
       
        
        
        
        
       
       