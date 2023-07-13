def checkDistance(layout, word, algorithm):
    algorithms = {
            "rfp": rightHandFingerPecking,
            "lfp": leftHandFingerPecking
            }
    layout = listToLayout(layout)
    algorithm = algorithms[algorithm]
    word = removeDuplicates(word).lower()
    return algorithm(layout, word)

def rightHandFingerPecking(layout, word):
    origin = (1, 6.2)
    word = word.lower()
    previousCoordinate = layoutToCoordinate(layout, word[0])
    startDistance = distanceCoordinates(origin, previousCoordinate)
    return startDistance + fingerPecking(layout, word, previousCoordinate)

def leftHandFingerPecking(layout, word):
    origin = (1, 3.2)
    word = word.lower()
    previousCoordinate = layoutToCoordinate(layout, word[0])
    startDistance = distanceCoordinates(origin, previousCoordinate)
    return startDistance + fingerPecking(layout, word, previousCoordinate)

def fingerPecking(layout, word, previousCoordinate):
    distanceTotal = 0 
    spacebarCol = False

    for letter in word[1:]:
        coordinate = layoutToCoordinate(layout, letter)
        if not coordinate:
            distance, spacebarCol = spaceBarDistance(previousCoordinate)
        elif not previousCoordinate:
            distance, spacebarCol = spaceBarDistance(coordinate, spacebarCol)
        else:
            distance = distanceCoordinates(previousCoordinate, coordinate)
        previousCoordinate = coordinate
        distanceTotal += distance

    return distanceTotal

def removeDuplicates(word):
    newWord = ""
    previousLetter = ""
    for letter in word:
        if letter != previousLetter:
            newWord += letter
            previousLetter = letter
    return newWord

def listToLayout(layoutList):
    return [layoutList[:10], layoutList[10:20], layoutList[20:30]]

def pythagoreanTheorem(deltaX, deltaY):
    return (deltaX ** 2 + deltaY ** 2) ** 0.5

def spaceBarDistance(coordinate, spacebarCol=False):
    if coordinate == -1:
        return 0, spacebarCol
    if coordinate[1] <= 2.8:
        col = 2.8
    elif coordinate[1] >= 6.8:
        col = 6.8
    else:
        col = coordinate[1]
    if spacebarCol:
        col = spacebarCol
    deltaCol = coordinate[1] - col
    deltaRow = 3 - coordinate[0]
    return pythagoreanTheorem(deltaCol, deltaRow), col

def distanceCoordinates(coordinateOne, coordinateTwo):
    if coordinateOne == -1 or coordinateTwo == -1:
        return 0
    deltaRow = coordinateOne[0] - coordinateTwo[0]
    deltaCol = coordinateOne[1] - coordinateTwo[1]
    return pythagoreanTheorem(deltaRow, deltaCol)
    
def layoutToCoordinate(layout, letter):
    if letter == " ":
        return False
    for row, letters in enumerate(layout):
        if letter in letters:
            offset = 0
            if row == 1:
                offset = 0.2
            elif row == 2:
                offset = 0.8
            return (row, letters.index(letter) + offset)
    return -1

if __name__ == "__main__":
    qwerty = list("qwertyuiopasdfghjkl;zxcvbnm,.")
    word = "hello"
    print(f"Total Distance for '{word}'")
    print("Right Hand Finger Pecking: " + str(checkDistance(qwerty, word, "rfp")))
    print("Left Hand Finger Pecking: " + str(checkDistance(qwerty, word, "lfp")))
