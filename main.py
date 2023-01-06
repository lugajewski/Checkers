import pygame
from pygame.locals import *
from data.classes.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, RED, FPS
from data.classes.game import Game
from data.classes.AI import minimax
from data.classes.ads import Ads

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    ads = Ads(WIN)
    #ads.start_ads()

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
                    elif game.menu.navigator == 1 or game.menu.navigator == 2 or (game.menu.navigator == 4 and game.settings.navigator == 0):
                        game.menu.navigator = 0
                    elif game.menu.navigator == 4 and (game.settings.navigator == 1 or game.settings.navigator == 2):
                        game.settings.navigator = 0
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
                elif game.menu.navigator == 4:
                    option = game.get_option_from_mouse(pos)
                    game.settings.chose_options(option, game)
        if ads.status == False:
            game.update()
    pygame.quit()


main()