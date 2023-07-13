def checkErgo(layout, text, algorithm):
    algorithms = {
            "rfp": fingerPicking,
            "lfp": fingerPicking,
            }
    algorithm = algorithms[algorithm]
    return algorithm(layout)

def fingerPicking(layout):
    return 1
