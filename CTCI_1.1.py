def is_unique(testString):
    myDict = {}

    for c in testString:
        if c in myDict:
            myDict[c] += 1
        else:
            myDict[c] = 1
    for k in myDict:
        if myDict[k] > 1:
            return False
    return True


myString = "defglcab"
print(is_unique(myString))
