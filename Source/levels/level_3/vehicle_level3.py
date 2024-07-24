from utils.vehicle_base import vehicle_base
from utils.cells import cell
import heapq


class vehicle_level3(vehicle_base):
    def __init__(self, name, start_y, start_x, time, fuel):
        super().__init__(name, start_y, start_x, time, fuel)

    def a_star(self, board):
        board.generate_visited(self.name)
        board.generate_parent(self.name)
        board.generate_cost(self.name)
        board.generate_heuristic(self.name)
        board.generate_fuel(self.name)

        if self.tmp_start_x == self.start_x and self.tmp_start_y == self.start_y:
            board.generate_time(self.name)

        self.current_fuel = self.fuel

        start_cell = board.cells[self.tmp_start_y][self.tmp_start_x]
        start_cell.visited[self.name] = True
        start_cell.cost[self.name] = 0
        start_cell.fuel[self.name] = self.fuel
        if self.tmp_start_x == self.start_x and self.tmp_start_y == self.start_y:
            start_cell.time[self.name] = 1
        else:
            start_cell.time[self.name] = start_cell.time[self.name]

        start_cell.current_vehicle = self.name

        start_cell.visited[self.name] = True
        frontier = [(start_cell)]

        while frontier:
            current_cell = heapq.heappop(frontier)
            y = [0, 0, 1, -1]
            x = [1, -1, 0, 0]
            for i in range(4):
                new_y = current_cell.y + y[i]
                new_x = current_cell.x + x[i]

                if board.can_visit(self.name, new_y, new_x) == True:
                    new_cost = (
                        board.cells[current_cell.y][current_cell.x].cost[self.name] + 1
                    )
                    new_t = (
                        board.cells[current_cell.y][current_cell.x].time[self.name]
                        + 1
                        + board.cells[new_y][new_x].value
                    )
                    if "F" in board.cells[new_y][new_x].raw_value:
                        new_t += float(
                            board.cells[new_y][new_x].raw_value.replace("F", "")
                        )

                    new_fuel = (
                        board.cells[current_cell.y][current_cell.x].fuel[self.name] - 1
                    )

                    if (
                        new_cost < board.cells[new_y][new_x].cost[self.name]
                        and new_fuel >= 0
                        and new_t <= board.t + 1
                    ):
                        board.cells[new_y][new_x].current_vehicle = self.name
                        board.cells[new_y][new_x].visited[self.name] = True
                        board.cells[new_y][new_x].cost[self.name] = new_cost
                        board.cells[new_y][new_x].time[self.name] = new_t
                        board.cells[new_y][new_x].fuel[self.name] = new_fuel
                        board.cells[new_y][new_x].parent[self.name] = (
                            current_cell.y,
                            current_cell.x,
                        )
                        heapq.heappush(frontier, (board.cells[new_y][new_x]))

            if current_cell.y == self.tmp_goal_y and current_cell.x == self.tmp_goal_x:
                board.cells[self.tmp_goal_y][self.tmp_goal_x].visited[self.name] = True
                break

        path = []
        if board.cells[self.tmp_goal_y][self.tmp_goal_x].visited[self.name] == True:
            path = board.tracepath(self.name)

        if (
            path == []
            or self.tmp_goal_x != self.goal_x
            and self.goal_y != self.tmp_goal_y
        ):
            board.cells[self.goal_y][self.goal_x].visited[self.name] = False
        return path

    def find_best_goal(self, board):
        if board.fuel_stations == []:
            self.tmp_goal_y = -1
            self.tmp_goal_x = -1
            return
        best_heuristic = float("inf")
        for fuel_station in board.fuel_stations:
            if (
                self.tmp_goal_x == fuel_station[1]
                and self.tmp_goal_y == fuel_station[0]
            ):
                continue
            if (
                board.cells[fuel_station[0]][fuel_station[1]].heuristic[self.name]
                < best_heuristic
            ):
                best_heuristic = board.cells[fuel_station[0]][
                    fuel_station[1]
                ].heuristic[self.name]
                new_y = fuel_station[0]
                new_x = fuel_station[1]
        if (
            self.tmp_goal_x == self.goal_x
            and self.tmp_goal_y == self.goal_y
            and self.tmp_start_x == self.start_x
            and self.tmp_start_y == self.start_y
        ):
            self.tmp_goal_y = new_y
            self.tmp_goal_x = new_x
        else:
            self.tmp_start_y = self.tmp_goal_y
            self.tmp_start_x = self.tmp_goal_x
            self.tmp_goal_y = new_y
            self.tmp_goal_x = new_x

    def process_lev3(self, board):

        board.cells[self.goal_y][self.goal_x].visited[self.name] = False

        self.tmp_start_y = self.current_y
        self.tmp_start_x = self.current_x
        self.tmp_goal_y = self.goal_y
        self.tmp_goal_x = self.goal_x

        paths = []
        flag = False
        while board.cells[self.goal_y][self.goal_x].visited[self.name] == False:
            path = self.a_star(board)

            if path != []:
                path = board.path_and_time(self.name, path)
                paths.append(path)
                self.tmp_start_y = self.tmp_goal_y
                self.tmp_start_x = self.tmp_goal_x

                self.tmp_goal_y = (
                    self.goal_y
                )  # Neu tim thay path, tim tiep tuc tu vi tri hien tai den goal
                self.tmp_goal_x = self.goal_x

            else:
                if flag == True:
                    return []
                self.find_best_goal(board)  # Neu tim k duoc, tim fuel tot nhat
                if self.tmp_goal_y == -1 and self.tmp_goal_x == -1:
                    return []
                flag = True

        joined_path = []
        for path in paths:
            joined_path.extend(path)
        joined_path = board.unique_path(joined_path)
        return joined_path
