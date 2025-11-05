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
            command=self.register_action, #regex
            text = "Register",
            width = 50,
            height = 25,
            hover_color="blue"
        )

        self.login_text = customtkinter.CTkLabel(
            self,
            text = "Already have an account? Login here"
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
    
    def are_passwords_matching(self, pass0, pass1):
        return pass0==pass1

    def register_action(self):
        username = self.username_entry.get()
        pass0 = self.password_entry.get()
        pass1 = self.repeat_password_entry.get()

        if is_username_unique(username):
            if self.are_passwords_matching(pass0, pass1):
                add_user(username, pass0)
                print("Registration succesfull")
            else:
                print("Passwords aren't matching")
        else:
            print("Username already taken")