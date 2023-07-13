import random
import distanceAlgorithms
import ergoAlgorithms

def initPopulation(popSize):
    alphabet = list("abcdefghijklmnopqrstuvwxyz.,?;")
    population = []
    testKeyboard = newKeyboard(alphabet) 
    for _ in range(popSize):
        population.append(newKeyboard(alphabet))
    return population

def newKeyboard(alphabet):
    alphabet = alphabet.copy()
    keyboard = []
    while len(alphabet) > 0:
        letter = random.choice(alphabet)
        alphabet.remove(letter)
        keyboard.append(letter)
    return keyboard

def fitnessTest(population, typing, text):
    results = []
    for keyboard in population:
        ergoResult = ergoAlgorithms.checkErgo(keyboard, text, typing)
        distanceResult = distanceAlgorithms.checkDistance(keyboard, text, typing)
        results.append((ergoResult, distanceResult, "".join(keyboard)))
    rankings = sorted(results, key=lambda result: result[0] + result[1])
    return [list(ranking[2]) for ranking in rankings]

def rankSelection(rankings):
    weights=[len(rankings) - i for i in range(len(rankings))]
    mother = random.choices(rankings, weights=weights)[0]
    father = random.choices(rankings, weights=weights)[0]
    return [mother, father]

def mateKeyboards(mother, father):
    mother = list(mother)
    father = list(father)
    crossoverPoint = random.randint(0, 10)
    return [crossover(mother, father, crossoverPoint), crossover(father, mother, crossoverPoint)]

def crossover(firstParent, secondParent, crossoverPoint):
    characters = list("qwertyuiopasdfghjkl;zxcvbnm,.?")
    finalLayout = [firstParent[:crossoverPoint], firstParent[10:crossoverPoint + 10], firstParent[20:crossoverPoint + 20]]
    layoutList = layoutToList(finalLayout)
    secondParent = secondParent.copy()
    for letter in layoutList:
        secondParent.remove(letter)
    for row in range(3):
        for character in range(crossoverPoint, 10):
            finalLayout[row].append(secondParent[0])
            secondParent.pop(0)

    return layoutToList(finalLayout)

def layoutToList(layout):
    return layout[0] + layout[1] + layout[2]

def nextPopulation(population, text, typing):
    popSize = len(population)
    newPop = []
    newPopSize = 0
    rankings = fitnessTest(population, typing, text)
    newPop.extend(rankings[:2])
    newPopSize = 2

    while newPopSize < popSize:
        parents = rankSelection(rankings)
        children = mateKeyboards(parents[0], parents[1])
        # TODO: Add Mutation Function
        newPop.extend(children)
        newPopSize += 2

    return newPop 

if __name__ == "__main__":
    population = initPopulation(100)
    with open("test.txt", "r") as f:
        text = f.read()
    for i in range(1):
        print(population)
        print(population[:2])
        population = nextPopulation(population, "Hi", "rfp")
    


