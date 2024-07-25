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

    def execute(self, board):
        """
        Executes the DFS algorithm on the given board.

        Args:
            board: The board object containing the grid and its cells.

        Returns:
            A list of tuples representing the path found by the DFS algorithm.
        """
        # Get the starting cell for the vehicle
        start_cell = board.cells[self.vehicle.start_y][self.vehicle.start_x]
        start_cell.visited[self.vehicle.name] = (
            True  # Mark the starting cell as visited
        )
        stack = [start_cell]  # Initialize the stack with the starting cell

        while stack:
            current_cell = stack.pop()  # Get the next cell from the stack
            if (
                current_cell.y == self.vehicle.goal_y
                and current_cell.x == self.vehicle.goal_x
            ):
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

        return board.path_time_fuel(
            self.vehicle.name, board.tracepath(self.vehicle.name)
        )  # Return the path found
