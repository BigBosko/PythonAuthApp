import tkinter
import customtkinter

class RegisterPage(customtkinter.CTkFrame):
    def __init__(self, parent, login_frame=None):
        super().__init__(parent)
        self.login_frame = login_frame

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
            command=self.go_to_login,
            text = "Go to Login",
            width = 50,
            height = 25,
            hover_color = "blue"
        )

        self.register_text.pack(pady=20)
        self.username_entry.pack(pady=10)
        self.password_entry.pack(pady=10)
        self.repeat_password_entry.pack(pady=10)
        self.register_button.pack(pady=10)
        self.login_text.pack(pady=10)
        self.go_login_button.pack(pady=5)

    def go_to_login(self):
        self.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

