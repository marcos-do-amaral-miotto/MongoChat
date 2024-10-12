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

    def get_user(self, username: str, password: str) -> Users:
        users = self.database["users"].find()
        for user in users:
            if user["username"] == username and user["password"] == password:
                found_user = Users()
                found_user.set_user_by_database(user)
                return found_user
        return Users()

    def get_all_users(self):
        documents = self.database["users"].find()
        users_list = []
        for doc in documents:
            doc.pop("password")
            found_user = Users()
            found_user.set_user_by_database(doc)
            users_list.append(found_user)
        return users_list

    def register_new_user(self, new_user: Users):
        users = self.database["users"]
        for user in users.find():
            if user["username"] == new_user.username:
                raise Exception('''Username já cadastrado!
O username informado já está associado
a uma conta. Por favor, utilize outro.''')
        user = new_user.__dict__
        user.pop("_id")
        users.insert_one(user)

    def get_messages(self, first_user: Users, second_user: Users) -> list[Messages]:
        results = self.database["messages"].find({
            "sender": {
                "$in": [first_user.get_id(), second_user.get_id()]
            },
            "receiver": {
                "$in": [first_user.get_id(), second_user.get_id()]
            }
        })
        messages = []
        for message in results:
            found_message = Messages()
            found_message.set_message_by_database(message)
            messages.append(found_message)
        return messages


    def register_message(self, message: Messages):
        if message.encrypted is False:
            raise Exception ("Mensagens não encriptadas não podem ser salvas no banco de dados!")
        self.database["messages"].insert_one(message.to_dict())