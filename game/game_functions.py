import sys
import pygame
import random
import objects
import random


def check_events(player, enemy, enemy_2, enemy_3):

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

            

###################################################

            if 120 < enemy.rect.centerx < 750 and 120 < enemy.rect.bottom < 750:
                x = random.choice([0,1])
                if x == 0:
                    enemy.step = random.choice([-80,80])
                    enemy.centerx += enemy.step
                    enemy.rect.centerx = enemy.centerx

                elif x == 1:
                    enemy.step = random.choice([-80, 80])
                    enemy.bottom +=enemy.step
                    enemy.rect.bottom = enemy.bottom

            else:
                if enemy.rect.centerx <= 120:
                    enemy.rect.centerx += 80

                elif enemy.rect.centerx >= 750:
                    enemy.rect.centerx -= 80

                elif enemy.rect.bottom <= 120:
                    enemy.rect.bottom += 80

                elif enemy.rect.bottom >= 750:
                    enemy.rect.bottom -= 80
              ###

            if 120 < enemy_2.rect.centerx < 750 and 120 < enemy_2.rect.bottom < 750:
                x = random.choice([0, 1])
                if x == 0:
                    enemy_2.step = random.choice([-80, 80])
                    enemy_2.centerx += enemy_2.step
                    enemy_2.rect.centerx = enemy_2.centerx

                elif x == 1:
                    enemy_2.step = random.choice([-80, 80])
                    enemy_2.bottom += enemy_2.step
                    enemy_2.rect.bottom = enemy_2.bottom

            else:
                if enemy_2.rect.centerx <= 120:
                    enemy_2.rect.centerx += 80

                elif enemy_2.rect.centerx >= 750:
                    enemy_2.rect.centerx -= 80

                elif enemy_2.rect.bottom <= 120:
                    enemy_2.rect.bottom += 80

                elif enemy_2.rect.bottom >= 750:
                    enemy_2.rect.bottom -= 80

            ###

            if 120 < enemy_3.rect.centerx < 750 and 120 < enemy_3.rect.bottom < 750:
                x = random.choice([0, 1])
                if x == 0:
                    enemy_3.step = random.choice([-80, 80])
                    enemy_3.centerx += enemy_3.step
                    enemy_3.rect.centerx = enemy_3.centerx

                elif x == 1:
                    enemy_3.step = random.choice([-80, 80])
                    enemy_3.bottom += enemy_3.step
                    enemy_3.rect.bottom = enemy_3.bottom

            else:
                if enemy_3.rect.centerx <= 120:
                    enemy_3.rect.centerx += 80

                elif enemy_3.rect.centerx >= 750:
                    enemy_3.rect.centerx -= 80

                elif enemy_3.rect.bottom <= 120:
                    enemy_3.rect.bottom += 80

                elif enemy_3.rect.bottom >= 750:
                    enemy_3.rect.bottom -= 80


###################################################

def update_screen(ai_settings, screen, player, gold, gold_2, hole, hole_2, enemy, enemy_2, enemy_3):
    screen.fill(ai_settings.bg_color)
    player.blitme()
    gold.blitme()
    gold_2.blitme()
    hole_2.blitme()
    hole.blitme()
    enemy.blitme()
    enemy_2.blitme()
    enemy_3.blitme()
    #enemy.update() #   < -------------------------------------------------  двигает врага
    player.screen()
    pygame.display.flip()
