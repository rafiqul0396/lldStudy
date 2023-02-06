import unittest
from  datastore import DataStore

class MyTestCase(unittest.TestCase):
    def test_something(self):
        a=DataStore.DataStoreBuilder().\
            sethostname("localhost").\
            set_port("80").\
            set_password("password").\
            build()
        #b=a.sethostname("localhost").set_port("80").set_password("password").build()
        print(a.__str__())
        assert isinstance(a,DataStore)
    def test_database_abd(self):
        a=DataStore.DataStoreBuilder

        a.sethostname("localhost").build()



        assert isinstance(a,DataStore)

# add assertion here


if __name__ == '__main__':
    unittest.main()
