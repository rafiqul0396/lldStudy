from abc import ABCMeta, abstractmethod
from models.checkBox import CheckBox

from models.Button import Button
class FormFactory(metaclass=ABCMeta):

    @abstractmethod
    def createButton(self)->Button:
        ...

    @abstractmethod
    def createCheckBox(self)->CheckBox:
        ...

