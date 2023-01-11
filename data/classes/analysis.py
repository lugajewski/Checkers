import pygame
from .board import Board
import pickle

class Analysis:
    def __init__(self, win):
        self.win = win
        self.board = Board()
        self.counter = 0
        self.moves = []

    def update(self, light_pieces_color, dark_pieces_color, light_squares_color, dark_squares_color):
        self.start_analysis()
        self.board.draw(self.win, light_pieces_color, dark_pieces_color, light_squares_color, dark_squares_color)

    def start_analysis(self):
        self.moves = pickle.load(open("file.p", "rb"))

    def change_board_next(self):
        if self.counter < len(self.moves) - 1:
            self.counter += 1
            self.board = self.moves[self.counter]

    def change_board_prev(self):
        if self.counter > 0:
            self.counter -= 1
            self.board = self.moves[self.counter]
