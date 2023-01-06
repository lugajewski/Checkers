import pygame
from data.classes.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, RED
from data.classes.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        if game.winner() is not None:
            print(game.winner())
            game.menu.status = True
        if game.online:
            game.game_online = game.network.s_r(game.game_online)

        for event in pygame.event.get():
            if event.type == pygame.QUIT and game.menu.status == True:
                run = False
            if event.type == pygame.QUIT and game.menu.status == False:
                game.menu.status = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if game.menu.status:
                    option = game.get_option_from_mouse(pos)
                    game.menu.chose_options(option, game)
                elif game.menu.status == False and game.online == True and game.turn != game.game_online.side:
                    pass
                else:
                    row, col = game.get_row_col_from_mouse(pos)
                    game.select(row, col)
                    if game.online:
                        game.game_online.turn = game.turn
        game.update()
    pygame.quit()


main()