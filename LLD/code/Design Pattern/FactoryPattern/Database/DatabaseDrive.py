from DatabaseFactory import  DatabaseFactory
class Test:
    @staticmethod
    def main(*args):
        factory=DatabaseFactory()
        database=factory.createDatabase("MySQL",*("id", "name","description"))
        print(database.__dict__)
        database.connect()
        database.query()
        database.close()


if __name__ =='__main__':
    Test.main()