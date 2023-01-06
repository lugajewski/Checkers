import pygame
from .constants import HEIGHT, WIDTH, BLACK, WHITE, RED, BLUE, GREY, BROWN


class Settings:
    def __init__(self):
        self.background_color = BLACK
        self.option1_color = RED
        self.option2_color = BLUE
        self.text = WHITE
        self.navigator = 0
        self.pieces_color = RED
        self.squares_color = RED

    def draw_settings_background(self, win):
        pygame.draw.rect(win, self.background_color, (0, 0, WIDTH, HEIGHT))

    def draw_settings_options(self, win):
        if not pygame.font.get_init():
            pygame.font.init()
        # kolor bierek
        pygame.draw.rect(win, self.option1_color, (0, 0 + HEIGHT//10, WIDTH, HEIGHT//3))
        font = pygame.font.Font("data/assets/arial1.ttf", 40)
        tekst = font.render("Zmiana koloru bierek", False, self.text)
        win.blit(tekst, (WIDTH//3, HEIGHT//10 + HEIGHT//6 - font.get_height()//2))
        # kolor pól
        pygame.draw.rect(win, self.option2_color, (0, HEIGHT // 3 + HEIGHT//10, WIDTH, HEIGHT // 3))
        tekst = font.render("Zmiana koloru pól", False, self.text)
        win.blit(tekst, (WIDTH//3, HEIGHT//10 + HEIGHT//6 + HEIGHT//3 - font.get_height()//2))

    def draw_pieces_settings_options(self, win):
        if not pygame.font.get_init():
            pygame.font.init()
        # kolor bierek
        pygame.draw.rect(win, self.option1_color, (0, 0 + HEIGHT//10, WIDTH, HEIGHT//3))
        font = pygame.font.Font("data/assets/arial1.ttf", 40)
        tekst = font.render("Biale i czerwone", False, self.text)
        win.blit(tekst, (WIDTH//3, HEIGHT//10 + HEIGHT//6 - font.get_height()//2))
        # kolor pól
        pygame.draw.rect(win, self.option2_color, (0, HEIGHT // 3 + HEIGHT//10, WIDTH, HEIGHT // 3))
        tekst = font.render("Biale i brazowe", False, self.text)
        win.blit(tekst, (WIDTH//3, HEIGHT//10 + HEIGHT//6 + HEIGHT//3 - font.get_height()//2))

    def draw_squares_settings_options(self, win):
        if not pygame.font.get_init():
            pygame.font.init()
        # kolor bierek
        pygame.draw.rect(win, self.option1_color, (0, 0 + HEIGHT//10, WIDTH, HEIGHT//3))
        font = pygame.font.Font("data/assets/arial1.ttf", 40)
        tekst = font.render("Czarne i czerwone", False, self.text)
        win.blit(tekst, (WIDTH//3, HEIGHT//10 + HEIGHT//6 - font.get_height()//2))
        # kolor pól
        pygame.draw.rect(win, self.option2_color, (0, HEIGHT // 3 + HEIGHT//10, WIDTH, HEIGHT // 3))
        tekst = font.render("Czarne i brazowe", False, self.text)
        win.blit(tekst, (WIDTH//3, HEIGHT//10 + HEIGHT//6 + HEIGHT//3 - font.get_height()//2))

    def chose_options(self, option, game):
        if self.navigator == 0:
            if option == 1:
                self.navigator = option
            elif option == 2:
                self.navigator = option
        elif self.navigator == 1:
            if option == 1:
                self.pieces_color = RED
            elif option == 2:
                self.pieces_color = BROWN
        elif self.navigator == 2:
            if option == 1:
                self.squares_color = RED
            elif option == 2:
                self.squares_color = BROWN