import pygame
from data.classes.constants import WIDTH, HEIGHT, SQUARE_SIZE
from data.classes.game import Game
from data.classes.menu import Menu

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def get_option_from_mouse(pos):
    x, y = pos
    option = 0
    if 0 < y < 300:
        option = 1
    if 300 < y < 600:
        option = 2
    if y > 600:
        option = 3
    return option


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if game.menu.status:
                    option = get_option_from_mouse(pos)
                    game.menu.chose_options(option, game)
                else:
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)
        game.update()
    pygame.quit()


main()