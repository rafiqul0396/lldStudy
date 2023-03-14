from threading import Thread

def display():
    for i in range(5):
        print("child thread  is print")

t=Thread(target=display)
t.start()


for i in range(5):
    print("main thread is running")

