import unittest, math
from work_place import *


class ScoreListTest(unittest.TestCase):

    def test_a_scenario(self):
        w = WorkPlace("quera")
        w.expertise = "mine"

        def f(self):
            self.capacity += 1

        WorkPlace.calc_capacity = f

        w.upgrade()

        class Person:
            pass

        p = Person()
        p.work_place = None
        w.hire(p)

        self.assertEqual(w.employees[0], p)
        self.assertEqual(w.level, 2)
        self.assertEqual(w.capacity, 2)
        self.assertEqual(w.name, "quera")
        self.assertEqual(w.get_expertise(), "mine")
        self.assertEqual(w.get_price(), Consts.BASE_PRICE["mine"])

        WorkPlace.instances = []

        def f(a):
            def g():
                return a

            return g

        WorkPlace("new workplace").calc_costs = f(-10)
        WorkPlace("new workplace").calc_costs = f(-20)
        WorkPlace("new workplace").calc_costs = f(-30)

        self.assertEqual(60, WorkPlace.calc_all())
