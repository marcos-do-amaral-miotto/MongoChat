from pymongo import MongoClient

class MongoHandler:
    def __init__(self, connection_string = None):
        if connection_string is None:
            self.connection_string = "mongodb+srv://main-user:database@aulas.sj2sb.mongodb.net/"
        else:
            self.connection_string = connection_string

    def connect(self):
        return MongoClient(self.connection_string)

    @staticmethod
    def authenticate(email, password) -> bool:
        if email == "marcos" and password == "123":
            return True
        else:
            return False
