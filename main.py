import pygame
from pygame.locals import *
from data.classes.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, RED, FPS
from data.classes.ads import Ads
from data.classes.menu import Menu
from data.classes.game import Game
from data.classes.game_multiplayer import Game_multiplayer
from data.classes.analysis import Analysis
from data.classes.settings import Settings
from data.classes.AI import minimax
import pickle

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def update(menu, game, game_multiplayer, analysis, settings):
    if menu.navigator == 0:
        menu.update()
    elif menu.navigator == 1:
        game.update(menu.difficulty, settings.light_pieces_color, settings.dark_pieces_color, settings.light_squares_color, settings.dark_squares_color)
    elif menu.navigator == 2:
        game_multiplayer.update(settings.light_pieces_color, settings.dark_pieces_color, settings.light_squares_color, settings.dark_squares_color)
    elif menu.navigator == 3:
        analysis.update(settings.light_pieces_color, settings.dark_pieces_color, settings.light_squares_color, settings.dark_squares_color)
    elif menu.navigator == 4:
        settings.update()
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    ads = Ads(WIN)
    menu = Menu(WIN)
    game = Game(WIN)
    game_multiplayer = Game_multiplayer(WIN)
    analysis = Analysis(WIN)
    settings = Settings(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), menu.difficulty, WHITE, game)
            game.ai_move(new_board)

        if game.winner() is not None:
            print(game.winner())
            menu.navigator = 0

        if game_multiplayer.winner() is not None:
            print(game.winner())
            menu.navigator = 0

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if menu.navigator == 0:
                        run = False
                    elif menu.navigator == 1:
                        menu.navigator = 0
                        pickle.dump(game.moves, open("file.p", "wb"))
                    elif menu.navigator == 2 or menu.navigator == 3 or (menu.navigator == 4 and settings.navigator == 0):
                        menu.navigator = 0
                    elif menu.navigator == 4 and (settings.navigator == 1 or settings.navigator == 2):
                        settings.navigator = 0
                elif event.key == K_RIGHT and menu.navigator == 3:
                    analysis.change_board_next()
                elif event.key == K_LEFT and menu.navigator == 3:
                    analysis.change_board_prev()
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if menu.navigator == 0:
                    option = menu.get_option_from_mouse(pos)
                    menu.chose_options(option)
                elif menu.navigator == 1:
                    row, col = game.get_row_col_from_mouse(pos)
                    game.select(row, col)
                elif menu.navigator == 2:
                    row, col = game.get_row_col_from_mouse(pos)
                    game_multiplayer.select(row, col)
                elif menu.navigator == 4:
                    option = settings.get_option_from_mouse(pos)
                    settings.chose_options(option, game)
                elif menu.navigator == 5:
                    run = False
        if ads.status == False:
            update(menu, game, game_multiplayer, analysis, settings)
    pygame.quit()


main()