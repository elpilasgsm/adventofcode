# data = open("input.txt").readlines()
import numpy


def closestToAvg(arr):
    avg = numpy.average(positions)
    # print("Avg {}".format(avg))
    curPos = positions[0]
    delta = abs(avg - curPos)
    for i in range(1, len(positions)):
        if abs(avg - positions[i]) < delta:
            delta = abs(avg - positions[i])
            curPos = positions[i]
    # print("Val {}".format(curPos))
    return curPos


# data = open("example.txt").read()
data = open("input.txt").read()
positions = numpy.array([int(i) for i in data.split(",")])

fuel = abs(positions - positions[0]).sum()
index = 0

for pos in range(max(positions)):
    curFuel = abs(positions - pos).sum()
    if curFuel < fuel:
        fuel = curFuel
        index = pos

print("Part1: Fuel=" + str(fuel) + " at pos: " + str(index))

CACHE = {}


def calcFuel(lengths):
    retVal = []
    for len in lengths:
        if len in CACHE:
            val = CACHE[len]
        else:
            val = sum(k for k in range(len + 1))
            CACHE[len] = val
        # print("len: {}, val: {}".format(len,val))
        retVal.append(val)
    return numpy.array(retVal)


fuel = 10000000000
index = 0
for pos in range(max(positions)):
    curFuel = calcFuel(abs(positions - pos)).sum()
    if curFuel < fuel:
        fuel = curFuel
        index = pos

print("Part2: Fuel=" + str(fuel) + " at pos: " + str(index))
