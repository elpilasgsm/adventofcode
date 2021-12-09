import copy

import numpy

#inputData = open("example.txt").readlines()
inputData = open("input.txt").readlines()
inputData = [val.replace("\n", "") for val in inputData]

xBound = len(inputData[0])
yBound = len(inputData)

vals = []

bases = []


def isBasinBase(x, y):
    cur = inputData[y][x]
    if cur == 9:
        return False

    if (x - 1 < 0 or inputData[y][x - 1] > cur) and (x + 1 >= xBound or inputData[y][x + 1] > cur) and (
            y + 1 >= yBound or inputData[y + 1][x] > cur) and (y - 1 < 0 or inputData[y - 1][x] > cur):
        return True
    return False


def point(x, y):
    return ["{}X{}".format(y, x), x, y]


def checkNode(x, y, curVal, targetStorage):
    added = 0

    if x >= 0 and x < xBound and y >= 0 and y < yBound:
        val = int(inputData[y][x])
        if val == 9 or val <= curVal:
            return added
        p = point(x, y)
        if p[0] not in targetStorage:
            added = added + 1
            targetStorage[p[0]] = p

    return added


def getBasinSize(basePoint):
    buff1 = {basePoint[0]: basePoint}
    buff2 = {}
    final = {}
    final.update(buff1)
    added = 0
    while True:
        for ptn in buff1:
            x = buff1[ptn][1]
            y = buff1[ptn][2]
            curVal = int(inputData[y][x])
            added = added + checkNode(x, y - 1, curVal, buff2)
            added = added + checkNode(x, y + 1, curVal, buff2)
            added = added + checkNode(x + 1, y, curVal, buff2)
            added = added + checkNode(x - 1, y, curVal, buff2)

        if added == 0:
            return len(final)
        else:
            added = 0
            buff1 = copy.copy(buff2)
            final.update(buff1)
            buff2 = {}


# 247
for _y in range(yBound):
    for _x in range(xBound):
        if isBasinBase(_x, _y):
            vals.append(int(inputData[_y][_x]))
            bases.append(point(_x, _y))

data = numpy.array(vals) + 1
print("Part 1: {}".format(data.sum()))

sizes = []
for basin in bases:
    sizes.append(getBasinSize(basin))
#sizes=sizes[::-1].sort()
sizes = numpy.sort(sizes)[::-1]
#print(sizes)
print("Part 2: {}".format(sizes[0]*sizes[1]*sizes[2]))

