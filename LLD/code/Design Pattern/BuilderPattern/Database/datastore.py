

class DataStore:
    # step 1: create private constructor
    def __init__(self):
        pass
    # step 2: create inner class
    class   DataStorebUILDER:

        def __init__(self,hostname,port,password):
            self.setHostname =hostname
            self.setPort = port
            self.setPassword = password
        # step 3: inner method for building data
        def build(self):
            a=DataStore()
            a.__hostname = self.hostname
            a.__port = self.port
            a.__password = self.password
            return a
        def setHostname(self,hostname):

            self.__hostname = hostname
            return self
        def setPort(self,port):

            self.__port = port
            return self
        def setPassword(self,password):
            self.__password = password
            return self

    def __str__(self):
        print(self.hostname)

        print(self.port)
        print(self.password)