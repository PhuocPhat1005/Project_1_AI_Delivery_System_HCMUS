def write_paths_to_file(file_path, vehicles, level):
    """
    Write the paths of vehicles to a file.

    Args:
        file_path (str): Path to the file where paths will be written.
        vehicles (list): List of vehicle objects.
        level (int): Level of the algorithm (used to differentiate output format).
    """
    with open(file_path, "a") as file:  # Open the file in append mode
        if level == 1:  # Check if the level is 1
            for vehicle in vehicles:  # Iterate over each vehicle in the vehicles list
                algorithm_name = (
                    vehicle.get_algorithm_name()
                )  # Get the algorithm name used by the vehicle
                file.write(
                    f"{algorithm_name}:\n"
                )  # Write the algorithm name to the file
                file.write(f"{vehicle.name}\n")  # Write the vehicle name to the file
                if vehicle.path:  # Check if the vehicle has a valid path
                    path_str = "  ".join(
                        [f"({y}, {x})" for y, x, _, _ in vehicle.path]
                    )  # Format the path as a string with coordinates
                    file.write(
                        path_str + "\n\n"
                    )  # Write the formatted path to the file
                else:
                    file.write(
                        "No valid path found\n"
                    )  # Write a message if no valid path is found
        else:  # For levels other than 1
            for vehicle in vehicles:  # Iterate over each vehicle in the vehicles list
                file.write(f"{vehicle.name}\n")  # Write the vehicle name to the file
                if vehicle.path:  # Check if the vehicle has a valid path
                    path_str = "  ".join(
                        [f"({y}, {x})" for y, x, _, _ in vehicle.path]
                    )  # Format the path as a string with coordinates
                    file.write(
                        path_str + "\n\n"
                    )  # Write the formatted path to the file
                else:
                    file.write(
                        "No valid path found\n"
                    )  # Write a message if no valid path is found
