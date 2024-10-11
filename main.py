from databases.mongohandler import MongoHandler
from databases.entities import *
from customtkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()

        # Conexão com o banco
        self.mongo = MongoHandler()
        self.mongo.connect()

        # print(self.mongo.get_messages("marcos_miotto", "julia123"))
        self.mongo.send_message("user", "marcos_miotto", "Bem vindo ao MongoZap!")

        # Configurações da window:
        self.geometry("525x700")
        self.config(background="#00684a")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Conta do usuário atual
        self.current_user = Users(name="Marcos do Amaral Miotto", username="marcos_miotto", password="@Senha123")

        # Configurações dos widgets
        self.login = CTkFrame(self)
        self.register = CTkFrame(self)
        self.chat_list = CTkFrame(self)
        self.frame_menager(3)


    def frame_menager(self, frame_number):
        self.login.destroy()
        self.register.destroy()
        self.chat_list.destroy()
        if frame_number == 1:
            self.build_login()
        elif frame_number == 2:
            self.build_register()
        elif frame_number == 3:
            self.build_chat_list()

    def build_login(self):
        self.login = CTkFrame(self, bg_color="#00684a")
        self.login.grid(row=0, column=0, padx=20, pady=120, sticky="nsew")
        CTkLabel(self.login, text="Login", font=CTkFont(family="Arial", size=80, weight='bold')).pack(pady=50)
        username = CTkEntry(self.login, placeholder_text="Username", font=CTkFont(family="Arial", size=22),
                         bg_color='transparent', corner_radius=30, width=400)
        username.pack(pady=10)
        password_frame = CTkFrame(self.login, bg_color='transparent',fg_color='transparent')
        password_frame.pack(pady=10)
        password = CTkEntry(password_frame, placeholder_text="Senha", font=CTkFont(family="Arial", size=22), show='*',
                            bg_color='transparent', corner_radius=30, width=360)
        password.grid(column=0, row=0)
        password_visibility = CTkButton(password_frame, text='👁️', font=CTkFont(family='Arial', size=25), width=30,
                                        border_spacing=0, hover=False, cursor='hand2', bg_color='transparent',
                                        fg_color='transparent',
                                        command=lambda :password.configure(show='') if password.cget('show') == '*'
                                        else password.configure(show='*'))
        password_visibility.grid(column=1, row=0)
        redirector_frame = CTkFrame(self.login, bg_color="transparent", fg_color='transparent')
        redirector_frame.pack()
        register_label = CTkLabel(redirector_frame, text="Ainda não tem conta?", fg_color='transparent',
                                  bg_color='transparent', font=CTkFont(family="Arial", size=20), text_color="white")
        register_label.grid(column = 0, row=0)
        register_button = CTkButton(redirector_frame, text="Crie uma agora", fg_color='transparent',
                                    bg_color='transparent', font=CTkFont(family="Arial", size=20, weight='bold'),
                                    text_color="#00684a", hover=False, cursor='hand2',
                                    command=lambda : self.frame_menager(2))
        register_button.grid(column = 1, row=0)
        login_button = CTkButton(self.login, text="Entrar", font=CTkFont(family="Arial", size=30),
                                 bg_color='transparent', fg_color="#00684a", corner_radius=30, width=280,
                                 hover_color="#00533b", cursor='hand2',
                                 command=lambda:self.login_user(username.get(), password.get(), message_label))
        login_button.pack(pady=10)
        message_label = CTkLabel(self.login, text='', font=CTkFont(family="Arial", size=20, weight='bold'),
                                 text_color='#cc1919')
        message_label.pack()

    def build_register(self):
        self.register = CTkFrame(self, bg_color="#00684a")
        self.register.grid(row=0, column=0, padx=20, pady=80, sticky="nsew")
        back_button = CTkButton(self.register, text="⭠", font=CTkFont('Arial', 50), bg_color='transparent',
                                fg_color='transparent', width=30, hover=False, cursor='hand2',
                                command=lambda :self.frame_menager(1))
        back_button.place(x=10, y=10)
        CTkLabel(self.register, text="Cadastro", font=CTkFont(family="Arial", size=80, weight='bold')).pack(pady=(70, 30))
        name = CTkEntry(self.register, placeholder_text="Nome", font=CTkFont(family="Arial", size=22),
                        bg_color='transparent', corner_radius=30, width=400)
        name.pack()
        username = CTkEntry(self.register, placeholder_text="Username", font=CTkFont(family="Arial", size=22),
                         bg_color='transparent', corner_radius=30, width=400)
        username.pack(pady=12)

        password_frame = CTkFrame(self.register, bg_color='transparent',fg_color='transparent')
        password_frame.pack()
        password = CTkEntry(password_frame, placeholder_text="Senha", font=CTkFont(family="Arial", size=22), show='*',
                            bg_color='transparent', corner_radius=30, width=360)
        password.grid(column=0, row=0)
        password_visibility = CTkButton(password_frame, text='👁️', font=CTkFont(family='Arial', size=25), width=30,
                                        border_spacing=0, hover=False, cursor='hand2', bg_color='transparent',
                                        fg_color='transparent',
                                        command=lambda :password.configure(show='') if password.cget('show') == '*'
                                        else password.configure(show='*'))
        password_visibility.grid(column=1, row=0)
        message_label = CTkLabel(self.register, text='', font=CTkFont(family="Arial", size=20, weight='bold'))
        message_label.pack(pady=5)
        register_button = CTkButton(self.register, text="Cadastrar-se", font=CTkFont(family="Arial", size=30),
                                    bg_color='transparent', fg_color="#00684a", corner_radius=30, width=280,
                                    hover_color="#00533b", cursor='hand2',
                                    command=lambda :self.register_user(name.get(), username.get(), password.get(), message_label))
        register_button.pack()

    def select_messager(self, second_user: str):
        print(self.mongo.get_messages(self.current_user.username, second_user))

    def build_chat_list(self):
        self.chat_list = CTkFrame(self)
        self.chat_list.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.chat_list.grid_rowconfigure(0, weight=1)
        self.chat_list.grid_columnconfigure(0, weight=1)
        back_button = CTkButton(self.chat_list, text="⭠", font=CTkFont('Arial', size=50), bg_color='transparent',
                                fg_color='transparent', width=30, hover=False, cursor='hand2',
                                command=lambda :self.frame_menager(1))
        back_button.place(x=10, y=10)
        CTkLabel(self.chat_list, text="MongoZap", font=CTkFont(family='Arial', size=50)).place(x=125, y=10)
        users = CTkScrollableFrame(self.chat_list)
        users.grid_columnconfigure(0, weight=1)
        users.grid(row=0, column=0, padx=10, pady=(80, 10), sticky="nsew")
        users_list = self.mongo.get_all_users()
        for user in users_list:
            if user["username"] == self.current_user.username:
                continue

            button = CTkButton(users, fg_color='#545454', cursor='hand2', height=70, text=f'{user["name"]} ({user["username"]})',
                               font=CTkFont(family='Arial', size=25), anchor='w', command=lambda username = user["username"]:self.select_messager(username))
            button.grid(column=0, sticky="nsew", pady=(10, 0))

    def login_user(self, username: str, password: str, message_label:CTkLabel):
        try:
            if username == '' or password == '' or username.isspace() or password.isspace():
                return
            user = self.mongo.get_user(username, password)
            if user.is_empty():
                message_label.configure(text='Usuário ou senha incorretos!')
            else:
                self.current_user = user
                self.frame_menager(3)
        except Exception as e:
            message_label.configure(text=e)

    def register_user(self, name: str, username: str, password, message_label: CTkLabel):
        try:
            if name == '' or username == '' or password == ' ' or\
               name.isspace() or username.isspace() or password.isspace():
                return
            user = Users()
            user.set_name(name)
            user.set_username(username)
            user.set_password(password)
            self.mongo.register_new_user(user)
            self.current_user = user
            message_label.configure(text='Usuário cadastrado com sucesso!', text_color="#33866e")
        except Exception as e:
            message_label.configure(text=e, text_color='#cc1919')

if __name__ == '__main__':
    app = App()
    app.mainloop()
