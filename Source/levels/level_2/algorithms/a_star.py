import heapq


class AStarAlgorithm:
    def __init__(self, vehicle):
        """
        Initialize the A* algorithm with the given vehicle.

        Parameters:
        vehicle (vehicle_base): The vehicle for which the path is to be found.
        """
        self.vehicle = vehicle

    def a_star_execution(self, board):
        """
        Execute the A* algorithm to find the shortest path from the start position to the goal position.

        Parameters:
        board (Board): The board representing the map.

        Returns:
        list: The path from the start position to the goal position as a list of coordinates.
        """
        print("a_star")
        print("Start: ", self.vehicle.tmp_start_y, self.vehicle.tmp_start_x)
        print("Goal: ", self.vehicle.tmp_goal_y, self.vehicle.tmp_goal_x)
        board.generate_visited(self.vehicle.name)
        board.generate_parent(self.vehicle.name)
        board.generate_cost(self.vehicle.name)
        board.generate_heuristic(self.vehicle.name)

        if (
            self.vehicle.tmp_start_x == self.vehicle.start_x
            and self.vehicle.tmp_start_y == self.vehicle.start_y
        ):
            board.generate_time(self.vehicle.name)

        # Get the start cell based on the vehicle's start coordinates
        start_cell = board.cells[self.vehicle.tmp_start_y][self.vehicle.tmp_start_x]
        # Mark the start cell as vistited for the vehicle
        start_cell.visited[self.vehicle.name] = True
        # Initialize time for the start cell
        start_cell.cost[self.vehicle.name] = 0

        if (
            self.vehicle.tmp_start_x == self.vehicle.start_x
            and self.vehicle.tmp_start_y == self.vehicle.start_y
        ):
            start_cell.time[self.vehicle.name] = 1
        else:
            start_cell.time[self.vehicle.name] = start_cell.time[self.vehicle.name]

        start_cell.current_vehicle[self.vehicle.name] = self.vehicle.name
        # Initialize the priority queue (frontier) with the start cell and its heuristic value
        frontier = [(self.heuristic(start_cell), start_cell)]
        heapq.heapify(frontier)
        while frontier:
            # Pop the cell with the lowest f-score from the frontier
            _, current_cell = heapq.heappop(frontier)

            y = [0, 0, 1, -1]
            x = [1, -1, 0, 0]

            for i in range(4):
                new_y = current_cell.y + y[i]
                new_x = current_cell.x + x[i]

                if board.can_visit(self.vehicle.name, new_y, new_x) == True:
                    new_cost = (
                        board.cells[current_cell.y][current_cell.x].cost[
                            self.vehicle.name
                        ]
                        + 1
                    )
                    new_t = (
                        board.cells[current_cell.y][current_cell.x].time[
                            self.vehicle.name
                        ]
                        + 1
                        + board.cells[new_y][new_x].value
                    )

                    if (
                        new_cost < board.cells[new_y][new_x].cost[self.vehicle.name]
                        and new_t <= board.t + 1
                    ):
                        board.cells[new_y][new_x].current_vehicle = self.vehicle.name
                        board.cells[new_y][new_x].visited[self.vehicle.name] = True
                        board.cells[new_y][new_x].cost[self.vehicle.name] = new_cost
                        board.cells[new_y][new_x].time[self.vehicle.name] = new_t
                        board.cells[new_y][new_x].parent[self.vehicle.name] = (
                            current_cell.y,
                            current_cell.x,
                        )
                        f_score = new_cost + self.heuristic(board.cells[new_y][new_x])
                        heapq.heappush(frontier, (f_score, board.cells[new_y][new_x]))
            if (
                current_cell.y == self.vehicle.tmp_goal_y
                and current_cell.x == self.vehicle.tmp_goal_x
            ):
                board.cells[self.vehicle.tmp_goal_y][self.vehicle.tmp_goal_x].visited[
                    self.vehicle.name
                ] = True
                break

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

    def heuristic(self, cell):
        """
        Calculate the heuristic value for the given cell.

        Parameters:
        cell (Cell): The cell for which the heuristic is to be calculated.

        Returns:
        int: The heuristic value (Manhattan distance) for the cell.
        """
        return abs(cell.y - self.vehicle.goal_y) + abs(cell.x - self.vehicle.goal_x)

    def processs_lev2(self, board):
        self.vehicle.tmp_start_y = self.vehicle.current_y
        self.vehicle.tmp_start_x = self.vehicle.current_x
        self.vehicle.tmp_goal_y = self.vehicle.goal_y
        self.vehicle.tmp_goal_x = self.vehicle.goal_x
        path = self.a_star_execution(board)
        return board.path_and_time(self.vehicle.name, path)
