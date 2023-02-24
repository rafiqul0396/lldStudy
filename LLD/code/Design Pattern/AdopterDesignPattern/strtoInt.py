class Old:
    def get(self):
        return "123"


class New:
    def get(self):
        return 123

class Adopter:
    def __init__(self,cls):
        self.cls = cls

    def get(self):
        return str(self.cls.get())
def main(obj):
    print("this is the result:"+obj.get())


if __name__ == "__main__":
    obj =Adopter(New())
    main(obj)
