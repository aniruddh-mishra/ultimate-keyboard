def checkDistance(layout, word, algorithm):
    algorithms = {
            "rfp": rightHandFingerPecking,
            "lfp": leftHandFingerPecking
            }
    layout = listToLayout(layout)
    algorithm = algorithms[algorithm]
    word = removeDuplicates(word).lower()
    return algorithm(layout, word)

def nFingerTyping(numFingers, word, layout):
    fingerMap, fingerPositions = generateMap(numFingers)
    naturalPosition = fingerPositions
    distance = 0
    for letter in word:
        if letter == " ":
            fingerMap = naturalPosition
        letterIndex = layout.index(letter)
        finger = fingerMap[letter]
        currentPosition = fingerPositions[finger]
        letterCoordinate = letterToCoordinate(letter)
        fingerPositions[finger] = letterCoordinate
        distance += distanceBetweenCoordinates(letterCoordinate, currentPosition)
    return distance

def letterToCoordinate(letter): 
    row = int(key/10)
    col = key - (row * 10)
    return (row, col)

def distanceBetweenCoordinates(coordinateOne, coordinateTwo):
    row1 = coordinateOne[0]
    col1 = coordinateOne[1] + row1 ** 2 / 10
    row2 = coordinateTwo[0]
    col2 = coordinateTwo[1] + row2 ** 2 /10
    return pythagoreanTheorem(row2 - row1, col2 - col1)

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

def generateMap(numFingers, typingStyle):
    fingerLayouts = {
            1: [(0, 0, 3, 10)],
            2: [(0, 0, 3, 5), (0, 5, 3, 10)],
            }
    startingPositions = {
            "rfp": [(1, 6)],
            "lfp": [(1, 3.2)],
            "tft": [(1, 3.2), (1, 6)]
            }
    positions = fingerLayouts[numFingers]
    keyboardMap = {}
    for i in range(30):
        for pos, finger in enumerate(positions):
            if keyInRange(finger, i):
                keyboardMap[i] = pos
    
    return keyboardMap, startingPositions[typingStyle]
            
def keyInRange(fingerRange, key):
    row, col = letterToCoordinate(key)

    inRow = row in range(fingerRange[0], fingerRange[2])
    inCol = col in range(fingerRange[1], fingerRange[3])
    
    if inRow and inCol:
        return True
    
    return False

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

if __name__ == "__main__":
    qwerty = list("qwertyuiopasdfghjkl;zxcvbnm,.")
    word = "hello"
    print(f"Total Distance for '{word}'")
    print("Right Hand Finger Pecking: " + str(checkDistance(qwerty, word, "rfp")))
    print("Left Hand Finger Pecking: " + str(checkDistance(qwerty, word, "lfp")))
