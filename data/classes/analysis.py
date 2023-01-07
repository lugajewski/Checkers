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

    def change_board(self):
        if self.counter < len(self.moves):
            self.board = self.moves[self.counter]
            self.counter += 1

