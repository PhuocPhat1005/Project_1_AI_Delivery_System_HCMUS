from collections import deque


class BFS:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] != -1

    def search(self):
        queue = deque([self.start])
        visited = set([self.start])
        parent = {self.start: None}

        while queue:
            x, y = queue.popleft()

            if (x, y) == self.goal:
                path = []
                while (x, y) is not None:
                    path.append((x, y))
                    x, y = parent[(x, y)]
                path.reverse()
                return path

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny) and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)

        return None
