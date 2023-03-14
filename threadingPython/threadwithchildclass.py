from threading import Thread


class ChildThread(Thread):
    def run(self):
        for i in range(5):
            print("this is child thread")


thread=ChildThread()
print(thread.name)
thread.start()
thread.join()

for i in range(5):
    print(" this main thread")