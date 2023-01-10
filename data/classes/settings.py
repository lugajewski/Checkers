import pygame
from .constants import HEIGHT, WIDTH, BLACK, WHITE, RED, BLUE, GREY, BROWN, BACKGROUND_COLOR, BUTTON_COLOR, SELECTED_BUTTON_COLOR, TEXT_COLOR


class Settings:
    def __init__(self):
        self.button_width = HEIGHT // 2
        self.space_height = (HEIGHT - HEIGHT // 4) / 16
        self.button_height = self.space_height * 2
        self.text_offset = self.button_height
        self.icon_offset = 5
        self.button1_color = BUTTON_COLOR
        self.button2_color = BUTTON_COLOR
        self.text = WHITE
        self.navigator = 0
        self.pieces_color = RED
        self.squares_color = RED
        self.pieces_settings_button_icon = pygame.transform.scale(pygame.image.load('data/assets/pieces_settings_button_icon.png'), (65, 65))
        self.board_settings_button_icon = pygame.transform.scale(pygame.image.load('data/assets/board_settings_button_icon.png'), (65, 65))

    def update(self, win):
        self.draw_settings_background(win)
        pos = pygame.mouse.get_pos()
        option = self.get_option_from_mouse(pos)
        if self.navigator == 0:
            self.draw_settings_options(win, option)
        elif self.navigator == 1:
            self.draw_pieces_settings_options(win, option)
        elif self.navigator == 2:
            self.draw_squares_settings_options(win, option)

    def set_button_colors(self, option):
        if option == 1:
            self.button1_color = SELECTED_BUTTON_COLOR
        elif option == 2:
            self.button2_color = SELECTED_BUTTON_COLOR
        else:
            self.button1_color = BUTTON_COLOR
            self.button2_color = BUTTON_COLOR

    def draw_settings_background(self, win):
        pygame.draw.rect(win, BACKGROUND_COLOR, (0, 0, WIDTH, HEIGHT))

    def draw_settings_options(self, win, option):
        if not pygame.font.get_init():
            pygame.font.init()

        self.set_button_colors(option)

        font = pygame.font.Font("data/assets/broadway.ttf", 90)
        # header
        tekst = font.render("SUPER", False, TEXT_COLOR)
        win.blit(tekst, (243.35, font.get_height() // 2))
        tekst = font.render("SETTINGS", False, TEXT_COLOR)
        win.blit(tekst, (170.6, font.get_height() + font.get_height() // 2))

        font = pygame.font.Font("data/assets/broadway.ttf", 40)
        # pieces settings button
        pygame.draw.rect(win, self.button1_color, (WIDTH // 4, HEIGHT // 4 + self.space_height, self.button_width, self.button_height))
        tekst = font.render("Pieces settings", False, TEXT_COLOR)
        win.blit(tekst, (WIDTH //4 + self.text_offset, HEIGHT // 4 + 2 * self.space_height - font.get_height() // 2))
        win.blit(self.pieces_settings_button_icon, (WIDTH // 4 + self.icon_offset, HEIGHT // 4 + self.space_height + self.icon_offset))
        # board settings button
        pygame.draw.rect(win, self.button2_color, (WIDTH//4, HEIGHT//4 + 2 * self.space_height + self.button_height, self.button_width, self.button_height))
        tekst = font.render("Board settings", False, TEXT_COLOR)
        win.blit(tekst, (WIDTH // 4 + self.text_offset, HEIGHT // 4 + 3 * self.space_height + self.button_height - font.get_height() // 2))
        win.blit(self.board_settings_button_icon, (WIDTH // 4 + self.icon_offset, HEIGHT // 4 + 2 * self.space_height + self.button_height + self.icon_offset))

    def draw_pieces_settings_options(self, win, option):
        if not pygame.font.get_init():
            pygame.font.init()

        self.set_button_colors(option)

        font = pygame.font.Font("data/assets/broadway.ttf", 90)
        # header
        tekst = font.render("SUPER", False, TEXT_COLOR)
        win.blit(tekst, (243.35, font.get_height() // 2))
        tekst = font.render("SETTINGS", False, TEXT_COLOR)
        win.blit(tekst, (170.6, font.get_height() + font.get_height() // 2))

        font = pygame.font.Font("data/assets/broadway.ttf", 40)
        # red and white pieces
        pygame.draw.rect(win, self.button1_color, (WIDTH // 4, HEIGHT // 4 + self.space_height, self.button_width, self.button_height))
        tekst = font.render("Red and white pieces", False, TEXT_COLOR)
        win.blit(tekst, (WIDTH // 4 + self.text_offset, HEIGHT // 4 + 2 * self.space_height - font.get_height() // 2))

        # brown and white pieces
        pygame.draw.rect(win, self.button2_color, (WIDTH // 4, HEIGHT // 4 + 2 * self.space_height + self.button_height, self.button_width, self.button_height))
        tekst = font.render("Brown and white pieces", False, TEXT_COLOR)
        win.blit(tekst, (WIDTH // 4 + self.text_offset, HEIGHT // 4 + 3 * self.space_height + self.button_height - font.get_height() // 2))

    def draw_squares_settings_options(self, win, option):
        if not pygame.font.get_init():
            pygame.font.init()

        self.set_button_colors(option)

        font = pygame.font.Font("data/assets/broadway.ttf", 90)
        # header
        tekst = font.render("SUPER", False, TEXT_COLOR)
        win.blit(tekst, (243.35, font.get_height() // 2))
        tekst = font.render("SETTINGS", False, TEXT_COLOR)
        win.blit(tekst, (170.6, font.get_height() + font.get_height() // 2))

        font = pygame.font.Font("data/assets/broadway.ttf", 40)
        # red and black squares
        pygame.draw.rect(win, self.button1_color, (WIDTH // 4, HEIGHT // 4 + self.space_height, self.button_width, self.button_height))
        tekst = font.render("Red and black squares", False, TEXT_COLOR)
        win.blit(tekst, (WIDTH // 4 + self.text_offset, HEIGHT // 4 + 2 * self.space_height - font.get_height() // 2))

        # brown and black squares
        pygame.draw.rect(win, self.button2_color, (WIDTH // 4, HEIGHT // 4 + 2 * self.space_height + self.button_height, self.button_width, self.button_height))
        tekst = font.render("Brown and black squares", False, TEXT_COLOR)
        win.blit(tekst, (WIDTH // 4 + self.text_offset, HEIGHT // 4 + 3 * self.space_height + self.button_height - font.get_height() // 2))

    def get_option_from_mouse(self, pos):
        x, y = pos
        option = 0
        if HEIGHT // 4 + self.space_height < y < HEIGHT // 4 + self.space_height + self.button_height:
            option = 1
        elif HEIGHT//4 + 2 * self.space_height + self.button_height < y < HEIGHT//4 + 2 * self.space_height + self.button_height + self.button_height:
            option = 2
        return option

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