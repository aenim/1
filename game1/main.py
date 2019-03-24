import pygame
import sys
from settings import Settings
from player import Player, Gold, Hole, Enemy
import game_functions as gf
from pygame.sprite import Group

def run_game():

    # инициализирует игру и создает объект экрана
    pygame.init() # инициализация настроек необходимых pygame для нормальной работы
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # создание отображаемой области инры с указанием размера экрана
    pygame.display.set_caption('iosskills')
    bg_color = (ai_settings.bg_color)
    player = Player(screen)
    gold = Gold(screen)
    hole = Hole(screen)
    enemy = Enemy(screen)
    # запуск основного цикла игры
    while True:
        gf.check_events(player)
        gf.update_screen(ai_settings,screen,player, gold, hole, enemy)
        ai_settings.draw_grid()

        '''
        for event in pygame.event.get(): # отслеживание событий выполняемых игроком
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(bg_color) # заливка экрана фоновым цветом
        player.blitme()
        pygame.display.flip() # обновление экрана
        '''

run_game()