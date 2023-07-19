import customtkinter

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

def nextGeneration(genNumber, generations, bestKeyboards, app):
    if genNumber == generations:
        return
    
    app.motherKeyboard(bestKeyboards[genNumber][0])
    app.fatherKeyboard(bestKeyboards[genNumber][1])
    app.after(3000, lambda : nextGeneration(genNumber + 1, generations, bestKeyboards, app))

if __name__ == "__main__":
    import sys
    import json

    app = App()

    args = sys.argv[1:]
    with open(args[0], 'r') as f:
        data = json.load(f)
        generations = data['generations']
        print(f"This simulation had a population size of {data['popSize']} and ran for {generations} generations. It was trained with the text \"{data['text'][:100]}\" for the {data['algorithm']} typing style.")
    bestKeyboards = data['bestKeyboards']

    if int(args[1]):
        nextGeneration(0, generations, bestKeyboards, app)
    else:
        nextGeneration(generations - 1, generations, bestKeyboards, app)
    
    app.mainloop()
