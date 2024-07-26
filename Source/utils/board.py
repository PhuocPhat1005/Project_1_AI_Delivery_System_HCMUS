from utils.cells import cell  # import the cell class from the utils.cells module

# Importing vehicle classes from different level modules.
from levels.level_1.vehicle_level1 import vehicle_level1
from levels.level_2.vehicle_level2 import vehicle_level2
from levels.level_3.vehicle_level3 import vehicle_level3
from levels.level_4.vehicle_level4 import vehicle_level4


def fought_cells(y, x, paths):
    """
    Check if a given cell (y, x) is part of any path.

    Args:
        y (int): the y-coordinate of the cell.
        x (_type_): the x-coordinate of the cell.
        paths (list): a list of paths, where each path is a list of tuples representing coordinates.

    Returns:
        int: the index of the path that contains the cell (y, x), or -1 if no path contains the cell.
    """
    for i, path in enumerate(paths):  # Iterate over all paths
        coordinates = [
            (py, px) for py, px, _, _ in path
        ]  # Extract the coordinates (y, x) from each path.
        if (y, x) in coordinates:  # Check if the cell (y, x) is in current path
            return i  # Return the index of the path
    return -1  # Return -1 if the cell is not in the path


class Board:
    """
    Class representing the game board.
    """

    def __init__(self, n, m, f, t, map_data, level=1, algo="algo"):
        """
        Initialize the Board object.

        Args:
            n (int): number of rows in the board
            m (int): number of columns in the board
            f (int): initial fuel amount
            t (int): time limit (delivery time)
            map_data (list): 2D list representing the map data.
            level (int, optional): this is the game level. Defaults to 1.
            algo (str, optional): The algorithm used for pathfinding. Defaults to "algo".
        """
        self.n = n  # Set the number of rows
        self.m = m  # Set the number of columns
        self.f = f  # Set the initial fuel amount
        self.t = t  # Set the time limit
        self.map_data = map_data  # Set the map data
        self.cells = []  # Initialize the cells list
        self.vehicle = []  # Initialize the vehicle list
        goals = []  # Initialize the goal list
        self.fuel_stations = []  # Initialize the fuel station list.
        self.algo = algo  # Set the algorithm used for Level 1.

        # Initialize cells and vehicles based on map data.
        for i in range(n):  # Iterate over the rows
            self.cells.append(list())  # Append on an empty list to cells for each row.
            for j in range(m):  # Iterate over the columns
                self.cells[i].append(
                    cell(y=i, x=j, raw_value=map_data[i][j])
                )  # Create a cell object for each map cell.
                if "S" in map_data[i][j]:  # Start position of a vehicle.
                    name = map_data[i][j]  # Get the name of the vehicle.
                    if level == 1:  # If the level is 1, create a vehicle_level1 object.
                        self.vehicle.append(vehicle_level1(name, i, j, t, f, algo))
                    if level == 2:  # If the level is 2, create a vehicle_level2 object.
                        self.vehicle.append(vehicle_level2(name, i, j, t, f))
                    if level == 3:  # If the level is 3, create a vehicle_level3 object.
                        self.vehicle.append(vehicle_level3(name, i, j, t, f))
                    if level == 4:  # If the level is 4, create a vehicle_level4 object.
                        self.vehicle.append(vehicle_level4(name, i, j, t, f))
                # Dung de truy vet goal cua tung start S.
                if "G" in map_data[i][j]:  # Check if the cell is a goal position.
                    goal = map_data[i][j].replace(
                        "G", "S"
                    )  # Replace "G" with "S" to get the goal name.
                    goals.append((goal, i, j))  # Append the goal to the goals list.
                if "F" in map_data[i][j]:  # Check if the cell is a fuel station.
                    self.fuel_stations.append(
                        (i, j)
                    )  # Append the fuel station to the fuel_stations list.

        for goal in goals:  # Iterate over the goals.
            for vehicle in self.vehicle:
                if vehicle.name == goal[0]:  # Check if the vehicle matches the goal.
                    vehicle.goal_y = goal[
                        1
                    ]  # Set the goal y-coordinate for the vehicle.
                    vehicle.goal_x = goal[
                        2
                    ]  # Set the goal x-coordinate for the vehicle.
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
