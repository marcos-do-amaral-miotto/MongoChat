from pymongo import MongoClient


class MongoHandler:
    def __init__(self, connection_string="mongodb+srv://main-user:database@aulas.sj2sb.mongodb.net/?retryWrites"
                                         "=true&w=majority&appName=Aulas", database_name="mongo_chat"):
        self.connection_string = connection_string
        self.database_name = database_name
        self.client = None
        self.database = None

    def connect(self):
        try:
            self.client = MongoClient(self.connection_string)
            self.database = self.client[self.database_name]
        except Exception as e:
            print(f"Falha na conexão com o Banco de Dados: {e}")
            self.client = None

    def authenticate(self, email, password) -> bool:
        try:
            users = self.database["users"]
            for user in users.find():
                if user["email"] == email and user["password"] == password:
                    return True
            return False
        except Exception as e:
            print(f"Erro de conexão com o Banco de Dados: {e}\n")
