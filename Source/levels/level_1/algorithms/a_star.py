import heapq


class AStarAlgorithm:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def execute(self, board):
        board.generate_visited(self.vehicle.name)
        board.generate_parent(self.vehicle.name)
        board.generate_cost(self.vehicle.name)
        board.generate_heuristic(self.vehicle.name)
        board.generate_fuel(self.vehicle.name)
        board.generate_time(self.vehicle.name)

        start_cell = board.cells[self.vehicle.start_y][self.vehicle.start_x]
        start_cell.visited[self.vehicle.name] = True
        start_cell.cost[self.vehicle.name] = 0
        start_cell.current_vehicle = self.vehicle.name
        frontier = [(start_cell.heuristic[self.vehicle.name], start_cell)]

        while frontier:
            _, current_cell = heapq.heappop(frontier)

            y = [0, 0, 1, -1]
            x = [1, -1, 0, 0]
            for i in range(4):
                new_y = current_cell.y + y[i]
                new_x = current_cell.x + x[i]

                if board.can_visit(self.vehicle.name, new_y, new_x):
                    new_cost = current_cell.cost[self.vehicle.name] + 1
                    if new_cost < board.cells[new_y][new_x].cost[self.vehicle.name]:
                        board.cells[new_y][new_x].current_vehicle = self.vehicle.name
                        board.cells[new_y][new_x].visited[self.vehicle.name] = True
                        board.cells[new_y][new_x].cost[self.vehicle.name] = new_cost
                        board.cells[new_y][new_x].parent[self.vehicle.name] = (
                            current_cell.y,
                            current_cell.x,
                        )
                        total_cost = (
                            new_cost
                            + board.cells[new_y][new_x].heuristic[self.vehicle.name]
                        )
                        heapq.heappush(
                            frontier, (total_cost, board.cells[new_y][new_x])
                        )
            if (
                current_cell.y == self.vehicle.goal_y
                and current_cell.x == self.vehicle.goal_x
            ):
                break

        return board.path_time_fuel(
            self.vehicle.name, board.tracepath(self.vehicle.name)
        )
