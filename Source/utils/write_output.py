def write_paths_to_file(file_path, vehicles):
    with open(file_path, "a") as file:
        for vehicle in vehicles:
            algorithm_name = vehicle.get_algorithm_name()
            file.write(f"{algorithm_name}:\n")
            file.write(f"{vehicle.name}\n")  # Write the vehicle name on the first line
            if vehicle.path:
                path_str = "  ".join(
                    [f"({y}, {x})" for y, x, _ in vehicle.path]
                )  # Each coordinate on a new line
                file.write(path_str + "\n\n")
            else:
                file.write("No valid path found\n")  # Handle cases with no valid path
