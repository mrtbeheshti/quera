class Drug:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name):
        self.name = name
        self.drugs = list()
        self.employees = list()

    def add_drug(self, drug):
        self.drugs.append(drug)

    def add_employee(self, first_name, last_name, age):
        self.employees.append(
            {"first_name": first_name, "last_name": last_name, "age": age}
        )

    def total_value(self):
        value = 0
        for drug in self.drugs:
            value += drug.amount * drug.price
        return value

    def employees_summary(self):
        result = ""
        result += "Employees:\n"
        for i in range(len(self.employees)):
            employee = self.employees[i]
            result += (
                "The employee number "
                + str(i + 1)
                + " is "
                + employee["first_name"]
                + " "
                + employee["last_name"]
                + " who is "
                + str(employee["age"])
                + " years old.\n"
            )
        return result


pharmacy = Pharmacy("ahmadi")
pharmacy.add_employee("ahmad", "ahmadPoor", 20)
print(pharmacy.employees_summary())
