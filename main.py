import display
import geneticAlgorithm

app = display.App()

population = geneticAlgorithm.initPopulation(10)
keyboard = iter(population)
app.motherKeyboard(next(keyboard))
app.fatherKeyboard(next(keyboard))

app.after(1000, lambda : app.motherKeyboard(nextKeyboard()))

def nextKeyboard():
    if next(keyboard, False):
        app.after(1000, lambda : app.motherKeyboard(nextKeyboard()))
    return next(keyboard, "qwertyuiopasdfghjkl;zxcvbnm,.?")

app.mainloop()
