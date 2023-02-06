from .DB import Database

from .datastore import DataStore
def test_database():
    a=Database("sql",123,"rafik","12345")
    assert  isinstance(a,Database)



def test_database_():
    map={}
    map["host"]= "localhost"
    map["port"]=12345
    map["database"]="bd"
    map["password"]="password"
    a=Database(**map)
    print(map)
    assert isinstance(a,Database)


def test_database_builder():
        b=DataStore.DataStorebUILDER("sql",123,12346)
        a=DataStore.DataStorebUILDER.build(b)

        assert  isinstance(a,DataStore)
@staticmethod
def test_database_abd(self):
    a=DataStore.DataStorebUILDER.setHostname("localhost").setPort("12346").setPassword("password")
    b=a.build()
    assert isinstance(b,DataStore)
