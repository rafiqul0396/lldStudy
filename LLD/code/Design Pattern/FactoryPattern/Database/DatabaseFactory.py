
from Database import  Database
from MySqlDatabase import MySQLDatabase
from OracleDatabase import OracleDB

class DatabaseFactory:
    @staticmethod
    def createDatabase(type_:str,*args)->Database:

        database:Database=None
        if type_=='Oracle':
            database=OracleDB(*args)
        elif type_=='MySQL':
            database=MySQLDatabase(*args)

        return database
