import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
FPS = 60

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
BROWN = (100, 30, 0)
BEIGE = (217, 186, 140)
BACKGROUND_COLOR = (242, 239, 222)
SELECTED_BUTTON_COLOR = (196, 193, 169)
BUTTON_COLOR = (222, 221, 195)
TEXT_COLOR = (122, 118, 103)

CROWN = pygame.transform.scale(pygame.image.load('data/assets/crown.png'), (44, 25))