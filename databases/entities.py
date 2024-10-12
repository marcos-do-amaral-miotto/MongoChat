from bson.objectid import ObjectId
from datetime import datetime
from re import compile
from aes_pkcs5.algorithms.aes_cbc_pkcs5_padding import AESCBCPKCS5Padding

class Users:
    def __init__(self, name=None, username=None, password=None):
        self._id = None
        self.name = None
        self.username = None
        self.password = None
        if name is not None:
            self.set_name(name)
        if username is not None:
            self.set_username(username)
        if password is not None:
            self.set_password(password)

    @staticmethod
    def format_name(name: str) -> str:
        for i in range(2):
            blank_space = 0
            for letter in name:
                if letter == ' ':
                    blank_space += 1
                else:
                    break
            name = name[blank_space: len(name)]
            name = name[::-1]
        return name

    def is_empty(self) -> bool:
        if self.name is None and self.username is None and self.password is None:
            return True
        else:
            return False

    def set_name(self, name: str):
        name = Users.format_name(name)
        if name.replace(' ', '').isalpha() is False:
            raise Exception("Nome inválido!\nO nome não pode conter números.")
        self.name = name

    def set_username(self, username: str):
        username = username.replace(' ', '')
        regex = compile(r"^(?=[a-zA-Z0-9._-]{3,16}$)(?!.*[_.-]{2})[a-zA-Z0-9]+([._-][a-zA-Z0-9]+)*$")
        if regex.match(username) is None:
            raise Exception('''Username inválido!
Deve ter de 3 a 16 caracteres alfanuméricos
e pode incluir '_', '.' ou '-'. Não pode
começar ou terminar com caracteres especiais,
nem usá-los consecutivamente.''')
        self.username = username

    def set_password(self, password: str):
        password = password.replace(' ', '')
        regex = compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
        if regex.match(password) is None:
            raise Exception('''Senha inválida!
A senha deve ter no mínimo 8 caracteres,
incluindo uma letra maiúscula, uma minúscula,
um número e um caractere especial (@$!%*?&).''')
        self.password = password

    def set_id(self, _id):
        if type(_id) != ObjectId:
            raise Exception("Id inválido!")
        self._id = _id

    def get_id(self):
        return self._id

    def set_user_by_database(self, user:dict):
        self._id = user.pop("_id")
        self.name = user.pop("name", None)
        self.username = user.pop("username", None)
        self.password = user.pop("password", None)

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if other.get_id() != self._id:
            return False
        if other.name != self.name:
            return False
        if other.username != self.username:
            return False
        return True

class Messages:
    def __init__(self, sender: Users=None, receiver: Users=None, content: str=None, encrypted=False):
        self._id = None
        self.sender = None
        self.receiver = None
        self.content = None
        self.timestamp = datetime.now()
        self.encrypted = False
        if sender is not None:
            self.set_sender(sender)
        if receiver is not None:
            self.set_receiver(receiver)
        if content is not None:
            self.set_content(content)
        if encrypted:
            self.encrypted = True

    def set_sender(self, sender: Users):
        if self.receiver is not None and self.receiver == sender:
            raise Exception("Não é possível enviar uma mensagem de mesmo remetente e destinatário!")
        self.sender = sender.get_id()

    def set_receiver(self, receiver: Users):
        if self.sender is not None and self.sender == receiver:
            raise Exception("Não é possível enviar uma mensagem de mesmo remetente e destinatário!")
        self.receiver = receiver.get_id()

    def set_content(self, content: str):
        if content.isspace() or content == '':
            raise Exception("A mensagem não pode ser vazia!")
        self.content = content

    def encrypt_content(self, key, iv_parameter="0011223344556677", output_format="b64"):
        if self.encrypted:
            raise Exception("Mensagem já encriptada!")
        if self.content is None:
            raise Exception("Não há mensagem a ser encriptadas!")
        cipher = AESCBCPKCS5Padding(key, output_format, iv_parameter)
        encrypted = cipher.encrypt(self.content)
        self.set_content(encrypted)
        self.encrypted = True

    def decrypt_content(self, key, iv_parameter="0011223344556677", output_format="b64"):
        if self.encrypted is False:
            raise Exception("Mensagem já desencriptada!")
        if self.content is None:
            raise Exception("Não há mensagem a ser desencriptada!")
        cipher = AESCBCPKCS5Padding(key, output_format, iv_parameter)
        decrypted = cipher.decrypt(self.content)
        self.set_content(decrypted)
        self.encrypted = False

    def set_message_by_database(self, message: dict):
        self._id = message.pop("_id")
        self.sender = message.pop("sender", None)
        self.receiver = message.pop("receiver", None)
        self.content = message.pop("content", None)
        self.timestamp = message.pop("timestamp", None)
        self.encrypted = True
