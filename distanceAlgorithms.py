def checkDistance(layout, word, algorithm):
    numFingers = {
            "rfp": 1,
            "lfp": 1,
            "tft": 2,
            "nt": 8
            }
    numFinger = numFingers[algorithm]
    word = removeDuplicates(word).lower()
    fingerMap, fingerPositions = generateMap(numFinger, algorithm)
    return nFingerTyping(fingerMap, fingerPositions, word, layout)

def nFingerTyping(fingerMap, fingerPositions, word, layout):
    naturalPosition = fingerPositions.copy()
    distance = 0
    for letter in word:
        if letter == " ":
            fingerPositions = naturalPosition
       
        if letter not in layout:
            continue

        
        letterIndex = layout.index(letter)
        finger = fingerMap[letterIndex]
        currentPosition = fingerPositions[finger]
        letterCoordinate = letterToCoordinate(letterIndex)
        fingerPositions[finger] = letterCoordinate
        distance += distanceBetweenCoordinates(letterCoordinate, currentPosition)
    
    return distance

def letterToCoordinate(letter): 
    row = int(letter/10)
    col = letter - (row * 10)
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
            8: [(0, 0, 3, 1), (0, 1, 3, 2), (0, 2, 3, 3), (0, 3, 3, 5), (0, 5, 3, 7), (0, 7, 3, 8), (0, 8, 3, 9), (0, 9, 3, 10)]
            }
    startingPositions = {
            "rfp": [(1, 6)],
            "lfp": [(1, 3)],
            "tft": [(1, 3), (1, 6)],
            "nt": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 6), (1, 7), (1, 8), (1, 9)]
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

def pythagoreanTheorem(deltaX, deltaY):
    return (deltaX ** 2 + deltaY ** 2) ** 0.5

if __name__ == "__main__":
    qwerty = list("qwertyuiopasdfghjkl;zxcvbnm,.")
    word = "hello"
    print(f"Total Distance for '{word}'")
    print("Right Hand Finger Pecking: " + str(checkDistance(qwerty, word, "rfp")))
    print("Left Hand Finger Pecking: " + str(checkDistance(qwerty, word, "lfp")))
    print("Two Finger Typing: " + str(checkDistance(qwerty, word, "tft")))
    print("Normal Typing: " + str(checkDistance(qwerty, word, "nt")))
