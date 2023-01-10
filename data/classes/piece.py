from .constants import SQUARE_SIZE, GREY, CROWN, WHITE
import pygame


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()
        self.outline_color = GREY

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win, light_pieces_color, dark_pieces_color):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.outline_color, (self.x, self.y), radius + self.OUTLINE)
        if self.color == WHITE:
            pygame.draw.circle(win, dark_pieces_color, (self.x, self.y), radius)
        else:
            pygame.draw.circle(win, light_pieces_color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)