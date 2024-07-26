class cell:
    """
    Class representing a cell in the map.
    """

    def __init__(self, y, x, raw_value):
        """
        Initialize a cell.

        Args:
            y (int): y-coordinate of the cell.
            x (int): x-coordinate of the cell.
            raw_value (str): raw value of the cell from the map data.
        """
        self.y = y  # Set the y-coordinate of the cell.
        self.x = x  # Set the x-coordinate of the cell.
        self.raw_value = raw_value  # Store the raw value of the cell from the map data.
        try:
            self.value = float(
                raw_value
            )  # Try to convert the raw value to a float and store it as the cell's value.
        except:
            self.value = 0  # If conversion fails, set the cell's value to 0
        self.visited = (
            {}
        )  # Initialize a dictionary to track which vehicles have visited the cell
        self.parent = (
            {}
        )  # Initialize a dictionary to store the parent of the cell for each vehicle
        self.cost = (
            {}
        )  # Initialize a dictionary to store the cost to reach the cell for each vehicle
        self.heuristic = (
            {}
        )  # Initialize a dictionary to store the heuristic value of the cell for each vehicle
        self.fuel = (
            {}
        )  # Initialize a dictionary to store the fuel level at the cell for each vehicle
        self.time = (
            {}
        )  # Initialize a dictionary to store the time taken to reach the cell for each vehicle
        self.current_vehicle = (
            {}
        )  # Initialize a dictionary to store the current vehicle in the cell

    def __lt__(self, other):
        """
        Less than operator to compare cells based on cost, time, fuel, and heuristic.

        Args:
            other (cell): Another cell to compare with.

        Returns:
            bool: True if self is less than other, False otherwise.
        """
        # Compare cells first by the time taken to reach the cell.
        if self.time[self.current_vehicle] == other.time[other.current_vehicle]:
            # If the time is the same, compare by the cost to reach the cell.
            if self.cost[self.current_vehicle] == other.cost[other.current_vehicle]:
                try:
                    # If cost is the same, compare by the fuel level at the cell.
                    if (
                        self.fuel[self.current_vehicle]
                        == other.fuel[other.current_vehicle]
                    ):
                        # If fuel value is the same, compare by the heuristic value of the cell.
                        return (
                            self.heuristic[self.current_vehicle]
                            < other.heuristic[other.current_vehicle]
                        )
                    return (
                        self.fuel[self.current_vehicle]
                        < other.fuel[other.current_vehicle]
                    )
                except:
                    pass
            return self.cost[self.current_vehicle] < other.cost[other.current_vehicle]
        return self.time[self.current_vehicle] < other.time[other.current_vehicle]
