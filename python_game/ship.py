import pygame
class Ship:
    """This class is to manage the ship."""

    def __init__(self, ai_game):
        """Initialise the ship and set it's starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Ship settings
        self.ship_speed = 3

        # Load the ship image and get it's rect.
        self.image = pygame.image.load("spaceship.bmp")
        self.rect = self.image.get_rect()

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)
    
    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.ship_speed
    
    def blitme(self):
        """draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)