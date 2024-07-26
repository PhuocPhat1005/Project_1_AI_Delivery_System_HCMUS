import heapq


class AStarAlgorithm:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def a_star(self, board):
        board.generate_visited(self.vehicle.name)
        board.generate_parent(self.vehicle.name)
        board.generate_cost(self.vehicle.name)
        board.generate_heuristic(self.vehicle.name)
        board.generate_fuel(self.vehicle.name)

        if (
            self.vehicle.tmp_start_x == self.vehicle.start_x
            and self.vehicle.tmp_start_y == self.vehicle.start_y
        ):
            board.generate_time(self.vehicle.name)

        self.vehicle.current_fuel = self.vehicle.fuel

        start_cell = board.cells[self.vehicle.tmp_start_y][self.vehicle.tmp_start_x]
        start_cell.visited[self.vehicle.name] = True
        start_cell.cost[self.vehicle.name] = 0
        start_cell.fuel[self.vehicle.name] = self.vehicle.fuel
        if (
            self.vehicle.tmp_start_x == self.vehicle.start_x
            and self.vehicle.tmp_start_y == self.vehicle.start_y
        ):
            start_cell.time[self.vehicle.name] = 1
        else:
            start_cell.time[self.vehicle.name] = start_cell.time[self.vehicle.name]

        start_cell.current_vehicle = self.vehicle.name

        start_cell.visited[self.vehicle.name] = True
        frontier = [(start_cell)]

        while frontier:
            current_cell = heapq.heappop(frontier)
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

                    new_fuel = (
                        board.cells[current_cell.y][current_cell.x].fuel[
                            self.vehicle.name
                        ]
                        - 1
                    )

                    if "F" in board.cells[new_y][new_x].raw_value:
                        new_t += float(
                            board.cells[new_y][new_x].raw_value.replace("F", "")
                        )
                        new_fuel = self.vehicle.fuel

                    if (
                        new_cost < board.cells[new_y][new_x].cost[self.vehicle.name]
                        and new_fuel >= 0
                        and new_t <= board.t + 1
                    ):
                        board.cells[new_y][new_x].current_vehicle = self.vehicle.name
                        board.cells[new_y][new_x].visited[self.vehicle.name] = True
                        board.cells[new_y][new_x].cost[self.vehicle.name] = new_cost
                        board.cells[new_y][new_x].time[self.vehicle.name] = new_t
                        board.cells[new_y][new_x].fuel[self.vehicle.name] = new_fuel
                        board.cells[new_y][new_x].parent[self.vehicle.name] = (
                            current_cell.y,
                            current_cell.x,
                        )
                        heapq.heappush(frontier, (board.cells[new_y][new_x]))

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
            and self.vehicle.goal_y != self.vehicle.tmp_goal_y
        ):
            board.cells[self.vehicle.goal_y][self.vehicle.goal_x].visited[
                self.vehicle.name
            ] = False
        return path

    def find_best_goal(self, board):
        if board.fuel_stations == []:
            self.vehicle.tmp_goal_y = -1
            self.vehicle.tmp_goal_x = -1
            return
        best_heuristic = float("inf")
        for fuel_station in board.fuel_stations:
            if (
                self.vehicle.tmp_goal_x == fuel_station[1]
                and self.vehicle.tmp_goal_y == fuel_station[0]
            ):
                continue
            if (
                board.cells[fuel_station[0]][fuel_station[1]].heuristic[
                    self.vehicle.name
                ]
                < best_heuristic
            ):
                best_heuristic = board.cells[fuel_station[0]][
                    fuel_station[1]
                ].heuristic[self.vehicle.name]
                new_y = fuel_station[0]
                new_x = fuel_station[1]
        if (
            self.vehicle.tmp_goal_x == self.vehicle.goal_x
            and self.vehicle.tmp_goal_y == self.vehicle.goal_y
            and self.vehicle.tmp_start_x == self.vehicle.start_x
            and self.vehicle.tmp_start_y == self.vehicle.start_y
        ):
            self.vehicle.tmp_goal_y = new_y
            self.vehicle.tmp_goal_x = new_x
        else:
            self.vehicle.tmp_start_y = self.vehicle.tmp_goal_y
            self.vehicle.tmp_start_x = self.vehicle.tmp_goal_x
            self.vehicle.tmp_goal_y = new_y
            self.vehicle.tmp_goal_x = new_x

    def process_lev3(self, board):

        board.cells[self.vehicle.goal_y][self.vehicle.goal_x].visited[
            self.vehicle.name
        ] = False

        self.vehicle.tmp_start_y = self.vehicle.current_y
        self.vehicle.tmp_start_x = self.vehicle.current_x
        self.vehicle.tmp_goal_y = self.vehicle.goal_y
        self.vehicle.tmp_goal_x = self.vehicle.goal_x

        paths = []
        flag = False
        while (
            board.cells[self.vehicle.goal_y][self.vehicle.goal_x].visited[
                self.vehicle.name
            ]
            == False
        ):
            path = self.a_star(board)

            if path != []:
                path = board.path_time_fuel(self.vehicle.name, path)
                paths.append(path)
                self.vehicle.tmp_start_y = self.vehicle.tmp_goal_y
                self.vehicle.tmp_start_x = self.vehicle.tmp_goal_x

                self.vehicle.tmp_goal_y = (
                    self.vehicle.goal_y
                )  # Neu tim thay path, tim tiep tuc tu vi tri hien tai den goal
                self.vehicle.tmp_goal_x = self.vehicle.goal_x

            else:
                if flag == True:
                    return []
                self.find_best_goal(board)  # Neu tim k duoc, tim fuel tot nhat
                if self.vehicle.tmp_goal_y == -1 and self.vehicle.tmp_goal_x == -1:
                    return []
                flag = True

        joined_path = []
        for path in paths:
            joined_path.extend(path)
        joined_path = board.unique_path(joined_path)
        return joined_path
