import pygame
from pygame.sprite import Sprite

class Cross(Sprite):
    """Class responsible for managing the crosses."""
    def __init__(self, ai_game):
        """Initialization of the class."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.color_cross

        self.start_x = 0
        self.start_y = 0
    def draw_cross(self, x_pos, y_pos):
        """Drawing the cross."""
        cross_size = 80

        pygame.draw.line(self.screen, self.color, (x_pos, y_pos), (x_pos + cross_size, y_pos + cross_size), self.settings.cross_width)
        pygame.draw.line(self.screen, self.color, (x_pos + cross_size, y_pos), (x_pos, y_pos + cross_size), self.settings.cross_width)


