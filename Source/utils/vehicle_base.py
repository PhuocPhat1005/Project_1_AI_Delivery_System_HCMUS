class vehicle_base:
    def __init__(self, name, start_y, start_x, delivery_time, fuel):
        self.start_y = start_y
        self.start_x = start_x
        self.fuel = fuel
        self.current_fuel = fuel
        self.goal_x = -1
        self.goal_y = -1
        self.delivery_time = delivery_time
        self.current_time = delivery_time
        self.name = name
        self.tmp_start_x = start_x
        self.tmp_start_y = start_y
        self.tmp_goal_x = self.goal_x
        self.tmp_goal_y = self.goal_y
