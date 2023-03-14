from abc import ABC,abstractmethod


#single responsibity principles
class Employee(ABC):
    def __init__(self,name:str,salary:float):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        ...


class Developer(Employee):

    def __init__(self,name:str,salary:float):
        super().__init__(name,salary)

    def work(self):
        print("{} deveolment working with developers".format(self.name))


class Tester(Employee):
    def __init__(self,name:str,salary:float):
        super().__init__(name,salary)

    def work(self):
        print("{} Tester working with testing".format(self.name))

class DataEngineer(Employee):
    def __init__(self,name:str,salary:float):
        super().__init__(name,salary)
    def work(self):
        print("{} DataEngineer working with data".format(self.name))
class Company:
    def __init__(self, name):
        self.name = name

    def work(self, employee:Employee):
        employee.work()




ibs = Company("Impressico")
developer = Developer("yasra", "1000000")
tester = Tester("Aaksh", "1000000")
ibs.work(developer) # Will print Nusret is developing
ibs.work(tester) # Will print Someone is testing
dataeng=DataEngineer("rafik",100000)
ibs.work(dataeng)