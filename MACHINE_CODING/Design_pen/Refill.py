
from RefillType import RefillType
from Ink import Ink
from Nib import  Nib

class Refill:
    def __init__(self,RefillType,refillable=True):
        self.RefillType = RefillType
        self.Refillable = refillable
        self.ink=ink
        self.nib=nib
