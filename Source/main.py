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

#main chay frontend
def main():
    #khi chay backend thi comment het nhung dong co _UI
    #menu_UI: 0->3 | level: 1->4
    level = 1
    algo = 'algo'
    level, algo = menu_UI()
    level += 1


    # Read input data
    map_order = 1
    input_filename = f"input/level{level}/input{map_order}_level{level}.txt"
    if not os.path.exists(input_filename):
        print(f"File {input_filename} does not exist. Please enter the details again.")
        return
    n, m, t, f, map_data = read_input_file(input_filename)

    #vua hien UI map, vua tim canh cell
    cell_side = map_UI(n, m, t, f, map_data, level, algo)

    # Initialize the board and vehicles
    board = Board(n, m, f, t, map_data, level, algo)
    vehicles = board.get_vehicle()
    paths = []

    for vehicle in vehicles:
        #if level == 1:
            #vehicle.get_algorithm(algo)
        print(
            vehicle.name,
            f"\t\tStart: {vehicle.start_y}, {vehicle.start_x}",
            f"\t\tGoal: {vehicle.goal_y}, {vehicle.goal_x}",
        )
        path = vehicle.process(board)
        vehicle.path = path
        paths.append(path)
    board.test_display_path(paths)


    # Determine output filename based on the input filename
    output_filename = f"output/level{level}/output_{os.path.basename(input_filename).split('.')[0]}_level{level}.txt"

    # Create the output directory for the level if it does not exist
    if not os.path.exists(f"output/level{level}"):
        os.makedirs(f"output/level{level}")

    # Write paths to the output file
    write_paths_to_file(output_filename, vehicles)
    print(paths)
    #hien path, hien line
    path_UI(n, m, map_data, paths, cell_side)


#main chay backend
'''
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

    # vua hien UI map, vua tim canh cell
    cell_side = map_UI(n, m, t, f, map_data, level)
    if level != 4:
        for vehicle in vehicles:
            # if level == 1:
            # vehicle.get_algorithm(algo)
            print(
                vehicle.name,
                f"\t\tStart: {vehicle.start_y}, {vehicle.start_x}",
                f"\t\tGoal: {vehicle.goal_y}, {vehicle.goal_x}",
            )
            path = vehicle.process(board)
            vehicle.path = path
            paths.append(path)
    else 
        paths = process_lev4(board) #Level thuc thi tren n vehicle, ta khong the goi trong 1 vehicle duoc
    board.test_display_path(paths)

    # Determine output filename based on the input filename
    output_filename = f"output/level{level}/output_{os.path.basename(input_filename).split('.')[0]}_level{level}.txt"

    # Create the output directory for the level if it does not exist
    if not os.path.exists(f"output/level{level}"):
        os.makedirs(f"output/level{level}")

    # Write paths to the output file
    write_paths_to_file(output_filename, vehicles)


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

'''
if __name__ == "__main__":
    main()
