from abc import ABCMeta, abstractmethod


class Database(metaclass=ABCMeta):


    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def query(self):
        ...



    @abstractmethod
    def close(self):
        ...

