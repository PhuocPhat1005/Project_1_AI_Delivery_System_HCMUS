import heapq
import random
from utils.vehicle_base import vehicle_base
from GUI.gui import *


class vehicle_level4(vehicle_base):
    def __init__(self, name, start_y, start_x, time, fuel):
        super().__init__(name, start_y, start_x, time, fuel)
        self.is_regenerated = False
        self.final_path = []
        self.reason_not_found = "No path found"
        
    def regenerate(self, board):
        self.is_regenerated = True
        board.cells[self.start_y][self.start_x].raw_value = "0"

        board.cells[self.goal_y][self.goal_x].raw_value = self.name
        try:
            board.cells[self.goal_y][self.goal_x].value = float(
                board.cells[self.goal_y][self.goal_x].raw_value
            )
        except:
            self.value = 0

        self.start_y = self.current_y
        self.start_x = self.current_x
        self.goal_y = random.randint(0, board.n - 1)
        self.goal_x = random.randint(0, board.m - 1)
        while (
            board.get_distance(self.start_x, self.start_y, self.goal_x, self.goal_y) > 5
            or board.cells[self.goal_y][self.goal_x].raw_value != "0"
        ):
            self.goal_y = random.randint(0, board.n - 1)
            self.goal_x = random.randint(0, board.m - 1)
        self.path = []

        # while(self.path == [] or board.cells[self.goal_x][self.goal_y].raw_value == '0'):
        # self.path = self.process_lev3(board)

        board.cells[self.goal_y][self.goal_x].raw_value = self.name.replace("S", "G")
        board.generate_heuristic(self.name)
        board.generate_time(self.name)
        board.generate_cost(self.name)
        # board.generate_fuel(self.name)
        board.generate_visited(self.name)
        board.generate_parent(self.name)
        self.tmp_start_x = self.start_x
        self.tmp_start_y = self.start_y
        self.tmp_goal_x = self.goal_x
        self.tmp_goal_y = self.goal_y

        self.blocked_opposite = []
        self.blocked_temp = []

    def a_star(self, board):
        # board.cells[self.tmp_goal_y][self.tmp_goal_x].visited[self.name] = False
        # while board.cells[self.tmp_goal_y][self.tmp_goal_x].visited[self.name] == False:

        # print("A star")
        # print("Name: ", self.name)
        # print("OP Cells: ", self.blocked_opposite)
        # print("Temp Cells: ", self.blocked_temp)

        board.generate_visited(self.name)
        board.generate_parent(self.name)
        board.generate_cost(self.name)
        board.generate_heuristic(self.name)
        if self.tmp_start_x == self.start_x and self.tmp_start_y == self.start_y:
            board.generate_time(self.name)
            # board.generate_fuel(self.name)

        for cell in self.blocked_opposite:
            board.cells[cell[0]][cell[1]].visited[self.name] = True
        # for i in range(1, len(self.blocked_temp)):
        #     board.cells[self.blocked_temp[i-1][0]][self.blocked_temp[i-1][1]].time[self.name] += 1
        #     print("Cell: ", self.blocked_temp[i-1][0], self.blocked_temp[i-1][1], "Time: ", board.cells[self.blocked_temp[i-1][0]][self.blocked_temp[i-1][1]].time[self.name])

        # for i in range(board.n):
        #     for j in range(board.m):
        #         print(board.cells[i][j].raw_value, end = ' ')
        #     print()

        if "F" in board.cells[self.current_y][self.current_x].raw_value:
            self.current_fuel = self.fuel

        start_cell = board.cells[self.tmp_start_y][self.tmp_start_x]
        start_cell.visited[self.name] = True
        start_cell.cost[self.name] = 0
        start_cell.fuel[self.name] = self.current_fuel
        if self.tmp_start_x == self.start_x and self.tmp_start_y == self.start_y:
            start_cell.time[self.name] = 1
        else:
            start_cell.time[self.name] = start_cell.time[self.name]

        start_cell.current_vehicle = self.name

        # current_f = start_cell.cost[self.name] + start_cell.heuristic[self.name]
        start_cell.visited[self.name] = True
        # start_cell.compare_value = current_f
        # frontier = [(current_f, start_cell)]
        frontier = [(start_cell)]

        # while frontier and self.current_fuel > 0:
        while frontier:
            # self.current_fuel -= 1 #chi di nhanh tot nhat nen tru fuel o day, tru xong moi di chuyen
            # for cell in frontier:
            #     print(cell[1].y, cell[1].x, cell[1].compare_value, end = ' ')
            # print()
            # current_f, current_cell = heapq.heappop(frontier)
            current_cell = heapq.heappop(frontier)
            self.current_fuel = board.cells[current_cell.y][current_cell.x].fuel[
                self.name
            ]
            # board.cells[current_cell.y][current_cell.x].current_vehicle = None
            y = [0, 0, 1, -1]
            x = [1, -1, 0, 0]
            for i in range(4):
                new_y = current_cell.y + y[i]
                new_x = current_cell.x + x[i]

                # in_block = False
                if board.can_visit(self.name, new_y, new_x) == True:
                    for cell in self.blocked_temp:
                        if new_y == cell[0] and new_x == cell[1]:
                            board.cells[current_cell.y][current_cell.x].time[
                                self.name
                            ] += 1
                            # print("Current cell: ", current_cell.y, current_cell.x, "Time: ", board.cells[current_cell.y][current_cell.x].time[self.name])
                            # print(board.cells[current_cell.y][current_cell.x].time[self.name] + 1 + board.cells[new_y][new_x].value)

                    new_cost = (
                        board.cells[current_cell.y][current_cell.x].cost[self.name] + 1
                    )
                    new_t = (
                        board.cells[current_cell.y][current_cell.x].time[self.name]
                        + 1
                        + board.cells[new_y][new_x].value
                    )

                    new_fuel = (
                        board.cells[current_cell.y][current_cell.x].fuel[self.name] - 1
                    )

                    if "F" in board.cells[new_y][new_x].raw_value:
                        new_t += float(
                            board.cells[new_y][new_x].raw_value.replace("F", "")
                        )
                        new_fuel = self.fuel

                    # for cell in self.blocked_opposite:
                    #     if new_y == cell[0] and new_x == cell[1]:
                    #         in_block = True
                    #         break

                    if (
                        new_cost < board.cells[new_y][new_x].cost[self.name]
                        and new_fuel >= 0
                        and new_t <= min(board.t + 1, board.S_vehicle_time)
                    ):
                        # if (new_y, new_x) in self.blocked_temp:
                        #     board.cells[current_cell.y][current_cell.x].time[self.name] += 1
                        board.cells[new_y][new_x].current_vehicle = self.name
                        board.cells[new_y][new_x].visited[self.name] = True
                        board.cells[new_y][new_x].cost[self.name] = new_cost
                        board.cells[new_y][new_x].time[self.name] = new_t
                        board.cells[new_y][new_x].fuel[self.name] = new_fuel
                        board.cells[new_y][new_x].parent[self.name] = (
                            current_cell.y,
                            current_cell.x,
                        )
                        # f = new_cost + board.cells[new_y][new_x].heuristic[self.name]
                        # board.cells[new_y][new_x].compare_value = f
                        # heapq.heappush(frontier, (f, board.cells[new_y][new_x]))
                        heapq.heappush(frontier, (board.cells[new_y][new_x]))
                    else:
                        if new_fuel < 0:
                            self.reason_not_found = "Not enough fuel"
                        if new_t > min(board.t + 1, board.S_vehicle_time):
                            self.reason_not_found = "Not enough time"
                            
            if current_cell.y == self.tmp_goal_y and current_cell.x == self.tmp_goal_x:
                # board.cells[self.tmp_goal_y][self.tmp_goal_x].visited[self.name] = True
                break

        path = []
        if board.cells[self.tmp_goal_y][self.tmp_goal_x].visited[self.name] == True:
            # tmp_path = board.tracepath(self.name)
            # if len(tmp_path) <= self.fuel:
            #     path = tmp_path
            path = board.tracepath(self.name)

        if (
            path == []
            or self.tmp_goal_x != self.goal_x
            and self.goal_y != self.tmp_goal_y
        ):
            board.cells[self.goal_y][self.goal_x].visited[self.name] = False
        return path

    def find_best_goal(self, board):
        if board.fuel_stations == []:
            self.tmp_goal_y = -1
            self.tmp_goal_x = -1
            return
        best_heuristic = float("inf")
        for fuel_station in board.fuel_stations:
            if (
                self.tmp_goal_x == fuel_station[1]
                and self.tmp_goal_y == fuel_station[0]
            ):
                continue
            # print ("fuel_station: ", fuel_station[0], fuel_station[1])
            # print (board.cells[fuel_station[0]][fuel_station[1]].heuristic[self.name])
            # print (board.cells[fuel_station[0]][fuel_station[1]].visited[self.name])
            if (
                board.cells[fuel_station[0]][fuel_station[1]].heuristic[self.name]
                < best_heuristic
            ):
                best_heuristic = board.cells[fuel_station[0]][
                    fuel_station[1]
                ].heuristic[self.name]
                new_y = fuel_station[0]
                new_x = fuel_station[1]
        if (
            self.tmp_goal_x == self.goal_x
            and self.tmp_goal_y == self.goal_y
            and self.tmp_start_x == self.start_x
            and self.tmp_start_y == self.start_y
        ):
            self.tmp_goal_y = new_y
            self.tmp_goal_x = new_x
        else:
            self.tmp_start_y = self.tmp_goal_y
            self.tmp_start_x = self.tmp_goal_x
            self.tmp_goal_y = new_y
            self.tmp_goal_x = new_x

    def find_best_path(self, board):

        board.cells[self.goal_y][self.goal_x].visited[self.name] = False

        self.tmp_start_y = self.current_y
        self.tmp_start_x = self.current_x
        self.tmp_goal_y = self.goal_y
        self.tmp_goal_x = self.goal_x

        paths = []
        flag = False
        while board.cells[self.goal_y][self.goal_x].visited[self.name] == False:
            path = self.a_star(board)

            # print("Start: ", self.current_y, self.current_x)
            # print("Tmp goal: ", self.tmp_goal_y, self.tmp_goal_x)

            # print(path)
            if path != []:
                flag = False
                path = board.path_time_fuel(self.name, path)
                paths.append(path)
                self.tmp_start_y = self.tmp_goal_y
                self.tmp_start_x = self.tmp_goal_x

                self.tmp_goal_y = (
                    self.goal_y
                )  # Neu tim thay path, tim tiep tuc tu vi tri hien tai den goal
                self.tmp_goal_x = self.goal_x

                # print("Path: ", path)
            else:
                if flag == True:
                    return []
                self.find_best_goal(board)  # Neu tim k duoc, tim fuel tot nhat
                if self.tmp_goal_y == -1 and self.tmp_goal_x == -1:
                    return []
                flag = True
        # self.current_y = self.start_y
        # self.current_x = self.start_x

        # print("TMP START: ", self.tmp_start_y, self.tmp_start_x)
        # print("TMP GOAL: ", self.tmp_goal_y, self.tmp_goal_x)

        joined_path = []
        for path in paths:
            joined_path.extend(path)
        joined_path = board.unique_path(joined_path)
        # print("Joined path: ", joined_path)
        return joined_path


def process_lev4(board):

    vehicles = board.get_vehicle()
    S_vehicle = vehicles[0]

    # paths = []
    # for vehicle in vehicles:
    #     path = vehicle.find_best_path(board)
    #     paths.append(path)
    # board.test_display_path(paths)
    # return

    flag = True
    board.cells[S_vehicle.goal_y][S_vehicle.goal_x].visited[S_vehicle.name] = False
    # while S_vehicle.current_y != S_vehicle.goal_y or S_vehicle.current_x != S_vehicle.goal_x:
    # cnt = 0
    time = 0

    while flag:
        flag = False
        paths = []
        for vehicle in vehicles:
            if (
                vehicle.current_x == vehicle.start_x
                and vehicle.current_y == vehicle.start_y
            ):
                path = vehicle.find_best_path(board)
                if path == [] and vehicle.name == S_vehicle.name:
                    return []
                if S_vehicle.name == vehicle.name:
                    board.S_vehicle_time = path[-1][2]
                vehicle.path = path
            paths.append(path)

        for cells in board.cells:
            for cell in cells:
                cell.current_vehicle = None

        for vehicle in vehicles:
            board.cells[vehicle.current_y][
                vehicle.current_x
            ].current_vehicle = vehicle.name
            if vehicle.final_path == []:
                vehicle.final_path.append(vehicle.path)

        while time <= board.t:
            if flag == True:
                break

            for vehicle in vehicles:
                # print("Vehicle name: ", vehicle.name, "current_y: ", vehicle.current_y, "current_x: ", vehicle.current_x)

                for i in range(len(vehicle.path) - 1):
                    if (
                        vehicle.path[i][2] == time
                        and vehicle.blocked_opposite == []
                        and vehicle.blocked_temp == []
                    ):
                        # print("Time here: ", vehicle.path[i][2])
                        next_y, next_x = vehicle.path[i + 1][0], vehicle.path[i + 1][1]
                        # print("next_y: ", next_y, "next_x: ", next_x, "vehicle: ", board.cells[next_y][next_x].current_vehicle)
                        if (
                            board.cells[next_y][next_x].current_vehicle != None
                            and vehicle.name != S_vehicle.name
                        ):
                            flag = True
                            name = board.cells[next_y][next_x].current_vehicle
                            for v in vehicles:
                                if v.name == name:
                                    try:
                                        next_next_y = v.path[i + 2][0]
                                        next_next_x = v.path[i + 2][1]
                                    except:
                                        next_next_y = v.goal_y
                                        next_next_x = v.goal_x
                                        # next_next_x = v.current_x
                                        # next_next_y = v.current_y

                            if (
                                vehicle.current_x == next_next_x
                                or vehicle.current_y == next_next_y
                            ):
                                vehicle.blocked_opposite.append(vehicle.path[i + 1])
                                print(
                                    "Blocked cell OP: ",
                                    vehicle.path[i + 1],
                                    "by ",
                                    name,
                                    "current: ",
                                    vehicle.name,
                                )
                            else:
                                vehicle.blocked_temp.append(vehicle.path[i + 1])
                                print(
                                    "Blocked cell Temp: ",
                                    vehicle.path[i + 1],
                                    "by ",
                                    name,
                                    "current: ",
                                    vehicle.name,
                                )
                        else:
                            if (
                                board.get_distance(
                                    vehicle.current_x, vehicle.current_y, next_x, next_y
                                )
                                == 1
                            ):
                                board.cells[vehicle.current_y][
                                    vehicle.current_x
                                ].current_vehicle = None
                                vehicle.current_y, vehicle.current_x = next_y, next_x
                                board.cells[vehicle.current_y][
                                    vehicle.current_x
                                ].current_vehicle = vehicle.name

            print("Time: ", time)
            for vehicle in vehicles:
                print("--------------------------------")
                print("Name: ", vehicle.name)
                print("Start: ", vehicle.start_y, vehicle.start_x)
                print("Goal: ", vehicle.goal_y, vehicle.goal_x)
                print("Current: ", vehicle.current_y, vehicle.current_x)
                vehicle.current_fuel = board.cells[vehicle.current_y][
                    vehicle.current_x
                ].fuel[vehicle.name]
                print("Fuel: ", vehicle.current_fuel)
                print("Path: ", vehicle.path)
                if (
                    vehicle.path == []
                    or vehicle.blocked_opposite != []
                    or vehicle.blocked_temp != []
                ):
                    print("Need find best path")
                    vehicle.path = vehicle.find_best_path(board)
                    if vehicle.path != []:
                        if vehicle.path not in vehicle.final_path:
                            if (
                                vehicle.current_x == vehicle.start_x
                                and vehicle.current_y == vehicle.start_y
                            ):
                                vehicle.final_path.append(vehicle.path)
                                print("aaaaaaaaa")
                            else:
                                print("bbbbbbbbb")
                                tmp_path = []
                                tmp_cell = vehicle.path[0]
                                for cell in vehicle.final_path[-1]:
                                    if cell != tmp_cell:
                                        tmp_path.append(cell)
                                    else:
                                        break
                                for cell in vehicle.path:
                                    tmp_path.append(cell)

                                print(len(vehicle.final_path))

                                vehicle.final_path[-1] = tmp_path
                paths.append(vehicle.path)

                print("Vehicle final path: ", vehicle.final_path)

            board.test_display_path(paths)
            # map_UI(board.n, board.m, board.t, board.f, board.map_data, 4, "", len(vehicles))
            # path_UI(board.n, board.m, board.t, board.f, board.map_data, paths, cell_side)
            # map_UI(n, m, t, f, board.map_data, 4, "", len(vehicles))
            # path_UI(n, m, t, f, board.map_data, paths, cell_side)

            # path_UI(board.n, board.m, board.t, board.f, board.map_data, paths, cell_side)
            # map_UI(board.n, board.m, board.t, board.f, board.map_data, 4, "")
            if (
                S_vehicle.current_y == S_vehicle.goal_y
                and S_vehicle.current_x == S_vehicle.goal_x
            ):
                return paths

            for vehicle in vehicles:
                if vehicle.name != S_vehicle.name:
                    if (
                        vehicle.current_y == vehicle.goal_y
                        and vehicle.current_x == vehicle.goal_x
                    ) or vehicle.path == []:
                        # print(
                        #     "Time: ",
                        #     time,
                        #     " Vehicle: ",
                        #     vehicle.name,
                        #     "Start: ",
                        #     vehicle.start_y,
                        #     vehicle.start_x,
                        #     "Goal: ",
                        #     vehicle.goal_y,
                        #     vehicle.goal_x,
                        #     "Current: ",
                        #     vehicle.current_y,
                        #     vehicle.current_x,
                        # )
                        vehicle.regenerate(board)

            paths = []

            time += 1
            # cnt += 1
            # if cnt == 10:
            #     break
