def write_paths_to_file(file_path, vehicle_paths):
    with open(file_path, "w") as file:
        for vehicle_name, path in vehicle_paths.items():
            file.write(f"{vehicle_name}\n")  # Write the vehicle name on the first line
            if path:
                path_str = "  ".join(
                    [f"({y}, {x})" for y, x in path]
                )  # Each coordinate on a new line
                file.write(path_str + "\n")
            else:
                file.write("No valid path found\n")  # Handle cases with no valid path
