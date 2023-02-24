from abc import ABCMeta, abstractmethod


class Button(metaclass=ABCMeta):


    @abstractmethod
    def render(self):
        ...
    @abstractmethod
    def onClick(self):
        ...

