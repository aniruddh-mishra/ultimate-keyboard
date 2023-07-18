import display
import geneticAlgorithm
import sys

def main():
    app = display.App()

    if sys.argv[1] in ["-h", "--help"]:
        print("python3 main.py <population size> <number of generations> <display all generations> <typing style> <training text>\n")
        print("\t<population size>: number of keyboards in each generation")

        print("\t<number of generations>: number of generations to run the program for")
        print("\t<display all generations>: 1 to display elites of all generations and 0 to display elites final generation")
        print("\t<typing style>: rfp for right finger pecking; lfp for left finger pecking; tft for two finger typing; nt (default) for normal ten finger typing")
        print("\t<training text>: any training text to simulate the fitness test on (default is generic english text)")

        return

    TEXT, VISUALIZE, ALGORITHM, POP_SIZE, GENERATIONS = setConstants(sys.argv[1:])

    bestKeyboards = runSim(GENERATIONS, ALGORITHM, POP_SIZE, TEXT)

    displayKeyboards(VISUALIZE, app, GENERATIONS, bestKeyboards)

    app.mainloop()

def runSim(generations, algorithm, popSize, text):  
    population = geneticAlgorithm.initPopulation(popSize)

    bestKeyboards = []

    for i in range(generations):
        updateStatus(i + 1, generations)
        bestKeyboards.append(population[:2])
        population = geneticAlgorithm.nextPopulation(population, text, algorithm)

    return bestKeyboards

def setConstants(args): 
    POP_SIZE = 10
    GENERATIONS = 100
    VISUALIZE = 0
    ALGORITHM = "nt"

    if len(args) > 0:
        POP_SIZE = int(args[0])
        GENERATIONS = int(args[1])
        VISUALIZE = int(args[2])

    if len(args) > 3:
        ALGORITHM = args[3]

    if len(args) > 4:
        TEXT = args[4]
    else:
        with open("test.txt", "r") as f:
            TEXT = f.read()

    print(f"Running Genetic algorithm with a population size of {POP_SIZE} for {GENERATIONS} generations.")

    return TEXT, VISUALIZE, ALGORITHM, POP_SIZE, GENERATIONS

def displayKeyboards(visualize, app, generations, parents):
    if visualize:
        nextGeneration(0, generations, parents, app)
    else:
        nextGeneration(generations - 1, generations, parents, app)

def updateStatus(progress, generations):
    percent = progress/generations * 100
    progress = int(percent * 0.2)
    complete = "=" * progress
    remainder = " " * (20 - progress)
    print("[" + complete + remainder + "]" + str(round(percent, 2)) + "%\r", end="")

def nextGeneration(genNumber, generations, parents, app):
    if genNumber == generations:
        return
    
    app.motherKeyboard(parents[genNumber][0])
    app.fatherKeyboard(parents[genNumber][1])
    app.after(5000, lambda : nextGeneration(genNumber + 1))

main()
