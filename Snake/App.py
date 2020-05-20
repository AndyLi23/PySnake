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

    def update(self, pressed_keys):

        if pressed_keys[K_UP] and self.direction != "D":
            self.direction = "U"

        if pressed_keys[K_DOWN] and self.direction != "U":
            self.direction = "D"

        if pressed_keys[K_LEFT] and self.direction != "R":
            self.direction = "L"

        if pressed_keys[K_RIGHT] and self.direction != "L":
            self.direction = "R"

        if self.direction == "U":
            self.rect.move_ip(0, -20)

        elif self.direction == "D":
            self.rect.move_ip(0, 20)

        elif self.direction == "L":
            self.rect.move_ip(-20, 0)

        elif self.direction == "R":
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
            time.sleep(timeSleep)


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


running = True
player = Player()
apple = None
timeSleep = 0.1

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    if not apple:
        while True:
            apple = (randint(0, SCREEN_WIDTH//20-20)*20,
                     randint(0, SCREEN_HEIGHT//20-20)*20)
            if apple not in player.prev:
                break

    screen.fill((0, 0, 0))

    ap = pygame.Surface((20, 20))
    ap.fill((255, 0, 0))
    screen.blit(ap, (apple[0], apple[1]))

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.blit(player.surf, player.rect)
    for i in player.prev[:-1]:
        if player.rect.left == i[0] and player.rect.top == i[1]:
            running = False
        surf = pygame.Surface((20, 20))
        surf.fill((0, 255, 0))
        screen.blit(surf, (i[0], i[1]))

    if apple[0] == player.rect.left and apple[1] == player.rect.top:
        player.len += 5
        apple = None
        timeSleep -= 0.003

    pygame.display.flip()

pygame.quit()
