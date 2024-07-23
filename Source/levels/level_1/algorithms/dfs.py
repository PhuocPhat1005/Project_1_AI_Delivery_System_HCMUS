class DFS:
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
        stack = [(self.start, [self.start])]
        visited = set([self.start])

        while stack:
            (x, y), path = stack.pop()

            if (x, y) == self.goal:
                return path

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny) and (nx, ny) not in visited:
                    stack.append(((nx, ny), path + [(nx, ny)]))
                    visited.add((nx, ny))

        return None
