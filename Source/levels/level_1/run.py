from levels.level_1.algorithms.bfs import BFS
from levels.level_1.algorithms.dfs import DFS
from levels.level_1.algorithms.ucs import UCS
from levels.level_1.algorithms.gbfs import GreedyBestFirstSearch
from levels.level_1.algorithms.a_star import AStar
from utils.parser import parse_input
from utils.visualizer import visualize_path


class Level1:
    def __init__(self, input_file):
        self.input_file = input_file
        self.grid = None
        self.start = None
        self.goal = None
        self.load_map()

    def load_map(self):
        n, m, t, f, self.grid = parse_input(self.input_file)
        for i in range(n):
            for j in range(m):
                if self.grid[i][j] == "S":
                    self.start = (i, j)
                elif self.grid[i][j] == "G":
                    self.goal = (i, j)

    def run_algorithm(self, algorithm_cls):
        if not self.start or not self.goal:
            print("Start or Goal not defined in the input.")
            return

        algorithm = algorithm_cls(self.grid, self.start, self.goal)
        path = algorithm.search()
        return path

    def execute(self):
        algorithms = [
            ("BFS", BFS),
            ("DFS", DFS),
            ("UCS", UCS),
            ("Greedy Best First Search", GreedyBestFirstSearch),
            ("A*", AStar),
        ]

        for name, algorithm_cls in algorithms:
            print(f"\n{name} Path:")
            path = self.run_algorithm(algorithm_cls)
            if path:
                visualize_path([row[:] for row in self.grid], path)
            else:
                print("No path found")
