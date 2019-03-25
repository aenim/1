# настройки игры
import pygame

class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.screen_size = self.screen_width, self.screen_width
        self.bg_color = (255,255,255)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_size = 80
        self.enemy_step_range = 80

    def draw_grid(self):
        for x in range(0, self.screen_width, 80):
            pygame.draw.line(self.screen, pygame.Color('black'), (x,0), (x, self.screen_height))

        for y in range(0, self.screen_height, 80):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.screen_width, y))
