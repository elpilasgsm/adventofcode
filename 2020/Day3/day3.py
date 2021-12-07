resp = open("input.txt").readlines()
#resp = open("example.txt").readlines()
print(resp)
x = 3
y = 1

rowsNum = len(resp)
patternLen = len(resp[0]) - 1
lastY = rowsNum


def findTrees(deltaX, deltaY, data):
    trees = 0
    curX = 0
    curY = 0
    while curY < lastY:
        if curX >= patternLen:
            curX = curX % patternLen
        if data[curY][curX] == '#':
            trees = trees + 1
        curX = curX + deltaX
        curY = curY + deltaY

    return trees


one_one = findTrees(1, 1, resp)
three_one = findTrees(3, 1, resp)
five_one = findTrees(5, 1, resp)
seven_one = findTrees(7, 1, resp)
one_two = findTrees(1, 2, resp)

print(one_one)
print(three_one)
print(five_one)
print(seven_one)
print(one_two)

print("result: {}".format(one_one * three_one * five_one * seven_one * one_two))
