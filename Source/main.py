from utils.read_input import read_input_file
from utils.write_output import write_paths_to_file
from utils.board import Board
from GUI.gui import UI
from GUI.constants import *
from GUI.text import *
from GUI.menu import *
from GUI.credit import *
import os


def main():
    # Create the output directory if it does not exist
    if not os.path.exists("output"):
        os.makedirs("output")

    # Read input data
    n, m, t, f, map_data = read_input_file("input\\input1_level1.txt")

    # Initialize the board and vehicles
    board = Board(n, m, f, t, map_data, level=1)
    vehicles = board.get_vehicle()
    vehicle_paths = {}
    paths = []
    UI(n, m, t, f, map_data, paths)

    for vehicle in vehicles:
        print(
            vehicle.name,
            f"\t\tStart: {vehicle.start_y}, {vehicle.start_x}",
            f"\t\tGoal: {vehicle.goal_y}, {vehicle.goal_x}",
        )
        path = vehicle.process(board)
        vehicle_paths[vehicle.name] = path
        paths.append(path)
    # print(path)
    board.test_display_path(paths)
    #UI(n, m, t, f, map_data, paths)
    # Write paths to the output file
    write_paths_to_file("output/output1_level1.txt", vehicle_paths)
    print("Done")
    # board.test_input()


if __name__ == "__main__":
    main()