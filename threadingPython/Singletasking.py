from threading  import Thread
import threading
class Tasking:
    def  solve(self):
        self.q1()
        self.q2()
    

    def q1(self):
        print("question one solve")
    def q2(self):
        print("question 2 is solved")

ob=Tasking()
t=Thread(target=ob.solve)

t.start()