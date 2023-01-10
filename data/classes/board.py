import pygame
from .constants import ROWS, RED, SQUARE_SIZE, COLS, WHITE, BACKGROUND_COLOR, TEXT_COLOR, WIDTH, HEIGHT, OUTLINE_COLOR
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.light_left = self.dark_left = 12
        self.light_kings = self.dark_kings = 0
        self.create_board()

    def draw_squares(self, win, light_squares_color, dark_squares_color):
        win.fill(dark_squares_color)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, light_squares_color, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):
        return self.dark_left - self.light_left + (self.dark_kings * 0.5 - self.light_kings * 0.5)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.dark_kings += 1
            else:
                self.light_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win, light_pieces_color, dark_pieces_color, light_squares_color, dark_squares_color):
        self.draw_squares(win, light_squares_color, dark_squares_color)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win, light_pieces_color, dark_pieces_color, OUTLINE_COLOR)


    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.light_left -= 1
                else:
                    self.dark_left -= 1

    def winner(self):
        if self.light_left <= 0:
            return WHITE
        elif self.dark_left <= 0:
            return RED

        return None

    def draw_result(self, win, result):
        pygame.draw.rect(win, BACKGROUND_COLOR, (0, 0, WIDTH, HEIGHT))
        if not pygame.font.get_init():
            pygame.font.init()
        font = pygame.font.Font("data/assets/arial1.ttf", 50)
        if result == RED:
            tekst = font.render("You won!", False, TEXT_COLOR)
        if result == WHITE:
            tekst = font.render("You lost!", False, TEXT_COLOR)
        win.blit(tekst, (WIDTH//5, HEIGHT//2))
        pygame.display.update()
        pygame.time.wait(3000)

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves