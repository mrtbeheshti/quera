import work_place as w


class Mine(w.WorkPlace):
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        self.expertise = "mine"

    def calc_capacity(self):
        self.capacity = int((self.level) ** 2)

    def calc_costs(self):
        costs = w.Consts.BASE_PLACE_COST + w.Consts.LEVEL_MUL * self.level
        return costs
