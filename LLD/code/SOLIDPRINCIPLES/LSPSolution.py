from abc import ABC, abstractmethod
from typing import List

class Payer(ABC):
    @abstractmethod
    def pay(self):
        ...

class Member(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def save_database(self):
        pass




class Teacher(Member,Payer):
    def __init__(self, name: str, age: int, teacher_id: str):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def save_database(self):
        print("Saving teacher data to database")
    def pay(self):
        print("teacher have to pay")
class Manager(Member, Payer):
    def __init__(self, name, age, manager_id):
        super().__init__(name, age)
        self.manager_id = manager_id

    def save_database(self):
        print("Saving manager data to database")

    def pay(self):
        print("manger have to be Paying")

# but i dont want to implement the pay method
class Student(Member):
    def __init__(self, name: str, age: int , student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
    def save_database(self):
        print("saving Student database")

    ## there are two ways we can do it
    ## throws an exception

payers: List[Payer] = [Teacher("John", 30, "123"), Manager("Mary", 25, "456")]
for payer in payers:
    payer.pay()
members: List[Member] = [Teacher("John",30, "123"),Manager("John", 25, "456"),Student("John", 30, "4567")]
for member in members:
    member.save_database()

