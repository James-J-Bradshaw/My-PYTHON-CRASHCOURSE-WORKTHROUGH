import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage the game assets and behaviours"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        
        """Current settings for Fullscreen mode"""
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        """Old settings for windowed mode"""
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # pygame.display.set_caption("Alien Invasion")

        self.clock = pygame.time.Clock()
        self.ship = Ship(self)

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
               self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
        
    def _check_keydown_events(self, event):
            """responds to keyrpess"""
            if event.key == pygame.K_d:
                self.ship.moving_right = True
            elif event.key == pygame.K_a:
                self.ship.moving_left = True
            elif event.key == pygame.K_w:
                self.ship.moving_up = True
            elif event.key == pygame.K_s:
                self.ship.moving_down = True
            elif event.key == pygame.K_BACKSPACE:
                sys.exit()

    def _check_keyup_events(self, event):
            if event.key == pygame.K_d:
                self.ship.moving_right = False
            elif event.key == pygame.K_a:
                self.ship.moving_left = False
            elif event.key == pygame.K_w:
                self.ship.moving_up = False
            elif event.key == pygame.K_s:
                self.ship.moving_down = False


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        # This redraws the screen during each pass through the loop
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
            
        # Make the most recently drawn screen visable.
        pygame.display.flip()


    def run_game(self):
        """This will start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            # This redraws the screen during each pass through the loop
            self.screen.fill(self.settings.bg_colour)
            self.ship.blitme()
            
            # Make the most recently drawn screen visable.
            pygame.display.flip()
            
            # Frame rate of game
            self.clock.tick(60)

if __name__ == "__main__":
    # Make game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()