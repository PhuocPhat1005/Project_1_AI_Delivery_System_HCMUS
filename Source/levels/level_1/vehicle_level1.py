from utils.vehicle_base import vehicle_base
from levels.level_1.algorithms.bfs import BFSAlgorithm
from levels.level_1.algorithms.dfs import DFSAlgorithm
from levels.level_1.algorithms.ucs import UCSAlgorithm
from levels.level_1.algorithms.gbfs import GBFSAlgorithm
from levels.level_1.algorithms.a_star import AStarAlgorithm


class vehicle_level1(vehicle_base):
    """
    Class representing a level 1 vehicle that can use various search algorithms.

    Args:
        vehicle_base (class): the base class for vehicles.
    """

    def __init__(self, name, start_y, start_x, delivery_time, fuel, algorithm):
        """
        Initialize a level 1 vehicle with a specified algorithm.

        Args:
            name (str): The name of the vehicle.
            start_y (int): The starting y-coordinate of the vehicle.
            start_x (int): The starting x-coordinate of the vehicle.
            delivery_time (int): The delivery time limit for the vehicle.
            fuel (int): The fuel capacity of the vehicle.
            algorithm (str): The search algorithm to be used by the vehicle.
        """
        super().__init__(name, start_y, start_x, delivery_time, fuel, algorithm)
        self.set_algorithm(algorithm)

    def set_algorithm(self, algorithm):
        """
        Set the algorithm for the vehicle based on the provided algorithm name.

        Args:
            algorithm (str): The name of the algorithm to be used.

        Raises:
            ValueError: If an unknown algorithm name is provided.
        """

        if algorithm == "BFS":
            self.algorithm = BFSAlgorithm(self)
        elif algorithm == "DFS":
            self.algorithm = DFSAlgorithm(self)
        elif algorithm == "UCS":
            self.algorithm = UCSAlgorithm(self)
        elif algorithm == "GBFS":
            self.algorithm = GBFSAlgorithm(self)
        elif algorithm == "A*":
            self.algorithm = AStarAlgorithm(self)
        else:
            raise ValueError(f"Unknown algorithm: {algorithm}")

    def process(self, board):
        """
        Execute the vehicle's algorithm on the provided board.

        Args:
            board (object): The board on which the algorithm will be executed.

        Returns:
            list: The path with time and fuel information.
        """
        return self.algorithm.execute(board)
