import sys

import pygame

from settings import Settings
from lines import Lines
from circle import Circle
from cross import Cross
from tiles import Tiles

class TicTacToe:
    """Główna klasa gry zajmująca się jej zasobami."""
    def __init__(self):
        """Inicjalizacja danych gry."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()

        self.lines = Lines(self)
        self.tiles = Tiles(self)
        self.circles = pygame.sprite.Group()
        self.crosses = pygame.sprite.Group()
        self.turn_circle = True
        self.game_active = True
        self.winning_numbers = []
    def run_game(self):
        """Główna pętla gry."""
        while True:
            self._check_events()
            self._check_game_logic()
            self._update_screen()
            self.clock.tick(60)
    def _check_keydown_events(self, event):
        """Function checks if any keys are being pressed."""
        if event.key == pygame.K_q:
            sys.exit()

    def _mouse_button_press(self):
        """Function acts accordingly to rules and draws a circle or a cross if pressed in the correct space"""
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
                        self.lines.who_won_dict[i] = "Circle"
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
                        self.lines.who_won_dict[i] = "Cross"

    def _check_events(self):
        """Function responsible for all the events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_active:
                    self._mouse_button_press()

    def _check_game_logic(self):
        """Function checks whether the game is over or not."""
        if self.lines.who_won_dict[0] == self.lines.who_won_dict[3] == self.lines.who_won_dict[6] == "Circle" or self.lines.who_won_dict[0] == self.lines.who_won_dict[3] == self.lines.who_won_dict[6] == "Cross":
            self.game_active = False
            self.winning_numbers = [0, 6]
        elif self.lines.who_won_dict[1] == self.lines.who_won_dict[4] == self.lines.who_won_dict[7] == "Circle" or self.lines.who_won_dict[1] == self.lines.who_won_dict[4] == self.lines.who_won_dict[7] == "Cross":
            self.game_active = False
            self.winning_numbers = [1, 7]
        elif self.lines.who_won_dict[2] == self.lines.who_won_dict[5] == self.lines.who_won_dict[8] == "Circle" or self.lines.who_won_dict[2] == self.lines.who_won_dict[5] == self.lines.who_won_dict[8] == "Cross":
            self.game_active = False
            self.winning_numbers = [2, 8]
        elif self.lines.who_won_dict[0] == self.lines.who_won_dict[1] == self.lines.who_won_dict[2] == "Circle" or self.lines.who_won_dict[0] == self.lines.who_won_dict[1] == self.lines.who_won_dict[2] == "Cross":
            self.game_active = False
            self.winning_numbers = [0, 2]
        elif self.lines.who_won_dict[3] == self.lines.who_won_dict[4] == self.lines.who_won_dict[5] == "Circle" or self.lines.who_won_dict[3] == self.lines.who_won_dict[4] == self.lines.who_won_dict[5] == "Cross":
            self.game_active = False
            self.winning_numbers = [3, 5]
        elif self.lines.who_won_dict[6] == self.lines.who_won_dict[7] == self.lines.who_won_dict[8] == "Circle" or self.lines.who_won_dict[6] == self.lines.who_won_dict[7] == self.lines.who_won_dict[8] == "Cross":
            self.game_active = False
            self.winning_numbers = [6, 8]
        elif self.lines.who_won_dict[0] == self.lines.who_won_dict[4] == self.lines.who_won_dict[8] == "Circle" or self.lines.who_won_dict[0] == self.lines.who_won_dict[4] == self.lines.who_won_dict[8] == "Cross":
            self.game_active = False
            self.winning_numbers = [0, 8]
        elif self.lines.who_won_dict[2] == self.lines.who_won_dict[4] == self.lines.who_won_dict[6] == "Circle" or self.lines.who_won_dict[2] == self.lines.who_won_dict[4] == self.lines.who_won_dict[6] == "Cross":
            self.game_active = False
            self.winning_numbers = [2, 6]

    def _update_screen(self):
        """Funtion responsible for refreshing the screen"""
        self.screen.fill((255,255,255))
        self.lines.draw_lines()
        self.tiles.draw_tiles()
        for circle in self.circles:
            circle.draw_circle(circle.circle_center)

        for cross in self.crosses:
            cross.draw_cross(cross.start_x, cross.start_y)
        if self.game_active == False:
            self.lines.draw_endgame_line(self.winning_numbers[0], self.winning_numbers[1])
        pygame.display.flip()


if __name__ == "__main__":
    ai = TicTacToe()
    ai.run_game()
