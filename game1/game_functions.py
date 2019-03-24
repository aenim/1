import sys
import pygame
import player
from pygame.sprite import  Group


def check_events(player):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if player.rect.centerx < 760:
                    player.rect.centerx += 80
                else:
                    pass
            elif event.key == pygame.K_LEFT:
                if player.rect.centerx > 40 :
                    player.rect.centerx -= 80
                else:
                    pass
            elif event.key == pygame.K_UP:
                if player.rect.bottom > 80 :
                    player.rect.bottom -= 80
                else:
                    pass

            elif event.key == pygame.K_DOWN:
                if player.rect.bottom < 760 :
                    player.rect.bottom += 80
                else:
                    pass


def update_screen(ai_settings, screen, player, gold, hole, enemy):
    screen.fill(ai_settings.bg_color)
    player.blitme()
    gold.blitme()
    hole.blitme()
    enemy.blitme()
    pygame.display.flip()