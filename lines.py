import pygame

class Lines:
    """The class is responsible for drawing the lines for the game."""
    def __init__(self, ai_game):
        """Initialization of the classes data."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.lines_color


        #Creating a rectangle for the lines top, bottom, left, right
        #And definitng the right placement.
        self.rect_left = pygame.Rect(500, 100, self.settings.lines_width, self.settings.lines_height)
        self.rect_right = pygame.Rect(700, 100, self.settings.lines_width, self.settings.lines_height)
        self.rect_top = pygame.Rect(300, 300, self.settings.lines_height, self.settings.lines_width)
        self.rect_bottom = pygame.Rect(300, 500, self.settings.lines_height, self.settings.lines_width)

        # Granice kolumn (x)
        x0 = self.rect_top.left  # 300
        x1 = self.rect_left.left  # 500
        x2 = self.rect_right.left  # 700
        x3 = self.rect_top.right  # 300 + 600 = 900

        # Granice wierszy (y)
        y0 = self.rect_left.top  # 100
        y1 = self.rect_top.top  # 300
        y2 = self.rect_bottom.top  # 500
        y3 = self.rect_left.bottom  # 100 + 600 = 700

        self.squares = [
            # górny rząd
            pygame.Rect(x0, y0, x1 - x0, y1 - y0),  # lewy-górny
            pygame.Rect(x1 + self.settings.lines_width, y0, x2 - (x1 + self.settings.lines_width), y1 - y0),
            # środkowy-górny
            pygame.Rect(x2 + self.settings.lines_width, y0, x3 - (x2 + self.settings.lines_width), y1 - y0),
            # prawy-górny

            # środkowy rząd
            pygame.Rect(x0, y1 + self.settings.lines_width, x1 - x0, y2 - (y1 + self.settings.lines_width)),
            # lewy-środkowy
            pygame.Rect(x1 + self.settings.lines_width, y1 + self.settings.lines_width,
                        x2 - (x1 + self.settings.lines_width),
                        y2 - (y1 + self.settings.lines_width)),  # środkowy-środkowy
            pygame.Rect(x2 + self.settings.lines_width, y1 + self.settings.lines_width,
                        x3 - (x2 + self.settings.lines_width),
                        y2 - (y1 + self.settings.lines_width)),  # prawy-środkowy

            # dolny rząd
            pygame.Rect(x0, y2 + self.settings.lines_width, x1 - x0, y3 - (y2 + self.settings.lines_width)),
            # lewy-dolny
            pygame.Rect(x1 + self.settings.lines_width, y2 + self.settings.lines_width,
                        x2 - (x1 + self.settings.lines_width),
                        y3 - (y2 + self.settings.lines_width)),  # środkowy-dolny
            pygame.Rect(x2 + self.settings.lines_width, y2 + self.settings.lines_width,
                        x3 - (x2 + self.settings.lines_width),
                        y3 - (y2 + self.settings.lines_width)),  # prawy-dolny
        ]
        
        self.squares_active = {i: False for i, square in enumerate(self.squares)}


    def draw_lines(self):
        """Drawing the lines on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect_top)
        pygame.draw.rect(self.screen, self.color, self.rect_bottom)
        pygame.draw.rect(self.screen, self.color, self.rect_left)
        pygame.draw.rect(self.screen, self.color, self.rect_right)
