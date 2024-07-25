from utils.read_input import read_input_file
from utils.write_output import write_paths_to_file
from utils.board import Board
from GUI.gui import *
from GUI.constants import *
from GUI.text import *
from GUI.menu import *
from GUI.credit import *
import os
from levels.level_4.vehicle_level4 import process_lev4


def main():
    # # Create the output directory if it does not exist
    if not os.path.exists("output"):
        os.makedirs("output")
    
    #khi chay backend thi comment het nhung dong co _UI
    #menu_UI: 0->3 | level: 1->4
    #level = menu_UI() + 1
    level = 1
    # Read input data
    n, m, t, f, map_data = read_input_file("input\\level" + str(level) + "\\input1_level" + str(level) + ".txt")

    # Initialize the board and vehicles
    board = Board(n, m, t, f, map_data, level)
    vehicles = board.get_vehicle()
    paths = []

    #vua hien UI map, vua tim canh cell
    #cell_side = map_UI(n, m, t, f, map_data, level)
    for vehicle in vehicles:
        print(
            vehicle.name,
            f"\t\tStart: {vehicle.start_y}, {vehicle.start_x}",
            f"\t\tGoal: {vehicle.goal_y}, {vehicle.goal_x}",
        )
        path = vehicle.process(board)
        vehicle.path = path
        paths.append(path)
    board.test_display_path(paths)


    # Write paths to the output file
    write_paths_to_file("output/output1_level1.txt", vehicles)
    print(paths)
    #hien path, hien line
    #path_UI(n, m, map_data, paths, cell_side)


if __name__ == "__main__":
    main()