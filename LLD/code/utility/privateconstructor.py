class OnlyCreatable(object):
    __create_key=object()
    @classmethod
    def created(cls,value):
        return OnlyCreatable(cls.__create_key,value)
    def __init__(self,create_key,value):
        assert(create_key == OnlyCreatable.__create_key), \
            "OnlyCreatable objects must be created using OnlyCreatable.create"
        self.value = value


OnlyCreatable.created("I'm a test")
#OnlyCreatable(0, "I'm a test")