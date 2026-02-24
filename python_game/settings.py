
class Settings:
    """A class to store all settings all settings for Alien invasion"""

    def __init__(self):
        """Initialising the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (200, 200, 255)

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)