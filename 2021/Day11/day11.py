import copy

import numpy

inputData = open("example.txt").readlines()
#inputData = open("input.txt").readlines()
inputData = [[int(v) for v in val.replace("\n", "")] for val in inputData]
workingData = numpy.array(copy.copy(inputData))
bounds = workingData.shape
flashes = 0


def toNum(x, y):
    return bounds[0] * y + x


def fromNum(val):
    x = val % bounds[0]
    y = (val - x) // bounds[0]
    return x, y


def incrementAndFlashIfRequired(x, y, arr, flashedAdStep):
    if 0 <= x < bounds[0] and 0 <= y < bounds[1]:
        arr[y][x] = arr[y][x] + 1
        if arr[y][x] > 9:
            flashAtPosition(x, y, arr, flashedAdStep)


def flashAtPosition(x, y, arr, flashedAdStep):
    arr[y][x] = 0
    flashedAdStep[toNum(x,y)]={}
    for _y in range(-1, 2):
        for _x in range(-1, 2):
            if _x == 0 and _y == 0:
                continue
            # print("for ({},{}) check point({},{})".format(x,y,x + _x,y + _y))
            incrementAndFlashIfRequired(x + _x, y + _y, arr, flashedAdStep)


def flash(array):
    flashedAdStep = {}
    for y in range(bounds[1]):
        for x in range(bounds[0]):
            if array[y][x] > 9:
                flashAtPosition(x, y, array, flashedAdStep)

    res = len(flashedAdStep)
    print("flashedAdStep: {}".format(res))
    for key in flashedAdStep:
        curX,curY = fromNum(key)
        array[curY][curX] = 0
    return res

days = 100
part1 = 0
for i in range(days):
    workingData = workingData + 1
    part1 = part1 + flash(workingData)

print("Part #1: {}".format(part1))

workingData = numpy.array(copy.copy(inputData))
inc = 0
while True:
    inc = inc + 1
    workingData = workingData + 1
    flash(workingData)
    if numpy.all(workingData == workingData[0]):
        print("Part #2: {}".format(inc))
        break
