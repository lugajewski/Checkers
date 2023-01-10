from copy import deepcopy
import pygame
from .constants import SQUARE_SIZE, WHITE, RED, BLUE
from .board import Board
from .menu import Menu
from .settings import Settings
from .analysis import Analysis
from .game_multiplayer import Game_multiplayer
from .AI import minimax


class Game:
    def __init__(self, win):
        self.win = win
        self._init()

    def _init(self):
        self.settings = Settings()
        self.selected = None
        self.board = Board()
        self.analysis = Analysis()
        self.turn = RED
        self.valid_moves = {}
        self.menu = Menu()
        self.online = False
        self.moves = []
        temp_board = deepcopy(self.board)
        self.moves.append(temp_board)
        self.game_multiplayer = Game_multiplayer()

    def update(self):
        if self.turn == WHITE:
            value, new_board = minimax(self.get_board(), 3, WHITE, self)
            self.ai_move(new_board)
        self.board.draw(self.win, self.settings.pieces_color, self.settings.squares_color)
        self.draw_valid_moves(self.valid_moves)

    def winner(self):
        if self.board.winner() is not None:
            self.menu.draw_result(self.win, self.board.winner())
            self.reset()
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        temp_board = deepcopy(self.board)
        self.moves.append(temp_board)
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        temp_board = deepcopy(self.board)
        self.moves.append(temp_board)
        self.change_turn()

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col