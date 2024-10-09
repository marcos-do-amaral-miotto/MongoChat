from databases.mongohandler import MongoHandler
from databases.entities import *
from getpass import getpass

def build_chat():
    print("\n" * 130)
    input("digite algo pra voltar pro menu")

def sign_in():
    for i in range(4, 0, -1):
        print("\n" * 130)
        if i != 4:
            print(f"Usuário inválido! Você ainda tem {i} chance(s).")
        print("--- Login ---")
        email = input("Digite o email: ")
        password = getpass("Digite a senha: ")
        if mongo.authenticate(email, password):
            build_chat()
            break

def format_name(name):
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

def sign_up():
    error_message = None
    while True:
        try:
            user = Users()
            print("\n" * 130)
            print("--- Cadastro ---\nCaso queira voltar ao menu inicial digite -1\n")
            if error_message is not None:
                print(f"{error_message}\n")
            name = format_name(input("Digite o nome de usuário: "))
            for i in name:
                print(i)
            print(name.isalpha())
            if name == '-1':
                break
            user.set_name(name)
            email = input("Digite o endereço de email: ").replace(' ', '')
            if email == '-1':
                break
            user.set_email(email)
            password = input("Digite a senha:").replace(' ', '')
            if password == '-1':
                break
            user.set_password(password)
            mongo.register_new_user(user)
            break
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
        if option == "1":
            sign_up()
        elif option == "2":
            sign_in()
            header = "--- Olá, bem vindo ao MongoZap! ---"
        elif option == "3":
            print("Saindo...")
            break
        else:
            header = "Opção inválida. Tente novamente."

if __name__ == '__main__':
    mongo = MongoHandler()
    mongo.connect()
    menu()
