from  threading import Thread
from  queue import Queue 
from time import sleep


class ODD:
    def __init__(self):
        self.q=Queue()

    def odd(self):
        for i in range(1,10):
            if(i%2!=0):
                print("this is odd number ",i)
                self.q.put(i)
                sleep(1)
class  EVEN:
    def __init__(self,pro):
        self.pro=pro

    def even(self):
        l=self.pro.q.qsize()
        print(l)
        for i in range(0,10):
            a=self.pro.q.get()
            a+=1
            print("this is even number",a)
            
                
                


p=ODD()
c=EVEN(p)
t1=Thread(target=p.odd)
t2=Thread(target=c.even)
t1.start()
t2.start()
t1.join(timeout=2)
t1.join(timeout=2)






