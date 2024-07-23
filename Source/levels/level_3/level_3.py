import sys
sys.path.insert(0, 'C:\\Users\\thaih\\Documents\\K22\\Nam_2\\HK3\\CoSoTriTueNhanTao\\Projects\\Project1\\22127174_22127322_22127388_22127441\\Source')

from main import *

class vehicle_level3(vehicle_base):
    def __init__(self, name, start_y, start_x, fuel):
        super().__init__(name, start_y, start_x, fuel)
        
    def bfs(self, board):
        start_cell = board.cells[self.start_y][self.start_x]
        start_cell.visited[self.name] = True
        frontier = deque([start_cell]) #y, x start
        

        while frontier:
            print(frontier)
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
    n, m, t, f, map_data = read_input_file('input1_level3.txt')
    board = Board(n, m, f, t, map_data, level=1)
    vehicles = board.get_vehicle()
    for vehicle in vehicles:
        print(vehicle.name, f'\t\tStart: {vehicle.start_y}, {vehicle.start_x}', f'\t\tGoal: {vehicle.goal_y}, {vehicle.goal_x}')
    path = vehicles[1].bfs(board)
    board.test_display_path(path)

if __name__ == "__main__":
    main()