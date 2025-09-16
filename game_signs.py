import pygame.font

class GameSigns:
    """Class responsible for showing the 'Game' text as well as 'P1 wins' or 'P2 wins'."""
    def __init__(self, ai_game):
        """Initializing the class."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.font = pygame.font.SysFont(None, 70)

        self.prep_game_str()
        self.prep_side_wins_str(None, (0, 0, 0))
        self.prep_whose_turn(None, (0, 0, 0))
        self.prep_draw()

    def prep_game_str(self):
        """Preparing the string 'game'."""
        game_str = 'GAME'
        self.game_str_image = self.font.render(game_str, True, (0, 0, 0), (0, 255, 0))
        #Showing the str in the center of the screen.
        self.game_str_rect = self.game_str_image.get_rect()
        self.game_str_rect.centerx = self.screen_rect.centerx
        self.game_str_rect.y = self.screen_rect.y + 50

    def prep_side_wins_str(self, winner, winner_color):
        """Preparing the string 'BLUE WINS' or 'RED WINS'."""
        side_wins_str = f"{winner} WINS"
        self.side_wins_str_image = self.font.render(side_wins_str, True, (0, 0, 0), winner_color)
        #Showing the str above the 'GAME' str on the screen.
        self.side_wins_str_rect = self.side_wins_str_image.get_rect()
        self.side_wins_str_rect.center = self.screen_rect.center

    def prep_whose_turn(self, turn, turn_color):
        """Preparing the string 'TURN: CIRCLE' or 'TURN: CROSS'."""
        whose_turn_str = f"TURN: {turn}"
        self.whose_turn_str_image = self.font.render(whose_turn_str, True, (0, 0, 0), turn_color)
        #Showing the str where the GAME sign is.
        self.whose_turn_str_rect = self.whose_turn_str_image.get_rect()
        self.whose_turn_str_rect.centerx = self.screen_rect.centerx
        self.whose_turn_str_rect.y = self.screen_rect.y + 50

    def prep_draw(self):
        """Preparing the string 'DRAW'."""
        draw_str = "DRAW"
        self.draw_str_image = self.font.render(draw_str, True, (0, 0, 0), (0, 255, 0))
        #Showing the str where the GAME sign is.
        self.draw_str_rect = self.draw_str_image.get_rect()
        self.draw_str_rect.centerx = self.screen_rect.centerx
        self.draw_str_rect.y = self.screen_rect.y + 50

    def draw_whose_turn(self):
        """Drawing the TURN string on the screen."""
        self.screen.blit(self.whose_turn_str_image, self.whose_turn_str_rect)

    def draw_draw(self):
        """Drawing the DRAW string on the screen."""
        self.screen.blit(self.draw_str_image, self.draw_str_rect)

    def draw_signs(self):
        """Drawing the game_str."""
        self.screen.blit(self.game_str_image, self.game_str_rect)
        self.screen.blit(self.side_wins_str_image, self.side_wins_str_rect)