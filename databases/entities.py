from datetime import datetime
from re import compile

class Users:
    def __init__(self, name=None, username=None, password=None):
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

    def set_user_by_database(self, user:dict):
        self.name = user.pop("name", None)
        self.username = user.pop("username", None)
        self.password = user.pop("password", None)

class Messages:
    def __init__(self, sender=None, receiver=None, content=None, timestamp = None):
        self.sender = None
        self.receiver = None
        self.content = None
        self.timestamp = None
        if sender is not None:
            self.set_sender(sender)
        if receiver is not None:
            self.set_receiver(receiver)
        if content is not None:
            self.set_content(content)
        if timestamp is not None:
            self.set_timestamp(timestamp)

    def set_sender(self, sender: str):
        self.sender = sender

    def set_receiver(self, receiver: str):
        self.receiver = receiver

    def set_content(self, content: str):
        if content.isspace() or content == '':
            raise Exception("A mensagem não pode ser vazia!")
        self.content = content

    def set_timestamp(self, timestamp: datetime):
        self.timestamp = timestamp
