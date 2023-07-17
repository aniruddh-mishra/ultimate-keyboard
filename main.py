import display
import geneticAlgorithm

app = display.App()

POP_SIZE = 10
GENERATIONS = 1000
VISUALIZE = False

population = geneticAlgorithm.initPopulation(POP_SIZE)
with open("test.txt", "r") as f:
    text = f.read()

parents = []

for i in range(GENERATIONS):
    print(i)
    parents.append(population[:2])
    population = geneticAlgorithm.nextPopulation(population, text, "nt")

def nextGeneration(genNumber):
    if genNumber == GENERATIONS:
        return
    app.motherKeyboard(parents[genNumber][0])
    app.fatherKeyboard(parents[genNumber][1])
    app.after(500, lambda : nextGeneration(genNumber + 1))

if VISUALIZE:
    nextGeneration(0)
else:
    nextGeneration(GENERATIONS - 1)

app.mainloop()
