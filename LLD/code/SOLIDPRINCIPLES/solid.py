class Employee:

    def __init__(self, name: str, salary: str):
        self.name = name
        self.salary = salary


class Tester(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def test(self):
        print("{} is testing".format(self.name))

class Developer(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def develop(self):
        print("{} is developing".format(self.name))


class Company:

    def __init__(self, name: str):
        self.name = name

    def work(self, employee):
        if isinstance(employee, Developer):
            employee.develop()
        elif isinstance(employee, Tester):
            employee.test()
        else:
            raise Exception("Unknown employee")




