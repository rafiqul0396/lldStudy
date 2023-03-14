

def gen(a):
    for i in range(0,a):
        yield  i
        
4 bytes  8 bytes   20 bytes 
1,2,3,4,5

a=gen(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))


