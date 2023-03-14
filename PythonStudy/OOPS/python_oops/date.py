class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)







class Date2:
    __slots__=['year','month','day']
    def __init__(self, year, month, day):
        self.year=year
        self.month=month
        self.day=day





class A:
    def __init__(self):
        self._internal=0 # an internal attributes
        self.public=1 # public attributes
        self.__private=0

    def __private_method(self):
        pass
    def public_mehtod(self):
        pass
    def _internal_method(self):
        pass




class B:
    def __init__(self):
        self.__private=0

    def private_method(self):

        print("i am from class B")
        #self.__private_method()
        


class C(B):
    def __init__(self):
        super().__init__()
        self.__private=1

    def private_method(self):

        print("i am from class C",self.__private)



## 8.6. Creating Managed Attributes

class Person:
    def __init__(self,first_name):
        self.first_name=first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name
    # setter function
    @first_name.setter
    def first_name(self,value):
        if not isinstance(value,str):
            raise TypeError("Expecting String value")
        self._first_name=value

    # deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("con't dlete attribtes")



class Person2:
    def __init__(self, first_name):
        self.set_first_name(first_name)
    # Getter function
    def get_first_name(self):
        return self._first_name
    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value
    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")
    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)


## dont repeted the same code twice
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value
    # Repeated property code, but for a different name (bad!)
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._last_name = value



if __name__=='__main__':
    _formats = {
        'ymd' : '{d.year}-{d.month}-{d.day}',
        'mdy' : '{d.month}/{d.day}/{d.year}',
        'dmy' : '{d.day}/{d.month}/{d.year}'
        }

    d=Date(2022, 12, 13)
    d2=Date(2012,12,23)
    d3=Date2(2012,11,12)
    print(dir(d3))
    print(format(d2))

    c=C()
    c.private_method()

    #----

    a=Person('rafik')
    print(a.first_name)
    a.first_name="aakash"
    print(a.first_name)
    print(a._first_name)
    #del a.first_name

    p=Person2("abdul")
    p.set_first_name("ahad")
    print(p.get_first_name())
    print()


    
