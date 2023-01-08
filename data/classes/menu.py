import pygame
from .constants import HEIGHT, WIDTH, WHITE, RED, BACKGROUND_COLOR, BUTTON_COLOR, SELECTED_BUTTON_COLOR, TEXT_COLOR


class Menu:
    def __init__(self):
        self.button_width = HEIGHT//2
        self.space_height = (HEIGHT - HEIGHT // 4) / 16
        self.button_height = self.space_height*2
        self.text_offset = self.button_height
        self.icon_offset = 5
        self.navigator = 0
        self.start_button_color = BUTTON_COLOR
        self.multiplayer_button_color = BUTTON_COLOR
        self.analysis_button_color = BUTTON_COLOR
        self.settings_button_color = BUTTON_COLOR
        self.exit_button_color = BUTTON_COLOR
        self.start_button_icon = pygame.transform.scale(pygame.image.load('data/assets/start_button_icon.png'), (65, 65))
        self.multiplayer_button_icon = pygame.transform.scale(pygame.image.load('data/assets/multiplayer_button_icon.png'), (65, 65))
        self.analysis_button_icon = pygame.transform.scale(pygame.image.load('data/assets/analysis_button_icon.png'), (65, 65))
        self.settings_button_icon = pygame.transform.scale(pygame.image.load('data/assets/settings_button_icon.png'), (65, 65))
        self.exit_button_icon = pygame.transform.scale(pygame.image.load('data/assets/exit_button_icon.png'), (65, 65))

    def set_button_colors(self, option):
        if option == 1:
            self.start_button_color = SELECTED_BUTTON_COLOR
        elif option == 2:
            self.multiplayer_button_color = SELECTED_BUTTON_COLOR
        elif option == 3:
            self.analysis_button_color = SELECTED_BUTTON_COLOR
        elif option == 4:
            self.settings_button_color = SELECTED_BUTTON_COLOR
        elif option == 5:
            self.exit_button_color = SELECTED_BUTTON_COLOR
        else:
            self.start_button_color = BUTTON_COLOR
            self.multiplayer_button_color = BUTTON_COLOR
            self.analysis_button_color = BUTTON_COLOR
            self.settings_button_color = BUTTON_COLOR
            self.exit_button_color = BUTTON_COLOR

    def draw_background(self, win):
        pygame.draw.rect(win, BACKGROUND_COLOR, (0, 0, WIDTH, HEIGHT))

    def draw_options(self, win, option):
        if not pygame.font.get_init():
            pygame.font.init()

        self.set_button_colors(option)

        font = pygame.font.Font("data/assets/broadway.ttf", 90)
        # header
        tekst = font.render("SUPER", False, TEXT_COLOR)
        win.blit(tekst, (243.35, font.get_height() // 2))
        tekst = font.render("CHECKERS", False, TEXT_COLOR)
        win.blit(tekst, (148.25, font.get_height() + font.get_height() // 2))

        font = pygame.font.Font("data/assets/broadway.ttf", 40)
        # single player
        pygame.draw.rect(win, self.start_button_color, (WIDTH // 4, HEIGHT // 4 + self.space_height, self.button_width, self.button_height))
        tekst = font.render("Start", False, TEXT_COLOR)
        win.blit(tekst, (WIDTH //4 + self.text_offset, HEIGHT // 4 + 2 * self.space_height - font.get_height() // 2))
        win.blit(self.start_button_icon, (WIDTH // 4 + self.icon_offset, HEIGHT // 4 + self.space_height + self.icon_offset))
        # online
        pygame.draw.rect(win, self.multiplayer_button_color, (WIDTH//4, HEIGHT//4 + 2 * self.space_height + self.button_height, self.button_width, self.button_height))
        tekst = font.render("Multiplayer", False, TEXT_COLOR)
        win.blit(tekst, (WIDTH // 4 + self.text_offset, HEIGHT // 4 + 3 * self.space_height + self.button_height - font.get_height() // 2))
        win.blit(self.multiplayer_button_icon, (WIDTH // 4 + self.icon_offset, HEIGHT//4 + 2 * self.space_height + self.button_height + self.icon_offset))
        # analysis
        pygame.draw.rect(win, self.analysis_button_color, (WIDTH//4, HEIGHT//4 + 3 * self.space_height + 2 * self.button_height, self.button_width, self.button_height))
        tekst = font.render("Analysis", False, TEXT_COLOR)
        win.blit(tekst, (WIDTH // 4 + self.text_offset, HEIGHT // 4 + 4 * self.space_height + 2 * self.button_height - font.get_height() // 2))
        win.blit(self.analysis_button_icon, (WIDTH // 4 + self.icon_offset, HEIGHT//4 + 3 * self.space_height + 2 * self.button_height + self.icon_offset))
        # settings
        pygame.draw.rect(win, self.settings_button_color, (WIDTH // 4, HEIGHT // 4 + 4 * self.space_height + 3 * self.button_height, self.button_width, self.button_height))
        tekst = font.render("Settings", False, TEXT_COLOR)
        win.blit(tekst, (WIDTH // 4 + self.text_offset, HEIGHT // 4 + 5 * self.space_height + 3 * self.button_height - font.get_height() // 2))
        win.blit(self.settings_button_icon, ( WIDTH // 4 + self.icon_offset, HEIGHT // 4 + 4 * self.space_height + 3 * self.button_height + self.icon_offset))
        # exit
        pygame.draw.rect(win, self.exit_button_color, (WIDTH // 4, HEIGHT // 4 + 5 * self.space_height + 4 * self.button_height, self.button_width, self.button_height))
        tekst = font.render("Exit", False, TEXT_COLOR)
        win.blit(tekst, (WIDTH // 4 + self.text_offset, HEIGHT // 4 + 6 * self.space_height + 4 * self.button_height - font.get_height() // 2))
        win.blit(self.exit_button_icon, (WIDTH // 4 + self.icon_offset, HEIGHT // 4 + 5 * self.space_height + 4 * self.button_height + self.icon_offset))

    def draw_result(self, win, result):
        pygame.draw.rect(win, BACKGROUND_COLOR, (0, 0, WIDTH, HEIGHT))
        if not pygame.font.get_init():
            pygame.font.init()
        font = pygame.font.Font("data/assets/arial1.ttf", 50)
        if result == RED:
            tekst = font.render("Czerwone wygraly", False, TEXT_COLOR)
        if result == WHITE:
            tekst = font.render("Biale wygraly", False, TEXT_COLOR)
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
