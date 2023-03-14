class Person:
    def move(self,a,b,*args):
        print(args)
        _,*w=args # unpacking 
        print(_)
        #print(y)
        print(a)
        print(b)


p=Person()
p.move(1, 2,3,3,2233,3444)