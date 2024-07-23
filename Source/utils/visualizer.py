def visualize_path(grid, path):
    for x, y in path:
        if grid[x][y] == 0:
            grid[x][y] = "*"

    for row in grid:
        print(" ".join(map(str, row)))

    print("\nPath taken:")
    print(" -> ".join(f"({x}, {y})" for x, y in path))
