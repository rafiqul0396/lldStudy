##interface and Abstract Base class 

from abc import ABCMeta,abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass
    @abstractmethod
    def write(self, data):
        pass    



class SocketStream(IStream):
    def read(self,maxbytes=-1):
        ...
    def write(self,data):
        ...
        


if __name__=='__main__':
    a=IStream()