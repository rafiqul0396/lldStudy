

'''class A:

    def __init__(self):
        self.x=0
    def spam(self):
        print("A.Spam")


class B(A):
    def __init__(self):
        super().__init__()
        self.y=1
    def spam(self):
        print("B.spam")
        super().spam()



'''
'''
class Base:
    def __init__(self):
        print('Base.__init__')
class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')
class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')

'''

class Base:
    def __init__(self):
        print('Base.__init__')
class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')
class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')
class C(A,B):
    def __init__(self):
        super().__init__()     # Only one call to super() here
        print('C.__init__')
"""
 Child classes get checked before parents
• Multiple parents get checked in the order listed.
• If there are two valid choices for the next class, pick the one from the first parent.
"""


if __name__=='__main__':
    #b=B()
    #b.spam()

    c=C()
    print(C.__mro__)