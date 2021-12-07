import re

data = open("input.txt").readlines()
#data = open("example.txt").readlines()
regex = r"(\d*),(\d*) -> (\d*),(\d*)"


def countMoreThan1(ventStorage):
    count = 0
    for key in ventStorage:
        if ventStorage[key] > 1:
            count = count + 1
    return count


def part1Filter(row, ventStorage):
    matches = re.search(regex, row, re.IGNORECASE)
    if matches and len(matches.groups()) == 4:
        x1 = int(matches.group(1))
        y1 = int(matches.group(2))
        x2 = int(matches.group(3))
        y2 = int(matches.group(4))
        # print("({x1},{y1}) -> ({x2},{y2})".format(x1=x1, x2=x2, y1=y1, y2=y2))
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                key = str(x1) + "X" + str(y)
                if key not in ventStorage:
                    ventStorage[key] = 0
                ventStorage[key] = ventStorage[key] + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                key = str(x) + "X" + str(y1)
                if key not in ventStorage:
                    ventStorage[key] = 0
                ventStorage[key] = ventStorage[key] + 1


def part2Filter(row, ventStorage):
    matches = re.search(regex, row, re.IGNORECASE)
    if matches and len(matches.groups()) == 4:
        x1 = int(matches.group(1))
        y1 = int(matches.group(2))
        x2 = int(matches.group(3))
        y2 = int(matches.group(4))
        # print("({x1},{y1}) -> ({x2},{y2})".format(x1=x1, x2=x2, y1=y1, y2=y2))
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                key = str(x1) + "X" + str(y)
                if key not in ventStorage:
                    ventStorage[key] = 0
                ventStorage[key] = ventStorage[key] + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                key = str(x) + "X" + str(y1)
                if key not in ventStorage:
                    ventStorage[key] = 0
                ventStorage[key] = ventStorage[key] + 1
        else:
            # go from 1 to 2
            xStep = (x2 - x1) // abs(x1 - x2)
            yStep = (y2 - y1) // abs(y1 - y2)
            y = y1
            for x in range(x1, x2+xStep, xStep):
                key = str(x) + "X" + str(y)
                if key not in ventStorage:
                    ventStorage[key] = 0
                ventStorage[key] = ventStorage[key] + 1
                y=y+yStep

commonStorage = {}
for row in data:
    part1Filter(row, commonStorage)

print("Part #1 answer: " + str(countMoreThan1(commonStorage)))

commonStorage = {}
for row in data:
    part2Filter(row, commonStorage)

print("Part #2 answer: " + str(countMoreThan1(commonStorage)))
#print(commonStorage)
