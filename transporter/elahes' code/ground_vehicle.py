import vehicle

class GroundVehicle(vehicle.Vehicle):
    def __init__(self, number_of_wheels, steering_wheel, **kwargs):
        self.number_of_wheels = number_of_wheels
        self.steering_wheel = steering_wheel
        super().__init__(**kwargs)