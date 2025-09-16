import sys

import pygame

from settings import Settings

from lines import Lines
from circle import Circle
from cross import Cross

from tiles import Tiles
from game_signs import GameSigns
from game_stats import GameStats

class TicTacToe:
    """Główna klasa gry zajmująca się jej zasobami."""
    def __init__(self):
        """Inicjalizacja danych gry."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()

        self.game_stats = GameStats()
        self.lines = Lines(self)

        self.tiles = Tiles(self)
        self.game_signs = GameSigns(self)

        self.circles = pygame.sprite.Group()
        self.crosses = pygame.sprite.Group()

        self.turn_circle = True
        self.game_active = True

        self.winning_numbers = []

    def run_game(self):
        """Główna pętla gry."""
        while True:
            self._check_events()
            if self.game_active:
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

    def _check_play_button(self, mouse_pos):
        """Checking if the 'GAME' button has been pressed and reacting."""
        button_clicked = self.game_signs.game_str_rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.circles.empty()
            self.crosses.empty()
            self.lines._reset_dict()
            self.game_active = True

    def _check_events(self):
        """Function responsible for all the events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                if self.game_active:
                    self._mouse_button_press()

    def _check_game_logic(self):
        """Checking if the game is over and mark winning cells."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            a, b, c = combo
            if self.lines.who_won_dict[a] == self.lines.who_won_dict[b] == self.lines.who_won_dict[c] and self.lines.who_won_dict[a] in ['Circle', 'Cross']:
                self.game_active = False
                self.winning_numbers = combo
                if self.lines.who_won_dict[a] == 'Circle':
                    self.game_stats.p1_score += 1
                    self.tiles.prep_number_p1()
                    self.game_signs.prep_side_wins_str('BLUE', (0, 0, 255))
                else:
                    self.game_stats.p2_score += 1
                    self.tiles.prep_number_p2()
                    self.game_signs.prep_side_wins_str('RED', (255, 0, 0))
                break

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
            self.lines.draw_endgame_line(self.winning_numbers[0], self.winning_numbers[2])
            self.game_signs.draw_signs()

        pygame.display.flip()


if __name__ == "__main__":
    ai = TicTacToe()
    ai.run_game()
