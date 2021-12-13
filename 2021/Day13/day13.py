# inputData = open("example.txt").readlines()
import copy
import functools

inputData = open("input.txt").readlines()
FOLD_PREFIX = "fold along "
COORDS = []
FOLDS = []


def foldX(line, inputCoords):
    retVal = []
    twiceLine = 2 * line
    for coords in inputCoords:
        if coords[0] > line:
            retVal.append([twiceLine - coords[0], coords[1]])
        else:
            retVal.append(coords)
    return retVal


def foldY(line, inputCoords):
    retVal = []
    twiceLine = 2 * line
    for coords in inputCoords:
        if coords[1] > line:
            retVal.append([coords[0], twiceLine - coords[1]])
        else:
            retVal.append(coords)
    return retVal


def fold(foldLine, inputCoords):
    if 'y' in foldLine:
        return foldY(foldLine['y'], inputCoords)
    if 'x' in foldLine:
        return foldX(foldLine['x'], inputCoords)


def getUniqueNum(data):
    mySet = set()
    for c in data:
        mySet.add(".".join(str(c)))
    return len(mySet)


def getUnique(data):
    mySet = {}
    vals = []
    for c in data:
        if ".".join(str(c)) not in mySet:
            mySet[".".join(str(c))] = c
    for k in mySet:
        vals.append(mySet[k])
    return vals


for row in inputData:
    if len(row) > 1:
        if row.startswith(FOLD_PREFIX):
            splitted = row.replace(FOLD_PREFIX, "").split("=")
            FOLDS.append({splitted[0]: int(splitted[1])})
        else:
            splitted = row.split(",")
            COORDS.append([int(splitted[0]), int(splitted[1])])


# print(COORDS)
# print(FOLDS)

def numCompare(n1, n2):
    if n1 < n2:
        return -1
    if n1 > n1:
        return 1
    else:
        return 0


def compareCoords(item1, item2):
    if item1[1] == item2[1]:
        return numCompare(item1[0], item2[0])
    else:
        return numCompare(item1[1], item2[1])


def printData(sortedCoords):
    sortedCoords = sorted(sortedCoords, key=functools.cmp_to_key(compareCoords))
    maxX = sortedCoords[-1][0] + 1
    maxY = sortedCoords[-1][1] + 1

    nextPoint = 0
    for y in range(maxY):
        for x in range(maxX):
            if sortedCoords[nextPoint][0] == x and sortedCoords[nextPoint][1] == y:
                print("#", end='')
                nextPoint = nextPoint + 1
            else:
                print(" ", end='')
        print()


print("Part 1: {}".format(getUniqueNum(fold(FOLDS[0], COORDS))))
current = copy.copy(COORDS)
for f in FOLDS:
    current = fold(f, current)

# current = sorted(getUnique(current), key=functools.cmp_to_key(compareCoords))
current = getUnique(current)
print("Part2: ")
printData(current)

# print(fold(FOLDS[0], COORDS))
