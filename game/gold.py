import pygame
import random

class Gold():

    def __init__(self, screen):
        # создаем игрока и указываем его начальную позицию

        self.screen = screen
        self.image = pygame.image.load('files/gold.bmp')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() # сохраняем экран

        self.rect.centerx = random.randint(0,400)     #self.screen_rect.centerx # координата Х центра игрока
        self.rect.bottom = random.randint(0,400)      #self.screen_rect.bottom   # координата У центра корабля


