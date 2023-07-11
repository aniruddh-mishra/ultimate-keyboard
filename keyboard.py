import customtkinter

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

class keyboard(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
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
            key = customtkinter.CTkLabel(self, text=alphabet[i], text_color="black")
            key.grid(row=row, column=column, padx=padx, pady=5, sticky="w")
