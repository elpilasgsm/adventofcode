import copy
import numpy

inputData = open("example.txt").readlines()
# inputData = open("input.txt").readlines()
inputData = [[int(v) for v in val.replace("\n", "")] for val in inputData]
workingData = numpy.array(copy.copy(inputData))
bounds = workingData.shape
flashes = 0


def incrementAndFlashIfRequired(x, y, arr):
    if x >= 0 and y >= 0 and x < bounds[0] and y < bounds[1]:
        arr[y][x] = arr[y][x] + 1
        if arr[y][x] > 9:
            flashAtPosition(x, y, arr)


def flashAtPosition(x, y, arr):
    arr[y][x] = 0
    for _y in range(-1, 2):
        for _x in range(-1, 2):
            if _x == 0 and _y == 0:
                continue
            incrementAndFlashIfRequired(x + _x, y + _y, arr)


def flash(array):
    for y in range(bounds[1]):
        for x in range(bounds[0]):
            if array[y][x] >= 9:
                flashAtPosition(x, y, array)


days = 101
for i in range(days):
    workingData = workingData + 1
    flash(workingData)
    print(workingData)
