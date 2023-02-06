from abc import ABCMeta, abstractmethod
from button import Button

class ButtonFactory(metaclass=ABCMeta):
    @abstractmethod
    def createButton(self)->Button:
        pass
    