from  threading import Thread


class newThread(Thread):
    def  __init__(self):
        Thread.__init__(self)
        print(" this child thread excute")
    def run(self):
        print("hello world")
    

t=newThread()
t.start()