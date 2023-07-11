import customtkinter
from keyboard import keyboard

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Optimal Keyboard")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.keyboard = keyboard(self)
        self.keyboard.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

app = App()
app.mainloop()
