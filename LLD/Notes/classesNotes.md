### Interfaces, Abstract Classes, and Static Methods in python\


In Python, interfaces, abstract classes, and static methods are used to promote code

reusability, maintainability, and structure.

 Here's a brief explanation of each:

1. **Interfaces**: Interfaces define a set of methods that a class must implement, but do not provide an implementation for those methods. In Python, interfaces can be implemented using abstract base classes (ABCs).
2. **Abstract Classes**: An abstract class is a class that contains one or more abstract methods. An abstract method is a method that has no implementation, only a declaration. Subclasses of an abstract class must implement the abstract methods. In Python, abstract classes can be created using the `abc` module.
3. **Static Methods**: A static method is a method that belongs to a class rather than an instance of a class. It does not have access to the instance and cannot modify the state of an object. In Python, static methods are defined using the `@staticmethod` decorator.

Here's an example of how you could use interfaces, abstract classes, and static methods in Python:

```python
from abc import ABC, abstractmethod


# Interface for shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


```
