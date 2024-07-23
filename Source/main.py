from collections import deque
from termcolor import colored #chi dung tam de test, sau nay doi thanh UI khac
import heapq

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
    def __init__(self, y, x, raw_value):
        self.y = y
        self.x = x
        self.raw_value = raw_value
        try:
            self.value = float(raw_value)
        except:
            self.value = 0
        self.visited = {}
        self.parent = {}
        self.cost = {}
        self.heuristic = {}
        self.fuel = {}
        self.time = {}
        self.current_vehicle = None
        
    def __lt__(self, other):
        if self.cost[self.current_vehicle] == other.cost[other.current_vehicle]:
            if self.fuel[self.current_vehicle] == other.fuel[other.current_vehicle]:
                if self.time[self.current_vehicle] == other.time[other.current_vehicle]:
                    return self.heuristic[self.current_vehicle] < other.heuristic[other.current_vehicle]
                return self.time[self.current_vehicle] < other.time[other.current_vehicle]
            return self.fuel[self.current_vehicle] < other.fuel[other.current_vehicle]
        return self.cost[self.current_vehicle] < other.cost[other.current_vehicle]

    # def __repr__(self):
    #     return f"Cell({self.raw_value})"

def fought_cells(x, y, paths):
    for i, path in enumerate(paths):
        if (x, y) in path:
            return i
    return -1
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
        self.fuel_stations = []
        
        for i in range(n):
            self.cells.append(list())
            for j in range(m):
                self.cells[i].append(cell(y = i, x = j, raw_value = map_data[i][j]))
                if 'S' in map_data[i][j]:
                    name = map_data[i][j]
                    if level == 1:
                        self.vehicle.append(vehicle_lev1(name, i, j, f))
                    # if level == 2:
                    #     self.vehicle.append(vehicle_lev2(name, i, j, f))
                    # if level == 3:
                    #     self.vehicle.append(vehicle_lev3(name, i, j, f))
                    if level == 4:
                        self.vehicle.append(vehicle_lev4(name, i, j, f))
                if 'G' in map_data[i][j]:
                    goal = map_data[i][j].replace('G', 'S')
                    goals.append((goal, i, j))
                if 'F' in map_data[i][j]:
                    self.fuel_stations.append((i, j))
        
        for goal in goals:
            for vehicle in self.vehicle:
                if vehicle.name == goal[0]:
                    vehicle.goal_y = goal[1]
                    vehicle.goal_x = goal[2]
                    vehicle.tmp_goal_y = goal[1]
                    vehicle.tmp_goal_x = goal[2]
                    break
    
    def generate_visited(self, name):
        for i in range(self.n):
            for j in range(self.m):
                self.cells[i][j].visited[name] = False
                    
    def generate_parent(self, name):
        for i in range(self.n):
            for j in range(self.m):
                    self.cells[i][j].parent[name] = (-1, -1)     
                    
    def generate_heuristic(self, name):
        for i in range(self.n):
            for j in range(self.m):
                for vehicle in self.vehicle:
                    if vehicle.name == name:
                        # self.cells[i][j].heuristic[name] = 0
                        self.cells[i][j].heuristic[name] = self.get_distance(j, i, vehicle.goal_x, vehicle.goal_y)
                        if 'F' in self.cells[i][j].raw_value:
                            # self.cells[i][j].heuristic[name] += self.get_distance(j, i, vehicle.goal_x, vehicle.goal_y) - vehicle.fuel
                            self.cells[i][j].heuristic[name] += int(self.cells[i][j].raw_value.replace('F', ''))
                        
    def generate_cost(self, name):
        for i in range(self.n):
            for j in range(self.m):
                    self.cells[i][j].cost[name] = float('inf')
    
    def generate_fuel(self, name):
        for i in range(self.n):
            for j in range(self.m):
                    self.cells[i][j].fuel[name] = float('inf')
                    
    def generate_time(self, name):
        for i in range(self.n):
            for j in range(self.m):
                    self.cells[i][j].time[name] = float('inf')
                    
    def get_vehicle(self):
        return sorted(self.vehicle, key=lambda vehicle: vehicle.name)

    def get_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    def can_visit(self, name, y, x):
        if x < 0 or y < 0 or x >= self.n or y >= self.m:
            return False
        come_cell = self.cells[y][x]
        if come_cell.visited[name] == True:
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
        y, x = vehicle.tmp_goal_y, vehicle.tmp_goal_x
        while y != vehicle.tmp_start_y or x != vehicle.tmp_start_x:
            path.append((y, x))
            y, x = self.cells[y][x].parent[name]
        path.append((vehicle.tmp_start_y, vehicle.tmp_start_x))
        return path[::-1] 
                                  
    def test_input(self):
        print("Number of rows: ", self.n)
        print("Number of columns: ", self.m)
        print("Initial fuel: ", self.f)
        print("Time limit: ", self.t)
        print("Map data: ")
        for i in range(self.n):
            for j in range(self.m):
                print(f"{self.cells[i][j].raw_value:5}", end=' ')
            print('\n')
    

            
    def test_display_path(self, paths):
        colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]
        for i in range(self.n):
            for j in range(self.m):
                k = fought_cells(i, j, paths)
                if k != -1:
                    print(colored(f"{self.cells[i][j].raw_value:5}", colors[k]), end = ' ')
                else:
                    print(f"{self.cells[i][j].raw_value:5}", end=' ')
            print('\n')
            
class vehicle_base:
    def __init__(self, name, start_y, start_x, fuel):
        self.start_y = start_y
        self.start_x = start_x
        self.fuel = fuel
        self.current_fuel = fuel
        self.goal_x = -1
        self.goal_y = -1
        self.time = 0
        self.name = name
        self.tmp_start_x = start_x
        self.tmp_start_y = start_y
        self.tmp_goal_x = self.goal_x
        self.tmp_goal_y = self.goal_y
        
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
                    if board.can_visit(self.name, new_y, new_x) == True:
                        board.cells[new_y][new_x].visited[self.name] = True
                        board.cells[new_y][new_x].parent[self.name] = (current_cell.y, current_cell.x)
                        frontier.append(board.cells[new_y][new_x])
                        
        return board.tracepath(self.name)

class vehicle_lev4(vehicle_base):
    def __init__(self, name, start_y, start_x, fuel):
        super().__init__(name, start_y, start_x, fuel)
            
    def a_star(self, board):
        # board.cells[self.tmp_goal_y][self.tmp_goal_x].visited[self.name] = False
        # while board.cells[self.tmp_goal_y][self.tmp_goal_x].visited[self.name] == False:
        
        board.generate_visited(self.name)
        board.generate_parent(self.name)
        board.generate_cost(self.name)
        board.generate_heuristic(self.name)
        board.generate_fuel(self.name)
        board.generate_time(self.name)
        
        # for i in range(board.n):
        #     for j in range(board.m):
        #         print(board.cells[i][j].raw_value, end = ' ')
        #     print()
            
        self.current_fuel = self.fuel
        
        start_cell = board.cells[self.tmp_start_y][self.tmp_start_x]
        start_cell.visited[self.name] = True
        start_cell.cost[self.name] = 0
        start_cell.fuel[self.name] = self.fuel
        start_cell.time[self.name] = 0
        start_cell.current_vehicle = self.name
        
        current_f = start_cell.cost[self.name] + start_cell.heuristic[self.name]
        start_cell.visited[self.name] = True
        start_cell.compare_value = current_f
        frontier = [(current_f, start_cell)]

        # while frontier and self.current_fuel > 0:
        while frontier:
            # self.current_fuel -= 1 #chi di nhanh tot nhat nen tru fuel o day, tru xong moi di chuyen
            # for cell in frontier:
            #     print(cell[1].y, cell[1].x, cell[1].compare_value, end = ' ')
            # print()
            current_f, current_cell = heapq.heappop(frontier)
            y = [0, 0, 1, -1]
            x = [1, -1, 0, 0]
            for i in range(4):
                new_y = current_cell.y + y[i]
                new_x = current_cell.x + x[i]
                    
                if board.can_visit(self.name, new_y, new_x) == True:
                    new_cost = board.cells[current_cell.y][current_cell.x].cost[self.name] + 1
                    new_t = board.cells[current_cell.y][current_cell.x].time[self.name] + 1 + board.cells[new_y][new_x].value
                    if 'F' in board.cells[new_y][new_x].raw_value:
                        new_t += int(board.cells[new_y][new_x].raw_value.replace('F', ''))
                    new_fuel = board.cells[current_cell.y][current_cell.x].fuel[self.name] - 1
                    if new_cost < board.cells[new_y][new_x].cost[self.name] and new_fuel >= 0 and new_t <= board.t:
                        board.cells[new_y][new_x].current_vehicle = self.name
                        board.cells[new_y][new_x].visited[self.name] = True
                        board.cells[new_y][new_x].cost[self.name] = new_cost
                        board.cells[new_y][new_x].time[self.name] = new_t
                        board.cells[new_y][new_x].fuel[self.name] = new_fuel
                        board.cells[new_y][new_x].parent[self.name] = (current_cell.y, current_cell.x)
                        f = new_cost + board.cells[new_y][new_x].heuristic[self.name]
                        board.cells[new_y][new_x].compare_value = f
                        heapq.heappush(frontier, (f, board.cells[new_y][new_x]))
                        
            if current_cell.y == self.tmp_goal_y and current_cell.x == self.tmp_goal_x:
                board.cells[self.tmp_goal_y][self.tmp_goal_x].visited[self.name] = True
                break
        
        path = []
        if board.cells[self.tmp_goal_y][self.tmp_goal_x].visited[self.name] == True:
            # tmp_path = board.tracepath(self.name)
            # if len(tmp_path) <= self.fuel:
            #     path = tmp_path
            path = board.tracepath(self.name)
            
        if path == [] or self.tmp_goal_x != self.goal_x and self.goal_y != self.tmp_goal_y:
            board.cells[self.goal_y][self.goal_x].visited[self.name] = False
        return path

    def find_best_goal(self, board):
        
        best_heuristic = float('inf')
        for fuel_station in board.fuel_stations:
            if self.tmp_goal_x == fuel_station[1] and self.tmp_goal_y == fuel_station[0]:
                continue
            # print ("fuel_station: ", fuel_station[0], fuel_station[1])
            # print (board.cells[fuel_station[0]][fuel_station[1]].heuristic[self.name])
            # print (board.cells[fuel_station[0]][fuel_station[1]].visited[self.name])
            if board.cells[fuel_station[0]][fuel_station[1]].heuristic[self.name] < best_heuristic:
                best_heuristic = board.cells[fuel_station[0]][fuel_station[1]].heuristic[self.name]
                new_y = fuel_station[0]
                new_x = fuel_station[1]
        if self.tmp_goal_x == self.goal_x and self.tmp_goal_y == self.goal_y and self.tmp_start_x == self.start_x and self.tmp_start_y == self.start_y:
            self.tmp_goal_y = new_y
            self.tmp_goal_x = new_x
        else:
            self.tmp_start_y = self.tmp_goal_y
            self.tmp_start_x = self.tmp_goal_x
            self.tmp_goal_y = new_y
            self.tmp_goal_x = new_x


    def process(self, board):

        board.cells[self.goal_y][self.goal_x].visited[self.name] = False
        paths = []
        while board.cells[self.goal_y][self.goal_x].visited[self.name] == False:
            path = self.a_star(board)
            
            # print(path)
            if path != []:
                paths.append(path)
                
                self.tmp_start_y = self.tmp_goal_y
                self.tmp_start_x = self.tmp_goal_x
                
                self.tmp_goal_y = self.goal_y#Neu tim thay path, tim tiep tuc tu vi tri hien tai den goal
                self.tmp_goal_x = self.goal_x
            else:
                self.find_best_goal(board)#Neu tim k duoc, tim fuel tot nhat
                
            # print("Start: ", self.tmp_start_y, self.tmp_start_x)
            # print("Tmp goal: ", self.tmp_goal_y, self.tmp_goal_x)
            
        joined_path = []
        for path in paths:
            joined_path.extend(path)
        return joined_path
        
def main():
    n, m, t, f, map_data = read_input_file('Source//input1_level1.txt')
    board = Board(n, m, f, t, map_data, level=4)
    vehicles = board.get_vehicle()
    paths = []
    for vehicle in vehicles:
        print(vehicle.name, f'\t\tStart: {vehicle.start_y}, {vehicle.start_x}', f'\t\tGoal: {vehicle.goal_y}, {vehicle.goal_x}')
        path = vehicle.process(board)
        # print (path)
        paths.append(path)
    # print(path)
    board.test_display_path(paths)
    print("Done")
    # board.test_input()

if __name__ == "__main__":
    main()
