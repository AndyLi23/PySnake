import pygame
from pygame.locals import *
import time
from random import randint


class Player(pygame.sprite.Sprite):

    def __init__(self):

        super(Player, self).__init__()

        self.surf = pygame.Surface((20, 20))

        self.surf.fill((0, 200, 0))
        self.direction = "R"

        self.rect = self.surf.get_rect()
        self.prev = []
        self.len = 5

    def update(self):
        if self.direction == "U":
            self.rect.move_ip(0, -20)

        if self.direction == "D":
            self.rect.move_ip(0, 20)

        if self.direction == "L":
            self.rect.move_ip(-20, 0)

        if self.direction == "R":
            self.rect.move_ip(20, 0)

        if self.rect.left < 0:
            self.rect.left = SCREEN_WIDTH-20

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = 20

        if self.rect.top < 0:
            self.rect.top = SCREEN_HEIGHT-20

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = 20

        if not self.prev or self.prev[-1] != (self.rect.left, self.rect.top):
            if len(self.prev) > self.len:
                self.prev.pop(0)
            self.prev.append((self.rect.left, self.rect.top))


pygame.init()
pygame.display.set_caption('PySnake')
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


def game():
    running = True
    player = Player()
    apple = None
    cnt = 0
    m = 400
    score = 0

    while running:
        cnt = (cnt+1) % max(200, m)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            elif event.type == QUIT:
                pygame.quit()

        if not apple:
            for i in range(10000):
                apple = (randint(0, SCREEN_WIDTH//20-1)*20,
                         randint(0, SCREEN_HEIGHT//20-1)*20)
                if apple not in player.prev:
                    break

        screen.fill((0, 0, 0))

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            player.direction = "U"

        if pressed_keys[K_DOWN]:
            player.direction = "D"

        if pressed_keys[K_LEFT]:
            player.direction = "L"

        if pressed_keys[K_RIGHT]:
            player.direction = "R"

        if cnt == 0:
            player.update()
            ap = pygame.Surface((20, 20))
            ap.fill((255, 0, 0))
            screen.blit(ap, (apple[0], apple[1]))

            screen.blit(player.surf, player.rect)
            for i in player.prev[:-1]:
                if player.rect.left == i[0] and player.rect.top == i[1]:
                    running = False
                surf = pygame.Surface((20, 20))
                surf.fill((0, 255, 0))
                screen.blit(surf, (i[0], i[1]))

            if apple[0] == player.rect.left and apple[1] == player.rect.top:
                player.len += 3
                apple = None
                m -= 5
                score += 1

            largeText = pygame.font.Font('freesansbold.ttf', 20)
            TextSurf, TextRect = text_objects(str(score), largeText)
            TextRect.center = (10, 10)
            screen.blit(TextSurf, TextRect)

            pygame.display.flip()

    return False


while True:
    while game() != False:
        pass
