from threading import Thread,current_thread


def display():
    current_thread().name="hello thread"
    print("this is child thread name",current_thread().name)


t=Thread(target=display)


t.start()

print("this main thread ",current_thread().getName())