import pygame
from pygame.sprite import Sprite

class Circle(Sprite):
    """Class that draws the cricles"""
    def __init__(self, ai_game):
        """Initalization of the class."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.color_circle

        self.circle_center = 0

    def draw_circle(self, center):
        """drawing the circle."""
        self.rect = pygame.draw.circle(self.screen, self.color, center, self.settings.circle_radius, self.settings.circle_width)
