import tkinter
import customtkinter
from database import is_login_correct

class LoginPage(customtkinter.CTkFrame):
    def __init__(self, controller, show_register, show_home):
        super().__init__(controller)
        self.controller = controller
        self.show_register = show_register
        self.show_home = show_home

        self.hidden_pass_unicode="\u25CF"

        pw_frame = customtkinter.CTkFrame(self, fg_color="transparent")

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
            pw_frame,
            placeholder_text = "password",
            show=self.hidden_pass_unicode,
            width=200,
        )

        self.toggle_password_btn = customtkinter.CTkButton(
            pw_frame,
            command= self.toggle_password,
            text="Show",
            width=55
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
        pw_frame.pack(pady=10)
        self.password_entry.pack(side="left", padx=(0,10))
        self.show_pass = False
        self.toggle_password_btn.pack(side="left")
        self.login_button.pack(pady=5)
        self.no_acc_text.pack(pady=(60,5))
        self.go_register_button.pack()

    def login_submit_action(self):
        username=self.username_entry.get().strip()
        password=self.password_entry.get().strip()
        if is_login_correct(username, password):
            self.show_home()
            print("Login succesfull")
        else:
            print("Invalid login information")
    
    def toggle_password(self):
        self.show_pass = not self.show_pass
        if self.show_pass:
            self.password_entry.configure(show="")
            self.toggle_password_btn.configure(text="Hide")
        else:
            self.password_entry.configure(show=self.hidden_pass_unicode)
            self.toggle_password_btn.configure(text="Show")

