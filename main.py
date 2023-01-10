import pygame
from pygame.locals import *
from data.classes.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, RED, FPS
from data.classes.game import Game
from data.classes.AI import minimax
from data.classes.ads import Ads
import pickle

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    ads = Ads(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)

        if game.winner() is not None:
            print(game.winner())
            game.menu.navigator = 0

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if game.menu.navigator == 0:
                        run = False
                    elif game.menu.navigator == 1:
                        game.menu.navigator = 0
                        pickle.dump(game.moves, open("file.p", "wb" ))
                    elif game.menu.navigator == 2 or game.menu.navigator == 3 or (game.menu.navigator == 4 and game.settings.navigator == 0):
                        game.menu.navigator = 0
                    elif game.menu.navigator == 4 and (game.settings.navigator == 1 or game.settings.navigator == 2):
                        game.settings.navigator = 0
                elif event.key == K_RIGHT and game.menu.navigator == 3:
                    game.analysis.change_board_next()
                elif event.key == K_LEFT and game.menu.navigator == 3:
                    game.analysis.change_board_prev()
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if game.menu.navigator == 0:
                    option = game.menu.get_option_from_mouse(pos)
                    game.menu.chose_options(option, game)
                elif game.menu.navigator == 1:
                    row, col = game.get_row_col_from_mouse(pos)
                    game.select(row, col)
                elif game.menu.navigator == 2:
                    row, col = game.get_row_col_from_mouse(pos)
                    game.game_multiplayer.select(row, col)
                elif game.menu.navigator == 4:
                    option = game.settings.get_option_from_mouse(pos)
                    game.settings.chose_options(option, game)
                elif game.menu.navigator == 5:
                    run = False
        if ads.status == False:
            game.update()
    pygame.quit()


main()