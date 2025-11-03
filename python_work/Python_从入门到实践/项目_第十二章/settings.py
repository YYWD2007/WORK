class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.color = (230,230,230)  
        self.ship_speed = 4
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3
        self.alien_speed = 2.5
        self.fleet_drop_speed = 8
        self.speedup_scale = 1.5
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        self.fleet_direction = 1
        self.ship_limit = 3

    def initialize_dynamic_settings(self):
        self.ship_speed=3
        self.bullet_speed = 3
        self.alien_speed = 2.5

        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

        
    


