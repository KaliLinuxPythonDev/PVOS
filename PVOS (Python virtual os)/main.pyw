from customtkinter import *
from Executer import execute_cmd

set_appearance_mode("System")
set_default_color_theme("green")

window = CTk()
window.title("Python Virtual Operating System")
window.geometry("1000x500")

command = CTkEntry(window,
                   placeholder_text="Enter command", placeholder_text_color="Grey",
                   width=1000, height=40,
                   font=("Lato", 20, "bold"))

submit_btn = CTkButton(window,
                       text="Submit", text_color="black",
                       fg_color="#aaffaa", hover_color="#ffaaff",
                       font=("Lato", 20, "bold"),
                       command=lambda: execute_cmd(command.get()))

command.pack()
submit_btn.place(x=0, y=40)

window.mainloop()