from typing import List
from abc import ABC, abstractmethod

#if S is a subtype of T, then objects of type T may be replaced by objects of type S,
# without breaking the program.
class Member(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def save_database(self):
        pass


class Teacher(Member):
    def __init__(self, name: str, age: int, teacher_id: str):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def save_database(self):
        print("Saving teacher data to database")


class Student(Member):
    def __init__(self, name: str, age: int , student_id: str):
        super().__init__(name, age)
        self.student_id = student_id

    def save_database(self):
        print("Saving student data to database")





members: List[Member] = []
members.append(Student('nusret',23,"12345"))
members.append(Teacher('Teacher_nusret',23,"12345"))
for member in members:
    member.save_database()