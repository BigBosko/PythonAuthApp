import tkinter
import customtkinter 

class HomePage(customtkinter.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.pack(fill="both", expand=True)

        self.welcome_label = customtkinter.CTkLabel(
            self,
            text="Welcome to your home page"
        )
        self.welcome_label.pack(pady=50)