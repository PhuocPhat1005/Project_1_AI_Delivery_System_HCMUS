import heapq


class AStarAlgorithm:
    def __init__(self, vehicle):
        """
        Initialize the A* algorithm with the given vehicle.

        Parameters:
        vehicle (VehicleBase): The vehicle for which the path is to be found.
        """
        self.vehicle = vehicle

    def execute(self, board):
        """
        Execute the A* algorithm to find the shortest path from the start position to the goal position.

        Parameters:
        board (Board): The board representing the map.

        Returns:
        list: The path from the start position to the goal position as a list of coordinates.
        """
        start_cell = board.cells[self.vehicle.start_y][self.vehicle.start_x]
        start_cell.visited[self.vehicle.name] = True
        start_cell.cost[self.vehicle.name] = 0
        start_cell.time[self.vehicle.name] = 0

        # Priority queue to store the frontier cells, initialized with the start cell
        frontier = [(0 + self.heuristic(start_cell), start_cell)]
        heapq.heapify(frontier)

        while frontier:
            # Get the cell with the lowest f-score from the frontier
            current_f, current_cell = heapq.heappop(frontier)

            # If the goal is reached, break out of the loop
            if (
                current_cell.y == self.vehicle.goal_y
                and current_cell.x == self.vehicle.goal_x
            ):
                break

            # Check all adjacent cells
            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_y, new_x = current_cell.y + dy, current_cell.x + dx

                if board.can_visit(self.vehicle.name, new_y, new_x):
                    next_cell = board.cells[new_y][new_x]
                    additional_time = (
                        next_cell.value if isinstance(next_cell.value, int) else 0
                    )
                    new_cost = current_cell.cost[self.vehicle.name] + 1
                    new_time = (
                        current_cell.time[self.vehicle.name] + 1 + additional_time
                    )

                    # Only consider this path if it doesn't exceed the delivery time
                    if new_time <= self.vehicle.delivery_time:
                        if (
                            new_cost < next_cell.cost[self.vehicle.name]
                            or not next_cell.visited[self.vehicle.name]
                        ):
                            next_cell.current_vehicle = self.vehicle.name
                            next_cell.cost[self.vehicle.name] = new_cost
                            next_cell.time[self.vehicle.name] = new_time
                            next_cell.visited[self.vehicle.name] = True
                            next_cell.parent[self.vehicle.name] = (
                                current_cell.y,
                                current_cell.x,
                            )

                            # Add the cell to the frontier with its new f-score
                            heapq.heappush(
                                frontier,
                                (new_cost + self.heuristic(next_cell), next_cell),
                            )

        # Trace and return the path from the start to the goal
        return board.tracepath(self.vehicle.name)

    def heuristic(self, cell):
        """
        Calculate the heuristic value for the given cell.

        Parameters:
        cell (Cell): The cell for which the heuristic is to be calculated.

        Returns:
        int: The heuristic value (Manhattan distance) for the cell.
        """
        return abs(cell.y - self.vehicle.goal_y) + abs(cell.x - self.vehicle.goal_x)
