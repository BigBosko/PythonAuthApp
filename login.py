import tkinter
import customtkinter
from database import is_login_correct

class LoginPage(customtkinter.CTkFrame):
    def __init__(self, controller, show_register, show_home):
        super().__init__(controller)
        self.controller = controller
        self.show_register = show_register
        self.show_home = show_home

        self.pack(fill="both", expand=True)

        self.login_text = customtkinter.CTkLabel(
            self,
            text="Login Page",
            )
        
        self.username_entry = customtkinter.CTkEntry(
            self,
            placeholder_text = "username"
        )

        self.password_entry = customtkinter.CTkEntry(
            self,
            placeholder_text = "password"
        )

        self.login_button = customtkinter.CTkButton(
            self,
            command=self.login_submit_action,
            text="Login",
            width = 50,
            height = 25,
            hover_color="blue"
        ) 

        self.no_acc_text = customtkinter.CTkLabel(
            self,
            text = "Don't have an account? Register here"
        )

        self.go_register_button = customtkinter.CTkButton(
            self,
            command=self.show_register,
            text="Go to Register",
            width = 50,
            height = 25,
            hover_color="blue"
        )

        self.login_text.pack(pady=10)
        self.username_entry.pack(pady=10)
        self.password_entry.pack(pady=10)
        self.login_button.pack(pady=10)
        self.no_acc_text.pack(pady=10)
        self.go_register_button.pack(pady=5)

    def login_submit_action(self):
        username=self.username_entry.get().strip()
        password=self.password_entry.get().strip()
        if is_login_correct(username, password):
            self.show_home()
            print("Login succesfull")
        else:
            print("Invalid login information")
