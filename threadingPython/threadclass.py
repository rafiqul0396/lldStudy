from threading import Thread


class Hello:
    def hi(self,a):
        print("hello how r u +{}".format(a))


h=Hello()

t= Thread(target=h.hi,args=("rafik",))
t.start()