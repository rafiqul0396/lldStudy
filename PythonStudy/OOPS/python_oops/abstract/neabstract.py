from  abc import  abstractmethod,ABC



class Food(ABC):
    @abstractmethod
    def food():
        print(" i am eating food")


if __name__ == '__main__':
    a=Food()
    a.food()