from _thread import *
import pygame
import random
import time

class Ads:
    def __init__(self, win):
        self.ad1 = pygame.transform.scale(pygame.image.load('data/assets/ad1.png'), (800, 800))
        self.ad2 = pygame.transform.scale(pygame.image.load('data/assets/ad2.png'), (800, 800))
        self.ad3 = pygame.transform.scale(pygame.image.load('data/assets/ad3.png'), (800, 800))
        self.ad4 = pygame.transform.scale(pygame.image.load('data/assets/ad4.png'), (800, 800))
        self.ad5 = pygame.transform.scale(pygame.image.load('data/assets/ad5.png'), (800, 800))
        self.status = True
        self.win = win

    def show_ads(self):
        while True:
            self.status = True
            ad = random.randint(1, 5)
            if ad == 1:
                self.win.blit(self.ad1, (0, 0))
            if ad == 2:
                self.win.blit(self.ad2, (0, 0))
            if ad == 3:
                self.win.blit(self.ad3, (0, 0))
            if ad == 4:
                self.win.blit(self.ad4, (0, 0))
            if ad == 5:
                self.win.blit(self.ad5, (0, 0))
            pygame.display.update()
            pygame.time.wait(3000)
            self.status = False
            time.sleep(120)

    def start_ads(self):
        start_new_thread(self.show_ads, ())
