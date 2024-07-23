import heapq


class UCS:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.n = len(grid)
        self.m = len(grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m and self.grid[x][y] != -1

    def search(self):
        pq = [(0, self.start)]
        parent = {self.start: None}
        cost = {self.start: 0}
        found = False

        while pq:
            current_cost, (x, y) = heapq.heappop(pq)

            if (x, y) == self.goal:
                found = True
                break

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy

                if self.is_valid(nx, ny):
                    new_cost = current_cost + 1
                    if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                        cost[(nx, ny)] = new_cost
                        heapq.heappush(pq, (new_cost, (nx, ny)))
                        parent[(nx, ny)] = (x, y)

        if not found:
            return None

        path = []
        step = self.goal
        while step is not None:
            path.append(step)
            step = parent.get(step)

        path.reverse()
        return path
