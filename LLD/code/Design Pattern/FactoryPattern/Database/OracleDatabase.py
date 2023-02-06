
from Database import  Database
class OracleDB(Database):
    def __init__(self,name,url):
        self.name = name
        self.url = url


    def connect(self):
        print("Connecting to Oracle")

    def query(self):
        print("Query to Oracle database")

    def close(self):
        print("Closing Oracle database")


