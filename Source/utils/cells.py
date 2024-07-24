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
        if self.time[self.current_vehicle] < other.time[self.current_vehicle]:
            return True
        if self.cost[self.current_vehicle] < other.cost[other.current_vehicle]:
            return True
        if (
            self.heuristic[self.current_vehicle]
            < other.heuristic[other.current_vehicle]
        ):
            return True
        if self.fuel[self.current_vehicle] > other.fuel[other.current_vehicle]:
            return True
        return False
