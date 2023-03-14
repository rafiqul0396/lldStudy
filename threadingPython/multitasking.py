from threading import Thread,Lock

class Hotel:

    def __init__(self,t):
        self.t=t
        self.l=Lock()
    def food(self):
        self.l.acquire(blocking=True,timeout=-1)
        for i in range(1,6):
            print(self.t,i)
        self.l.release()
    

h1=Hotel("take order from table")
h2=Hotel("serve Order from Table")

t1=Thread(target=h1.food)
t2=Thread(target=h2.food)
t1.start()
t2.start()