import heapq


class AStarAlgorithm:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def heuristic(self, current_y, current_x, goal_y, goal_x):
        return abs(current_y - goal_y) + abs(current_x - goal_x)

    def execute(self, board):
        board.generate_visited(self.vehicle.name)
        board.generate_parent(self.vehicle.name)
        board.generate_cost(self.vehicle.name)
        board.generate_heuristic(self.vehicle.name)
        board.generate_fuel(self.vehicle.name)
        board.generate_time(self.vehicle.name)

        start_cell = board.cells[self.vehicle.start_y][self.vehicle.start_x]
        goal_cell = board.cells[self.vehicle.goal_y][self.vehicle.goal_x]

        # Initialize cell properties
        for row in board.cells:
            for cell in row:
                cell.visited = {}
                cell.parent = {}
                cell.cost = {}
                cell.time = {}
                cell.fuel = {}
                cell.heuristic = {}

        # Set start cell properties
        start_cell.visited[self.vehicle.name] = False
        start_cell.cost[self.vehicle.name] = 0
        start_cell.time[self.vehicle.name] = self.vehicle.delivery_time
        start_cell.fuel[self.vehicle.name] = self.vehicle.fuel
        start_cell.parent[self.vehicle.name] = None
        start_cell.heuristic[self.vehicle.name] = self.heuristic(
            self.vehicle.start_y,
            self.vehicle.start_x,
            self.vehicle.goal_y,
            self.vehicle.goal_x,
        )

        frontier = [
            (
                start_cell.cost[self.vehicle.name]
                + start_cell.heuristic[self.vehicle.name],
                start_cell,
            )
        ]
        heapq.heapify(frontier)

        while frontier:
            current_f, current_cell = heapq.heappop(frontier)
            current_y, current_x = current_cell.y, current_cell.x

            if current_y == self.vehicle.goal_y and current_x == self.vehicle.goal_x:
                break

            # Explore neighbors
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_y, new_x = current_y + dy, current_x + dx

                if board.can_visit(self.vehicle.name, new_y, new_x):
                    neighbor_cell = board.cells[new_y][new_x]
                    new_cost = current_cell.cost[self.vehicle.name] + 1
                    new_time = (
                        current_cell.time[self.vehicle.name] + 1 + neighbor_cell.value
                    )
                    new_fuel = current_cell.fuel[self.vehicle.name] - 1

                    if new_time <= self.vehicle.delivery_time and (
                        neighbor_cell.visited.get(self.vehicle.name) is False
                        or new_cost
                        < neighbor_cell.cost.get(self.vehicle.name, float("inf"))
                    ):
                        neighbor_cell.current_vehicle = self.vehicle.name
                        neighbor_cell.visited[self.vehicle.name] = True
                        neighbor_cell.cost[self.vehicle.name] = new_cost
                        neighbor_cell.time[self.vehicle.name] = new_time
                        neighbor_cell.fuel[self.vehicle.name] = new_fuel
                        neighbor_cell.parent[self.vehicle.name] = (current_y, current_x)
                        f = new_cost + self.heuristic(
                            new_y, new_x, self.vehicle.goal_y, self.vehicle.goal_x
                        )
                        heapq.heappush(frontier, (f, neighbor_cell))

        return board.tracepath(self.vehicle.name)
