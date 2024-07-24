from termcolor import colored
from utils.cells import cell

from levels.level_1.vehicle_level1 import vehicle_level1
from levels.level_2.vehicle_level2 import vehicle_level2
from levels.level_4.vehicle_level4 import vehicle_level4


def fought_cells(x, y, paths):
    for i, path in enumerate(paths):
        if (x, y) in path:
            return i
    return -1


class Board:
    def __init__(self, n, m, f, t, map_data, level=1):
        self.n = n
        self.m = m
        self.f = f
        self.t = t
        self.map_data = map_data
        self.cells = []
        self.time = 0
        self.vehicle = []
        goals = []
        self.fuel_stations = []

        for i in range(n):
            self.cells.append(list())
            for j in range(m):
                self.cells[i].append(cell(y=i, x=j, raw_value=map_data[i][j]))
                print(f"Time: {t}")
                if "S" in map_data[i][j]:
                    name = map_data[i][j]
                    if level == 1:
                        self.vehicle.append(vehicle_level1(name, i, j, t, f))
                    if level == 2:
                        self.vehicle.append(vehicle_level2(name, i, j, t, f))
                    # if level == 3:
                    #     self.vehicle.append(vehicle_lev3(name, i, j, f))
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
        for i in range(self.n):
            for j in range(self.m):
                self.cells[i][j].visited[name] = False

    def generate_parent(self, name):
        for i in range(self.n):
            for j in range(self.m):
                self.cells[i][j].parent[name] = (-1, -1)

    def generate_heuristic(self, name):
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
        for i in range(self.n):
            for j in range(self.m):
                self.cells[i][j].cost[name] = float("inf")

    def generate_fuel(self, name):
        for i in range(self.n):
            for j in range(self.m):
                self.cells[i][j].fuel[name] = float("inf")

    def generate_time(self, name):
        for i in range(self.n):
            for j in range(self.m):
                self.cells[i][j].time[name] = float("inf")

    def get_vehicle(self):
        return sorted(self.vehicle, key=lambda vehicle: vehicle.name)

    def get_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def can_visit(self, name, y, x):
        if x < 0 or y < 0 or x >= self.n or y >= self.m:
            return False
        come_cell = self.cells[y][x]
        if come_cell.visited[name] == True:
            return False
        if come_cell.value == -1:
            return False
        return True

    # def can_visit(self, vehicle_name, y, x):
    #     if 0 <= y < len(self.cells) and 0 <= x < len(self.cells[0]):
    #         return not self.cells[y][x].visited[vehicle_name]
    #     return False

    def tracepath(self, name):
        vehicle = None
        for v in self.vehicle:
            if v.name == name:
                vehicle = v
                break
        path = []
        y, x = vehicle.tmp_goal_y, vehicle.tmp_goal_x
        while y != vehicle.tmp_start_y or x != vehicle.tmp_start_x:
            path.append((y, x))
            y, x = self.cells[y][x].parent[name]
        path.append((vehicle.tmp_start_y, vehicle.tmp_start_x))
        return path[::-1]

    def test_input(self):
        print("Number of rows: ", self.n)
        print("Number of columns: ", self.m)
        print("Initial fuel: ", self.f)
        print("Time limit: ", self.t)
        print("Map data: ")
        for i in range(self.n):
            for j in range(self.m):
                print(f"{self.cells[i][j].raw_value:5}", end=" ")
            print("\n")

    def test_display_path(self, paths):
        colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]
        for i in range(self.n):
            for j in range(self.m):
                k = fought_cells(i, j, paths)
                if k != -1:
                    print(
                        colored(f"{self.cells[i][j].raw_value:5}", colors[k]), end=" "
                    )
                else:
                    print(f"{self.cells[i][j].raw_value:5}", end=" ")
            print("\n")
