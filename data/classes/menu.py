import pygame
from .constants import HEIGHT, WIDTH, BLACK, WHITE, RED, BLUE, GREY


class Menu:
    def __init__(self):
        self.button_width = HEIGHT//2
        self.space_height = (HEIGHT - HEIGHT // 4) / 16
        self.button_height = self.space_height*2
        self.background = BLACK
        self.options1 = RED
        self.options2 = BLUE
        self.options3 = GREY
        self.text = WHITE
        self.navigator = 0

    def draw_background(self, win):
        pygame.draw.rect(win, self.background, (0, 0, WIDTH, HEIGHT))

    def draw_options(self, win):
        if not pygame.font.get_init():
            pygame.font.init()
        # single player
        pygame.draw.rect(win, self.options1, (WIDTH // 4, HEIGHT // 4 + self.space_height, self.button_width, self.button_height))
        font = pygame.font.Font("data/assets/arial1.ttf", 40)
        tekst = font.render("Start", False, self.text)
        win.blit(tekst, (WIDTH //4 , HEIGHT // 4 + 2 * self.space_height - font.get_height() // 2))
        # online
        pygame.draw.rect(win, self.options2, (WIDTH//4, HEIGHT//4 + 2 * self.space_height + self.button_height, self.button_width, self.button_height))
        tekst = font.render("Multiplayer (jeszcze nie dziala)", False, self.text)
        win.blit(tekst, (WIDTH // 4, HEIGHT // 4 + 3 * self.space_height + self.button_height - font.get_height() // 2))
        # analysis
        pygame.draw.rect(win, self.options2, (WIDTH//4, HEIGHT//4 + 3 * self.space_height + 2 * self.button_height, self.button_width, self.button_height))
        tekst = font.render("Analiza", False, self.text)
        win.blit(tekst, (WIDTH // 4, HEIGHT // 4 + 4 * self.space_height + 2 * self.button_height - font.get_height() // 2))
        # settings
        pygame.draw.rect(win, self.options2, (WIDTH // 4, HEIGHT // 4 + 4 * self.space_height + 3 * self.button_height, self.button_width, self.button_height))
        tekst = font.render("Ustawienia", False, self.text)
        win.blit(tekst, (WIDTH // 4, HEIGHT // 4 + 5 * self.space_height + 3 * self.button_height - font.get_height() // 2))
        # exit
        pygame.draw.rect(win, self.options2, (WIDTH // 4, HEIGHT // 4 + 5 * self.space_height + 4 * self.button_height, self.button_width, self.button_height))
        tekst = font.render("Wyjście (jeszcze nie dziala)", False, self.text)
        win.blit(tekst, (WIDTH // 4, HEIGHT // 4 + 6 * self.space_height + 4 * self.button_height - font.get_height() // 2))

    def draw_result(self, win, result):
        pygame.draw.rect(win, self.background, (0, 0, WIDTH, HEIGHT))
        if not pygame.font.get_init():
            pygame.font.init()
        font = pygame.font.Font("data/assets/arial1.ttf", 50)
        if result == RED:
            tekst = font.render("Czerwone wygraly", False, self.text)
        if result == WHITE:
            tekst = font.render("Biale wygraly", False, self.text)
        win.blit(tekst, (WIDTH//5, HEIGHT//2))
        pygame.display.update()
        pygame.time.wait(3000)

    def get_option_from_mouse(self, pos):
        x, y = pos
        option = 0
        if HEIGHT // 4 + self.space_height < y < HEIGHT // 4 + self.space_height + self.button_height:
            option = 1
        elif HEIGHT//4 + 2 * self.space_height + self.button_height < y < HEIGHT//4 + 2 * self.space_height + self.button_height + self.button_height:
            option = 2
        elif HEIGHT//4 + 3 * self.space_height + 2 * self.button_height < y < HEIGHT//4 + 3 * self.space_height + 2 * self.button_height + self.button_height:
            option = 3
        elif HEIGHT // 4 + 4 * self.space_height + 3 * self.button_height < y < HEIGHT // 4 + 4 * self.space_height + 3 * self.button_height + self.button_height:
            option = 4
        elif HEIGHT // 4 + 5 * self.space_height + 4 * self.button_height < y < HEIGHT // 4 + 5 * self.space_height + 4 * self.button_height + self.button_height:
            option = 5
        return option

    def chose_options(self, option, game):
        self.navigator = option
