import work_place
import math


class School(work_place.WorkPlace):
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        self.expertise = "school"

    def calc_capacity(self):
        self.capacity = math.floor(math.sqrt(self.level))

    def calc_costs(self):
        costs = work_place.Consts.BASE_PLACE_COST * math.floor(math.sqrt(self.level))
        return costs
