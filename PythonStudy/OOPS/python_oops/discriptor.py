class Integer:
    def __init__(self,name):
        self.name=name

    def __get__(self,intance,cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    def __set__(self,instance,value):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
            