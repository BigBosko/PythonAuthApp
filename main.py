import tkinter
import customtkinter

#theme and color
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title('UserAuth')
root.geometry('600x350')

click_counter=0
username=None
password=None

def submit_action():
    global click_counter
    click_counter+=1
    first_label.configure(text=f"Button clicked {click_counter} times")
    pass

login_text = customtkinter.CTkLabel(
    root,
    text="Login"
)

username_entry = customtkinter.CTkEntry(
    root, 
    placeholder_text="username"
    )
password_entry = customtkinter.CTkEntry(
    root,
    placeholder_text="password"
)

submit = customtkinter.CTkButton(
    root,
    text="Submit",
    command=submit_action,
    height=100,
    width=200,
    font=("Helvetica", 24),
    text_color="white",
    fg_color="blue",
    bg_color="white",
    hover_color="purple",
    corner_radius=50,
    border_width=2,
    border_color="yellow",
    )

login_text.pack(pady=10)

username_entry.pack(pady=10)
password_entry.pack(pady=10)

submit.pack(pady=20)




root.mainloop()