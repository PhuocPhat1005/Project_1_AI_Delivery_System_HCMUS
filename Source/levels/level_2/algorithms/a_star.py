import heapq


class AStarAlgorithm:
    def __init__(self, vehicle):
        """
        Initialize the A* algorithm with the given vehicle.

        Parameters:
        vehicle (vehicle_base): The vehicle for which the path is to be found.
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
        board.generate_visited(self.vehicle.name)
        board.generate_parent(self.vehicle.name)
        board.generate_cost(self.vehicle.name)
        board.generate_heuristic(self.vehicle.name)
        board.generate_fuel(self.vehicle.name)
        board.generate_time(self.vehicle.name)
        # Get the start cell based on the vehicle's start coordinates
        start_cell = board.cells[self.vehicle.start_y][self.vehicle.start_x]
        # Mark the start cell as vistited for the vehicle
        start_cell.visited[self.vehicle.name] = True
        # Initialize time for the start cell
        start_cell.time[self.vehicle.name] = 0
        start_cell.current_vehicle = self.vehicle.name

        # Initialize the priority queue (frontier) with the start cell and its heuristic value
        frontier = [(0 + self.heuristic(start_cell), start_cell)]
        heapq.heapify(frontier)  # Transform the list into a heap

        while frontier:
            # Pop the cell with the lowest f-score from the frontier
            _, current_cell = heapq.heappop(frontier)

            # If the goal is reached, break out of the loop
            if (
                self.check_goal_cell(current_cell)
                and current_cell.time[self.vehicle.name] <= self.vehicle.delivery_time
            ):
                return board.path_and_time(
                    self.vehicle.name, board.tracepath(self.vehicle.name)
                )

            for next_cell in self.get_neighbor(current_cell, board):
                # Calculate additional time if the next cell is a toll booth
                print(f"Cell: {(next_cell.y, next_cell.x)}")
                additional_time = self.time_to_move(next_cell, board)
                print("Additional time: ", additional_time)
                # Calculate the new cost to reach the next cell
                new_time = current_cell.time[self.vehicle.name] + additional_time
                print("New_time: ", new_time)

                # Only consider this path if it doesn't exceed the delivery time
                print(f"Delivery time: {self.vehicle.delivery_time}")
                if new_time <= self.vehicle.delivery_time and (
                    not next_cell.visited[self.vehicle.name]
                    or new_time < next_cell.time[self.vehicle.name]
                ):
                    # Update the cell details
                    next_cell.current_vehicle = self.vehicle.name
                    next_cell.time[self.vehicle.name] = new_time
                    next_cell.visited[self.vehicle.name] = True
                    next_cell.parent[self.vehicle.name] = (
                        current_cell.y,
                        current_cell.x,
                    )

                    # Add the cell to the frontier with its new f-score
                    heapq.heappush(
                        frontier,
                        (new_time + self.heuristic(next_cell), next_cell),
                    )
        return None

    def heuristic(self, cell):
        """
        Calculate the heuristic value for the given cell.

        Parameters:
        cell (Cell): The cell for which the heuristic is to be calculated.

        Returns:
        int: The heuristic value (Manhattan distance) for the cell.
        """
        return abs(cell.y - self.vehicle.goal_y) + abs(cell.x - self.vehicle.goal_x)

    def get_neighbor(self, current_cell, board):
        neighbors = []
        y = current_cell.y
        x = current_cell.x
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx
            if board.can_visit(self.vehicle.name, new_y, new_x):
                neighbors.append(board.cells[new_y][new_x])
        return neighbors

    def check_cell_is_toll_booth(self, current_cell, board):
        next_cell = board.cells[current_cell.y][current_cell.x]
        if isinstance(next_cell.value, int) and next_cell.value > 0:
            return True
        return False

    def time_to_move(self, next_cell, board):
        base_time = 1  # this is 1 minute for current_cell to move to the next_cell, which is adjacent cell
        if self.check_cell_is_toll_booth(next_cell, board):
            base_time += self.wait_time_for_tolll_booth(next_cell, board)
        print("base_time", base_time)
        return base_time

    def wait_time_for_tolll_booth(self, current_cell, board):
        return current_cell.value

    def check_goal_cell(self, current_cell):
        if (current_cell.y == self.vehicle.goal_y) and (
            current_cell.x == self.vehicle.goal_x
        ):
            return True
        return False
