class DFSAlgorithm:
    """
    Implements the Depth-First Search (DFS) algorithm for pathfinding.

    Attributes:
        vehicle: The vehicle for which the algorithm is being executed.
    """

    def __init__(self, vehicle):
        """
        Initializes the DFSAlgorithm with the given vehicle.

        Args:
            vehicle: The vehicle object.
        """
        self.vehicle = vehicle

    def dfs(self, board):
        """
        Executes the DFS algorithm on the given board.

        Args:
            board: The board object containing the grid and its cells.

        Returns:
            A list of tuples representing the path found by the DFS algorithm.
        """
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
        start_cell.current_vehicle[self.vehicle.name] = self.vehicle.name
        stack = [start_cell]  # Initialize the stack with the starting cell

        while stack:
            current_cell = stack.pop()  # Get the next cell from the stack
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
                    # Mark the new cell as visited and set its parent
                    board.cells[new_y][new_x].visited[self.vehicle.name] = True
                    board.cells[new_y][new_x].parent[self.vehicle.name] = (
                        current_cell.y,
                        current_cell.x,
                    )
                    stack.append(
                        board.cells[new_y][new_x]
                    )  # Add the new cell to the stack

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

        return path  # Return the path found

    def execute(self, board):
        self.vehicle.tmp_start_y = self.vehicle.current_y
        self.vehicle.tmp_start_x = self.vehicle.current_x
        self.vehicle.tmp_goal_y = self.vehicle.goal_y
        self.vehicle.tmp_goal_x = self.vehicle.goal_x
        path = self.dfs(board)
        return board.path_time_fuel(self.vehicle.name, path)
