from abc import ABCMeta, abstractmethod


class Button(metaclass=ABCMeta):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onClick(self):
        pass