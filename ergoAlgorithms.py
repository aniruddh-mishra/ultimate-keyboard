def checkErgo(layout, text, algorithm):
    algorithms = {
            "rfp": fingerPicking,
            "lfp": fingerPicking,
            "tft": twoFingerTyping,
            "nt": normalTyping
            }
    algorithm = algorithms[algorithm]
    return algorithm(layout)

def fingerPicking(layout):
    return 1

def twoFingerTyping(layout):
    return 1

def normalTyping(layout):
    return 1
