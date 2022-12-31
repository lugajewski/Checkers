import pygame
from .constants import HEIGHT, WIDTH, BLACK, WHITE, RED


class Menu:
    def __init__(self):
        self.background = BLACK
        self.options = RED
        self.text = WHITE
        self.status = True

    def draw_background(self, win):
        pygame.draw.rect(win, self.background, (0, 0, WIDTH, HEIGHT))

    def draw_options(self, win):
        if not pygame.font.get_init():
            pygame.font.init()
        # single player
        pygame.draw.rect(win, self.options, (WIDTH//4, HEIGHT//9, WIDTH//2, HEIGHT // 8))
        font = pygame.font.Font("data/assets/arial1.ttf", 40)
        tekst = font.render("Gra SinglePlayer", False, self.text)
        win.blit(tekst, (WIDTH//3-20, HEIGHT//7))
        # online
        pygame.draw.rect(win, self.options, (WIDTH // 4, HEIGHT // 2, WIDTH // 2, HEIGHT // 8))
        tekst = font.render("Gra Multiplayer", False, self.text)
        win.blit(tekst, (WIDTH // 3 - 20, HEIGHT // 2))
        # settings
        pygame.draw.rect(win, self.options, (WIDTH//4, HEIGHT//4, WIDTH//2, HEIGHT//8))
        tekst = font.render("Ustawienia", False, self.text)
        win.blit(tekst, (WIDTH//3-20, HEIGHT//4))
    def chose_options(self, option, game):
        if option == 1:
            self.status = False
            game.status = True