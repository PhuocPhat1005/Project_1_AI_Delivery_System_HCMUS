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


# main chay frontend
def main():
    # khi chay backend thi comment het nhung dong co _UI
    # menu_UI: 0->3 | level: 1->4
    level = 1
    algo = "algo"
    map_order, level, algo = menu_UI()
    level += 1

    # Read input data
    # map_order = 1
    input_filename = f"input/level{level}/input{map_order}_level{level}.txt"
    if not os.path.exists(input_filename):
        print(f"File {input_filename} does not exist. Please enter the details again.")
        return
    n, m, t, f, map_data = read_input_file(input_filename)

    # vua hien UI map, vua tim canh cell
    cell_side = map_UI(n, m, f, t, map_data, level, algo)

    # Initialize the board and vehicles
    board = Board(n, m, f, t, map_data, level, algo)
    vehicles = board.get_vehicle()
    paths = []

    if level != 4:
        for vehicle in vehicles:
            print(
                vehicle.name,
                f"\t\tStart: {vehicle.start_y}, {vehicle.start_x}",
                f"\t\tGoal: {vehicle.goal_y}, {vehicle.goal_x}",
            )
            path = vehicle.process(board)
            vehicle.path = path
            paths.append(path)
        path_UI(board, paths, cell_side)
    else:
        process_lev4(board)
        paths = []
        # paths = process_lev4(board)
        vehicles = board.get_vehicle()
        for vehicle in vehicles:
            vehicle.path = []
            prev_value = 0
            vehicle.final_path = board.unique_path(vehicle.final_path)
            for path in vehicle.final_path:
                if path != [] and path[-1][2] <= board.t + 1 - prev_value:
                    for i in range(0, len(path)):
                        path[i] = (
                            path[i][0],
                            path[i][1],
                            path[i][2] + prev_value,
                            path[i][3],
                        )
                    prev_value = path[-1][2] - 1
                    vehicle.path.extend(path)
                else:
                    # vehicle.path = board.unique_path(vehicle.path)
                    paths.append(path)
                    break

        print("FINAL STATE: ")
        print(paths)
        p_vehicle = []
        for vehicle in vehicles:
            p_vehicle.append(vehicle.path)
            vehicle.path = board.unique_path(vehicle.path)
        
        path_UI(board, p_vehicle, cell_side, len(p_vehicle))
    board.test_display_path(paths)

    for vehicle in vehicles:
        print(vehicle.name)
        print(vehicle.path)

    # Determine output filename based on the input filename
    output_filename = f"output/level{level}/output{map_order}_level{level}.txt"

    # Create the output directory for the level if it does not exist
    if not os.path.exists(f"output/level{level}"):
        os.makedirs(f"output/level{level}")

    # Write paths to the output file
    write_paths_to_file(output_filename, vehicles, level)
    print(paths)
    # hien path, hien line
    if level == 4:
        print(paths)


if __name__ == "__main__":
    while True:
        main()


# main chay backend
"""
def play_level(level, map_order):
    # Read input data
    input_filename = f"input/level{level}/input{map_order}_level{level}.txt"
    if not os.path.exists(input_filename):
        print(f"File {input_filename} does not exist. Please enter the details again.")
        return

    n, m, t, f, map_data = read_input_file(input_filename)

    # Initialize the board and vehicles
    board = Board(n, m, f, t, map_data, level=level)
    vehicles = board.get_vehicle()
    paths = []

    # # vua hien UI map, vua tim canh cell
    # cell_side = map_UI(board, level)
    if level != 4:
        for vehicle in vehicles:

            print(
                vehicle.name,
                f"\t\tStart: {vehicle.start_y}, {vehicle.start_x}",
                f"\t\tGoal: {vehicle.goal_y}, {vehicle.goal_x}",
            )
            path = vehicle.process(board)
            vehicle.path = path
            paths.append(path)
    else:
        paths = process_lev4(
            board
        )  # Level thuc thi tren n vehicle, ta khong the goi trong 1 vehicle duoc
    board.test_display_path(paths)

    # Determine output filename based on the input filename
    output_filename = f"output/level{level}/output{map_order}_level{level}.txt"

    # Create the output directory for the level if it does not exist
    if not os.path.exists(f"output/level{level}"):
        os.makedirs(f"output/level{level}")

    # Write paths to the output file
    write_paths_to_file(output_filename, vehicles, level)


def main():
    while True:
        while True:
            try:
                level = int(input("Enter your level (e.g., 1, 2, 3, 4): "))
                if 1 <= level <= 4:
                    break
                else:
                    print("The level is invalid. Please choose level from 1 to 4 !!!")
            except ValueError:
                print("Please choose a valid level (integer) !!!")

        while True:
            try:
                map_order = int(
                    input("Enter your map in your level (e.g., 1, 2, 3, 4, 5): ")
                )
                if 1 <= map_order <= 5:
                    break
                else:
                    print(
                        "The map is invalid. Please choose the suitable map in your level (1 to 5) !!!"
                    )
            except ValueError:
                print("Please choose a valid map (integer) !!!")

        play_level(level, map_order)

        play_again = (
            input("Do you want to play another level? (yes/no): ").strip().lower()
        )
        if play_again != "yes":
            print("Thank you for playing")
            break


if __name__ == "__main__":
    main()"""
