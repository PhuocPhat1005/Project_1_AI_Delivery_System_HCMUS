import heapq


class UCSAlgorithm:
    """
    Implements the Uniform Cost Search (UCS) algorithm for pathfinding.

    Attributes:
        vehicle: The vehicle for which the algorithm is being executed.
    """

    def __init__(self, vehicle):
        """
        Initializes the UCSAlgorithm with the given vehicle.

        Args:
            vehicle: The vehicle object.
        """
        self.vehicle = vehicle

    def ucs(self, board):
        """
        Executes the UCS algorithm on the given board.

        Args:
            board: The board object containing the grid and its cells.

        Returns:
            A list of tuples representing the path found by the UCS algorithm.
        """
        # Initialize board properties for the vehicle
        board.generate_visited(self.vehicle.name)
        board.generate_parent(self.vehicle.name)
        board.generate_cost(self.vehicle.name)
        board.generate_heuristic(self.vehicle.name)
        board.generate_fuel(self.vehicle.name)
        board.generate_time(self.vehicle.name)
        # Get the starting cell for the vehicle
        start_cell = board.cells[self.vehicle.tmp_start_y][self.vehicle.tmp_start_x]
        start_cell.visited[self.vehicle.name] = (
            True  # Mark the starting cell as visited
        )
        start_cell.cost[self.vehicle.name] = 0  # Initialize the starting cell cost
        start_cell.current_vehicle[self.vehicle.name] = self.vehicle.name
        frontier = [
            (0, start_cell)
        ]  # Initialize the frontier with the starting cell and its cost

        while frontier:
            _, current_cell = heapq.heappop(
                frontier
            )  # Get the cell with the lowest cost from the frontier
            if (
                current_cell.y == self.vehicle.tmp_goal_y
                and current_cell.x == self.vehicle.tmp_goal_x
            ):
                board.cells[self.vehicle.tmp_goal_y][self.vehicle.tmp_goal_x].visited[
                    self.vehicle.name
                ] = True
                break  # Exit if the goal cell is reached

            # Define possible movement directions (right, left, down, up)
            y = [0, 0, 1, -1]
            x = [1, -1, 0, 0]
            for i in range(4):
                new_y = current_cell.y + y[i]
                new_x = current_cell.x + x[i]
                if board.can_visit(self.vehicle.name, new_y, new_x):
                    new_cost = current_cell.cost[self.vehicle.name] + 1
                    if new_cost < board.cells[new_y][new_x].cost[self.vehicle.name]:
                        # Update cell properties if the new path is better
                        board.cells[new_y][new_x].current_vehicle = self.vehicle.name
                        board.cells[new_y][new_x].visited[self.vehicle.name] = True
                        board.cells[new_y][new_x].cost[self.vehicle.name] = new_cost
                        board.cells[new_y][new_x].parent[self.vehicle.name] = (
                            current_cell.y,
                            current_cell.x,
                        )
                        heapq.heappush(
                            frontier, (new_cost, board.cells[new_y][new_x])
                        )  # Add the new cell to the frontier with its cost

        path = []
        if (
            board.cells[self.vehicle.tmp_goal_y][self.vehicle.tmp_goal_x].visited[
                self.vehicle.name
            ]
            == True
        ):
            path = board.tracepath(self.vehicle.name)

        if (
            path == []
            or self.vehicle.tmp_goal_x != self.vehicle.goal_x
            and self.vehicle.tmp_goal_y != self.vehicle.goal_y
        ):
            board.cells[self.vehicle.goal_y][self.vehicle.goal_x].visited[
                self.vehicle.name
            ] = False

        return path

    def execute(self, board):
        self.vehicle.tmp_start_y = self.vehicle.current_y
        self.vehicle.tmp_start_x = self.vehicle.current_x
        self.vehicle.tmp_goal_y = self.vehicle.goal_y
        self.vehicle.tmp_goal_x = self.vehicle.goal_x
        path = self.ucs(board)
        return board.path_time_fuel(self.vehicle.name, path)
