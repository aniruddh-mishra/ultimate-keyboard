def fingerPecking(layout, word):
    previousCoordinate = layoutToCoordinate(layout, word[0])
    distanceTotal = 0
    for letter in word[1:]:
        coordinate = layoutToCoordinate(layout, letter)
        deltaRow = coordinate[0] - previousCoordinate[0]
        deltaCol = coordinate[1] - previousCoordinate[1]
        distance = (deltaRow ** 2 + deltaCol ** 2) ** 0.5
        previousCoordinate = coordinate
        distanceTotal += distance
    return distanceTotal

def layoutToCoordinate(layout, letter):
    for row, letters in enumerate(layout):
        if letter in letters:
            return (row, letters.index(letter))
    return False

if __name__ == "__main__":
    layout = [
            ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
            ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
            ["z", "x", "c", "v", "b", "n", "m"]
            ]
    word = "qa"
    print(fingerPecking(layout, word))
