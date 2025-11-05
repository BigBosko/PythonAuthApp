import tkinter
import customtkinter
from login import LoginPage
from register import RegisterPage
from home import HomePage

#theme and color
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class Controller(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('UserAuth')
        self.geometry('600x350')

        self.frames={}

        login_page = LoginPage(self, show_register=lambda: self.show_frame(RegisterPage), show_home=lambda: self.show_frame(HomePage))
        register_page = RegisterPage(self, show_login=lambda: self.show_frame(LoginPage))
        home_page = HomePage(self)

        self.frames[LoginPage] = login_page
        self.frames[RegisterPage] = register_page
        self.frames[HomePage] = home_page
        
        for page in self.frames.values():
            page.pack(fill="both", expand=True)
            page.pack_forget()
        
        self.show_frame(LoginPage)
    
    def show_frame(self, page_class):
        for page in self.frames.values():
            page.pack_forget()
        self.frames[page_class].pack(fill="both", expand=True)
    
controller = Controller()
controller.mainloop()