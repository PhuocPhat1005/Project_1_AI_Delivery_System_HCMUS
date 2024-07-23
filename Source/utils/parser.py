def parse_input(filename):
    with open(filename, "r") as file:
        n, m, t, f = map(int, file.readline().strip().split())
        grid = []
        for _ in range(n):
            row = list(
                map(
                    lambda x: int(x) if x.isdigit() or x == "-1" else x,
                    file.readline().strip().split(),
                )
            )
            grid.append(row)
        return n, m, t, f, grid
