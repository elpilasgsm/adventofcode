import numpy

numOfSegmentPerNum = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


# 6 - 0 6 9


def lenToDigit(nOfSegm):
    data = {}
    for i in range(len(nOfSegm)):
        curLn = nOfSegm[i]
        if curLn not in data:
            data[curLn] = []
        data[curLn].append(i)
    return data


letToDigitsDic = lenToDigit(numOfSegmentPerNum)


def decideNumber(str):
    strLen = len(str)
    if strLen in letToDigitsDic:
        possibleNums = letToDigitsDic[strLen]
        if len(possibleNums) == 1:
            return possibleNums[0]
        else:
            return possibleNums
    else:
        return None


output = 0
inputData = open("input.txt").readlines()
#inputData = open("example.txt").readlines()

for row in inputData:
    digits = row.split(" | ")[1].replace("\n", "").split(" ")
    for digit in digits:
        decided = decideNumber(digit)
        if decided is not None:
            if isinstance(decided, list):
                continue
            else:
                output = output + 1

#print("output part one: {}".format(output))

def countContains(source, target):
    val = 0
    for i in target:
        if i in source:
            val = val + 1
    return val

def contains(source, target):
    for i in target:
        if i not in source:
            return False
    return True


def process253(leftPart, currentNum):
    toDecide3 = [value for value in leftPart if len(value) == 3][0]
    if len(toDecide3) == 0:
        toDecide3 = [value for value in leftPart if len(value) == 2][0]
    if len(toDecide3) == 0:
        print("No 1 or 7 in the row")
        exit(1)
    #print("To decide 3 for {} we have {}".format("".join(currentNum), "".join(toDecide3)))
    if contains(currentNum, toDecide3):
        #print("This is 3")
        #print("".join(currentNum))
        return 3
    toDecide25 = [value for value in leftPart if len(value) == 4][0]
    if len(toDecide25) == 0:
        print("No 4 to decide 2 or 5")
        exit(1)
    containesNum = countContains(currentNum,toDecide25)
    if containesNum == 3:
        return 5
    else:
        return 2

def process069(leftPart, currentNum):
    toDecide6 = [value for value in leftPart if len(value) == 3][0]
    if len(toDecide6) == 0:
        toDecide6 = [value for value in leftPart if len(value) == 2][0]
    if len(toDecide6) == 0:
        print("No 1 or 7 in the row")
        exit(1)
    if contains(currentNum,toDecide6):
        toDecide09 = [value for value in leftPart if len(value) == 4][0]
        if len(toDecide09) == 0:
            print("No 4 to decide 0 or 9")
            exit(1)
        if contains(currentNum,toDecide09):
            return 9
        else:
            return 0
    else:
        return 6


def extract(leftPart, currentNum):
    #print("Extractions based on: {}, {}, {}".format(leftPart, currentNum, decided))
    curLn = len(currentNum)
    if curLn == 5:
        return process253(leftPart, currentNum)
    if curLn == 6:
        return process069(leftPart, currentNum)

toSum = 0

def num(arr):
    return 1000 * arr[0] + 100*arr[1] + 10*arr[2] + arr[3]

for row in inputData:
    val = []
    splitted = row.split(" | ")
    digits = [sorted(val) for val in splitted[1].replace("\n", "").split(" ")]
    outputs = [sorted(val) for val in splitted[0].replace("\n", "").split(" ")]
    for digit in digits:
        decided = decideNumber(digit)
        if decided is not None:
            if isinstance(decided, list):
                val.append(extract(outputs, digit))
            else:
                val.append(decided)
    print("Val: {}, totalNum: {}".format(val,num(val)))
    toSum = toSum +  num(val)
print(toSum)

