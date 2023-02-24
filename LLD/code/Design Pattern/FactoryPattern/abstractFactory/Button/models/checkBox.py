from abc import ABCMeta, abstractmethod


class CheckBox(metaclass=ABCMeta):


    @abstractmethod
    def render(self):
        ...
    @abstractmethod
    def onSelect(self):
        ...
    