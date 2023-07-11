import customtkinter

class keyboard(customtkinter.CTkFrame):
    def __init__(self, master, characters):
        super().__init__(master)
        
        for i in range(26):
            if i < 10:
                row = 0
                column = i
            elif i < 19:
                row = 1
                column = i - 10
            else:
                row = 2
                column = i - 18
            padx = 10
            if row == 1:
                padx = (17, 3)
            if row == 2:
                padx = (3, 17)
            key = customtkinter.CTkLabel(self, text=characters[i], text_color="black")
            key.grid(row=row, column=column, padx=padx, pady=5, sticky="w")
