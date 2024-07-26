from termcolor import colored
from utils.cells import cell

from levels.level_1.vehicle_level1 import vehicle_level1
from levels.level_2.vehicle_level2 import vehicle_level2
from levels.level_3.vehicle_level3 import vehicle_level3
from levels.level_4.vehicle_level4 import vehicle_level4


def fought_cells(y, x, paths):
    """_summary_

    Args:
        y (_type_): _description_
        x (_type_): _description_
        paths (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i, path in enumerate(paths):
        # Tạo danh sách các tọa độ (x, y) từ mỗi đường dẫn
        coordinates = [(py, px) for py, px, _, _ in path]
        if (y, x) in coordinates:
            return i
    return -1


class Board:
    """_summary_"""

    def __init__(self, n, m, f, t, map_data, level=1, algo="algo"):
        """_summary_

        Args:
            n (_type_): _description_
            m (_type_): _description_
            f (_type_): _description_
            t (_type_): _description_
            map_data (_type_): _description_
            level (int, optional): _description_. Defaults to 1.
            algo (str, optional): _description_. Defaults to "algo".
        """
        self.n = n
        self.m = m
        self.f = f
        self.t = t
        self.map_data = map_data
        self.cells = []
        self.vehicle = []
        goals = []
        self.fuel_stations = []
        self.algo = algo  # dung cho level1

        for i in range(n):
            self.cells.append(list())
            for j in range(m):
                self.cells[i].append(cell(y=i, x=j, raw_value=map_data[i][j]))
                if "S" in map_data[i][j]:
                    name = map_data[i][j]
                    if level == 1:
                        self.vehicle.append(vehicle_level1(name, i, j, t, f, algo))
                    if level == 2:
                        self.vehicle.append(vehicle_level2(name, i, j, t, f))
                    if level == 3:
                        self.vehicle.append(vehicle_level3(name, i, j, t, f))
                    if level == 4:
                        self.vehicle.append(vehicle_level4(name, i, j, t, f))
                if "G" in map_data[i][j]:
                    goal = map_data[i][j].replace("G", "S")
                    goals.append((goal, i, j))
                if "F" in map_data[i][j]:
                    self.fuel_stations.append((i, j))

        for goal in goals:
            for vehicle in self.vehicle:
                if vehicle.name == goal[0]:
                    vehicle.goal_y = goal[1]
                    vehicle.goal_x = goal[2]
                    vehicle.tmp_goal_y = goal[1]
                    vehicle.tmp_goal_x = goal[2]
                    break
        for vehicle in self.vehicle:
            self.generate_visited(vehicle.name)
            self.generate_parent(vehicle.name)
            self.generate_cost(vehicle.name)
            self.generate_heuristic(vehicle.name)
            self.generate_time(vehicle.name)
            self.generate_fuel(vehicle.name)

    def generate_visited(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        for i in range(self.n):
            for j in range(self.m):
                self.cells[i][j].visited[name] = False

    def generate_parent(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        for i in range(self.n):
            for j in range(self.m):
                self.cells[i][j].parent[name] = (-1, -1)

    def generate_heuristic(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        for i in range(self.n):
            for j in range(self.m):
                for vehicle in self.vehicle:
                    if vehicle.name == name:
                        # self.cells[i][j].heuristic[name] = 0
                        self.cells[i][j].heuristic[name] = self.get_distance(
                            j, i, vehicle.goal_x, vehicle.goal_y
                        )
                        if "F" in self.cells[i][j].raw_value:
                            # self.cells[i][j].heuristic[name] += self.get_distance(j, i, vehicle.goal_x, vehicle.goal_y) - vehicle.fuel
                            self.cells[i][j].heuristic[name] += int(
                                self.cells[i][j].raw_value.replace("F", "")
                            )

    def generate_cost(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        for i in range(self.n):
            for j in range(self.m):
                self.cells[i][j].cost[name] = float("inf")

    def generate_fuel(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        for i in range(self.n):
            for j in range(self.m):
                self.cells[i][j].fuel[name] = float("inf")

    def generate_time(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        for i in range(self.n):
            for j in range(self.m):
                self.cells[i][j].time[name] = float("inf")

    def get_vehicle(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return sorted(self.vehicle, key=lambda vehicle: vehicle.name)

    def get_distance(self, x1, y1, x2, y2):
        """_summary_

        Args:
            x1 (_type_): _description_
            y1 (_type_): _description_
            x2 (_type_): _description_
            y2 (_type_): _description_

        Returns:
            _type_: _description_
        """
        return abs(x1 - x2) + abs(y1 - y2)

    def can_visit(self, name, y, x):
        """_summary_

        Args:
            name (_type_): _description_
            y (_type_): _description_
            x (_type_): _description_

        Returns:
            _type_: _description_
        """
        if x < 0 or y < 0 or x >= self.n or y >= self.m:
            return False
        come_cell = self.cells[y][x]
        if come_cell.visited[name] == True:
            return False
        if come_cell.value == -1:
            return False
        return True

    def tracepath(self, name):
        """_summary_

        Args:
            name (_type_): _description_

        Returns:
            _type_: _description_
        """
        vehicle = None
        for v in self.vehicle:
            if v.name == name:
                vehicle = v
                break
        path = []
        y, x = vehicle.tmp_goal_y, vehicle.tmp_goal_x
        while y != vehicle.tmp_start_y or x != vehicle.tmp_start_x:
            # time_leave = self.cells[y][x].time[name] + 1
            path.append((y, x))
            # path.append((y, x, time_leave))
            y, x = self.cells[y][x].parent[name]

        # path.append((vehicle.current_y, vehicle.current_x, 1))
        path.append((vehicle.tmp_start_y, vehicle.tmp_start_x))
        return path[::-1]  # return reverse path

    def unique_path(self, path):
        """_summary_

        Args:
            path (_type_): _description_

        Returns:
            _type_: _description_
        """
        unique_list = []
        for item in path:
            if item not in unique_list:
                unique_list.append(item)
        return unique_list

    def path_time_fuel(self, name, path):
        """_summary_

        Args:
            name (_type_): _description_
            path (_type_): _description_

        Returns:
            _type_: _description_
        """
        unique_list = []
        for item in path:
            if item not in unique_list:
                unique_list.append(item)
        new_path = []
        for i in range(len(unique_list)):
            y, x = unique_list[i]
            time_leave = self.cells[y][x].time[name]  # + 1
            fuel = self.cells[y][x].fuel[name]
            new_path.append((y, x, time_leave, fuel))
        # print("New path: ", new_path)
        return new_path

    # def test_input(self):
    #     print("Number of rows: ", self.n)
    #     print("Number of columns: ", self.m)
    #     print("Initial fuel: ", self.f)
    #     print("Time limit: ", self.t)
    #     print("Map data: ")
    #     for i in range(self.n):
    #         for j in range(self.m):
    #             print(f"{self.cells[i][j].raw_value:5}", end=" ")
    #         print("\n")

    # def test_input_2(self, name):
    #     print("Number of rows: ", self.n)
    #     print("Number of columns: ", self.m)
    #     print("Initial fuel: ", self.f)
    #     print("Time limit: ", self.t)
    #     print("Map data: ")
    #     for i in range(self.n):
    #         for j in range(self.m):
    #             print(f"{self.cells[i][j].heuristic[name]:5}", end=" ")
    #         print("\n")

    # def test_display_path(self, paths):
    #     colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]
    #     for i in range(self.n):
    #         for j in range(self.m):
    #             k = fought_cells(i, j, paths)
    #             if k != -1:
    #                 print(
    #                     colored(f"{self.cells[i][j].raw_value:5}", colors[k]), end=" "
    #                 )
    #             else:
    #                 print(f"{self.cells[i][j].raw_value:5}", end=" ")
    #         print("\n")
