

class DataStore:
    # step 1: create private constructor
    def __init__(self):
        pass
    # step 2: create inner class

    class   DataStoreBuilder:

        def __init__(self):
            pass


        def set_port(self,port):
            self._port = port
            return self
        def set_password(self,password):
            self._password = password
            return self
        def sethostname(self,hostname):
            self._hostname =hostname
            return self

        # Getter function
        @property
        def hostname(self):
             return self._hostname

        # Setter function
        @hostname.setter
        def first_name(self, value):
            if not isinstance(value, str):
                raise TypeError('Expected a string')
            self._hostname = value

        # Getter function
        @property
        def password(self):
            return self._password

        # Setter function
        @password.setter
        def password(self, value):
            if not isinstance(value, str):
                raise TypeError('Expected a String')
            self._password = value

        # Getter function
        @property
        def port(self):
            return self._port

        # Setter function
        @port.setter
        def port(self, value):
            if not isinstance(value, int):
                raise TypeError('Expected a int')
            self._port = value



# step 3: inner method for building data
        def build(self):
            a=DataStore()
            a.hostname = self.hostname
            a.port = self.port
            a.password = self.password
            return a



    def __str__(self):
        print(self.hostname)

        print(self.port)
        print(self.password)