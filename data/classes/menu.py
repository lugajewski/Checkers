import pygame
from .constants import HEIGHT, WIDTH, BLACK, WHITE, RED, BLUE, GREY


class Menu:
    def __init__(self):
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
        pygame.draw.rect(win, self.options1, (0, 0 + HEIGHT//10, WIDTH, HEIGHT//3))
        font = pygame.font.Font("data/assets/arial1.ttf", 40)
        tekst = font.render("Gra SinglePlayer", False, self.text)
        win.blit(tekst, (WIDTH//3, HEIGHT//10 + HEIGHT//6 - font.get_height()//2))
        # online
        pygame.draw.rect(win, self.options2, (0, HEIGHT // 3 + HEIGHT//10, WIDTH, HEIGHT // 3))
        tekst = font.render("Gra Multiplayer", False, self.text)
        win.blit(tekst, (WIDTH//3, HEIGHT//10 + HEIGHT//6 + HEIGHT//3 - font.get_height()//2))
        # settings
        pygame.draw.rect(win, self.options3, (0, HEIGHT//3 + HEIGHT//3 + HEIGHT//10, WIDTH, HEIGHT//3))
        tekst = font.render("Ustawienia", False, self.text)
        win.blit(tekst, (WIDTH//3,HEIGHT//6 + HEIGHT//3 + HEIGHT//3 + font.get_height()//2))

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



    def chose_options(self, option, game):
        if option == 1:
            self.navigator = 1
        elif option == 2:
            self.navigator = 2
            game.init_online()