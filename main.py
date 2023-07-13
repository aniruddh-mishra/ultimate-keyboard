import display
import geneticAlgorithm

app = display.App()

population = geneticAlgorithm.initPopulation(100)
with open("test.txt", "r") as f:
    text = f.read()

parents = []

for i in range(100):
    parents.append(population[:2])
    population = geneticAlgorithm.nextPopulation(population, "Hi", "lfp")

def nextGeneration(genNumber):
    print(genNumber)
    if genNumber == 100:
        return
    app.motherKeyboard(parents[genNumber][0])
    app.fatherKeyboard(parents[genNumber][1])
    app.after(5000, lambda : nextGeneration(genNumber + 1))

nextGeneration(0)

app.mainloop()
