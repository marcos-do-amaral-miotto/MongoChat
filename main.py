from databases.mongohandler import MongoHandler
from databases.entities import *
from getpass import getpass
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Window properties:
        self.geometry("480x640")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)

    def button_callbck(self):
        print("button clicked")




def build_chat():
    print("\n" * 130)
    input("digite algo pra voltar pro menu")


def sign_in():
    for i in range(4, 0, -1):
        print("\n" * 130)
        print("--- Login ---\nCaso queira voltar ao menu inicial digite -1\n")
        if i != 4:
            print(f"Usuário inválido! Você ainda tem {i} chance(s).\n")
        email = input("Digite o email: ")
        if email == '-1':
            break
        password = getpass(prompt="Digite a senha: ")
        if password == '-1':
            break
        if mongo.authenticate(email, password):
            build_chat()
            break


def sign_up():
    error_message = None
    while True:
        try:
            user = Users()
            print("\n" * 130)
            print("--- Cadastro ---\nCaso queira voltar ao menu inicial digite -1\n")
            if error_message is not None:
                print(f"{error_message}\n")
            name = Users.format_name(input("Digite o nome de usuário: "))
            if name == '-1':
                break
            user.set_name(name)
            email = input("Digite o endereço de email: ").replace(' ', '')
            if email == '-1':
                break
            user.set_email(email)
            password = input("Digite a senha: ").replace(' ', '')
            if password == '-1':
                break
            user.set_password(password)
            mongo.register_new_user(user)
            return 0
        except Exception as e:
            error_message = e
    

def menu():
    header = "--- Olá, bem vindo ao MongoZap! ---"
    while True:
        print("\n" * 130)
        print(header)
        print("1. Cadastrar usuário")
        print("2. Logar")
        print("3. Sair")
        option = input("Escolha uma opção: ")
        header = "--- Olá, bem vindo ao MongoZap! ---"
        if option == "1":
            if sign_up() == 0:
                header = "Usuário cadastrado com sucesso!"
        elif option == "2":
            sign_in()
        elif option == "3":
            print("Saindo...")
            break
        else:
            header = "Opção inválida. Tente novamente."


if __name__ == '__main__':
    app = App()
    app.mainloop()
    mongo = MongoHandler()
    mongo.connect()
    menu()
