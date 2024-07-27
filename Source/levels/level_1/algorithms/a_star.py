import heapq


class AStarAlgorithm:
    """
    Class representing the A* search algorithm.
    """

    def __init__(self, vehicle):
        """
        Initialize the A* algorithm with a vehicle.

        Args:
            vehicle (vehicle_base): The vehicle using the A* algorithm.
        """
        self.vehicle = vehicle

    def a_star(self, board):
        """
        Execute the A* search algorithm on the provided board.

        Args:
            board (object): The board on which the algorithm will be executed.

        Returns:
            list: The path with time and fuel information.
        """
        # Initialize board properties for the vehicle
        board.generate_visited(self.vehicle.name)
        board.generate_parent(self.vehicle.name)
        board.generate_cost(self.vehicle.name)
        board.generate_heuristic(self.vehicle.name)
        board.generate_fuel(self.vehicle.name)
        board.generate_time(self.vehicle.name)

        # Get the starting cell

        start_cell = board.cells[self.vehicle.tmp_start_y][self.vehicle.tmp_start_x]
        start_cell.visited[self.vehicle.name] = True  # Mark the start cell as visited
        start_cell.cost[self.vehicle.name] = (
            0  # Set the cost to reach the start cell to 0
        )
        start_cell.current_vehicle = (
            self.vehicle.name
        )  # Set the current vehicle in the start cell
        frontier = [
            (start_cell.heuristic[self.vehicle.name], start_cell)
        ]  # Initialize the priority queue with the start cell

        while frontier:
            _, current_cell = heapq.heappop(
                frontier
            )  # Pop the cell with the lowest total cost
            if (
                current_cell.y == self.vehicle.tmp_goal_y
                and current_cell.x == self.vehicle.tmp_goal_x
            ):  # Check if the goal is reached
                board.cells[self.vehicle.tmp_goal_y][self.vehicle.tmp_goal_x].visited[
                    self.vehicle.name
                ] = True
                break
            # Directions for moving in the grid (right, left, down, up)
            y = [0, 0, 1, -1]
            x = [1, -1, 0, 0]
            for i in range(4):
                new_y = current_cell.y + y[i]
                new_x = current_cell.x + x[i]

                if board.can_visit(
                    self.vehicle.name, new_y, new_x
                ):  # Check if the cell can be visited
                    new_cost = (
                        current_cell.cost[self.vehicle.name] + 1
                    )  # Calculate the new cost
                    if (
                        new_cost < board.cells[new_y][new_x].cost[self.vehicle.name]
                    ):  # Check if the new cost is lower
                        # Update the properties of the new cell
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
                        )  # Push the new cell into the priority queue

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
        path = self.a_star(board)
        return board.path_time_fuel(self.vehicle.name, path)
