from termcolor import (
    colored,
)  # Import the colored function from the termcolor module to color terminal text.
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
                    vehicle.tmp_goal_y = goal[
                        1
                    ]  # Set the temporary goal y-coordinates for the vehicle.
                    vehicle.tmp_goal_x = goal[
                        2
                    ]  # Set the temporary goal x-coordinates for the vehicle.
                    break  # Break the loop once the goal is assigned
        for vehicle in self.vehicle:  # Iterate over the vehicles.
            self.generate_visited(
                vehicle.name
            )  # Generate visited status for each vehicle.
            self.generate_parent(
                vehicle.name
            )  # Generate parent pointers for each vehicle.
            self.generate_cost(vehicle.name)  # Generate cost values for each vehicle.
            self.generate_heuristic(
                vehicle.name
            )  # Generate heuristic values for each vehicle.
            self.generate_time(vehicle.name)  # Generate time values for each vehicle.
            self.generate_fuel(vehicle.name)  # Generate fuel values for each vehicle.

    def generate_visited(self, name):
        """
        Initial visited status for all cells for a specific vehicle.

        Args:
            name (str): name of the vehicle.
        """
        for i in range(self.n):  # Iterate over the rows
            for j in range(self.m):  # Iterate over the columns
                self.cells[i][j].visited[
                    name
                ] = False  # Set the visited status to False.

    def generate_parent(self, name):
        """
        Initialize parent pointers for all cells for a specific vehicle.

        Args:
            name (str): name of the vehicle.
        """
        for i in range(self.n):  # Iterate over the rows
            for j in range(self.m):  # Iterate over the columns
                self.cells[i][j].parent[name] = (
                    -1,
                    -1,
                )  # Set the parent pointer to (-1, -1)

    def generate_heuristic(self, name):
        """
        Initialize heuristic values for all cells for a specific vehicle.

        Args:
            name (str): name of the vehicle.
        """
        for i in range(self.n):  # Iterate over the rows
            for j in range(self.m):  # Iterate over the columns
                for vehicle in self.vehicle:  # Iterate over the vehicles.
                    if vehicle.name == name:  # Check if the vehicle matches the name.
                        self.cells[i][j].heuristic[name] = self.get_distance(
                            j, i, vehicle.goal_x, vehicle.goal_y
                        )  # Set the heurisic value based on the distance to the goal.
                        if "F" in self.cells[i][j].raw_value:
                            self.cells[i][j].heuristic[name] += int(
                                self.cells[i][j].raw_value.replace("F", "")
                            )  # Adjust the heuristic value based on the fuel station.

    def generate_cost(self, name):
        """
        Initialize cost values for all cells in the game board for a specific vehicle.
        This cost represents the cumulative effort or resources needed for the vehicle to
        travel through the cells.
        Initially, all cells are set to have an infinite cost, indicating that they are not
        reachable or that their travel cost has not been calculated yet.

        Args:
            name (str): the name of the vehicle for which the cost values are being initialized.
        """
        for i in range(self.n):  # Iterate over the rows.
            for j in range(self.m):  # Iterate over the columns.
                self.cells[i][j].cost[name] = float("inf")  # Set the cost to infinity
                # => that cells is initially considered unreachable or that the travel cost has not been determined.

    def generate_fuel(self, name):
        """
        Initialize fuel values for all cells in the game board for a specific vehicle.

        Args:
            name (str): the name of the vehicle for which the fuel values are being initialized.
        """
        for i in range(self.n):  # Iterate over the rows.
            for j in range(self.m):  # Iterate over the columns.
                self.cells[i][j].fuel[name] = float("inf")  # Set the fuel to infinity
                # => that cells is initially considered unreachable or that the fuel has not been determined.

    def generate_time(self, name):
        """
        Initialize time values for all cells in the game board for a specific vehicle.

        Args:
            name (str): the name of the vehicle for which the time values are being initialized.
        """
        for i in range(self.n):  # Iterate over the rows
            for j in range(self.m):  # Iterate over the columns
                self.cells[i][j].time[name] = float("inf")  # Set the time to infinity
                # => that cells is initially considered unreachable or that the time has not been determined.

    def get_vehicle(self):
        """
        Get a list of vehicles sorted by name.

        Returns:
            list: Sorted list of vehicles.
        """
        return sorted(
            self.vehicle, key=lambda vehicle: vehicle.name
        )  # Return the sorted list of vehicles

    def get_distance(self, x1, y1, x2, y2):
        """
        Calculate the Manhattan distance between two points (y1, x1) and (y2, x2).

        Args:
            x1 (int): x-coordinate of the first point (y1, x1)
            y1 (int): y-coordinate of the first point (y1, x1)
            x2 (int): x-coordinate of the second point (y2, x2)
            y2 (int): y-coordinate of the second point (y2, x2)

        Returns:
            int: Manhattan distance between (y1, x1) and (y2, x2).
        """
        return abs(x1 - x2) + abs(
            y1 - y2
        )  # Calculate and return the Manhattan distance.

    def can_visit(self, name, y, x):
        """
        Check if a cell can be visited by a specific vehicle.

        Args:
            name (str): name of the vehicle.
            y (int): y-coordinate of the cell.
            x (int): x-coordinate of the cell.

        Returns:
            bool : True if the cell can be visited, False otherwise.
        """
        if (
            x < 0 or y < 0 or x >= self.n or y >= self.m
        ):  # Check if the cell is out of bounds.
            return False
        come_cell = self.cells[y][x]  # Get the cell object.
        if (
            come_cell.visited[name] == True
        ):  # Check if the cell has already been visited.
            return False
        if come_cell.value == -1:  # Check if the cell is an obstacle
            return False
        return True  # Return True if the cell can be visited.

    def tracepath(self, name):
        """
        Trace the path from the goal to the start for a specific vehicle.

        Args:
            name (str): name of the vehicle.

        Returns:
            list: list of tuples representing the path.
        """
        vehicle = None
        for v in self.vehicle:  # Iterate over the vehicles.
            if v.name == name:  # Check if the vehicle matches the name.
                vehicle = v  # Set the vehicle.
                break
        path = []
        y, x = (
            vehicle.tmp_goal_y,
            vehicle.tmp_goal_x,
        )  # Set the starting point as the goal.
        while (
            y != vehicle.tmp_start_y or x != vehicle.tmp_start_x
        ):  # Loop until the start point is reached.
            path.append((y, x))  # Append the current position to the path.
            y, x = self.cells[y][x].parent[name]  # Move to the parent cell.

        path.append((vehicle.tmp_start_y, vehicle.tmp_start_x))
        return path[::-1]  # return reverse path

    def unique_path(self, path):
        """Get a list of unique coordinates in the path.

        Args:
            path (list): List of tuples representing the path.

        Returns:
            list: List of unique coordinates.
        """
        unique_list = []
        for item in path:  # Iterate over the path.
            if item not in unique_list:  # Check if the item is not in the unique list.
                unique_list.append(item)  # Append the item to the unique list.
        return unique_list  # Return the unique list.

    def path_time_fuel(self, name, path):
        """Get the path with time and fuel information for a specific vehicle.

        Args:
            name (str): Name of the vehicle.
            path (list): List of tuples representing the path.

        Returns:
            list: List of tuples (y, x, time_leave, fuel) representing the path with time and fuel information.
        """
        # Call the unique_path method to remove duplicate coordinates from the path
        unique_list = []
        for item in path:
            if item not in unique_list:
                unique_list.append(item)
        # Initialize a new list to store the path with time and fuel information
        new_path = []
        for i in range(len(unique_list)):
            y, x = unique_list[i]
            # Get the time the vehicle leaves the current cell
            time_leave = self.cells[y][x].time[name]
            # Get the remaining fuel of the vehicle when it leaves the current cell
            fuel = self.cells[y][x].fuel[name]
            # Append the current cell's coordinates along with the time and fuel information to the new path list
            new_path.append((y, x, time_leave, fuel))
        # Return the new path with time and fuel information
        return new_path

    # The following methods are for testing and debugging purposes.
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

    def test_input_2(self, name):
        print("Number of rows: ", self.n)
        print("Number of columns: ", self.m)
        print("Initial fuel: ", self.f)
        print("Time limit: ", self.t)
        print("Map data: ")
        for i in range(self.n):
            for j in range(self.m):
                print(f"{self.cells[i][j].heuristic[name]:5}", end=" ")
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
