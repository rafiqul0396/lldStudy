from RefillType import RefillType
from InkType import InkType
from Refill import Refill
from Ink import Ink
from Nib import Nib
from PenType import PenType
class Pen:
    def __init__(self,brand,PenType ,price,refill,ink,nib):
        self.brand = brand
        self.penType = PenType
        self.price = price
        self.refill =refill
        self.ink =ink
        self.nib=nib


    def Write(self):
        print("Writing")



refill=Refill(RefillType.BALL,True)
ink=Ink("red","selo",InkType.BALL)
nib=Ink("green","selo",InkType.BALL)
a=Pen("celona",PenType.BALL,10,refill,ink,nib)
a.Write()


