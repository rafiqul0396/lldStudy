

def gen(a):
    for i in range(0,a):
        yield  i
        
#

a=gen(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))


