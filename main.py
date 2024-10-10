from databases.mongohandler import MongoHandler
from databases.entities import *
from customtkinter import *

class App(CTk):
    def __init__(self):
        super().__init__()

        # Window properties:
        self.geometry("525x700")
        self.config(background="#00684a")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.login = CTkFrame(self)
        self.register = CTkFrame(self)
        option = self.build_login()

    def build_login(self):
        self.login = CTkFrame(self, bg_color="#00684a")
        self.login.grid(row=0, column=0, padx=20, pady=120, sticky="nsew")
        CTkLabel(self.login, text="Login", font=CTkFont(family="Arial", size=80, weight='bold')).pack(pady=50)
        email = CTkEntry(self.login, placeholder_text="Email", font=CTkFont(family="Arial", size=22))
        email.configure(bg_color='transparent', corner_radius=30, width=400)
        email.pack(pady=10)
        password = CTkEntry(self.login, placeholder_text="Senha", font=CTkFont(family="Arial", size=22), show='*')
        password.configure(bg_color='transparent', corner_radius=30, width=400)
        password.pack(pady=10)
        sign_up_frame = CTkFrame(self.login, bg_color="transparent", fg_color='transparent')
        sign_up_frame.pack()
        sign_up_label = CTkLabel(sign_up_frame, text="Ainda não tem conta?", fg_color='transparent',
                                 bg_color='transparent', font=CTkFont(family="Arial", size=20), text_color="white")
        sign_up_label.grid(column = 0, row=0)
        sign_up_button = CTkButton(sign_up_frame, text="Crie uma agora", fg_color='transparent', bg_color='transparent',
                                   font=CTkFont(family="Arial", size=20, weight='bold'), text_color="#00684a",
                                   hover=False, command=self.build_register)
        sign_up_button.configure(cursor='hand2')
        sign_up_button.grid(column = 1, row=0)
        login_button = CTkButton(self.login, text="Entrar", font=CTkFont(family="Arial", size=30))
        login_button.configure(bg_color='transparent', fg_color="#00684a", corner_radius=30, width=280,
                               hover_color="#00533b", cursor='hand2')
        login_button.pack(pady=10)

    def build_register(self):
        self.login.destroy()
        self.register = CTkFrame(self, bg_color="#00684a")
        self.register.grid(row=0, column=0, padx=20, pady=80, sticky="nsew")
        back_button = CTkButton(self.register, text="⭠", font=CTkFont('Arial', 50), bg_color='transparent',
                                fg_color='transparent', width=30, hover=False, command=self.build_login())
        back_button.configure(cursor='hand2')
        back_button.place(x=10, y=10)
        CTkLabel(self.register, text="Cadastro", font=CTkFont(family="Arial", size=80, weight='bold')).pack(pady=70)
        email = CTkEntry(self.register, placeholder_text="Email", font=CTkFont(family="Arial", size=22))
        email.configure(bg_color='transparent', corner_radius=30, width=400)
        email.pack()
        password = CTkEntry(self.register, placeholder_text="Senha", font=CTkFont(family="Arial", size=22), show='*')
        password.configure(bg_color='transparent', corner_radius=30, width=400)
        password.pack(pady=20)
        sign_up_frame = CTkFrame(self.register, bg_color="transparent", fg_color='transparent')
        sign_up_frame.pack()
        sign_up_label = CTkLabel(sign_up_frame, text="Ainda não tem conta?", fg_color='transparent',
                                 bg_color='transparent', font=CTkFont(family="Arial", size=20), text_color="white")
        sign_up_label.grid(column = 0, row=0)
        sign_up_button = CTkButton(sign_up_frame, text="Crie uma agora", fg_color='transparent', bg_color='transparent',
                                   font=CTkFont(family="Arial", size=20, weight='bold'), text_color="#00684a",
                                   hover=False)
        sign_up_button.configure(cursor='hand2')
        sign_up_button.grid(column = 1, row=0)
        login_button = CTkButton(self.register, text="Entrar", font=CTkFont(family="Arial", size=30))
        login_button.configure(bg_color='transparent', fg_color="#00684a", corner_radius=30, width=280,
                               hover_color="#00533b", cursor='hand2')
        login_button.pack(pady=10)



def build_chat():
    print("\n" * 130)
    input("digite algo pra voltar pro menu")




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
            # sign_in()
            print("sla")
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
    # menu()
