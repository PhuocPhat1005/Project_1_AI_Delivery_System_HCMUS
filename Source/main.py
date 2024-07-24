from utils.read_input import read_input_file
from utils.write_output import write_paths_to_file
from utils.board import Board
from GUI.gui import *
from GUI.constants import *
from GUI.text import *
from GUI.menu import *
from GUI.credit import *
import os


def main():
    # Create the output directory if it does not exist
    if not os.path.exists("output"):
        os.makedirs("output")
    
    #menu_UI: 0->3 | level: 1->4
    level = menu_UI() + 1

    # Read input data
    n, m, t, f, map_data = read_input_file("input\\input1_level" + str(level) + ".txt")

    # Initialize the board and vehicles
    board = Board(n, m, f, t, map_data, 1)
    vehicles = board.get_vehicle()
    vehicle_paths = {}
    paths = []
    cell_side = map_UI(n, m, t, f, map_data, level)
    for vehicle in vehicles:
        print(
            vehicle.name,
            f"\t\tStart: {vehicle.start_y}, {vehicle.start_x}",
            f"\t\tGoal: {vehicle.goal_y}, {vehicle.goal_x}",
        )
        path = vehicle.process(board)
        vehicle_paths[vehicle.name] = path
        paths.append(path)
    board.test_display_path(paths)


    # Write paths to the output file
    write_paths_to_file("output/output1_level1.txt", vehicle_paths)
    print("Done")
    path_UI(n, m, paths, cell_side)
    # board.test_input()


if __name__ == "__main__":
    main()