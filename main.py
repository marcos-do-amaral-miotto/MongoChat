from databases.mongohandler import MongoHandler

if __name__ == '__main__':
    print("\n" * 130)
    client = MongoHandler()
    client.connect()
    print("Olá, bem vindo ao MongoZap!\n")
    while True:
        option = input("1 - Fazer Login\n2 - Criar uma conta\nEscolha a opção desejada: ")
        if option == "1" or option == "2":
            option = int(option)
            break
        else:
            print("\n" * 130)
            print("Opção inválida, tente novamente com uma das opções fornecidas (1 / 2)")

    print("\n" * 130)
    if option == 1:
        user = input("Digite o email para acesso: ")
        password = input("Digite a senha para acesso: ")
        if client.authenticate(user, password):
            print("massa")
        else:
            print("Not massa")
