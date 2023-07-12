import random
import distanceAlgorithms

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

def fitnessTest(keyboard):
    with open("test.txt", "r") as f:
        text = f.read()
        return distanceAlgorithms.checkDistance(keyboard, text, "rfp")

if __name__ == "__main__":
    population = initPopulation(100)
    fittestScore = fitnessTest(population[0])
    fittestKeyboard = population[0]
    for keyboard in population[1:]:
        score = fitnessTest(keyboard)
        if score < fittestScore:
            fittestScore = score
            fittestKeyboard = keyboard
        print(score)
    print(fittestKeyboard)
    print(fittestScore)

