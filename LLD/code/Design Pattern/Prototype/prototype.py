from abc import ABCMeta, abstractmethod


class IPrototype(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def clone():
        ...



class Concreateclass1(IPrototype):


    def __init__(self,i=0,s="",l=[],d={}):
        self.i = i
        self.s = s
        self.d = d
        self.l = l

    def clone(self):
        return type(self)(self.i,self.s,self.l.copy(),self.d.copy())


    def __str__(self):
        return f"{id(self)}\ts:{self.s}\ti:{self.i}\tl:{self.l}\td:{self.d}"


class Concreateclass2(IPrototype):


    def __init__(self,i=0,s="",l=[],d={}):
        self.i = i
        self.s = s
        self.d = d
        self.l = l

    def clone(self):
        return type(self)(self.i,self.s,self.l.copy(),self.d.copy())


    def __str__(self):
        return f"{id(self)}\ts:{self.s}\ti:{self.i}\td:{self.d}\tl:{self.l}"



if __name__ == "__main__":
    object1=Concreateclass1(1,"rafik",[1,2,4],{"name":"raf","address":"127.0.0.1","port":"5432"})
    print(object1)
    object2=object1.clone()
    print(object2)

    object12=Concreateclass2(1,"rafik",[1,2,4],{"name":"raf","address":"127.0.0.1","port":"5432"})
    print(object12)
    object21=object12.clone()
    print(object21)
    object21.l[0]=123
    print(object21)