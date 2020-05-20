from random import randint
from functools import lru_cache
from itertools import permutations


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
                r = [0, 1, 2, 3]
                p = list(permutations(r))
                p = p[randint(0, len(p)-1)]

                visited.add((i, j))
                if p[0] == 0:
                    if isValid(i+1, j) and isSafe(visited, i+1, j):
                        findLongestPath(visited, i+1, j, x, y,
                                        dist+1, path+[(i, j)])
                if p[0] == 1:
                    if isValid(i-1, j) and isSafe(visited, i-1, j):
                        findLongestPath(visited, i-1, j, x, y,
                                        dist+1, path+[(i, j)])
                if p[0] == 2:
                    if isValid(i, j+1) and isSafe(visited, i, j+1):
                        findLongestPath(visited, i, j+1, x, y,
                                        dist+1, path+[(i, j)])
                if p[0] == 3:
                    if isValid(i, j-1) and isSafe(visited, i, j-1):
                        findLongestPath(visited, i, j-1, x, y,
                                        dist+1, path+[(i, j)])
                if p[1] == 0:
                    if isValid(i+1, j) and isSafe(visited, i+1, j):
                        findLongestPath(visited, i+1, j, x, y,
                                        dist+1, path+[(i, j)])
                if p[1] == 1:
                    if isValid(i-1, j) and isSafe(visited, i-1, j):
                        findLongestPath(visited, i-1, j, x, y,
                                        dist+1, path+[(i, j)])
                if p[1] == 2:
                    if isValid(i, j+1) and isSafe(visited, i, j+1):
                        findLongestPath(visited, i, j+1, x, y,
                                        dist+1, path+[(i, j)])
                if p[1] == 3:
                    if isValid(i, j-1) and isSafe(visited, i, j-1):
                        findLongestPath(visited, i, j-1, x, y,
                                        dist+1, path+[(i, j)])
                if p[2] == 0:
                    if isValid(i+1, j) and isSafe(visited, i+1, j):
                        findLongestPath(visited, i+1, j, x, y,
                                        dist+1, path+[(i, j)])
                if p[2] == 1:
                    if isValid(i-1, j) and isSafe(visited, i-1, j):
                        findLongestPath(visited, i-1, j, x, y,
                                        dist+1, path+[(i, j)])
                if p[2] == 2:
                    if isValid(i, j+1) and isSafe(visited, i, j+1):
                        findLongestPath(visited, i, j+1, x, y,
                                        dist+1, path+[(i, j)])
                if p[2] == 3:
                    if isValid(i, j-1) and isSafe(visited, i, j-1):
                        findLongestPath(visited, i, j-1, x, y,
                                        dist+1, path+[(i, j)])
                if p[3] == 0:
                    if isValid(i+1, j) and isSafe(visited, i+1, j):
                        findLongestPath(visited, i+1, j, x, y,
                                        dist+1, path+[(i, j)])
                if p[3] == 1:
                    if isValid(i-1, j) and isSafe(visited, i-1, j):
                        findLongestPath(visited, i-1, j, x, y,
                                        dist+1, path+[(i, j)])
                if p[3] == 2:
                    if isValid(i, j+1) and isSafe(visited, i, j+1):
                        findLongestPath(visited, i, j+1, x, y,
                                        dist+1, path+[(i, j)])
                if p[3] == 3:
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


G = g()
print(G.generatePath(10, 10))
