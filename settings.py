class Settings:
    """Class responsible for holding the settings of the game."""
    def __init__(self):
        """Initialization of the class."""
        #Data regarding the screen
        self.screen_width = 1200
        self.screen_height = 800

        #Data regarding the lines.
        self.lines_color = (0, 0, 0)
        self.lines_width = 3
        self.lines_height = 600

        #Data regarding cross and circle
        #Circle
        self.color_circle = (0, 0, 255)
        self.circle_radius = 50
        self.circle_width = 3
        #Cross
        self.color_cross = (255, 0, 0)
        self.cross_width = 5
        self.cross_height = 10

