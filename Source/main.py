from utils.read_input import read_input_file
from utils.write_output import write_paths_to_file
from utils.board import Board
import os
from levels.level_4.vehicle_level4 import process_lev4


def main():
    # # Create the output directory if it does not exist
    if not os.path.exists("output"):
        os.makedirs("output")

    # # Read input data
    n, m, t, f, map_data = read_input_file("input/input1_level2.txt")

    # # Initialize the board and vehicles
    board = Board(n, m, f, t, map_data, level=2)
    vehicles = board.get_vehicle()
    paths = []

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
    write_paths_to_file("output/output1_level2.txt", vehicles)

    #Test level 2
    # board = Board(n, m, f, t, map_data, level=2)
    # S_vehicle = board.vehicle[0]   
    # paths = []     
    # board.test_display_path(paths)
    # print (paths)
    # print(S_vehicle.process_lev3(board))
    # paths.append(S_vehicle.process_lev2(board))
    # if(paths != []):
    #     board.test_display_path(paths)
    # else:
    #     print("Can't find path, lev 2")

    # Test level 3
    # board = Board(n, m, f, t, map_data, level=4)
    # S_vehicle = board.vehicle[0]
    # paths = []
    # # print(paths)
    # paths.append(S_vehicle.process_lev3(board))
    # if paths != []:
    #     board.test_display_path(paths)
    # else:
    #     print("Can't find path, lev 3")

    #Test level 4
    # board = Board(n, m, f, t, map_data, level=4)
    # paths = process_lev4(board)
    # print(paths)
    # if paths != []:
    #     print("THE FINAL STATE: ")
    #     board.test_display_path(paths)
    # else:
    #     print("Can't find path, lev 4")


if __name__ == "__main__":
    main()
