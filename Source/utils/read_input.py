def read_input_file(filename: str):
    """
    Reads the input file and extracts the city map and relevant parameters.

    Args:
        filename (str): the name of the input file to read.

    Returns:
        tuple: a tuple containing the following elements:
            - n (int): the number of rows in the city map.
            - m (int): the number of columns in the city map.
            - t (int): the commited delivery time.
            - f (int): the fuel tank capacity.
            - map_data(list of lists): a 2D list representing the city map, where each element is either:
                - 0: space that the delivery vehicle can move into.
                - -1: impassable space (buildings, walls, and objects).
                - 'S': the starting location of the delivery vehicle.
                - 'G': the goal location (customer's location).
                - Positive integers representing the toll booth times.
    """
    with open(filename, "r") as file:  # Open the file in the read mode
        # Read the first line and extract n, m, t, f
        first_line = (
            file.readline().strip()
        )  # Read the first line and strip any leading / trailling whitespace
        n, m, t, f = map(
            int, first_line.split()
        )  # Split the first line into four integers: n, m, t, f

        # Read the next n lines to get the map information
        map_data = []  # Initialize an empty list to store the map data
        for _ in range(n):
            line = file.readline().strip()
            map_data.append(line.split())
        return n, m, t, f, map_data  # Return the extracted values as a tuple.
