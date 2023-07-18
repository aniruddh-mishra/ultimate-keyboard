import display
import geneticAlgorithm
import sys
import json
from datetime import datetime
import uuid

def main():
    app = display.App()

    if sys.argv[1] in ["-h", "--help"]:
        helpDocs()
        return

    TEXT, VISUALIZE, ALGORITHM, POP_SIZE, GENERATIONS = setConstants(sys.argv[1:])

    bestKeyboards = runSim(GENERATIONS, ALGORITHM, POP_SIZE, TEXT)

    saveData(bestKeyboards, TEXT, VISUALIZE, ALGORITHM, POP_SIZE, GENERATIONS)

    displayKeyboards(VISUALIZE, app, GENERATIONS, bestKeyboards)
    
    app.mainloop()

def saveData(bestKeyboards, text, visualize, algorithm, popSize, generations):
    data = {
            "text": text,
            "algorithm": algorithm,
            "popSize": popSize,
            "generations": generations,
            "date": str(datetime.now()),
            "bestKeyboards": bestKeyboards
            }
    jsonData = json.dumps(data)

    with open(f"outputs/{uuid.uuid4()}.json", "w") as f:
        f.write(jsonData)

def runSim(generations, algorithm, popSize, text):  
    population = geneticAlgorithm.initPopulation(popSize)

    bestKeyboards = []

    for i in range(generations):
        updateStatus(i + 1, generations)
        bestKeyboards.append(population[:2])
        population = geneticAlgorithm.nextPopulation(population, text, algorithm)

    return bestKeyboards

def helpDocs():
    print("python3 main.py <population size> <number of generations> <display all generations> <typing style> <training text>\n")
    print("\t<population size>: number of keyboards in each generation")

    print("\t<number of generations>: number of generations to run the program for")
    print("\t<display all generations>: 1 to display elites of all generations and 0 to display elites final generation")
    print("\t<typing style>: rfp for right finger pecking; lfp for left finger pecking; tft for two finger typing; nt (default) for normal ten finger typing")
    print("\t<training text>: any training text to simulate the fitness test on (default is generic english text)")

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
        display.nextGeneration(0, generations, parents, app)
    else:
        display.nextGeneration(generations - 1, generations, parents, app)

def updateStatus(progress, generations):
    percent = progress/generations * 100
    progress = int(percent * 0.2)
    complete = "=" * progress
    remainder = " " * (20 - progress)
    print("[" + complete + remainder + "]" + str(round(percent, 2)) + "%\r", end="")

main()
