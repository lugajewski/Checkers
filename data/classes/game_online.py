import pygame.event

from .board import Board
from .constants import *
from .network import Network
from .settings import Settings
class Game_online():
    def __init__(self, win, game):
        self.win = win
        self._init(game)

    def update(self):
        self.board.draw(self.win, self.settings.pieces_color, self.settings.squares_color)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self, game):
        self.settings = Settings()
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.menu = game.menu
        self.network = Network()
        self.side = self.network.getP()
        self.last_board = self.board.board

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

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

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
        self.change_turn()

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def get_option_from_mouse(self, pos):
        x, y = pos
        option = 0
        if 0 < y < 300:
            option = 1
        if 300 < y < 600:
            option = 2
        if y > 600:
            option = 3
        return option

    def start_online_game(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            self.board.board = self.network.get_board()
            for event in pygame.event.get():
                if self.winner() is not None:
                    print(self.winner())
                    self.menu.navigator = 0
                    run = False
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.turn == self.side:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_row_col_from_mouse(pos)
                    self.select(row, col)
                    self.network.send_board(self.board.board)
            self.update()


