from utils.vehicle_base import vehicle_base
from levels.level_1.algorithms.bfs import BFSAlgorithm
from levels.level_1.algorithms.dfs import DFSAlgorithm
from levels.level_1.algorithms.ucs import UCSAlgorithm
from levels.level_1.algorithms.gbfs import GBFSAlgorithm
from levels.level_1.algorithms.a_star import AStarAlgorithm


class vehicle_level1(vehicle_base):
    def __init__(self, name, start_y, start_x, delivery_time, fuel, algorithm):
        super().__init__(name, start_y, start_x, delivery_time, fuel, algorithm)
        #algorithm = input("Choose algorithms: ")
        self.set_algorithm(algorithm)

    def set_algorithm(self, algorithm):
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
        return self.algorithm.execute(board)
