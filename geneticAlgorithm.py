import random
import distanceAlgorithms
import ergoAlgorithms

def initPopulation(popSize):
    alphabet = list("abcdefghijklmnopqrstuvwxyz.,?;")
    population = []
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
    return [ranking[2] for ranking in rankings]

def rankSelection(rankings):
    weights=[len(rankings) - i for i in range(len(rankings))]
    mother = random.choices(rankings, weights=weights)[0]
    father = random.choices(rankings, weights=weights)[0]
    return [mother, father]

if __name__ == "__main__":
    population = initPopulation(100)
    with open("test.txt", "r") as f:
        text = f.read()
    rankings = fitnessTest(population, "rfp", "Hi")
    print(rankings)
    print(rankSelection(rankings))

