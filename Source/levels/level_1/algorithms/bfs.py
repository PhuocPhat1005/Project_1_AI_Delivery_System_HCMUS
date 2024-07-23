from collections import deque


class BFS:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])

    def search(self):
        queue = deque([self.start])
        parent = {self.start: None}
        visited = set()
        visited.add(self.start)

        while queue:
            current = queue.popleft()

            if current == self.goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return path

            neighbors = [
                (current[0] + 1, current[1]),
                (current[0] - 1, current[1]),
                (current[0], current[1] + 1),
                (current[0], current[1] - 1),
            ]
            for neighbor in neighbors:
                if 0 <= neighbor[0] < self.rows and 0 <= neighbor[1] < self.cols:
                    if (
                        self.grid[neighbor[0]][neighbor[1]] != -1
                        and neighbor not in visited
                    ):
                        queue.append(neighbor)
                        parent[neighbor] = current
                        visited.add(neighbor)

        return None
