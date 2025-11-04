import tkinter
import customtkinter
from login import LoginPage
from register import RegisterPage

#theme and color
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title('UserAuth')
root.geometry('600x350')

register_frame= RegisterPage(root)
login_frame = LoginPage(root, register_frame)
register_frame.login_frame = login_frame

def show_login():
    register_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def show_register():
    login_frame.pack_forget()
    register_frame.pack(fill="both", expand=True)

show_login()
root.mainloop()