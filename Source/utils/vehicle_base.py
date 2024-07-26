class vehicle_base:
    """
    Base class for vehicles.
    """

    def __init__(self, name, start_y, start_x, delivery_time, fuel, algo="algo"):
        """
        Initialize a vehicle.

        Args:
            name (str): name of the vehicle.
            start_y (int): starting y-coordinate of the vehicle.
            start_x (int): starting x-coordinate of the vehicle.
            delivery_time (int): delivery time limit for the vehicle.
            fuel (int): Initialize fuel for the vehicle.
            algo (str, optional): Algorithm used for vehicle in level 1. Defaults to "algo".
        """
        self.start_y = start_y  # Set the starting y-coordinate of the vehicle.
        self.start_x = start_x  # Set the starting x-coordinate of the vehicle.
        self.fuel = fuel  # Initialize the fuel for the vehicle.
        self.current_fuel = fuel  # Set the current fuel to the initial fuel value.
        self.goal_x = -1  # Initialize the goal x-coordinate (to be set later).
        self.goal_y = -1  # Initialize the goal y-coordinate (to be set later).
        self.time = 0  # Initialize the time taken to 0.
        self.name = name  # Set the name of the vehicle.
        self.current_x = (
            start_x  # Set the current x-coordinate to the starting x-coordinate.
        )
        self.current_y = (
            start_y  # Set the current y-coordinate to the starting y-coordinate.
        )
        self.tmp_start_x = (
            start_x  # Temporary start x-coordinate for intermediate calculations.
        )
        self.tmp_start_y = (
            start_y  # Temporary start y-coordinate for intermediate calculations.
        )
        self.tmp_goal_x = (
            self.goal_x
        )  # Temporary goal x-coordinate for intermediate calculations.
        self.tmp_goal_y = (
            self.goal_y
        )  # Temporary goal y-coordinate for intermediate calculations.
        self.path = []  # Initialize the path list to store the vehicle's path.
        self.blocked_opposite = (
            []
        )  # Initialize a list to store blocked cells by the opposite vehicle.
        self.blocked_temp = (
            []
        )  # Initialize a list to store temporarily blocked cells (need to wait 1 minute).

    def get_algorithm_name(self):
        """
        Get the name of the algorithm used by the vehicle.

        Returns:
            str: Name of the algorithm.
        """
        return (
            self.algorithm.__class__.__name__
        )  # Return the class name of the algorithm used by the vehicle.
