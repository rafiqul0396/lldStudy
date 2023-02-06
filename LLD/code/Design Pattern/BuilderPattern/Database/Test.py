import unittest
from .datastore import DataStore
from .DB import Database

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



    def test_database_(self):
        map={}
        map["host"]= "localhost"
        map["port"]=12345
        map["database"]="bd"
        map["password"]="password"
        a=Database(**map)
        print(map)
        assert isinstance(a,Database)


    def test_database_builder(self):
        #b=DataStore.DataStorebUILDER("sql",123,12346)
        #a=DataStore.DataStorebUILDER.build(b)

        assert  isinstance(True,bool)

    def test_database_abd(self):
        a=DataStore.DataStoreBuilder().sethostname("h").set_password("password").set_port("port").build()

        assert isinstance(a,DataStore)

    def test__database(self):
        map={}
        map["host"]= "localhost"
        map["port"]=12345
        map["database"]="bd"
        map["password"]="password"
        a=Database(**map)
        assert  isinstance(a,Database)




# add assertion here


if __name__ == '__main__':
    unittest.main()
