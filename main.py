import pygame
from data.classes.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, RED
from data.classes.game import Game
from data.classes.ads import Ads

FPS = 60

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
        if game.winner() is not None:
            print(game.winner())
            game.menu.navigator = 0
        if game.online:
            game.game_online = game.network.s_r(game.game_online)

        for event in pygame.event.get():
            if event.type == pygame.QUIT and game.menu.navigator == 0:
                run = False
            if event.type == pygame.QUIT and (game.menu.navigator == 1 or game.menu.navigator == 2 or (game.menu.navigator == 3 and game.settings.navigator == 0)):
                game.menu.navigator = 0
            if event.type == pygame.QUIT and game.menu.navigator == 3 and (game.settings.navigator == 1 or game.settings.navigator == 2):
                game.settings.navigator = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if game.menu.navigator == 0:
                    option = game.get_option_from_mouse(pos)
                    game.menu.chose_options(option, game)
                elif game.menu.navigator == 2 and game.turn != game.game_online.side:
                    pass
                elif game.menu.navigator == 1:
                    row, col = game.get_row_col_from_mouse(pos)
                    game.select(row, col)
                    if game.online:
                        game.game_online.turn = game.turn
                elif game.menu.navigator == 3:
                    option = game.get_option_from_mouse(pos)
                    game.settings.chose_options(option, game)
        if ads.status == False:
            game.update()
    pygame.quit()


main()