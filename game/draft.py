import random


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

    def update(self):

        if 120 < self.rect.centerx < 750 and 120 < self.rect.bottom < 750:
            x = random.choice([0, 1])
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