import tkinter
import customtkinter
from database import add_user, is_username_unique

class RegisterPage(customtkinter.CTkFrame):
    def __init__(self, controller, show_login):
        super().__init__(controller)
        self.controller = controller
        self.show_login = show_login

        self.pack(fill="both", expand=True)

        self.register_text = customtkinter.CTkLabel(
            self,
            text="Registration Page"
        )

        self.username_entry = customtkinter.CTkEntry(
            self,
            placeholder_text = "username"
        )

        self.password_entry = customtkinter.CTkEntry(
            self,
            placeholder_text = "password"
        )

        self.repeat_password_entry = customtkinter.CTkEntry(
            self,
            placeholder_text = "repeat password"
        )

        self.register_button = customtkinter.CTkButton(
            self,
            #command= kaj se zgodi ko se uporabnik hoče registrirsti?
            #preveriti se mora če sta obe gesli enaki, če uprabniško ime še ne obstaja in regex
            text = "Register",
            width = 50,
            height = 25,
            hover_color="blue"
        )

        self.login_text = customtkinter.CTkLabel(
            self,
            text = "Already have an accounnt? Login here"
        )

        self.go_login_button = customtkinter.CTkButton(
            self,
            command = self.show_login,
            text = "Go to Login",
            width = 50,
            height = 25,
            hover_color = "blue"
        )

        self.register_text.pack(pady=10)
        self.username_entry.pack(pady=10)
        self.password_entry.pack(pady=10)
        self.repeat_password_entry.pack(pady=10)
        self.register_button.pack(pady=10)
        self.login_text.pack(pady=10)
        self.go_login_button.pack(pady=5)
