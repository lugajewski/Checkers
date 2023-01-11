from .constants import SQUARE_SIZE, CROWN, WHITE, PADDING, OUTLINE
import pygame


class Piece:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win, light_pieces_color, dark_pieces_color, outline_color):
        radius = SQUARE_SIZE // 2 - PADDING
        pygame.draw.circle(win, outline_color, (self.x, self.y), radius + OUTLINE)
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