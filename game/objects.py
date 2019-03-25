import pygame
import random
from settings import Settings
import game_functions

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

        self.rect.centerx = random.randrange(40,760,80)   # рандомные координаты загрузки врага
        self.rect.bottom = random.randrange(80,760,80)    #
        self.centerx = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)


    def update(self):

                    if 40 < self.rect.centerx < 760 and 40 < self.rect.bottom < 760:
                        x = random.choice([0,1])
                        if x == 0:
                            self.step = random.choice([-80, 80])
                            self.centerx += self.step
                            self.rect.centerx = self.centerx


                        elif x == 1:
                            self.step = random.choice([-80, 80])
                            self.bottom += self.step
                            self.rect.bottom = self.bottom

                    else:
                        if self.rect.centerx <= 120:
                            self.rect.centerx += 80

                        elif self.rect.centerx >= 750:
                            self.rect.centerx -= 80

                        elif self.rect.bottom <= 120:
                            self.rect.bottom += 80

                        elif self.rect.bottom >= 750:
                            self.rect.bottom -= 80


    def blitme(self):
        self.screen.blit(self.image, self.rect)
