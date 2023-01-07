import pygame
from .constants import SQUARE_SIZE, WHITE, RED, BLUE
from .board import Board
import pickle

class Analysis:
    def __init__(self):
        self.board = Board()
        self.counter = 0
        self.moves = []

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
