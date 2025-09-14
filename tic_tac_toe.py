import sys

import pygame

from settings import Settings
from lines import Lines
from circle import Circle
from cross import Cross

class TicTacToe:
    """Główna klasa gry zajmująca się jej zasobami."""
    def __init__(self):
        """Inicjalizacja danych gry."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()

        self.lines = Lines(self)
        self.circles = pygame.sprite.Group()
        self.crosses = pygame.sprite.Group()
        self.turn_circle = True

    def run_game(self):
        """Główna pętla gry."""
        while True:
            self.screen.fill((255,255,255))
            self.lines.draw_lines()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.turn_circle:
                        
                        for i, square in enumerate(self.lines.squares):
                            if square.collidepoint(mouse_pos):
                                if self.lines.squares_active[i] == False:
                                    new_circle = Circle(self)
                                    new_circle.circle_center = square.center
                                    self.circles.add(new_circle)
                                    self.turn_circle = False
                                    self.lines.squares_active[i] = True
                    else:
                        for i, square in enumerate(self.lines.squares):
                            if square.collidepoint(mouse_pos):
                                if self.lines.squares_active[i] == False:
                                    new_cross = Cross(self)
                                    new_cross.start_x = square.center[0] - 40
                                    new_cross.start_y = square.center[1] - 40
                                    self.crosses.add(new_cross)
                                    self.turn_circle = True
                                    self.lines.squares_active[i] = True

            for circle in self.circles:
                circle.draw_circle(circle.circle_center)

            for cross in self.crosses:
                cross.draw_cross(cross.start_x, cross.start_y)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    ai = TicTacToe()
    ai.run_game()
