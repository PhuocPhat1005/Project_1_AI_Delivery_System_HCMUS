from collections import deque
from termcolor import colored #chi dung tam de test, sau nay doi thanh UI khac

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        # Read the first line and extract n, m, t, f
        first_line = file.readline().strip()
        n, m, t, f = map(int, first_line.split())

        # Read the next n lines to get the map information
        map_data = []
        for _ in range(n):
            line = file.readline().strip()
            map_data.append(line.split())

    return n, m, t, f, map_data

class cell:
    def __init__(self, y, x, value):
        self.y = y
        self.x = x
        self.value = value
        self.visited = {}
        self.parent = {}
    
class Board:
    def __init__(self, n, m, f, t, map_data, level = 1):
        self.n = n
        self.m = m
        self.f = f
        self.t = t
        self.map_data = map_data
        self.cells = []
        self.time = 0
        self.vehicle = []
        goals = []
        
        for i in range(n):
            self.cells.append(list())
            for j in range(m):
                self.cells[i].append(cell(y = i, x = j, value = map_data[i][j]))
                if 'S' in map_data[i][j]:
                    name = map_data[i][j]
                    if level == 1:
                        self.vehicle.append(vehicle_lev1(name, i, j, f))
                    # if level == 2:
                        # self.vehicle.append(vehicle_lev2(name, i, j, f))
                if 'G' in map_data[i][j]:
                    goal = map_data[i][j].replace('G', 'S')
                    goals.append((goal, i, j))
        
        for goal in goals:
            for vehicle in self.vehicle:
                if vehicle.name == goal[0]:
                    vehicle.goal_y = goal[1]
                    vehicle.goal_x = goal[2]
                    break
            
    def get_vehicle(self):
        return self.vehicle
    
    def get_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    def can_visit(self, name, y, x):
        if x < 0 or y < 0 or x >= self.n or y >= self.m:
            return False
        come_cell = self.cells[y][x]
        if name in come_cell.visited and come_cell.visited[name] == True:
            return False
        if come_cell.value == -1:
            return False
        return True

    def tracepath(self, name):
        vehicle = None
        for v in self.vehicle:
            if v.name == name:
                vehicle = v
                break
        path = []
        y, x = vehicle.goal_y, vehicle.goal_x
        while y != vehicle.start_y or x != vehicle.start_x:
            path.append((y, x))
            y, x = self.cells[y][x].parent[name]
        path.append((vehicle.start_y, vehicle.start_x))
        return path
        
    
    def test_input(self):
        print("Number of rows: ", self.n)
        print("Number of columns: ", self.m)
        print("Initial fuel: ", self.f)
        print("Time limit: ", self.t)
        print("Map data: ")
        for i in range(self.n):
            for j in range(self.m):
                print(self.cells[i][j].value, end = ' ')
            print('\n')
            
    def test_display_path(self, path):
        for i in range(self.n):
            for j in range(self.m):
                if (i, j) in path:
                    print(colored(self.map_data[i][j], 'green'), end = ' ')
                else:
                    print(self.map_data[i][j], end = ' ')
            print('\n')
            
class vehicle_base:
    def __init__(self, name, start_y, start_x, fuel):
        self.start_y = start_y
        self.start_x = start_x
        self.fuel = fuel
        self.current_fuel = fuel
        self.goal_x = -1
        self.goal_y = -1
        self.parrent = []
        self.time = 0
        self.name = name
        
class vehicle_lev1(vehicle_base):
    def __init__(self, name, start_y, start_x, fuel):
        super().__init__(name, start_y, start_x, fuel)
        
    def bfs(self, board):
        start_cell = board.cells[self.start_y][self.start_x]
        start_cell.visited[self.name] = True
        frontier = deque([start_cell]) #y, x start
        

        while frontier:
            # print(frontier)
            current_cell = frontier.popleft()
            if current_cell.y == self.goal_y and current_cell.x == self.goal_x:
                break
            
            y = [0, 0, 1, -1]
            x = [1, -1, 0, 0]
            for i in range(4):
                    new_y = current_cell.y + y[i]
                    new_x = current_cell.x + x[i]
                    if board.can_visit(self.name, new_y, new_x):
                        
                        board.cells[new_y][new_x].visited[self.name] = True
                        board.cells[new_y][new_x].parent[self.name] = (current_cell.y, current_cell.x)
                        frontier.append(board.cells[new_y][new_x])
                        
        return board.tracepath(self.name)


def main():
    n, m, t, f, map_data = read_input_file('input1_level1.txt')
    board = Board(n, m, f, t, map_data, level=1)
    vehicles = board.get_vehicle()
    for vehicle in vehicles:
        print(vehicle.name, f'\t\tStart: {vehicle.start_y}, {vehicle.start_x}', f'\t\tGoal: {vehicle.goal_y}, {vehicle.goal_x}')
    path = vehicles[1].bfs(board)
    board.test_display_path(path)
    # board.test_input()

if __name__ == "__main__":
    main()