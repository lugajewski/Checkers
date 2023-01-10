import pygame
from .constants import HEIGHT, WIDTH, SQUARE_SIZE, WHITE, RED, BROWN, BACKGROUND_COLOR, BUTTON_COLOR, \
    SELECTED_BUTTON_COLOR, TEXT_COLOR, LIGHT_SQUARES_COLOR1, LIGHT_SQUARES_COLOR2, LIGHT_SQUARES_COLOR3, LIGHT_SQUARES_COLOR4, \
    LIGHT_SQUARES_COLOR5, LIGHT_SQUARES_COLOR6, DARK_SQUARES_COLOR1, DARK_SQUARES_COLOR2, DARK_SQUARES_COLOR3, DARK_SQUARES_COLOR4, \
    DARK_SQUARES_COLOR5, DARK_SQUARES_COLOR6


class Settings:
    def __init__(self, win):
        self.win = win
        self.button_width = HEIGHT // 2
        self.space_height = (HEIGHT - HEIGHT // 4) / 16
        self.button_height = self.space_height * 2
        self.text_offset = self.button_height
        self.icon_offset = 5
        self.board_offset = 50
        self.square_size = SQUARE_SIZE
        self.button1_color = BUTTON_COLOR
        self.button2_color = BUTTON_COLOR
        self.text = WHITE
        self.navigator = 0
        self.light_pieces_color = RED
        self.dark_pieces_color = WHITE
        self.light_squares_color = LIGHT_SQUARES_COLOR1
        self.dark_squares_color = DARK_SQUARES_COLOR1
        self.pieces_settings_button_icon = pygame.transform.scale(pygame.image.load('data/assets/pieces_settings_button_icon.png'), (65, 65))
        self.board_settings_button_icon = pygame.transform.scale(pygame.image.load('data/assets/board_settings_button_icon.png'), (65, 65))

    def update(self):
        self.draw_settings_background(self.win)
        pos = pygame.mouse.get_pos()
        option = 0
        if self.navigator == 0 or self.navigator == 1:
            option = self.get_first_option_from_mouse(pos)
        elif self.navigator == 0:
            option = self.get_second_from_mouse(pos)
        if self.navigator == 0:
            self.draw_settings_options(self.win, option)
        elif self.navigator == 1:
            self.draw_pieces_settings_options(self.win, option)
        elif self.navigator == 2:
            self.draw_squares_settings_options(self.win, option)

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

        pygame.draw.rect(win, LIGHT_SQUARES_COLOR1, (self.board_offset, HEIGHT // 4 + self.board_offset, 2*self.square_size, 2*self.square_size))
        pygame.draw.rect(win, DARK_SQUARES_COLOR1, (self.board_offset + self.square_size, HEIGHT // 4 + self.board_offset, self.square_size, self.square_size))
        pygame.draw.rect(win, DARK_SQUARES_COLOR1, (self.board_offset, HEIGHT // 4 + self.board_offset + self.square_size, self.square_size, self.square_size))

        pygame.draw.rect(win, LIGHT_SQUARES_COLOR2, (2*self.board_offset + 2*self.square_size, HEIGHT // 4 + self.board_offset, 2 * self.square_size, 2 * self.square_size))
        pygame.draw.rect(win, DARK_SQUARES_COLOR2, (2*self.board_offset + 2*self.square_size + self.square_size, HEIGHT // 4 + self.board_offset, self.square_size, self.square_size))
        pygame.draw.rect(win, DARK_SQUARES_COLOR2, (2*self.board_offset + 2*self.square_size, HEIGHT // 4 + self.board_offset + self.square_size, self.square_size, self.square_size))

        pygame.draw.rect(win, LIGHT_SQUARES_COLOR3, (3 * self.board_offset + 4 * self.square_size, HEIGHT // 4 + self.board_offset, 2 * self.square_size, 2 * self.square_size))
        pygame.draw.rect(win, DARK_SQUARES_COLOR3, (3 * self.board_offset + 4 * self.square_size + self.square_size, HEIGHT // 4 + self.board_offset, self.square_size, self.square_size))
        pygame.draw.rect(win, DARK_SQUARES_COLOR3, (3 * self.board_offset + 4 * self.square_size, HEIGHT // 4 + self.board_offset + self.square_size, self.square_size, self.square_size))

        pygame.draw.rect(win, LIGHT_SQUARES_COLOR4, (self.board_offset, HEIGHT // 4 + 2*self.board_offset + 2* self.square_size, 2 * self.square_size, 2 * self.square_size))
        pygame.draw.rect(win, DARK_SQUARES_COLOR4, (self.board_offset + self.square_size, HEIGHT // 4 + 2*self.board_offset + 2* self.square_size, self.square_size, self.square_size))
        pygame.draw.rect(win, DARK_SQUARES_COLOR4, (self.board_offset, HEIGHT // 4 + 2*self.board_offset + 3*self.square_size, self.square_size, self.square_size))

        pygame.draw.rect(win, LIGHT_SQUARES_COLOR5, (2 * self.board_offset + 2 * self.square_size, HEIGHT // 4 + 2*self.board_offset + 2* self.square_size, 2 * self.square_size, 2 * self.square_size))
        pygame.draw.rect(win, DARK_SQUARES_COLOR5, (2 * self.board_offset + 2 * self.square_size + self.square_size, HEIGHT // 4 + 2*self.board_offset + 2* self.square_size, self.square_size, self.square_size))
        pygame.draw.rect(win, DARK_SQUARES_COLOR5, (2 * self.board_offset + 2 * self.square_size, HEIGHT // 4 + 2*self.board_offset + 3*self.square_size, self.square_size, self.square_size))

        pygame.draw.rect(win, LIGHT_SQUARES_COLOR6, (3 * self.board_offset + 4 * self.square_size, HEIGHT // 4 + 2 * self.board_offset + 2 * self.square_size, 2 * self.square_size, 2 * self.square_size))
        pygame.draw.rect(win, DARK_SQUARES_COLOR6, (3 * self.board_offset + 4 * self.square_size + self.square_size, HEIGHT // 4 + 2 * self.board_offset + 2 * self.square_size, self.square_size, self.square_size))
        pygame.draw.rect(win, DARK_SQUARES_COLOR6, (3 * self.board_offset + 4 * self.square_size, HEIGHT // 4 + 2 * self.board_offset + 3 * self.square_size, self.square_size, self.square_size))


    def get_second_option_from_mouse(self, pos):
        x, y = pos
        option = 1
        if self.board_offset < x < self.board_offset + 2*self.square_size:
            if HEIGHT // 4 + self.board_offset < y < HEIGHT // 4 + self.board_offset + 2*self.square_size:
                option = 1
            elif HEIGHT // 4 + 2*self.board_offset + 2*self.square_size < y < HEIGHT // 4 + 2*self.board_offset + 4*self.square_size:
                option = 4
        elif 2*self.board_offset + 2*self.square_size < x < 2*self.board_offset + 4*self.square_size:
            if HEIGHT // 4 + self.board_offset < y < HEIGHT // 4 + self.board_offset + 2 * self.square_size:
                option = 2
            elif HEIGHT // 4 + 2 * self.board_offset + 2 * self.square_size < y < HEIGHT // 4 + 2 * self.board_offset + 4 * self.square_size:
                option = 5
        elif 3*self.board_offset + 4*self.square_size < x < 3*self.board_offset + 6*self.square_size:
            if HEIGHT // 4 + self.board_offset < y < HEIGHT // 4 + self.board_offset + 2 * self.square_size:
                option = 3
            elif HEIGHT // 4 + 2 * self.board_offset + 2 * self.square_size < y < HEIGHT // 4 + 2 * self.board_offset + 4 * self.square_size:
                option = 6
        return option


    def get_first_option_from_mouse(self, pos):
        x, y = pos
        option = 0
        if HEIGHT // 4 + self.space_height < y < HEIGHT // 4 + self.space_height + self.button_height:
            option = 1
        elif HEIGHT//4 + 2 * self.space_height + self.button_height < y < HEIGHT//4 + 2 * self.space_height + self.button_height + self.button_height:
            option = 2
        return option

    def choose_options(self, option):
        if self.navigator == 0:
            if option == 1:
                self.navigator = option
            elif option == 2:
                self.navigator = option
        elif self.navigator == 1:
            if option == 1:
                self.light_pieces_color = RED
            elif option == 2:
                self.light_pieces_color = BROWN
        elif self.navigator == 2:
            if option == 1:
                self.light_squares_color = LIGHT_SQUARES_COLOR1
                self.dark_squares_color = DARK_SQUARES_COLOR1
            elif option == 2:
                self.light_squares_color = LIGHT_SQUARES_COLOR2
                self.dark_squares_color = DARK_SQUARES_COLOR2
            elif option == 3:
                self.light_squares_color = LIGHT_SQUARES_COLOR3
                self.dark_squares_color = DARK_SQUARES_COLOR3
            elif option == 4:
                self.light_squares_color = LIGHT_SQUARES_COLOR4
                self.dark_squares_color = DARK_SQUARES_COLOR4
            elif option == 5:
                self.light_squares_color = LIGHT_SQUARES_COLOR5
                self.dark_squares_color = DARK_SQUARES_COLOR5
            elif option == 6:
                self.light_squares_color = LIGHT_SQUARES_COLOR6
                self.dark_squares_color = DARK_SQUARES_COLOR6