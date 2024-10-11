from pymongo import MongoClient
from pymongo.synchronous.database import Database

from databases.entities import *

class MongoHandler:
    def __init__(self, connection_string=None, database_name=None):
        self.connection_string = connection_string
        self.database_name = database_name
        self.client = MongoClient
        self.database = Database
        if connection_string is None:
            self.connection_string = "mongodb+srv://main-user:database@aulas.sj2sb.mongodb.net/?retryWrites=true&w=majority&appName=Aulas"
        if database_name is None:
            self.database_name="mongo_chat"

    def connect(self):
        try:
            self.client = MongoClient(self.connection_string)
            self.database = self.client.get_database(self.database_name)
        except Exception as e:
            print(f"Falha na conexão com o Banco de Dados: {e}")
            self.client = None

    def get_user(self, username, password) -> Users:
        users = self.database["users"].find()
        for user in users:
            if user["username"] == username and user["password"] == password:
                found_user = Users()
                found_user.set_user_by_database(user)
                return found_user
        return Users()

    def get_all_users(self):
        documents = list(self.database["users"].find())
        for doc in documents:
            doc.pop("password")
        return documents

    def register_new_user(self, new_user: Users):
        users = self.database["users"]
        for user in users.find():
            if user["username"] == new_user.username:
                raise Exception('''Username já cadastrado!
O username informado já está associado
a uma conta. Por favor, utilize outro.''')
        users.insert_one(new_user.__dict__)

    def get_messages(self, first_user: str, second_user: str):
        return list(self.database["messages"].find(
            {
                "$and": [
                    {
                        "$or": [
                            {"sender": first_user},
                            {"sender": second_user}
                        ]
                    },
                    {
                        "$or": [
                            {"receiver": first_user},
                            {"receiver": second_user}
                        ]
                    }
                ]
            }))

    def send_message(self, sender: str, receiver: str, content: str):
        message = Messages(sender, receiver, content, datetime.now())
        self.database["messages"].insert_one(message.__dict__)