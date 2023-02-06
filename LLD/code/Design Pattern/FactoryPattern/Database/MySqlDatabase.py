from Database import Database

class MySQLDatabase(Database):
    def __init__(self, id, username,db):
        self.id = id
        self.username = username
        self.db = db


    def connect(self):
        print("Connecting as MySQL...")
    def query(self):
        print("Query... Mysteries")
    def close(self):
        print("Closing...")
