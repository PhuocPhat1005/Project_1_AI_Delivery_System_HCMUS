class vehicle_base:
    def __init__(self, name, start_y, start_x, delivery_time, fuel):
        self.start_y = start_y
        self.start_x = start_x
        self.fuel = fuel
        self.current_fuel = fuel
        self.goal_x = -1
        self.goal_y = -1
        self.time = 0
        self.name = name
        self.current_x = start_x
        self.current_y = start_y
        self.tmp_start_x = start_x
        self.tmp_start_y = start_y
        self.tmp_goal_x = self.goal_x
        self.tmp_goal_y = self.goal_y
        self.path = []
        self.blocked_opposite = []  # blocked cells of opposite vehicle
        self.blocked_temp = (
            []
        )  # blocked temporary, need to wait 1 min to verhicle in that cell move

    def get_algorithm_name(self):
        return self.algorithm.__class__.__name__
