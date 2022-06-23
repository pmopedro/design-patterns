import sqlite3

class MetaSingleton(type):
    _instances={}
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton,cls).__call__(*args, **kwds)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.db")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()

print("Database 1 object : ", db1)
print("Database 2 object : ", db2)