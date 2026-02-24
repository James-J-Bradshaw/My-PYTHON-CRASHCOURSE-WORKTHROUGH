import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """This is a class to manage the bullets fired from the ship."""

    def __init__(self, ai_game):
        """This is to create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.bullet_colour

        #  Creates a bullet object rect at (0,0), then sets it to the correct position
        self.rect = pygame.rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #This stores the bullet's position as a float
        self.y = float(self.rect.y)