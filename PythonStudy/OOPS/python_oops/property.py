class Person:
    def __init__(self,name):
        self.name=name

    # getter function
    @property
    def name(self):
        return self._name

    # setter function 
    @name.setter
    def name(self,val):
        if not isinstance(val, str):
            raise  TypeError("expecting String value ")

        self._name=val
    

    @name.deleter
    def name(self):
        raise AttributeError("Can't not delete this attribute")


class SubPerson(Person):
    @property
    def name(self):
        print("getting name")
        return super().name

    @name.setter
    def name(self,val):
        print("setting name to",val)
        super(SubPerson,SubPerson).name.__set__(self,val)

    @name.deleter
    def name(self):
        print("deletings name")
        super(SubPerson,SubPerson).name.__delete__(self)





if __name__=='__main__':
    s=SubPerson('rafik')
    print(s.name)
