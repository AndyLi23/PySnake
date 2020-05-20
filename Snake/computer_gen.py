import pygame
from pygame.locals import *
import time
from random import randint
from itertools import permutations


class Player(pygame.sprite.Sprite):

    def __init__(self):

        super(Player, self).__init__()

        self.surf = pygame.Surface((20, 20))

        self.surf.fill((0, 200, 0))
        self.direction = "R"

        self.rect = self.surf.get_rect()
        self.prev = []
        self.len = 1

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
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


class g:
    def generatePath(self, m, n):
        grid = []
        self.longest_path = None

        for i in range(n):
            grid.append([1]*m)

        def isValid(x, y):
            return (x < n and y < m and x >= 0 and y >= 0)

        def isSafe(visited, x, y):
            return not (grid[x][y] == 0 or (x, y) in visited)

        def findLongestPath(visited, i, j, x, y, dist, path):
            if grid[i][j] == 0:
                return False
            if i == x and j == y:
                path += [(i, j)]
                if dist == m*n-1:
                    self.longest_path = path
                    return True
            if not self.longest_path:
                visited.add((i, j))

                if isValid(i+1, j) and isSafe(visited, i+1, j):
                    findLongestPath(visited, i+1, j, x, y,
                                    dist+1, path+[(i, j)])

                if isValid(i-1, j) and isSafe(visited, i-1, j):
                    findLongestPath(visited, i-1, j, x, y,
                                    dist+1, path+[(i, j)])

                if isValid(i, j+1) and isSafe(visited, i, j+1):
                    findLongestPath(visited, i, j+1, x, y,
                                    dist+1, path+[(i, j)])

                if isValid(i, j-1) and isSafe(visited, i, j-1):
                    findLongestPath(visited, i, j-1, x, y,
                                    dist+1, path+[(i, j)])

                visited.remove((i, j))

        findLongestPath(set(), 0, 0, 0, m-1, 0, [])

        ans = []
        for i in range(len(self.longest_path)-1):
            if self.longest_path[i][0] > self.longest_path[i+1][0]:
                ans.append("U")
            elif self.longest_path[i][0] < self.longest_path[i+1][0]:
                ans.append("D")
            elif self.longest_path[i][1] > self.longest_path[i+1][1]:
                ans.append("L")
            elif self.longest_path[i][1] < self.longest_path[i+1][1]:
                ans.append("R")

        return ans+["R"]


def game():
    running = True
    player = Player()
    apple = None
    m = 4000
    score = 0

    G = g()
    path = G.generatePath(SCREEN_WIDTH//20, SCREEN_HEIGHT//20)
    cur = 0

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            elif event.type == QUIT:
                pygame.quit()

        if not apple:
            a = True
            for i in range(10000):
                apple = (randint(0, SCREEN_WIDTH//20-1)*20,
                         randint(0, SCREEN_HEIGHT//20-1)*20)
                if apple not in player.prev:
                    a = False
                    break
            if a:
                pygame.quit()

        screen.fill((0, 0, 0))

        player.direction = path[cur]
        cur = (cur+1) % len(path)
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
            player.len += 1
            apple = None
            m -= 20
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
