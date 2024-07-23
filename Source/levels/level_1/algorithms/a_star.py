from queue import PriorityQueue


class AStar:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def search(self):
        open_set = PriorityQueue()
        open_set.put((0, self.start))
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.goal)}

        while not open_set.empty():
            _, current = open_set.get()

            if current == self.goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
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
                    if self.grid[neighbor[0]][neighbor[1]] != -1:
                        tentative_g_score = g_score[current] + 1

                        if (
                            neighbor not in g_score
                            or tentative_g_score < g_score[neighbor]
                        ):
                            came_from[neighbor] = current
                            g_score[neighbor] = tentative_g_score
                            f_score[neighbor] = tentative_g_score + self.heuristic(
                                neighbor, self.goal
                            )
                            open_set.put((f_score[neighbor], neighbor))

        return None
