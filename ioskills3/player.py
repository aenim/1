import pygame
import random
from settings import Settings

class Player():

    def __init__(self, screen):
        # создаем игрока и указываем его начальную позицию

        self.screen = screen
        self.image = pygame.image.load('files/doomguy_4.bmp')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() # сохраняем экран

        # место появлениы корабля

        self.rect.centerx = 440     #self.screen_rect.centerx # координата Х центра игрока
        self.rect.bottom = 400      #self.screen_rect.bottom   # координата У центра игрока


    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Gold():

    def __init__(self, screen):


        self.screen = screen
        self.image = pygame.image.load('files/gold.bmp')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() # сохраняем экран

        self.rect.centerx = random.randrange(40,760,80)   # рандомные координаты загрузки золота
        self.rect.bottom = random.randrange(80,760,80)    #

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Hole():

    def __init__(self, screen):


        self.screen = screen
        self.image = pygame.image.load('files/hole.bmp')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() # сохраняем экран

        self.rect.centerx = random.randrange(40,760,80)   # рандомные координаты загрузки дырки
        self.rect.bottom = random.randrange(80,760,80)    #

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Enemy():
    def __init__(self, screen):


        self.screen = screen
        self.image = pygame.image.load('files/cacodemon.bmp')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() # сохраняем экран

        self.rect.centerx = random.randrange(40,760,80)   # рандомные координаты загрузки дырки
        self.rect.bottom = random.randrange(80,760,80)    #



    def blitme(self):
        self.screen.blit(self.image, self.rect)