import customtkinter

customtkinter.set_appearance_mode("Dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Optimal Keyboard")
        self.geometry("800x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)

    def motherKeyboard(self, characters):
        if hasattr(self, "keyboardMother"):
            self.keyboardMother.destroy()
        self.keyboardMother = keyboard(self, characters)
        self.keyboardMother.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")
    
    def fatherKeyboard(self, characters):
        if hasattr(self, "keyboardFather"):
            self.keyboardFather.destroy()
        self.keyboardFather = keyboard(self, characters)
        self.keyboardFather.grid(row=0, column=1, padx=10, pady=10, sticky="nse")

class keyboard(customtkinter.CTkFrame):
    def __init__(self, master, characters):
        super().__init__(master)
        
        for i in range(30):
            column = i % 10
            row = int(i/10)
            padx = 10
            if row == 1:
                padx = (17, 3)
            if row == 2:
                padx = (3, 17)
                column += 1
            key = customtkinter.CTkLabel(self, text=characters[i], text_color="black")
            key.grid(row=row, column=column, padx=padx, pady=5, sticky="w")
