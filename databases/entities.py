from re import compile

class Users:
    def __init__(self, name = None, email = None, password = None):
        if name is not None and email is not None and password is not None:
            self.name = None
            self.email = None
            self.password = None
            self.set_name(name)
            self.set_email(email)
            self.set_password(password)
    
    def set_name(self, name:str):
        if name.isalpha() is False:
            raise Exception("Nome inválido!\nO nome não pode conter números.")
        self.name = name

    def set_email(self, email):
        regex = compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        if regex.match(email) is None:
            raise Exception("Email inválido!")
        self.email = email

    def set_password(self, password):
        regex = compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
        if regex.match(password) is None:
            raise Exception('''Senha inválida!
A senha deve atender aos seguintes critérios:
- Conter no mínimo 8 caracteres.
- Incluir pelo menos uma letra maiúscula.
- Incluir pelo menos uma letra minúscula.
- Incluir pelo menos um número.
- Incluir pelo menos um caractere especial: @$!%*?&.
''')
        self.password = password

