import customtkinter
from keyboard import keyboard
import time

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Optimal Keyboard")
        self.geometry("600x180")
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

alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
a = ("a " * 26).split()
app = App()
app.motherKeyboard(alphabet)
app.fatherKeyboard(a)
app.after(5000, lambda : app.motherKeyboard(a))
app.after(5000, lambda : app.fatherKeyboard(alphabet))
app.mainloop()
