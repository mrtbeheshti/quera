import unittest
from vehicle import Vehicle
from ground_vehicle import GroundVehicle
from flying_vehicle import FlyingVehicle
from airplane import Airplane, B707


class InheritanceTest(unittest.TestCase):

    def test_vehicle(self):
        v = Vehicle(name="Car", price=5000, number_of_seats=5, max_speed=280)
        self.assertEqual(v.name, "Car")
        self.assertEqual(v.price, 5000)
        self.assertEqual(v.number_of_seats, 5)
        self.assertEqual(v.max_speed, 280)

    def test_ground_vehicle(self):
        v = GroundVehicle(name="Bicycle", price=100, number_of_seats=1, max_speed=60, number_of_wheels=2,
                          steering_wheel="Manual")
        self.assertTrue(issubclass(GroundVehicle, Vehicle))
        self.assertFalse(issubclass(GroundVehicle, FlyingVehicle))
        self.assertEqual(v.name, "Bicycle")
        self.assertEqual(v.price, 100)
        self.assertEqual(v.number_of_seats, 1)
        self.assertEqual(v.max_speed, 60)
        self.assertEqual(v.number_of_wheels, 2)
        self.assertEqual(v.steering_wheel, "Manual")

    def test_flying_vehicle(self):
        v = FlyingVehicle(name="Airplane", price=500000, number_of_seats=300, max_speed=400, fuel="Oil",
                          number_of_fins=2)
        self.assertTrue(issubclass(FlyingVehicle, Vehicle))
        self.assertFalse(issubclass(FlyingVehicle, GroundVehicle))
        self.assertEqual(v.name, "Airplane")
        self.assertEqual(v.price, 500000)
        self.assertEqual(v.number_of_seats, 300)
        self.assertEqual(v.max_speed, 400)
        self.assertEqual(v.fuel, "Oil")
        self.assertEqual(v.number_of_fins, 2)

    def test_airplane(self):
        v = Airplane(name="Airplane", price=500000, number_of_seats=300, max_speed=400, number_of_wheels=10,
                     steering_wheel="Manual", fuel="Oil", number_of_fins=2, airline="Quera Air", number_of_crew=65,
                     captain="Bagher")
        self.assertTrue(issubclass(Airplane, Vehicle))
        self.assertTrue(issubclass(Airplane, FlyingVehicle))
        self.assertTrue(issubclass(Airplane, GroundVehicle))
        self.assertEqual(v.name, "Airplane")
        self.assertEqual(v.price, 500000)
        self.assertEqual(v.number_of_seats, 300)
        self.assertEqual(v.max_speed, 400)
        self.assertEqual(v.number_of_wheels, 10)
        self.assertEqual(v.steering_wheel, "Manual")
        self.assertEqual(v.fuel, "Oil")
        self.assertEqual(v.number_of_fins, 2)
        self.assertEqual(v.airline, "Quera Air")
        self.assertEqual(v.number_of_crew, 65)
        self.assertEqual(v.captain, "Bagher")

    def test_b_707(self):
        v = B707(name="SAliB", price=850000, number_of_seats=850, max_speed=500, number_of_wheels=18,
                 steering_wheel="Manual", fuel="Oil", number_of_fins=2, airline="Quera Air", number_of_crew=65,
                 captain="Bagher")
        self.assertTrue(issubclass(B707, Vehicle))
        self.assertTrue(issubclass(B707, FlyingVehicle))
        self.assertTrue(issubclass(B707, GroundVehicle))
        self.assertTrue(issubclass(B707, B707))
        self.assertEqual(v.name, "SAliB")
        self.assertEqual(v.price, 850000)
        self.assertEqual(v.number_of_seats, 850)
        self.assertEqual(v.max_speed, 500)
        self.assertEqual(v.number_of_wheels, 18)
        self.assertEqual(v.steering_wheel, "Manual")
        self.assertEqual(v.fuel, "Oil")
        self.assertEqual(v.number_of_fins, 2)
        self.assertEqual(v.airline, "Quera Air")
        self.assertEqual(v.number_of_crew, 65)
        self.assertEqual(v.captain, "Bagher")


if __name__ == '__main__':
    unittest.main()
