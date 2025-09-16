import pygame.font

class Tiles:
    """The class responsible for showing tiles P1 and P2 as well as counting points"""
    def __init__(self, ai_game):
        """Initialization of the class"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats
        self.font = pygame.font.SysFont(None, 80)

        self.text_color_p1 = (0, 0, 255)
        self.text_color_p2 = (255, 0, 0)

        self.prep_p1()
        self.prep_p2()
        self.prep_number_p1()
        self.prep_number_p2()


    def prep_number_p1(self):
        """Preparign the number of times p1 has won."""
        score_str = str(self.game_stats.p1_score)
        self.score_str_p1_image = self.font.render(score_str, True, self.text_color_p1, (255, 255, 255))
        #Showing the string below the P1 sign.
        self.score_str_p1_rect = self.score_str_p1_image.get_rect()
        self.score_str_p1_rect.left = self.screen_rect.left + 50
        self.score_str_p1_rect.top = self.screen_rect.top + 126

    def prep_p1(self):
        """Generating text 'P1'"""
        string_p1 = 'P1'
        self.string_p1_image = self.font.render(string_p1, True, self.text_color_p1, (255, 255, 255))
        #Showing the string on the left side of the screen
        self.string_p1_rect = self.string_p1_image.get_rect()
        self.string_p1_rect.left = self.screen_rect.left + 50
        self.string_p1_rect.top = self.screen_rect.top + 63

    def prep_number_p2(self):
        """Preparing the number of times p2 has won."""
        score_str = str(self.game_stats.p2_score)
        self.score_str_p2_image = self.font.render(score_str, True, self.text_color_p2, (255, 255, 255))
        #Shwoing the string on the right side of the screen.
        self.score_str_p2_rect = self.score_str_p2_image.get_rect()
        self.score_str_p2_rect.right = self.screen_rect.right - 50
        self.score_str_p2_rect.top= self.screen_rect.top + 126

    def prep_p2(self):
        """Generating text 'P2'"""
        string_p2 = 'P2'
        self.string_p2_image = self.font.render(string_p2, True, self.text_color_p2, (255, 255, 255))
        #Showing the string on the right side of the screen.
        self.string_p2_rect = self.string_p2_image.get_rect()
        self.string_p2_rect.right = self.screen_rect.right - 50
        self.string_p2_rect.top = self.screen_rect.top + 63

    def draw_tiles(self):
        """Drawing the created text"""
        self.screen.blit(self.string_p1_image, self.string_p1_rect)
        self.screen.blit(self.string_p2_image, self.string_p2_rect)
        self.screen.blit(self.score_str_p1_image, self.score_str_p1_rect)
        self.screen.blit(self.score_str_p2_image, self.score_str_p2_rect)