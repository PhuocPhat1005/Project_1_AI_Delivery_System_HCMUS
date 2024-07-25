from utils.vehicle_base import vehicle_base
from levels.level_3.algorithms.a_star import AStarAlgorithm


class vehicle_level3(vehicle_base):
    def __init__(self, name, start_y, start_x, delivery_time, fuel):
        super().__init__(name, start_y, start_x, delivery_time, fuel)
        self.delivery_time = delivery_time
        self.fuel = fuel
        self.algorithm = AStarAlgorithm(self)

    def process(self, board):
        return self.algorithm.process_lev3(board)
