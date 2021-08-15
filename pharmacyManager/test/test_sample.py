import unittest, math
from solution import Drug, Pharmacy


class DrugTest(unittest.TestCase):

    def setUp(self):
        self.drug1 = Drug("T1", 10, 1000)
        self.drug2 = Drug("T2", 20, 2000)
        self.drug3 = Drug("T3", 30, 3000)
        self.drug4 = Drug("T4", 40, 4000)
        self.store1 = Pharmacy("S1")
        self.store2 = Pharmacy("S2")

    def test_drug_constructor(self):
        self.assertEqual(self.drug1.name, "T1")
        self.assertEqual(self.drug1.amount, 10)
        self.assertEqual(self.drug1.price, 1000)

    def test_store_constructor(self):
        self.assertEqual(self.store1.name, "S1")
        self.assertEqual(self.store1.drugs, list())
        self.assertEqual(self.store1.employees, list())

    def test_add_employee(self):
        self.assertEqual(self.store1.employees, list())

        self.store1.add_employee("Seyed Ali", "Babaei", 19)
        self.assertEqual(len(self.store1.employees), 1)
        self.assertEqual(self.store1.employees, [{'first_name': 'Seyed Ali', 'last_name': 'Babaei', 'age': 19}])

    def test_store_value(self):
        self.store2.drugs.append(self.drug1)
        self.assertEqual(self.store2.total_value(), 10000)
        self.store2.drugs.append(self.drug2)
        self.assertEqual(self.store2.total_value(), 50000)
        self.store2.drugs.append(self.drug3)
        self.assertEqual(self.store2.total_value(), 140000)
        self.store2.drugs.append(self.drug4)
        self.assertEqual(self.store2.total_value(), 300000)

